class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self):
        # Add a new transaction into current_transactions
        pass

    @staticmethod
    def hash(block):
        #Hashes a Block
        pass

    @property
    def last_block(self):
        #Return last block in the chain
        pass
