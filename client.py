import socket
import os

socket_address = '/tmp/socket_test.sock'
print 'Connecting...'
if os.path.exists(socket_address):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(socket_address)
    print 'Ready to stream data'
    print 'Ctrl-C to quit'
    print 'Sending "DONE" will shut down the server and quit the client'

    while True:
        try:
            msg = raw_input('> ')
            if msg:
                print 'SEND: {}'.format(msg)
                client.send(msg)
                if msg == 'DONE':
                    print 'Shut it all down'
                    break
        except KeyboardInterrupt, e:
            print 'Shutting client down'
    client.close()
else:
    print 'No Socket to which to connect'
print 'Process complete'
