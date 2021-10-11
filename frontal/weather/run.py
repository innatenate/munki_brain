queries = []
queryKeys = []

class Query():
    def __init__(self, queryName, queryKeys, queryFunction, querySTContext=None, whitelist=None, require=None):
        self.name = queryName,
        self.function = queryFunction,
        self.keys = queryKeys,
        self.STContext = querySTContext
        self.whitelist = whitelist
        self.require = require

        if querySTContext is not None:
            self.context = True
        else:
            self.context = False
    
    def grade(self, keyword, literal, override=False):
        truePass = False
        for key in self.keys:
            points = 0
            for kword in key:
                for word in keyword:
                    if self.require is not None and word in self.require:
                        points += 1.5
                        truePass = True
                    if self.whitelist is not None and word in self.whitelist:
                        points -= 5
                    if word == kword:
                        points += 1
        if (points > (len(keyword) * .74) or points > (len(key) * .74)) or (override and points > (len(keyword) * 0.5)):
            if truePass and self.require is not None:
                return True, self.name
            elif not truePass and self.require is None:
                return True, self.Name
        return False


    def trace(self, boolean=True):
        if not boolean:
            return
        else:
            print(f"Success performing command {self.name}.")
            pass

    def fire(self, keywords, additionalArgs=None, additionalArgs2=None):
        success = self.function(self, keywords, additionalArgs, additionalArgs2)
        if success:
            Query.trace(self, self.context)
            return True
        else:
            raise Exception(f"Failed to fire function {self.name}")

def exampleFunction(keywords, additionalArgs=None, additionalArgs2=None):
    if "print" in keywords:
        print("Printing")
        return True
    elif "error" in keywords:
        raise Exception("Throwing an error")
    return False

example = Query("example", ["print this", "could you print", "throw an error", "error"], exampleFunction, require=["print","error"])
queries.append(example)
queryKeys.append(example.keys)

def process(literal, profileInfo, override=False):
    
    pass