from time import sleep
import socket
import socketserver

class Stream(object):
    """
    Reading the book by words for stream generation
    """

    def __init__(self, bookname):
        """
        Open the book and generate the words
        :param bookname: path to txt file with book
        """
        with open(bookname, 'r') as book:
            self.all_words = book.read().split()
        return

    def get_word(self):
        return self.all_words.pop(0)

    def get_words(self, value=1, wait=0):
        """
        Generating words from book
        :param words: how much words you need take from book. Default = 1
        :return: several words from book
        """
        while value:
            sleep(wait)
            yield self.get_word()
            value -= 1
        return

    def stream(self, wait=.300):
        """
        Generating words from stream
        :return: stream
        """
        while self.all_words.__len__():
            sleep(wait)
            yield self.get_word()


if __name__ == '__main__':
    stream = Stream('book.txt')
    # for w in stream.stream():
    #     print(w)
    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    print(srv_socket.fileno())
    srv_socket.accept()
    srv_socket.recv(1)
