welcome = """
*Hey Hi* ... ```user_name```
Welcome to _Assign bot_ 
"""

intro = """
*1.* _my_ *Name*  
*2.* *random _joke_*
*3.*  *_Time_*
*4.*  *_Date_*
*5.* _ask AI + your prompt_ to get interact with *_AI_*

_say_  *Help* 
to get this ```message``` again
Ex: AI what is html
"""

response_xml = """
<?xml version="1.0" encoding="UTF-8"?><Response><Message>Body</Message></Response>
"""
empty_responce_xml = '<?xml version="1.0" encoding="UTF-8"?></Response>'

what_is_my_name = ('1',"say my name","what is my name", 'my name')
give_me_joke = ('2','joke','say joke','send a joke','tell me a joke','random joke')
picuture = ('3','random picture', 'random pic', 'pic','picuture','image','random image','photo','random photo')
# documents = ('4','send a file','file','documents','send docoment','send docoments','random file','random files','random document', 'random thing')
tim=('4','time','time now','what is the time','clock')
dat=('5','date','today date','waht is the date today')
ai=('ai','google','what','search','Ai',"AI")
help = ('*','help', 'help me', '/help', '\help')

max_files = "Sorry I have only *10* files "

picsum_link = "https://picsum.photos/200/300"
