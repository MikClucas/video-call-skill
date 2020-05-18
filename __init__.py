from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder


class VideoCall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        super().__init__()

    @intent_file_handler('call.video.intent')
    def handle_call_video(self, message):
        person = message.data.get('person')
        if person is not None:
            if person == 'michael' or person == 'philip':
                self.speak_dialog('call.video')
            else:
                self.speak_dialog('who.should.i.call', {'person': person})
        else:
            self.speak_dialog('who.should.i.call', {'person': "unknown"})

def stop(self):
    pass

def create_skill():
    return VideoCall()


