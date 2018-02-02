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
`time` | Access real-time date
`json` | Speed up dictionary sorting

<!-- ## Getting Started

### Run -->

<!-- ```bash
``` -->

## Code Walkthrough

#### Step 1: Creating Blockchain Class
In `class Blockchain`: a Blockchain object will contain a series of blocks within a single chain and another array to keep track of transactions. It should also have the ability to create a new block, keep track new transactions, and provide a sophisticated hash algorithm.

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

---

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

---

#### Step 3: Adding Transactions to a Block

We will also need to feed `transactions` into each `Block`, the data goes right into `self.current_transactions`, yet the return value is the index of the block that will hold the transaction, which will be useful in later implementation.

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
---

#### Step 4: Initialize a Genesis Block in Constructor

Each Blockchain needs to be initialized with a `Genesis Block` that other blocks can build upon. One thing to notice is that this block will have an arbitrary value for previous_hash because there is technically no previous_hash during its creation.

```python
class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)
```

---

#### Step 5: Let's implement `new_block()`, `new_transaction()` and `hash()`

`new_block()`
Time to actually implements some behaviors how our Blockchain would work.
Recall from Step 2 on how a Block looks like, we will build new blocks based on the same model following a few rules:
1. Increment `index` as we go
2. Pass in current time, here we are using a function from `time` package to get real-life timestamp
3. Pass in `transactions` using our `transactions()` method
4. Erase value inside of `self.current_transactions` array since this array only serves as a temporary array to hold the most recent transaction.

```python
def new_block(self, proof, previous_hash=None):
    """
    Create a new Block in the Blockchain
    :param proof: <int> The proof given by the Proof of Work algorithm
    :param previous_hash: (Optional) <str> Hash of previous Block
    :return: <dict> New Block
    """

    block = {
        'index': len(self.chain) + 1,
        'timestamp': time(),
        'transactions': self.current_transactions,
        'proof': proof,
        'previous_hash': previous_hash or self.hash(self.chain[-1]),
    }

    # Reset the current list of transactions
    self.current_transactions = []

    self.chain.append(block)
    return block
```

`new_transaction()`
Very self-explanatory, won't elaborate on this, this newly created transaction will later feed into `new_block`

```python
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
        'recipient' : recipient,
        'amount' : amount,
    })

    return self.last_block['index'] + 1
```

`hash()`
Before feeding the string to our hashing algorithm, we need to sort the key inside our dictionary because a key in the dictionary has arbitrary order, thus disrupt output hash due to inconsistency.
We are using [SHA-256 Hashing Algorithm](https://www.youtube.com/watch?v=DMtFhACPnTY) to create hexadecimal string hash.

```python
@staticmethod
def hash(block):
    """
    Creates a SHA-256 hash of a Block
    Block String needs to be sorted for consistency, as key in dictionary genenarted
    in random order.
    :param block: <dict> Block
    :return: <str>
    """
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
```

#### Step 6: Understanding Proof of Work

To understand POW or Proof of Work, read this [blog](https://medium.com/@karthik.seshu/cryptocurrency-proof-of-work-vs-proof-of-stake-e1eee1420b10). Quote from Karthik:

> Proof of Work (PoW) as the name states is the validation of the work that happened and proving it is correct. Bitcoin and many alt coins follow this way of consensus to make sure the authenticity of the chain is good.

> To understand how it works in simple terms, assume that you are in a math exam along with other students in a classroom. The student who can, not only come up with the correct answer but also can come up with the complete proof (steps in math terms) of arriving at the correct answer first gets the reward. As we know this needs the student with a lot of brain power which naturally consumes a lot of energy from the body.

Let's take a step back and think about our hashing function again. It's very easy for a `hash()` function to generate a hash based on an input because output is consistent. however, It will cost miners a lot of computational power to use given output and reverse engineer back to the input.

for example, if the hash of some integer `x` multiplied by another `y` must end in 0. So, `hash(x * y) = ac23dc...0.` And for this simplified example, let’s fix x = 5. Implementing this in Python:

```python
from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y = {y}')
```

The solution here is `y = 21`. Since, the produced hash ends in 0:

```python
hash(5 * 21) = 1253e9373e...5e3600155e860
```

To recap: In Bitcoin, the Proof of Work algorithm is called Hashcash. And it’s not too different from our basic example above. It’s the algorithm that miners race to solve in order to create a new block. In general, the difficulty is determined by the number of characters searched for in a string. The miners are then rewarded for their solution by receiving a coin—in a transaction.

The network is able to **easily** verify their solution, but the process of reverse engineer takes up a lot of computational power.

## Notes

🐌 **@staticmethod** is a method that belongs to a class but behaves exactly like a regular function, which doesn't take any first `arg` such as `self` or `class`.

```python
@staticmethod
def hash(block):
    #Hashes a Block
    pass
```

---

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

---

> ![home](http://yuzhoujr.com/emoji/home.svg) [yuzhoujr.com](http://www.yuzhoujr.com) · ![github](http://yuzhoujr.com/emoji/github.svg) [@yuzhoujr](https://github.com/yuzhoujr) · ![linkedin](http://yuzhoujr.com/emoji/linkedin.svg) [@yuzhoujr](https://linkedin.com/in/yuzhoujr)
