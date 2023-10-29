import os

import qrcode
import sys

import costants
from transformer import file_to_base64, enigma


def file_to_qrcode(input_file, key):
    """
    Generate a QR code from the Base64 encoded content of a file using the qrcode library.

    :param input_file: Path to the input file.
    :param key: to encrypt the message
    """
    encoded_content = file_to_base64(input_file)
    encrypted_content = enigma(encoded_content, key, costants.ENCRYPT, os.path.dirname(input_file))

    # Define the maximum characters per QR code (this is a rough estimate, actual capacity might vary)
    max_chars = 1800
    chunks = [encrypted_content[i:i + max_chars] for i in range(0, len(encoded_content), max_chars)]

    for index, chunk in enumerate(chunks):
        img = qrcode.make(chunk)
        img.save(os.path.join(os.path.join(os.path.dirname(input_file), f'qrcode_{index}.png')))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py input_file [Key]")
        sys.exit(1)

    input_file = sys.argv[1]
    key = sys.argv[2] if len(sys.argv) > 2 else costants.KEY

    file_to_qrcode(input_file, key)
