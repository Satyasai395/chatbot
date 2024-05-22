from random import choice

neutral = [
    "Complaining about the lack of smoking shelters, the nicotine addicted Python programmers said there ought to be 'spaces for tabs'.",
    "Ubuntu users are apt to get this joke.",
    # ... (other jokes)
]

chuck = [
    "When Chuck Norris throws exceptions, it's across the room.",
    "All arrays Chuck Norris declares are of infinite size, because Chuck Norris knows no bounds.",
    # ... (other jokes)
]

def get_joke():
    return choice(neutral + chuck)
