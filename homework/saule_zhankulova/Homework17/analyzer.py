import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='File name')
    parser.add_argument('--text', help='Text to search')
    return parser.parse_args()


def get_files(path):
    if os.path.isfile(path):
        return [path]

    return [path + "/" + name for name in os.listdir(path)]


def read_file(file_path):
    file = open(file_path, encoding="utf-8", errors="ignore")
    lines = file.readlines()
    file.close()
    return lines


def split_blocks(lines):
    blocks = []
    block = []
    time = ""

    for line in lines:
        if len(line) > 19 and line[4] == "-" and line[7] == "-":
            if block:
                blocks.append((time, block))
            time = line[:19]
            block = [line]
        else:
            block.append(line)

    if block:
        blocks.append((time, block))

    return blocks


def search_text(blocks, search_text, file_name):
    for time, block in blocks:
        text = " ".join(block)

        if search_text in text:
            words = text.split()

            for i in range(len(words)):
                if search_text in words[i]:
                    start = i - 5
                    end = i + 6

                    if start < 0:
                        start = 0

                    context = " ".join(words[start:end])
                    break

            print("Файл:", file_name)
            print("Время:", time)
            print("Фрагмент:", context)
            print("-" * 50)


def main():
    args = parse_args()

    files = get_files(args.path)

    for file_path in files:
        lines = read_file(file_path)
        blocks = split_blocks(lines)
        search_text(blocks, args.text, file_path)


main()
