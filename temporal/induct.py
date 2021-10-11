from temporal.longterm import friends
from temporal.longterm import nate
from temporal.longterm import self
from temporal.longterm import profiles
from temporal.longterm import weather

from temporal import shortterm
from temporal import grab

def ltCommit(request, rewrite=True):
    '''\tlongterm request format\trequest dict\tsaveplace list\tsavename str\tsavetype str\tsave\n'''

    if rewrite:
        if 'friends' in request['saveplace'][0]:
            if request['savetype'] == 'fold':
                friends.memories[request['savename']] = {}
            elif request['savetype'] == 'cell':
                friends.memories[request['saveplace'][1]][request['savename']] = {}
            elif request['savetype'] == 'neuron':
                friends.memories[request['saveplace'][1]][request['saveplace'][2]][request['savename']] = request['save']
        if 'profiles' in request['saveplace'][0]:
            if request['savetype'] == 'fold':
                profiles.memories[request['savename']] = {}
            elif request['savetype'] == 'cell':
                profiles.memories[request['saveplace'][1]][request['savename']] = {}
            elif request['savetype'] == 'neuron':
                profiles.memories[request['saveplace'][1]][request['saveplace'][2]][request['savename']] = request['save']

def inituser(name):
    if type(name) is dict:
        return name
    success = grab.requestMemory('longterm',{'type':'fold','path':['profiles',name], 'check':name}, returnMem=True)
    if success:
        return success
    else:
        ltCommit({'saveplace':['profiles'], 'savetype':'fold', 'savename':name})
        ltCommit({'saveplace':['profiles', name], 'savetype':'cell', 'savename':'info'})
        ltCommit({'saveplace':['profiles', name, 'info'], 'savetype':'neuron', 'savename':'prefname', 'save':name})
        success = grab.requestMemory('longterm',{'type':'fold','path':['profiles',name], 'check':name}, returnMem=True)
        print(success)
        return success
        
def stCommit(request, rewrite=True):
    '''short term request format\trequest dict\tsavename str\tsave'''
    shortterm.memories[request['savename']] = request['save']
    if len(shortterm.memories) > 15:
        shortterm.memories.pop(len(shortterm.memories)-1)