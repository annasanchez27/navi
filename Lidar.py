import serial
import time
from gtts import gTTS
import os

class LidarReader:

    def __init__(self):
        print("New Lidar Reader")

    def read_from_arduino(self):
        data = []
        ser = serial.Serial('/dev/tty.usbmodem1411', 115200)
        time.sleep(2)
        # Read and record the data
        data = []  # empty list to store the data
        for i in range(25):
            b = ser.readline()  # read a byte string
            string_n = b.decode() .rstrip() # decode byte string into Unicode
            print(string_n)
            data.append(string_n.split('cm')[0])
        print(data)
        return data

    def play_the_audio(self):
        # The text that you want to convert to audio
        data = self.read_from_arduino()
        centimeters = data.__getitem__(3)

        print(centimeters)
        mytext = "You have an object in" + centimeters + "centimeters"

        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg321 welcome.mp3")


if __name__ == '__main__':
    read = LidarReader()
    while True:
        read.play_the_audio()
        time.sleep(3)

