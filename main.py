import requests
from datetime import datetime, timedelta
import time

payload={'content':'hello'}
header={'authorization':'NTk1MTczMTc4MTA0NDc5NzU0.YGZtGw.QVE4fzfAoZoT0-m7nAlComBnTzY'}
while 1:
    print('Run something..')
    r=requests.post("https://discord.com/api/v9/channels/759805769566257193/messages",data=payload,headers=header)
    dt = datetime.now() + timedelta(seconds=10)

    while datetime.now() < dt:
        time.sleep(1)