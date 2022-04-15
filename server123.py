import socket
import threading

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345
AUTH_OK = 'AUTH_OK'

def  new_client(client_socket,username):
    while True:
         msg = client_socket.recv(1024)
         msg = msg.decode('utf-8')       
         if msg == 'q':
            break
         print('From {1}: {0}'.format(msg, username))
    


def authorization(client, users):
    for i in range(3):
        client.send('Type you name: '.encode('utf-8'))
        msg = client.recv(1024)
        username = msg.decode('utf-8')
        print('username: ', username)
        if username and username not in users:
            client.send(AUTH_OK.encode('utf-8'))
            return username
    return ''

if __name__ == '__main__':
    server_socket = socket.socket()

    users = dict()

    try:
        server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
        server_socket.listen()

        client_socket, addr = server_socket.accept()
        print('Connected {0[0]}:{0[1]}'.format(addr))
        
        msg = 'Connection success!'
        client_socket.send(msg.encode('utf-8'))
        
        username = authorization(client_socket, users.keys())
        
        if username:
            users[username] = client_socket

            user_thread = threading.Thread(target=new_client, args=(client_socket, username))
            user_thread.start()
        client_socket.close()
        server_socket.close()
        
    except KeyboardInterrupt:
        server_socket.close()
        print("\nThe wrong wolf has won!:(\n")
    except Exception as e:
        server_socket.close()
        print('\nException: {0}'.format(e))

    

