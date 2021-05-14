import requests
from datetime import datetime, timedelta
import time

payload={'content':'hello'}
header={'authorization':'Nzk5NTYxMDk2Nzk3MjI0OTgy.YJ6e2w.j8KgwyyHxCJ8WrSjsKZHfIo_PnU'}
while 1:
    print('Run something..')
    r=requests.post("https://discord.com/api/v9/channels/784868852681015337/messages",data=payload,headers=header)
    dt = datetime.now() + timedelta(seconds=10)

    while datetime.now() < dt:
        time.sleep(1)
