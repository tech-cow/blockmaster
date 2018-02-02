<h3 style="text-align:center;font-weight: 300;" align="center">
  <img src="http://yuzhoujr.com/logo/blockMaster.png" width="160px">
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/downloads-0k-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/build-passing-yellow.svg?style=flat-square">
</p>


>

<!-- ## Features -->

 ## External Libraries

Third Party library are used in this project

Package    |      Description
---------- | :--------------------:
`hashlib`  | SHA-256 Algorithm Core
`datetime` | Access real-time date

<!-- ## Getting Started

### Run -->

<!-- ```bash
``` -->

### Code Walkthrough

#### Step 1: Creating Blockchain Class
In `class Blockchain`: a Blockchain object will contains a series of blocks within a single chain and another array to keep track of transactions. It should also have the ability to create new block, keep track new transactions, and provide a sophisticated hash algorithm.

```python
# Abstract Data Type of a Blockchain
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
```

#### Step 2: Define a Block
A single `Block` consist the following data: an `index`, a `timestamp` (in Unix time), a list of `transactions`, a `proof`(implemented later), and the `hash` of the previous Block.

Here is how a single entry looks like:
```python
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}

```
#### Step 3: Adding Transactions to a Block

We will also need to feed transactions into each Blocks, the new_transaction function is quite straight-forward as the following.

```python
class Blockchain(object):
    ...

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
```
























### Lessons learned

🐌 **@staticmethod** is a method that belongs to a class but behaves exactly like a regular function, which doesn't take any first `arg` such as `self` or `class`.

```python
@staticmethod
def hash(block):
    #Hashes a Block
    pass
```

--------------------------------------------------------------------------------

🍜 **@property** is a shortcut for creating read-only properties. which, in turn, is the simplified syntax for creating a `property` with just a getter.

```python
@property
def x(self):
    return self._x
```

is equivalent to

```python
def getx(self):
    return self._x
x = property(getx)
```

## Demo

## License

🌱 MIT 🌱

--------------------------------------------------------------------------------

> ![home](http://yuzhoujr.com/emoji/home.svg) [yuzhoujr.com](http://www.yuzhoujr.com) · ![github](http://yuzhoujr.com/emoji/github.svg) [@yuzhoujr](https://github.com/yuzhoujr) · ![linkedin](http://yuzhoujr.com/emoji/linkedin.svg) [@yuzhoujr](https://linkedin.com/in/yuzhoujr)
