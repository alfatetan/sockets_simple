import socket


class ServerSocketExchange(object):
    def __init__(self, path=''):
        MAX_CLIENT_CONNECT = 10
        DEFAULT_PATH_TO_SOCK = '/Users/RyabovSergey/Projects/my_srv_sock'

        self.path_to_sock = DEFAULT_PATH_TO_SOCK if not path else path

        self.srv_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.srv_sock.bind(self.path_to_sock)
        self.srv_sock.listen(MAX_CLIENT_CONNECT)

        return

    def __del__(self):
        self.srv_sock.close()
        return

    @property
    def descriptor(self):
        return self.srv_sock.fileno()

    def hear(self):
        """
        Listening the socket and return message
        :return: msg
        """
        self.client_sock, self.client_addr = self.srv_sock.accept()

        msg = ''
        while True:
            data = self.client_sock.recv(1)
            if not data or data == '\r':
                break
            else:
                msg += data.decode('utf-8')

        return msg

    def say(self, msg=''):
        """
        Saying whatever
        :return: True/False
        """
        msg += '\r'
        self.client_sock.sendall(msg.encode())
        return


if __name__ == '__main__':
    my_srv = ServerSocketExchange()
    while True:
        msg = my_srv.hear()
        print(msg)
        if not msg:
            break
