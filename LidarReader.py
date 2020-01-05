import serial
import time
from gtts import gTTS
import os
import numpy as np

class LidarReader:

    def __init__(self):
        print("New Lidar Reader")
        self.total = 15
        self.errors = 0

    def read_from_arduino(self):
        data = []

        ser = serial.Serial('/dev/cu.usbmodem14401', 115200)
        # Read and record the data
        data = []  # empty list to store the data
        for i in range(self.total):
            b = ser.readline()  # read a byte string
            print(b)
            if len(b)>5:
                string_n = b.decode().rstrip() # decode byte string into Unicode
                print(string_n)
                data.append(string_n.split('cm')[0])
            else:
                print("WOULD HAVE BEEN AN ERROR")
                self.errors = self.errors + 1

        print(data)
        return data

    def parse_arduino_data(self):
        total = 0
        distance = ""
        # The text that you want to convert to audio
        data = self.read_from_arduino()
        results = list(map(int, data))
        for number in results:
            total = total + number
        maxim = self.total - self.errors
        average = round(total/maxim)

        if(average > 100):
            tupla = divmod(average,100)
            meters = tupla[0]
            centimeters = tupla[1]
            distance = str(meters) + "meters and" +str(centimeters)+ "centimeters"
        else:
            distance = str(average)+ "centimeters"
        return distance


    def play_the_audio(self, object):

        distance = self.parse_arduino_data()
        mytext = "You have a " + object + " in" + distance

        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg321 welcome.mp3")





if __name__ == "__main__":
    while True:
        lidar = LidarReader()
        lidar.play_the_audio("chair")
