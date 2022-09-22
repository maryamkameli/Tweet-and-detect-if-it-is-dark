api_key = 'zqJyVqK34hvrX3Zw18ZUefcJ9'
api_secret = '9iajak7RB5J8tvCoyjziRTwzohSXz2DncdjYTGrLE375c2jX0i'
access_token = '1141720970522189824-YSYY8bpjnZDxaD09GdPnEQXbktIgRO'
access_secret = 'ru8FNB2HpbspAOetoutXuIIWDJerE3X1yxFE3TUrCkJZf'

#sensors&iot
import tweepy
from grove.adc import ADC
import time
from datetime import datetime, timedelta

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



adc = ADC(0x08)
button_port = 0 # Modify this if you're using a different port for your button
light_sensor_port = 2 # Grad students only. Modify this if you're using a different port for your light sensor
button = thebutton(button_port)
light_sensor = GroveLightSensor(light_sensor_port)       

cooldown_seconds = 30 # The program will prevent you from tweeting again until this many seconds have passed. Be careful as we could quickly exceed our API limit

class GroveLightSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC(0x08)
 
    @property
    def light(self):
        value = self.adc.read(self.channel)
        return value
      
class thebutton:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC(0x08)
 
    @property
    def ispressed(self):
        value = self.adc.read(self.channel)
        return value
      
def is_button_pressed():
     # YOUR CODE HERE: Check if the button is pressed. If the analog port is >= 500, the button is pressed. Return True or False
                    # Perform an analog read using the adc variable defined above.
    if button.ispressed >= 500:
        return True
    else:
        return False

def is_dark():
       # Grad Students Only
                    # YOUR CODE HERE: Read from the light sensor. If it is dark, include that information in your tweet.
                    # Again, perform an analog read using the adc variable defined above.
    if light_sensor.light < 500:
        return True
    else:
        return False

def tweet():

                    # YOUR CODE HERE: Look at the tweepy documentation to see how to send a tweet. The twitter API variable is stored in 'api'
                    # Your tweet should include your and your partner's names, the current time (datetime.datetime.now()),
                    # and, if you are a grad student, whether or not it is dark.
    if is_dark():
        status = "Maryam, The room is Dark!"
        
    else:
        status = "Maryam, The room is Bright!"
    x = datetime.now
    dateTimeStr = str(x)
    api.update_status(status+dateTimeStr)

# Do not modify below this line
next_tweet_time = datetime.now()
while True:
    if is_button_pressed() and datetime.now() > next_tweet_time:
        next_tweet_time = datetime.now() + timedelta(seconds = cooldown_seconds)
        tweet()
    time.sleep(0.1)
