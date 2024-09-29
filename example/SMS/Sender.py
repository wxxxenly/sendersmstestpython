import abc
class Sender(abc.ABC):
    @abc.abstractmethod
    def send(self, number, message):
        pass
    def request(self, url, content):
        print('send requset to url '+url+' with content '+content)