import requests
from datetime import datetime, timedelta
import time

payload={'content':environ('d')}
header={'authorization':environ('key')}
while 1:
    print('Run something..')
    r=requests.post(environ('url'),data=payload,headers=header)
    dt = datetime.now() + timedelta(seconds=10)

    while datetime.now() < dt:
        time.sleep(1)
