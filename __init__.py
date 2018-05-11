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

    @intent_handler(IntentBuilder("OpenPPTIntent").require('OpenPPT').require("Filename"))
    def handle_ppt_open(self, message):
	filename = message.data.get("Filename")
	response = {'filename' : filename}
	self.enclosure.mouth_text("Nova opening file " + filename)
	# Send a rest request
        self.speak_dialog('ppt.open', data=response)

    @intent_handler(IntentBuilder("NextSlideIntent").require('NextSlide'))
    def handle_next_slide(self, message):
	# Send a rest request
        self.speak_dialog('ppt.next')

    @intent_handler(IntentBuilder("PrevSlideIntent").require('PrevSlide'))
    def handle_prev_slide(self, message):
	# Send a rest request
        self.speak_dialog('ppt.prev')

    @intent_handler(IntentBuilder("ClosePPTIntent").require('ClosePPT'))
    def handle_ppt_close(self, message):
	# Send a rest request
        self.speak_dialog('ppt.close')


def create_skill():
    return PptControllerSkill()

