import cv2
from pyzbar.pyzbar import decode
import sys

from transformer import find_qrcodes_in_directory


def decode_qrcodes(qr_code_images):
    """
    Decode an array of QR code images and return the concatenated text message.

    :param qr_code_images: List of paths to QR code images.
    :return: Concatenated text message from all QR codes.
    """
    decoded_text = ""

    for image_path in qr_code_images:
        image = cv2.imread(image_path)
        decoded_objects = decode(image)
        for obj in decoded_objects:
            decoded_text += obj.data.decode('utf-8')

    return decoded_text


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py directory_path")
        sys.exit(1)

    directory_path = sys.argv[1]
    qr_code_files = find_qrcodes_in_directory(directory_path)
    message = decode_qrcodes(qr_code_files)
    print(message)
