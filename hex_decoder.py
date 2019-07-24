#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("hex_text", type=str, help="hex text to convert")
args = parser.parse_args()

text_to_convert = args.hex_text

print(bytes.fromhex(text_to_convert).decode('utf-8'))