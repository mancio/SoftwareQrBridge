import os
import sys
import glob

import transformer


def append_files_in_directory(directory_path, output_filename="combined.txt"):
    """
    Append content of all .txt files in the specified directory into a single .txt file.

    :param directory_path: Path to the directory containing .txt files.
    :param output_filename: Name of the output file where content will be appended.
    :return: None
    """
    # Get a list of all .txt files in the directory
    txt_files = sorted(glob.glob(os.path.join(directory_path, "*.txt")), key=transformer.sort_key)

    with open(os.path.join(directory_path, output_filename), 'w') as outfile:
        for txt_file in txt_files:
            with open(txt_file, 'r') as infile:
                outfile.write(infile.read())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py directory_path")
        sys.exit(1)

    directory_path = sys.argv[1]
    append_files_in_directory(directory_path)
