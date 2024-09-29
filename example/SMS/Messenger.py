import MTCSender
import MegafonSender
import YotaSender
import BeelineSender

class Messenger():

    def __init__(self, new_dict_senders=None):
        self._senders = {"+7894":MTCSender(), "+7999":BeelineSender(), "+7903":MegafonSender(), "+7824":YotaSender()}
        if new_dict_senders:
            self._senders.update(new_dict_senders)

    def send_message(self, message, number):
        for i in self._senders:
            if number.startswith(i):
                self._senders[i].send(number, message)