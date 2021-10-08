weather = ['weather', 'temperature', 'humidity', 'pressure', 'barometric', 'atmospheric', 'atmosphere', 'rain', 'cloud', 'lightning', 'snow', 'flood', 'storm', 'dew', 'wind']
plant = ['none']
memory = ['memory', 'create', 'delete', 'update', 'new', 'neuron', 'cell']
question = ['what', 'where', 'when', 'how', 'why']



def judgePhrase(phrase):
    if type(phrase) is not list:
        phrase = phrase.lower()
        phrase = phrase.split(" ")

    weatherScore = 0
    plantScore = 0
    memoryScore = 0
    questionScore = 0

    for word in weather:
        if word in phrase:
            weatherScore += 1
    for word in plant:
        if word in phrase:
            plantScore += 1
    for word in memory:
        if word in phrase:
            memoryScore += 1
    for word in question:
        if word in phrase:
            questionScore += 1

    if questionScore > 2 and plantScore > 2:
        return "plant query"
    elif questionScore > 2 and weatherScore > 2:
        return "weather query"
    elif plantScore > 2:
        return "plant"
    elif weatherScore > 2:
        return "weather"
    elif memoryScore > 2:
        return "memory"
    elif questionScore > 2 and memory > 2:
        return "memory query"
    else:
        return "unsure"