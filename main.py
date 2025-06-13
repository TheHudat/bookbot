from stats import word_count, character_count


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_text = get_book_text("/home/jhudak/workspace/github.com/TheHudat/bookbot/books/frankenstein.txt")
    num_words = word_count(book_text)
    print (f"{num_words} words found in the document")
    character_count(book_text)

main()