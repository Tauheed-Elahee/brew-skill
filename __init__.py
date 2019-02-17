from mycroft import MycroftSkill, intent_file_handler

from gpiozero import Servo
from time import sleep


class Brew(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('brew.intent')
    def handle_brew(self, message):
        self.speak_dialog('brew')
        servo = Servo(17)
        servo.min()
        sleep(1)
        servo.max()
        sleep(1)
        servo.min()
        sleep(1)


def create_skill():
    return Brew()

