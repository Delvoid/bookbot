import sys


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    letter_count = count_letters(text)
    chars = list(key for key in letter_count.keys() if key.isalpha())
    chars.sort()
    for char in chars:
        print(f"The '{char}' character appears {letter_count[char]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_letters(text):
    letters = {}
    for char in text:
        c = char.lower()
        if c not in letters:
            letters[c] = 0
        letters[c] += 1
    return letters


if __name__ == '__main__':
    sys.exit(main())
