# Kode untuk generate file txt dengan ukuran yang diinginkan

import sys
import os

def generate_file(word, size_kb, output_dir="files"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{size_kb}kb.txt"
    filepath = os.path.join(output_dir, filename)

    target_size = size_kb * 1024  # in bytes
    content = (word + " ") * (target_size // len(word + " "))

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"Generated {filepath} with approx {size_kb} KB")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python generate_txt.py <word> <size_kb>")
        sys.exit(1)

    word = sys.argv[1]
    size_kb = int(sys.argv[2])
    generate_file(word, size_kb)
