import socket
import pickle
import time
import sys
                

if __name__ == '__main__':
    IP = '127.0.0.1'
    PORT = 5000
    try:
        server_client = socket.socket()
        server_client.connect((IP,PORT))
        
    except:
        print('\t\t\t-----------\nSorry for Inconvience but Server are down temporialy\n\t\t\t-----------\n')
        time.sleep(2)
        sys.exit()
    flag = True

    username = input('enter the username : ')
    uid = input("enter your device's unique id : ")
    name = input("enter name of your device : ")
    model = input("enter model name of your device : ")
    
    while flag:
        try:
            server_client.send(pickle.dumps([100, [username, uid, name, model]]))
            
        except:
            print("Connection problem")
            time.sleep(2)   
        message = pickle.loads(server_client.recv(1024))
        if message[0] == 2000:
            print(f'congratulation the transaction is accepted !! ')
            flag = False
            server_client.send(pickle.dumps([9999]))
        elif message[0] == 9999:
            print("Try again")
            flag=False
        else:
            flag = False