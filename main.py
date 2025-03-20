import sys
from stats import get_num_words, character_count, character_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count_dict = character_count(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {get_num_words(text)} total words')
    print("--------- Character Count -------")
    character_sort(count_dict)
    print("============= END ===============")

main()