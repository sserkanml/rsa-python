# RSA Algorithm Implementation in Python

This is a simple implementation of the RSA (Rivest-Shamir-Adleman) encryption and decryption algorithm using Python.

## Introduction

RSA is a widely used public-key encryption algorithm. It uses a pair of keys, a public key for encryption, and a private key for decryption. The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the factoring problem.

## Implementation Details

The implementation consists of the following main steps:

1. **Key Generation**: Two large prime numbers, `p` and `q`, are generated. The product of `p` and `q` is used as the modulus `n` for both the public and private keys. The public key also includes an exponent `e`, while the private key includes an exponent `d`.

2. **Encryption**: A message `m` is encrypted using the public key `(n, e)` to produce the ciphertext `c`. The encryption function is defined as `c ≡ m^e (mod n)`.

3. **Decryption**: The ciphertext `c` is decrypted using the private key `(n, d)` to recover the original message `m`. The decryption function is defined as `m ≡ c^d (mod n)`.

## Usage

To use this implementation, follow these steps:

1. Open a Python environment.

2. Run the `main.py` and give a custom parameter being integer file.

3. You will be prompted to either generate new keys or use existing ones.

4. If you choose to generate new keys, the program will create new public and private keys.

5. Enter a message to encrypt or decrypt.

6. Follow the prompts to encrypt or decrypt the message.

## Files

- `main.py`: Contains the RSA implementation.
- `README.md`: This file.

## Dependencies

This implementation does not rely on any external libraries.

## Note

This is a basic implementation for educational purposes. In practice, RSA encryption involves additional considerations, such as padding schemes and optimizations for performance and security.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
