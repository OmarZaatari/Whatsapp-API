import requests
import json
import time

while True:
  url = 'https://graph.facebook.com/v20.0/###/messages' 
  headers = {'Authorization' : 'Bearer ###',
             'Content-Type': 'application/json'} 
  data = {
      "messaging_product": "whatsapp",
      "to": "###",
      "type": "text",
      "text": {
          'body' : "Omar Zaatari API TESTING ma ten2az please zbate"
          }
      }

  response = requests.post(url, headers=headers, json=data) 
  print(response.status_code)

  print(response.text)
  time.sleep(3600)