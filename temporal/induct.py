from temporal.longterm import friends
from temporal.longterm import nate
from temporal.longterm import self
from temporal.longterm import weather

from temporal import shortterm

def ltCommit(request, rewrite=True):
    '''longterm request format
    request dict
    saveplace list
    savename str
    savetype str
    save'''

    if rewrite:
        if 'friends' in request['saveplace'][0]:
            if request['savetype'] == 'fold':
                friends.memories[request['savename']] = request['save']
            elif request['savetype'] == 'cell':
                friends.memories[request['saveplace'][1]][request['saveplace'][2]] = request['save']
            elif request['savetype'] == 'neuron':
                friends.memories[request['saveplace'][1]][request['saveplace'][2]][request['saveplace'][3]] = request['save']