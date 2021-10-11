from parietal import process
from temporal import induct
import time
import traceback
import json
lastProcessed = None

def process_request(request, type, profile=None):
    global lastProcessed
    if type == "clientrequest":
        if request['type'] == 'commandfire':
            if profile is None:
                raise Exception("You must specify a profile.")
            else:
                profile = induct.inituser(profile)
                try:
                    process.process(request['msg'], profile)
                except Exception as e:
                    print(repr(e))
                    traceback.print_tb(e.__traceback__)
                    lastProcessed = False
                for x in range(0,10):
                    time.sleep(1)
                    print("processing")
                    if lastProcessed is not None:
                        break
                if lastProcessed is None or lastProcessed == False:
                    return False, "Could not process request."
                phrase = f'lastProcessed{profile["info"]["prefname"]}'
                induct.stCommit({'savename': phrase, 'save': lastProcessed})
                returnP = json.dumps(lastProcessed)
                lastProcessed = None
                return True, returnP