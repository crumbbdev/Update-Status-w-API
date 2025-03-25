import requests

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
status = "Hello World!"

set_discord_status(token, status)
