# Example of socket implementation

Simple work with sockets between server and client apps for *nix (linux, MacOS etc.)

This code was made to practice using Linux/Unix OS interprocess communication.
The first class, serversocketexchange.py - is intended to simulate server work
The second class, clientsocketexchange.py - is intended to simulate the work of the client.

It is necessary to run serversocketexchange.py, specifying in the code in the section 
```py
if __name__ == '__main__':...
```
when creating a server instance - the path to the socket file will be created using the UNIX protocol. The same path should be specified in a similar section of clientsocketexchange.py. Also in clientsocketexchange.py you can write your own message (not necessarily 'Hello world', you can use letters of other alphabet, what is suitable for UTF-8) and run it in another terminal (as the server should be running at the moment).
As a result, the necessary message will appear on the server side.

The .encode and .decode methods are used in the hear() and say() methods of both classes for transmitted messages, since bytes are exchanged when working with the socket, so decoding and encoding must be used.
