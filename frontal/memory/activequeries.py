currentQueries = {}
pastQueries = {}
queryLimit = 10

def add(query, profname):
    '''    query = {
        'keys':['good', 'fair', 'excellent', 'great', 'thanks', 'thank', 'wonderful', 'you'],
        'func': None,
        'type': 'key-specific',
    }'''
    if profname in currentQueries:
        pastQueries[profname] = currentQueries[profname]
        currentQueries[profname] = query
    else:
        currentQueries[profname] = query
    if len(pastQueries) > queryLimit:
        pastQueries.pop(len(pastQueries)-1)