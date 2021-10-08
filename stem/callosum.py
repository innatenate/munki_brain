from parietal import process

def process_request(request, type):
    if type == "spinalreceive":
        if request['type'] == 'commandfire':
            process(request, 'command')