import socket


class ClientSocketExchange(object):
    def __init__(self, path=''):
        DEFAULT_PATH_TO_SOCK = '/Users/RyabovSergey/Projects/my_srv_sock'

        self.path_to_sock = DEFAULT_PATH_TO_SOCK if not path else path

        self.client_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.client_sock.connect(self.path_to_sock)
        return
    
    def __del__(self):
        self.client_sock.close()
        return
    
    def hear(self):
        """
        Hearing whatever
        :return: msg - message from server
        """
        msg = ''
        while True:
            data = self.client_sock.recv(1)
            if not data or data == '\r':
                break
            msg += data

        return msg
    
    def say(self, msg):
        """
        Saying whatever
        :param msg: message to server
        :return:
        """
        msg += '\r'
        self.client_sock.sendall(msg.encode())
        return


if __name__ == '__main__':
    client = ClientSocketExchange()
    client.say('Hello world')
