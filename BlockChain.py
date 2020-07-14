from ecdsa import SigningKey
from rsa import key, prime
import time
from hashlib import sha256
from json import dumps


class BlockChain:
    def __init__(self):
        genesis_block = {
            'block_id': 0,
            'previous_hash': '',
            'miner': '',
            'm_root': '',
            'timestamp': time.time(),
            'public_key': '19735300506366648606809216260158404176991332663628844568568026082041291980614950071160539355137829291271188972558194742721953221513772994466286888523194228311787678838953845226430147092007785706549758818109192986816887331261903861953256462164040176658411001537549117573103140507145588122488253420778855640532181785964137645395870857136938675215567810046598271028199409003312375275298936097068677737339756232305563294718805792340951177321641782846630266963106739768917160296776963166674599827856065092425962157137181596241284820050081104622439052827918934452544173902432257458043382774342045732563308224737052453803991, 65537',
            'transaction': []
        }

        self.blockchain = [genesis_block]
        #self.add_block()
        #self.print_chain()

    def add_block(self,tran):
        block_id = self.blockchain[-1]['block_id'] + 1
        public_key = SigningKey.generate()
        vk = public_key.verifying_key.to_string()
        pu_key, private_key = key.newkeys(2048)
        miner = input('Enter the Miner id: ')
        trans = self.add_transaction(public_key,tran)
        previous_hash = sha256(dumps(self.blockchain[-1]).encode()).hexdigest()
        m_root = self.m_root(trans)
        block = {
            'block_id': block_id,
            'previous_hash': previous_hash,
            'miner': miner,
            'm_root': m_root,
            'timestamp': time.time(),
            'public_key': public_key.to_string().hex(),
            'auth_public_key': str(pu_key)[10:-1],
            'transaction': trans
        }
        self.blockchain.append(block)
        self.creating_file(vk, private_key)

    @staticmethod
    def add_transaction(signing_key,tran):
        transaction = []
        end_time = time.time() + 10

        while time.time() < end_time:
            data = tran[0]+tran[1]+tran[2]+tran[3];
            signature = signing_key.sign(data.encode())
            transaction.append(signature.hex())
        return transaction

    def m_root(self, trans):
        n = len(trans)
        while n > 1:
            if n & 1:
                trans.append(trans[-1])
            trans = [self.create_hash(str.encode(trans[i] + trans[i + 1])) for i in range(0, len(trans), 2)]
            n = len(trans)
        return trans

    def create_hash(self, block):
        return sha256(block).hexdigest()

    def creating_file(self, vk, private_key):
        file_obj = open('private_key_rsa.txt', 'w')
        file_obj.write(str(private_key)[11:-1])
        file_obj.close()

    def print_chain(self):
        print('-----------------------------------')
        for i in self.blockchain:
            for data in i:
                print(data, ":", i[data])
            print('------------------------------------------')



