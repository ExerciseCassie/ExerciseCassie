import datetime

def GetTimeZone():
    dt_now = datetime.datetime.now()
    if dt_now.hour < 12:
        return 1
    else:
        return 2

res = GetTimeZone()
if res == 1:
    print('おはよう')
else:
    print('こんばんは')
        