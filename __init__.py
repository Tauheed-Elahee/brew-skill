from mycroft import MycroftSkill, intent_file_handler


class Brew(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('brew.intent')
    def handle_brew(self, message):
        self.speak_dialog('brew')


def create_skill():
    return Brew()

