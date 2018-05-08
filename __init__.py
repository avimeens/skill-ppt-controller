from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class PptControllerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('PptController'))
    def handle_ppt_controller(self, message):
        self.speak_dialog('ppt.controller')


def create_skill():
    return PptControllerSkill()

