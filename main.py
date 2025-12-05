import sys
from stats import count_words, count_characters, sort_characters


def get_book_text(file_path: str):
    with open(file_path) as f:
        return f.read()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counts = sort_characters(count_characters(text=text))
    for count in counts:
        print(f"{count['char']}: {count['num']}")
