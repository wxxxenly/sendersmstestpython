import Sender
class YotaSender(Sender):
    def send(self, number, message):
        if message.startswith("Привет"):
                message = message.replace("Привет", "Добрый вечер")
        super().request('https://sms.yota.ru/'+number, message)