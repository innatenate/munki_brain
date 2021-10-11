
# Munki (*Brain*)
 The easy to love voice assistant.

### Brain? 
Yes, this is the brain behind Munki -  a voice assistant paired with Home Assistant. 
Munki handles basic voice assistant commands and will automate many boring
home tasks using Home Assistant. Munki also excels at forecasting the weather,
making it's own forecast based on the current weather conditions for your area. 
Munki is also great at remember every small detail you through at it, and can 
even make a grocery list for you. Munki remembers the details you tell it with a
basic command. Munki does so much, that it's hard to utilize in one platform or computer;
therefore I adopted a server-client approach, where the brain is the server and the bodies are the clients.
Munki itself is actually roughly developed around the organizational pattern of a brain, making it easier to understand when debugging.


### Brain vs Body

You can think of the brain as the server. The brain is typically ran on stationary computer. I prefer my Raspberry Pi, *which is connected
to a power bank to prevent data loss in the event of a power outage*. The bodies would be the individual clients connecting
to the brain. Each body handles the vocal and auditory functions (*TTS and STT*). The body listens for commands, connects to the brain,  and then sends
the commands to the brain, which processes and better understands the commands. The result of the command (*usually in a JSON format*) is then sent
back to the body to be spoken and handled. The brain is entirely independent whereas the bodies rely on the brain to actually process the commands.


### Features
* Memory functionality
* Forecast and weather detail handling
* Home assistant functionality
* Basic scene and logic handling
* Local voice handling (*not saved server-side*)
* Undersold on this Readme

### Memory
Munki holds the ability to remember details and people. Munki's memory is a bit funky to explain.
Each memory bank holds folds, and each fold has cells, and each cell has neurons.

You can think of a memory bank as a general name for the category of memories, like **self** or **friends**. 

A fold is a category within the memory bank. You can think of a fold like **info** in self or **Sally** in friends.

A cell is a finer detail category in a fold. An example of a cell would be **how made** in info or **favorites** in Sally.

A neuron is the detail to remember. Neurons are typically named with the detail's descriptor as
the name and they hold the answer. An example of a neuron would be a neuron called **color** in favorites in Sally. You would then find that the neuron holds **blue** as the answer. 

It's a bit of a quirky sounding system, but it works well for remember and sorting a lot of 
information. 

#### Examples

``` 
Hey Munki, can you remember my birthday is August 12th?
    >> Sure I'll remember that from now own.
```
Munki will remember this in your memory bank under the info fold under the personal cell under the birthday neuron. The info 
directory also holds many other things you'd like Munki to remember, like your height, favorite book, or social media. This info is kept and later used in 
future commands or requests.

```
Hey Munki, can you remember Sally's favorite color is blue?
    >> Not a problem. Just ask me if you forget.
```
Munki will add this to the favorites cell for Sally. If you later ask Munki what Sally's 
favorite color is - or if Sally's favorite color is blue - Munki will give you the
appropriate response.

```
Hey Munki, will you add milk to my grocery list?
    >> Alright, I'll add that to the dairy section.
```
Munki will add this to a section in it's memory dedicated to grocery lists. Later, you can
ask Munki for the entire grocery list, or even the price of your grocery list. This functionality
also works for certain sections of your list.
```
Hey Munki, will you remind me to get milk?
    >> Will do. Adding to the dairy section of your grocery list.
```
Another thing I didn't really hit on, Munki will automatically determine certain sections for products
or items you ask it to remember. Adding a category to the end of your request, like, *will you remind me to get milk dairy*, will help specify the category. Munki will also grab the price of the items based on local Walmart pricing. 
This may not always be accurate though, as Munki utilizes the search api and can not always get the correct guess.

### Forecasting and weather detail handling
While Munki does gather it's information from Visual Crossing API, Munki presents the data gathered as well as it's own hardcoded interpretation
of the forecast. Using basic meteorology and understanding from weather patterns, Munki will process the barometric pressure, wind speed, humidity, dew point, average temperature,
average feels-like and UV to determine a basic understanding of what to expect for the day. Munki also warns of weather alerts sent by NWS (National Weather Service).

#### Examples
```
What's the weather like today?
    >> Today's weather is fairly cloudy with an average temperature of 68°. I've noticed that the barometric pressure is rather low,
        compared to average readings. You should anticipate a possibility of rain soon. 
```
I live in Oklahoma, where weather patterns are ever-changing. We receive a constant change between northerly, dry, cold winds and southerly, moist, warm winds, 
which means a constant change in pressure as well. Reading and knowing the pressure give a heartbeat to the weather changes, which can lead to a more accurate reading.

```
What's the weather like next hour?
    >> I'm not expecting much change. I did notice a slight increase in clouds, but that's about it.

```
Hour-by-hour updates and observations, down to every detail. Visual Crossing API is really beautiful for this. Munki checks every single important detail and compares to the previous hour.

```
What's the weather like this week?
    >> For Monday, you should expect lowering temperatures with rain towards the night. Temperatures should be around 76° with a feels-like of 73°. 
        On Tuesday, anticipate a chance of scattered thunderstorms early day, clearing towards night-time. I am forecasting an average temperature of 
            73°. It seems like barometric pressure is lowest at this point in the forecast.
        Thirdly, for Wednesday, expect clear skies. Temperatures will be averaging around 76° with a feels-like of 78°.
        For Thursday, I am forecasting clear skies. Seems like temperatures will be around 79° with a feels-like of 83°. Additionally; it seems like UV is
            at it's highest, so remember sunscreen.
        Lastly, Friday seems summery with clear skies. Expect temperatures to be averaging at 84° with a feels-like of 87°.
```
A lengthy, but informative response. This response takes about 30 seconds to speak, and people tend to clock-out at a minute, so Munki is under the bar. Munki will automatically
default to a five day forecast, but you may ask for a seven day as well. The seven-day forecast is more informative - giving information about air fronts and 
noticeable trends and patterns in the forecasting - but it is a bit of a lengthy response.
```
What's the atmospheric pressure on Thursday?
    >> Looks like I am currently expecting 1013 hectopascals. That's rather low compared to the average.

```
Asking specific details for specific days is no problem for Munki, it'll even give an observation of the data. I'd like to further this part a bit more, but it's a later work for a later time.

### Home Assistant
It's still something I'm working on, but I'd like to venture to the point of handling scenes and basic home automation.
It's not a tricky or hard thing to do, I just haven't gotten to it with all the other fun things on this project.

I'd ideally like to handle most scene and motion-sensor events on the Home Assistant server itself, rather than programming my
own workaround, but I'd still like to have some functionality. 

The current layout would be to have a body in each room to handle basic commands for the room and understand occupancy and automatically
log in to user profiles to handle commands, rather than having a general room profile. The only real challenge is handling differential voice
recognization as the voice is not downloaded as an audio file - which makes it challenging to send to a voice analyzer or neural network.


### Local voice handling
Whenever a body is started, the microphone is constantly listening. No data is processed from this nor is the data saved. It is instead directly sent to a 
neural network to determine a possible result and returns a string. Nothing is processed or further saved unless a conversation is or was initiated with Munki (*i.e. "Hey Munki."*)
This throws a bit of a problem into developing a system for differential voice recognization (*understanding different people's voices*), but this also ensures security.

If a result was understood, the string is translated to JSON format with more information stored (*such as user profile, etc*) and then re-translated to a string. The body will then connect to the brain (*rather than maintaining a consistent connection*) and send the string. The string is processed in the brain and then sent back to the body to be spoken.

### A better understanding
Munki is roughly organized around a brain, utilizing different sections of the cerebellum, brain stem, and cerebrum. All of the command processing is handling in the brain, whereas all the speaking and human interaction is handled with the body. 
#### Body (*client*)
* Handles understanding client (*Speech-to-text*)
* Handles speaking to client (*Text-to-speech*)
* Handles query understanding
* Holds local variables 

When you speak to Munki, you are speaking to the body. Your command is processed into a dictionary as 
```
request = {
    'type': 'command', # other options are queryresponse, weatherpull, weatherupdate
    'command': "what's the weather like?", # a string representation of what you've said
    'profile': 'nate'   # a string of your name which is then understood as a saved dictionary on the brain
}
```
This request is then translated to a JSON string and then to binary, and sent through a socket to the brain. The body then waits for a response.
An example of a response would be
```
response = {
    'type':'basic', #other options query, error
    'phrase': "The current weather is..." a string of what is going to be said,
}
```
The response type can initate different functions on the body. A basic response is nothing other than a basic response. Nothing happens other than the phrase being spoken. If a response is a query, then it needs a response back. Typically a query response 
will also return a list of keys needed for the response, and if the body does not hear the correct response it will loop until canceled or correctly responded.
Not all queries entail a response. An example of a query could be if you asked Munki, *"How are you?"* in which Munki would response, *"I'm doing great, Nate. How about yourself?"* which would intiate a query that does not require a certain response. 

#### Brain (*server*)
pass
