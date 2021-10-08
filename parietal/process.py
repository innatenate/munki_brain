from parietal import judge
from frontal.weather import run as wrun
from frontal.uni import run as urun
from frontal.memory import run as mrun

def process(literal):
    keywords = literal.lower()
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    keywords = ''.join(filter(whitelist.__contains__, keywords))

    judgement = judge.judgePhrase(keywords)
    if "weather" in judgement:
        success = wrun.process(literal)
    if not success or "unsure" in judgement:
        success = urun.process(literal)
    if not success or "memory" in judgement:
        success = mrun.process(literal)
    if not success:
        print("override")
        success = wrun.process(literal, override=True) 
        if not success:
            success = urun.process(literal, override=True)
            if not success:
                success = mrun.process(literal, override=True)
 
    if not success:
        raise FileNotFoundError("no process holds connections connectable to query")