import requests
import environ
from datetime import datetime, timedelta
import time

d=environ('d')
url=environ('url')
key=environ('key')

payload={'content':d}
header={'authorization':key}


print("{0}, {1}, {2}".format(d,key,url))
while 1:
    print('Run something..')
    r=requests.post(url,data=payload,headers=header)
    dt = datetime.now() + timedelta(seconds=10)

    while datetime.now() < dt:
        time.sleep(1)
