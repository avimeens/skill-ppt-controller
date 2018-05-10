import requests
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.log import getLogger


class PptControllerSkill(MycroftSkill):
    def __init__(self):
	super(PptControllerSkill, self).__init__(name="PptControllerSkill")
	self.rest_endpoint = "http://135.104.238.160"

    @intent_handler(IntentBuilder("PPTIntent").require('PptController'))
    def handle_ppt_controller(self, message):
        self.speak_dialog('ppt.controller')

    @intent_handler(IntentBuilder("OpenPPTIntent").require('OpenPPT'))
    def handle_ppt_controller(self, message):
	// Send a rest request
        self.speak_dialog('ppt.open')

    @intent_handler(IntentBuilder("ClosePPTIntent").require('ClosePPT'))
    def handle_ppt_controller(self, message):
	// Send a rest request
        self.speak_dialog('ppt.close')


def create_skill():
    return PptControllerSkill()

