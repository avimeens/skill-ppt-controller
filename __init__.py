import requests
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.log import getLogger


class PptControllerSkill(MycroftSkill):
    def __init__(self):
	super(PptControllerSkill, self).__init__(name="PptControllerSkill")
	self.url = "http://135.222.162.94:8001"
	self.file_opened = False

    @intent_handler(IntentBuilder("PPTIntent").require('PptController'))
    def handle_ppt_controller(self, message):
        self.speak_dialog('ppt.controller')

    @intent_handler(IntentBuilder("OpenPPTIntent").require('OpenPPT').require("Filename"))
    def handle_ppt_open(self, message):
	filename = message.data.get("Filename")
	self.enclosure.mouth_text("Nova opening file " + filename)
	self.file_opened = True;
	# Send a rest request
	param = {'filename':filename}
	self.enclosure.mouth_text("Sending request to " + self.url);
	response = requests.get(self.url, param)
	resp = {'filename' : filename}
	if response.status_code == requests.codes.ok:
        	self.speak_dialog('ppt.open', data=resp)
	else: 
		self.speak_dialog('ppt.filenotfound')

    @intent_handler(IntentBuilder("NextSlideIntent").require('NextSlide'))
    def handle_next_slide(self, message):
	if self.file_opened: 
		# Send a rest request
		nurl = self.url + "/nextpage"
		self.enclosure.mouth_text("Sending request to " + nurl);
		response = requests.get(nurl)
		if response.status_code == requests.codes.ok:
        		self.speak_dialog('ppt.next')
		else: 
			self.speak_dialog('ppt.filenotfound')
	else: 
		self.speak_dialog('ppt.filenotopen')

    @intent_handler(IntentBuilder("PrevSlideIntent").require('PrevSlide'))
    def handle_prev_slide(self, message):
	# Send a rest request
	if self.file_opened: 
		# Send a rest request
		purl = self.url + "/prevpage"
		self.enclosure.mouth_text("Sending request to " + purl);
		response = requests.get(purl)
		if response.status_code == requests.codes.ok:
        		self.speak_dialog('ppt.prev')
		else: 
			self.speak_dialog('ppt.filenotfound')
	else: 
		self.speak_dialog('ppt.filenotopen')

    @intent_handler(IntentBuilder("ClosePPTIntent").require('ClosePPT'))
    def handle_ppt_close(self, message):
	# Send a rest request
	if self.file_opened: 
		purl = self.url + "/close"
		self.enclosure.mouth_text("Sending request to " + purl);
		response = requests.get(purl)
		if response.status_code == requests.codes.ok:
        		self.speak_dialog('ppt.close')
		else: 
			self.speak_dialog('ppt.filenotfound')
	else: 
		self.speak_dialog('ppt.filenotopen')


def create_skill():
    return PptControllerSkill()

