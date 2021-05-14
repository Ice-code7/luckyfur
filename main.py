import requests
import environ
from datetime import datetime, timedelta
import time

payload={'content':environ('d')}
header={'authorization':environ('key')}

print("{0}, {1}, {2}".format(environ('d'),environ('key'),environ('url')))
while 1:
    print('Run something..')
    r=requests.post(environ('url'),data=payload,headers=header)
    dt = datetime.now() + timedelta(seconds=10)

    while datetime.now() < dt:
        time.sleep(1)
