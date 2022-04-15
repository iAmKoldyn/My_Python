import socket
from server123 import SERVER_ADDRESS, SERVER_PORT, AUTH_OK

def authorization(server):
    for i in range(3):
        msg = server.recv(1024)
        msg = msg.decode('utf-8')
        if msg == AUTH_OK:
            print('\nAuth success!\n')
            return True
        username = input(msg)
        print(username)
        server.send(username.encode('utf-8'))
    print('\nAuthorization failed!\n')
    return False

if __name__ == '__main__':
    server_socket = socket.socket()
    try:
        server_socket.connect((SERVER_ADDRESS, SERVER_PORT))
        
        msg = server_socket.recv(1024) # receive
        msg = msg.decode('utf-8')
        print('Inbox: {0}'.format(msg))

        if authorization(server_socket):
            while True:
                out_msg = input('Your msg: ')
                server_socket.send(out_msg.encode('utf-8'))
                if out_msg == 'q':
                    break
                msg = server_socket.recv(1024) # receive
                msg = msg.decode('utf-8')
                print('From server: {0}'.format(msg))
            
        server_socket.close()

    except KeyboardInterrupt:
        server_socket.close()
        print("\nHow rude of you!\n")
    except Exception as e:
        server_socket.close()
        print('\nException: {0}'.format(e))