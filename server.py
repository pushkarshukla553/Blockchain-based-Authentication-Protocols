import socket
import pickle
import BlockChain

def recieveMessages(client_socket):
    try:
        message = pickle.loads(client_socket.recv(1024))
        if not len(message):
            return False
        return message
    except:
        return False

def server_program():
    
    blockchain = BlockChain.BlockChain()
    # get the hostname
    host = '127.0.0.1'
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = recieveMessages(conn)
        if not data:
            break
        if(data[0] == 100):
            print("data recieved")
            blockchain.add_block(data[1])
            conn.send(pickle.dumps([2000]))  # send data to the client
        elif(data[0] == 200):
            print("Authentication")
            break
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()