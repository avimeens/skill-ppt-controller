from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.log import getLogger


class PptControllerSkill(MycroftSkill):
    def __init__(self):
	super(PptControllerSkill, self).__init__(name="PptControllerSkill")

    @intent_handler(IntentBuilder().require('PptController'))
    def handle_ppt_controller(self, message):
        self.speak_dialog('ppt.controller')


def create_skill():
    return PptControllerSkill()

