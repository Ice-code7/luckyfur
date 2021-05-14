import requests
import environ
from datetime import datetime, timedelta
import time

d="!work"
url="https://discord.com/api/v9/channels/833277824324468776/messages"
key="Nzk5NTYxMDk2Nzk3MjI0OTgy.YJ60Tw.SpHg7HoRk9K7wgC29swMj_87IJU"

payload={'content':d}
header={'authorization':key}


print("{0}, {1}, {2}".format(d,key,url))
while 1:
    print('Run something..')
    r=requests.post(url,data=payload,headers=header)
    print(r)
    dt = datetime.now() + timedelta(hours=1)

    while datetime.now() < dt:
        time.sleep(1)
