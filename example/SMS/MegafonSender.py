import Sender
class MegafonSender(Sender):
    def send(self, number, message):
        super().request('https://sms.megafon.ru/'+number, message)