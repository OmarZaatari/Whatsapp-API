import requests
import json

url = 'https://graph.facebook.com/v20.0/SENDER-ID/messages' 
headers = {'Authorization' : 'Bearer API-KEY',
           'Content-Type': 'application/json'} 
data = {
    "messaging_product": "whatsapp",
    "to": "PHONE-NUMBER",
    "type": "text",
    "text": {
        'body' : "DRINK WATER!"
        }
    }

response = requests.post(url, headers=headers, json=data) 
print(response.status_code)

print(response.text)
