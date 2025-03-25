import requests
import time
import psutil
from datetime import datetime

def set_discord_status(token, status):
    url = "https://discord.com/api/v8/users/@me/settings"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "status": "online",  # idle, dnd, invisible, online
        "custom_status": {
            "text": status
        }
    }
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"Status Updated: {status}")
    else:
        print(f"Failed to update status... Error Code: {response.status_code} - {response.text}")

token = open("token.data").read()

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1)

    status = f"{current_time} // CPU: {cpu_usage}%"

    set_discord_status(token, status)

    time.sleep(2)
