import random

def decision(phrases):
    phrase, phrase2, phrase3 = random.choice(phrases), random.choice(phrases), random.choice(phrases)
    phrases = [phrase, phrase2, phrase3]
    phrase, phrase2, phrase3 = random.choice(phrases), random.choice(phrases), random.choice(phrases)
    phrases = [phrase, phrase2, phrase3]
    phrase = random.choice(phrases)
    return phrase
