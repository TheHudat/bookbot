from stats import word_count, character_count, sort_char_list
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    char_dict = character_count(book_text)
    sorted_char_list = sort_char_list(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count -----------")
    print (f"Found {num_words} total words")
    print("-------- Character Count ---------")
    for n in range(0, len(sorted_char_list)):
        print(f"{sorted_char_list[n]["char"]}: {sorted_char_list[n]["num"]}")
    print("--------------- END ---------------")

main()