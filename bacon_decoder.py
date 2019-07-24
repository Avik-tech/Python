#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("bacon_text", type=str, help="encrypted message")
args = parser.parse_args()

bacon_text = args.bacon_text

list = []
for i in range(0, len(bacon_text), 5):
    x = i + 5
    list.append(bacon_text[i:x])

bacon_dict = {
    "00000": "A",
    "00001": "B",
    "00010": "C",
    "00011": "D",
    "00100": "E",
    "00101": "F",
    "00110": "G",
    "00111": "H",
    "01000": "I",
    "01000": "J",
    "01001": "K",
    "01010": "L",
    "01011": "M",
    "01100": "N",
    "01101": "O",
    "01110": "P",
    "01111": "Q",
    "10000": "R",
    "10001": "S",
    "10010": "T",
    "10011": "U",
    "10011": "V",
    "10100": "W",
    "10101": "X",
    "10110": "Y",
    "10111": "Z"
}

bacon_dict2 = {
    "aaaaa": "A",
    "aaaab": "B",
    "aaaba": "C",
    "aaabb": "D",
    "aabaa": "E",
    "aabab": "F",
    "aabba": "G",
    "aabbb": "H",
    "abaaa": "I",
    "abaaa": "J",
    "abaab": "K",
    "ababa": "L",
    "ababb": "M",
    "abbaa": "N",
    "abbab": "O",
    "abbba": "P",
    "abbbb": "Q",
    "baaaa": "R",
    "baaab": "S",
    "baaba": "T",
    "baabb": "U",
    "baabb": "V",
    "babaa": "W",
    "babab": "X",
    "babba": "Y",
    "babbb": "Z"
}

decoded_text = ""

for i in list:
    if i in bacon_dict.keys():
        decoded_text += bacon_dict[i]
    elif i.lower() in bacon_dict2.keys():
        decoded_text += bacon_dict2[i.lower()]
    else:
        pass
print(decoded_text))
