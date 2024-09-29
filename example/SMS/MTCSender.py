import Sender as SmsSender
class MTCSender(SmsSender):
    def send(self, number, message):
        if message.startswith('123'):
            message = message.replace ('123', '*')
        super().request('https://sms.mtc.ru/'+number, message)