import requests
import json
import time
import math

while True:
  text = 'How many Liters of water are you drinking today?(please don\'t hack me <:|)'
  url = 'https://graph.facebook.com/v20.0/###/messages' 
  headers = {'Authorization' : 'Bearer ###',
             'Content-Type': 'application/json'} 
  data = {
      "messaging_product": "whatsapp",
      "to": "###",
      "type": "text",
      "text": {
          'body' : text
          }
      }

  response = requests.post(url, headers=headers, json=data)
  time.sleep(10)
  try:
    file = open('output.txt', 'r')
    targetAmount = file.read()
    if len(targetAmount) != 1:
      continue
  except:
    time.sleep(10)
    file = open('output.txt', 'r')
    targetAmount = file.read()
    if len(targetAmount) == 1:
      break
    text = 'You didn\'t respond :('
    data = {
      "messaging_product": "whatsapp",
      "to": "###",
      "type": "text",
      "text": {
          'body' : text
          }
      }
    response = requests.post(url, headers=headers, json=data)
  break
  
targetAmount = int(targetAmount)
totalHours = 14
currentAmount = (targetAmount/ totalHours)

while currentAmount <= targetAmount:
  currentAmount += (targetAmount/ totalHours)
  text = f'Progress: {currentAmount:.2}/{targetAmount}'
  url = 'https://graph.facebook.com/v20.0/426094177249208/messages' 
  headers = {'Authorization' : 'Bearer ###',
             'Content-Type': 'application/json'} 
  data = {
      "messaging_product": "whatsapp",
      "to": "96170054477",
      "type": "text",
      "text": {
          'body' : text
          }
      }

  response = requests.post(url, headers=headers, json=data) 
  print(response.status_code)

  print(response.text)

  time.sleep(3600)