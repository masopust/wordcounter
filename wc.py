import argparse
import sys


def main():

    parser = argparse.ArgumentParser(
        description='Simple program which counts number of characters, words and lines in a text file by Jan Masopust.')
    parser.add_argument("-l", "--lines", action="store_true", help="gives number of lines in specified text file")
    parser.add_argument("-ch", "--chars", action="store_true", help="gives number of characters in specified text file")
    parser.add_argument("-w", "--words", action="store_true", help="gives number of words in specified text file")
    parser.add_argument("file", type=str, help="the name of the text file")
    args = parser.parse_args()

    file = open_file(args.file)
    if (not args.chars) and (not args.words) and (not args.lines):
        show_everything = True
    else:
        show_everything = False
    if file:
        if args.chars or show_everything:
            count_chars(file)
        if args.words or show_everything:
            count_words(file)
        if args.lines or show_everything:
            count_lines(file)

    print(args.file)


def open_file(file_name):

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("wc: ", file_name, ": No such file or directory")
        sys.exit()
    except PermissionError:
        print("wc:", file_name, ": Permission denied")
        sys.exit()
    except IsADirectoryError:
        print("wc:", file_name, ": Is Directory")
        print("0\t0\t0 ", file_name)
        sys.exit()

    read_file = file.read()
    file.close()
    return read_file


def count_chars(file):

    number_of_characters = len(file)
    print("Number of characters:", number_of_characters, " ", end='')


def count_words(file):

    number_of_words = len(file.split())
    print("Number of words:", number_of_words, " ", end='')


def count_lines(file):

    number_of_lines = len(file.split('\n'))
    print("Number of lines:", number_of_lines, " ", end='')


if __name__ == '__main__':
    main()
