# assignbot/views.py

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Message

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from random import choice
from .strings import *
from .jokes import get_joke
import time
from datetime import timedelta
from datetime import datetime
from twilio.rest import Client
from django.conf import settings
import google.generativeai as genai

starting_time = time.time()
now = datetime.now()

@api_view(['GET'])
def index(request):
    return Response("Hello, World!")

@csrf_exempt
@api_view(['POST'])
def on_message(request):
    msg = request.data
    # print(msg)
    user_number, user_name = msg.get("From").split(":")[1], msg.get("ProfileName")
    text = msg.get("Body").lower()
    words = text.split(" ")
    media_url = None

    user, created = User.objects.get_or_create(number=user_number,
        defaults={'profile_name': user_name, 'wa_id': msg.get('WaId')}
    )

    if created:
        text = str(welcome + intro).replace('user_name', user_name)
    elif text in help:
        text = intro
    elif text in what_is_my_name:
        text = f"Hey Hi ... {user_name}"
    elif text in give_me_joke:
        text = get_joke()
    elif text in picuture:
        media_url = [picsum_link]
    elif text in tim:
        current_time = now.strftime(" %H:%M:%S")
        text = "Time is {}".format(current_time)
    elif text in dat:
        current_date = now.strftime("%Y-%m-%d")
        text = "Today's Date : {}".format(current_date)        
    elif "alive" in text:
        text = f"Yes I am Alive since *{str(timedelta(seconds=int(time.time() - starting_time)))}*"
    elif words[0] in ai:
        print(text)
        # msg.get("From").split(":")[1]
        text=search(text[2:])
        # print(out)

    
    else:
        text = f"You Said : *{msg['Body']}* "

    

    if media_url:
        for url in media_url:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(media_url=[url], from_=msg["To"], to=msg["From"])
    else:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(body=text, from_=msg["To"], to=msg["From"])
        message = Message.objects.create(
            user=user,
            sms_message_sid=msg.get('SmsMessageSid'),
            body=msg.get('Body'),
            replied=text,
            sms_status=msg.get('SmsStatus'),
            from_number=msg.get("From").split(":")[1],
            to_number=msg.get("To").split(":")[1],
            profile_name=user_name,
            media_url=None if msg.get('NumMedia') == '0' else msg.get('MediaUrl0')  # Assuming media URL is provided in MediaUrl0 if exists
        )
        print(message)
       

    return JsonResponse({'status': 'success'}, status=200)

@csrf_exempt
@api_view(['POST'])
def on_sms_status(request):
    message = request.data

    msg, created = Message.objects.get_or_create(
        sms_message_sid=message.get('SmsMessageSid'),
        defaults={
            'body': message.get('Body', ''),
            'sms_status': message.get('SmsStatus', ''),
            'from_number': message.get('From'),
            'to_number': message.get('To'),
            'profile_name': message.get('ProfileName', ''),
            'media_url': message.get('MediaUrl0', '')
        }
    )

    if not created and msg.sms_status != 'read':
        msg.sms_status = message.get('SmsStatus')
        msg.save()

    return JsonResponse({'status': 'success'}, status=200)

# @api_view(['GET'])
# def random_file(request):
#     files = join(getcwd(), "static", 'files')
#     file = choice(listdir(files))
#     return send_from_directory(files, file)

def search(query):
    print(query)
    
    genai.configure(api_key=settings.API)

    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(query[5:]+"in simple way")
    # print(response.text)
    r1=response.text
    r2=r1.split("**")
    r3=''
    for i in range(len(r2)):
        if i==0 or i%2==0:
            r3+=r2[i]
        else:
            r3+= " " + r2[i] + " " 

# print(r3)
    r3.split("*")
# print(r3)
    r3.replace("<br>"," ")
    # print(r3) 
    r4=r3[:1600] 
   


    return r4
