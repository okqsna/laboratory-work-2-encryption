# laboratory-work-2-encryption
> Implementation of secure transmission of messages by using the RSA algorithm and <br>
fast exponentiation algorithm in modular arithmetic.

### RSA algorithm <br>
`rsa_algorithm.py`
In the implementation of the algorithm, we used such libraries:
- <b>Math</b> - for calculations
- <b>Secrets</b> - for generation of 2064-bits prime numbers

1. The algorithm starts with generating two 2064-bit prime numbers by the library <b>secrets</b>.
2. Then we calculate the first part of the public key by multiplying previously found prime numbers.
3. The next step done is finding a small odd number whose gcd with (p-1)(q-1), where p and q are 2064-bit prime numbers, is equal to 1.
4. And the last step is the calculation of the private key, which is an integer, the reciprocal of a small number modulo (p-1)(q-1)

`rsa_algorithm` function returns a dictionary with all data needed for later encryption & decryption of messages.
### Encryption & Decryption


### User-server communication
In this part, we worked according to the <b>socket.io</b> library demands.

### Hash of messages

### Contributors
- [Oksana Moskviak](https://github.com/okqsna) - RSA algorithm, user-server communication, documentation
- [Anastasiia Yablunovska](https://github.com/ystacy-ab) - Encryption & Decryption


<I>@ Created by CS UCU students, April 2025</i> 
