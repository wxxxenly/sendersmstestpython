import Sender
class BeelineSender(Sender):
    def send(self, number, message):
        super().request('https://sms.beeline.ru/'+number, message)