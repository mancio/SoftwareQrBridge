import base64
import os
import costants


def file_to_base64(file_path):
    """
    Encode the content of a file in Base64.

    :param file_path: Path to the input file.
    :return: Base64 encoded string of the file content.
    """
    with open(file_path, 'rb') as file:
        file_content = file.read()

    with open(os.path.join(os.path.join(os.path.dirname(file_path), 'text.txt')), 'w') as file:
        text = base64.b64encode(file_content).decode('utf-8')
        file.write(text)

    return text


def base64_to_file(text, path):
    """
    Decode the Base64 content from a .txt file and save it to a .zip file.

    :param text: Path to the .txt file containing Base64 encoded content.
    :param path: to save .zip file
    """

    decoded_content = base64.b64decode(text)

    # Determine the output path
    output_path = os.path.join(path, 'pr.zip')

    with open(output_path, 'wb') as file:
        file.write(decoded_content)


def enigma(text, key, mode=costants.ENCRYPT, file_path=None):
    """
    Encrypt or decrypt a text using a simple substitution cipher based on a text key.

    :param text: The input text to be encrypted or decrypted.
    :param key: The text key for the substitution cipher.
    :param mode: Either "encrypt" or "decrypt".
    :param file_path: path where the encrypted text message is saved
    :return: The encrypted or decrypted text.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates and keep the order
    key += ''.join([char for char in alphabet if char not in key])  # Append remaining chars

    if mode == costants.ENCRYPT:
        translation_table = str.maketrans(alphabet, key)
        with open(os.path.join(file_path, 'encrypted.txt'), 'w') as file:
            file.write(text.upper().translate(translation_table))
    elif mode == costants.DECRYPT:
        translation_table = str.maketrans(key, alphabet)
    else:
        raise ValueError("Invalid mode. Choose either 'encrypt' or 'decrypt'.")

    return text.upper().translate(translation_table)
