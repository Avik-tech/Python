#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ciphertext", type=str, help="encrypted message")
parser.add_argument("cipher_alphabet", type=str, help="substitute alphabet")
args = parser.parse_args()

plaintext_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = args.cipher_alphabet
ciphertext = args.ciphertext

ciphertext_decoded = ""

for i in ciphertext:
    if i.upper() in cipher_alphabet:
        index = cipher_alphabet.index(i.upper())
        ciphertext_decoded += plaintext_alphabet[index]
    else:
        ciphertext_decoded += i
print(ciphertext_decoded)
