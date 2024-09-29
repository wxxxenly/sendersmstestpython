import sys
sys.path.append('F:/example/SMS')

from SMS import Messenger, Sender

class TinkoffSender(Sender):
    def send(self, number, message):
        super().request('https://sms.tinkoff.ru/'+number, message)

class SberMobileSender(Sender):
    def send(self, number, message):
        super().request('https://sms.sbermobile.ru/'+number, message)

messanger = Messenger({'+7123':TinkoffSender(),'+7777':SberMobileSender()})
number, message = input(), input()

if len(message) > 0:
    messanger.send_message(message, number)
else:
    print("Error")
