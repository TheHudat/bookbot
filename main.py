from stats import word_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    num_words = word_count(get_book_text("/home/jhudak/workspace/github.com/TheHudat/bookbot/books/frankenstein.txt"))
    print (f"{num_words} words found in the document")

main()