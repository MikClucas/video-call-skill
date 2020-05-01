from mycroft import MycroftSkill, intent_file_handler


class VideoCall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('call.video.intent')
    def handle_call_video(self, message):
        self.speak_dialog('call.video')


def create_skill():
    return VideoCall()

