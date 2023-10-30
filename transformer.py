import base64
import glob
import os
import constants


def find_qrcodes_in_directory(directory):
    """
    Find all .png files containing the word "qrcode" in the specified directory.

    :param directory: Path to the directory to search.
    :return: List of paths to QR code images.
    """
    search_pattern = os.path.join(directory, "*qrcode*.png")
    return glob.glob(search_pattern)


def file_to_base64(file_path):
    """
    Encode the content of a file in Base64.

    :param file_path: Path to the input file.
    :return: Base64 encoded string of the file content.
    """
    with open(file_path, 'rb') as file:
        file_content = file.read()

    with open(os.path.join(os.path.join(os.path.dirname(file_path), 'base.txt')), 'w') as file:
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


def enigma(text, key, mode=constants.ENCRYPT, file_path=None):
    """
    Encrypt or decrypt a text using a simple substitution cipher based on a text key.

    :param text: The input text to be encrypted or decrypted.
    :param key: The text key for the substitution cipher.
    :param mode: Either "encrypt" or "decrypt".
    :param file_path: path where the encrypted text message is saved
    :return: The encrypted or decrypted text.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates and keep the order
    key += ''.join([char for char in alphabet if char not in key])  # Append remaining chars

    if mode == constants.ENCRYPT:
        translation_table = str.maketrans(alphabet, key)
        encrypted_text = text.translate(translation_table)
        save_to_files(encrypted_text, file_path)
    elif mode == constants.DECRYPT:
        translation_table = str.maketrans(key, alphabet)
    else:
        raise ValueError("Invalid mode. Choose either 'encrypt' or 'decrypt'.")

    return text.translate(translation_table)


def save_to_files(text, file_path):
    """
    Split the text into chunks and save each chunk into a separate file.

    :param text: The input text to be split and saved.
    :param file_path: The directory where the text chunks will be saved.
    :return: None
    """
    # Split the text into chunks of size not exceeding 250kB
    max_bytes = 230 * 1024  # 230kB in bytes
    max_chars = max_bytes  # Assuming 1 char = 1 byte, which holds for ASCII and UTF-8 without special characters
    chunks = [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

    # Save each chunk into a separate file
    for idx, chunk in enumerate(chunks):
        with open(os.path.join(file_path, f'en_{idx}.txt'), 'w') as file:
            file.write(chunk)
