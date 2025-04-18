# laboratory-work-2-encryption
> Implementation of secure transmission of messages by using the RSA algorithm and <br>
fast exponentiation algorithm in modular arithmetic.

### RSA algorithm <br>
`rsa_algorithm.py`
In the implementation of the algorithm, we used such libraries:
- <b>Math</b> - for calculations
- <b>Secrets</b> - for generation of 1024-bits prime numbers
- <b>Sumpy</b> - for generation of 1024-bits prime numbers
- <b>Hashlib</b> - for generation of hash of a messages

1. The algorithm starts by generating two 1024-bit prime numbers using the libraries.
2. Then we calculate the first part of the public key by multiplying the previously found prime numbers.
3. The next step is finding a small odd number whose gcd with (p-1)(q-1), where p and q are 1024-bit prime numbers, equals 1.
4. And the last step is the calculation of the private key, which is an integer, the reciprocal of a small number modulo (p-1)(q-1)

`rsa_algorithm` function returns a dictionary with all data needed for later encryption & decryption of messages.
### Encryption & Decryption
For encryption and decryption, we used the  algorithm provided in lecture 8.2 - `block cipher` <br>
The main idea of this cipher is to calculate a new block by the formula:
$$C = M^e modn$$ <br>
Decryption happens by this formula: $$M = C^d modn$$

In the ``encrypt`` function:
1. We find the maximum length of a block of symbols for the public key
2. Then we transform each symbol to a numeric value by the ord function, adding zeros to match the length of a block
3. Next, we divide the message into blocks of max length - numeric values to encrypt
4. The last step is the encryption of the numeric value we got from the formula

In the ``decrypt`` function:
1. We find the maximum length of a block of symbols for the public key
2. Next is decryption by the formula and filling it with zeros to match the length of a block
3. The last step is to loop through the message by breaking it into small blocks of max length<br>
and convert it to a symbol using the built-in function chr

### User-server communication
In this part, we worked according to the <b>socket.io</b> library and instructions in Client & Server files.

- `Client`<br>
The core functions of the class are read_handler and write_handler. <br>
`read_handler` <br>
Client receives an encrypted message and a hash from the server, decrypts it, and if the hash value is the same
prints it out; else, it shows the user that an error has occurred.
`write_handler` <br>
The client is asked to write a message. If it does not consist of whitespaces only, the message gets encrypted, and the hash value is created
to be sent to a server.


- `Server`<br>
The core functions of the class are start, handle_client, and broadcast. <br>
`start`<br>
In this function, the server begins to run, receives the keys from client(s), keeps track of connected users, and does all the manual connection job.
`handle client`<br>
In this function, the server receives the message from a client(s), decrypts it, and compares the hash values as well.
`broadcast`<br>
In this function, the server sends the message from a client(s), encrypts it, and creates the hash value.

### Hash of messages
For the implementation of this checking, we used ``hashlib`` library.<br>
<i> Example: </i><br>
When a user sends a message, he sends a hash of this message as well, generated in ``hash_message`` function.
Later, when the server decrypts it, it generates a hash of the decrypted message and compares those hashes with ``check_message_integrity`` function.


### Contributors
- [Oksana Moskviak](https://github.com/okqsna) 
- [Anastasiia Yablunovska](https://github.com/ystacy-ab)

The laboratory work was a collaborative effort between the two of us.
<br>
<I>@ Created by CS UCU students, April 2025</i> 
