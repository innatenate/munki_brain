from parietal import judge
from frontal.weather import run as wrun
from frontal.uni import run as urun
from frontal.memory import run as mrun

def process(literal, profileInfo):
    keywords = literal.lower()
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    keywords = ''.join(filter(whitelist.__contains__, keywords))
    literal = keywords
    success = False
    judgement = judge.judgePhrase(keywords)
    print(keywords)
    if "weather" in judgement:
        success = wrun.process(literal, profileInfo)
    if not success or "unsure" in judgement:
        success = urun.process(literal, profileInfo)
    if not success or "memory" in judgement:
        success = mrun.process(literal, profileInfo)
    if not success:
        print("override")
        success = wrun.process(literal, profileInfo, override=True) 
        if not success:
            success = urun.process(literal, profileInfo, override=True)
            if not success:
                success = mrun.process(literal, profileInfo, override=True)
 
    if not success:
        raise FileNotFoundError("no process holds connections connectable to query")