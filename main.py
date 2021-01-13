import RPi.GPIO as GPIO
import requests
import time # para utilizar tempo

GPIO.setmode(GPIO.BCM) #numeração BCM

GPIO.setup(5,GPIO.OUT) #porta de conexão do led
GPIO.setup(4,GPIO.IN) #resistor pull down externo

userID = 01

while True:
  if GPIO.input(4) == GPIO.LOW:
    requests.post('https://example.com/post', data = {ID : userID, state : 0)
  else:
    requests.post('https://example.com/post', data = {ID : userID, state : 1)
                                                      
  answer = requests.get('https://api.example.com/get/{}'.format(userID))
  
  if answer.raise_for_status() == None:                                                                                                        
    if answer.state == 0:
      GPIO.output(5, gpio.LOW)
    else:
      GPIO.output(5, gpio.HIGH) 
  else:
    print 'Erro de conexão'
  
GPIO.cleanup
