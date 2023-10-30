import os
import sys

import constants
from transformer import enigma, base64_to_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py input_txt_path [Key]")
        sys.exit(1)

    input_txt_path = sys.argv[1]
    key = sys.argv[2] if len(sys.argv) > 2 else constants.KEY

    with open(input_txt_path, 'r') as file:
        text = file.read()

    decrypted_message = enigma(text, key, mode=constants.DECRYPT)
    print(decrypted_message)
    base64_to_file(decrypted_message, os.path.dirname(input_txt_path))
