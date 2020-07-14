import socket
import pickle
import time
import sys
from rsa import PublicKey,encrypt

publickey = PublicKey(19735300506366648606809216260158404176991332663628844568568026082041291980614950071160539355137829291271188972558194742721953221513772994466286888523194228311787678838953845226430147092007785706549758818109192986816887331261903861953256462164040176658411001537549117573103140507145588122488253420778855640532181785964137645395870857136938675215567810046598271028199409003312375275298936097068677737339756232305563294718805792340951177321641782846630266963106739768917160296776963166674599827856065092425962157137181596241284820050081104622439052827918934452544173902432257458043382774342045732563308224737052453803991, 65537)

def encryption(blkaddrs):
    return encrypt(blkaddrs,publickey) #send across to server

def decrypt():
    pass

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
    blkaddr = input("Enter block address : ")
    #cyphertxt = encryption(blkaddr)
    cyphertxt = int(blkaddr)
    try:
        server_client.send(pickle.dumps([100, [cyphertxt]]))
    except:
        print('error')