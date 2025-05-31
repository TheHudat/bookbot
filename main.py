def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    print(get_book_text("/home/jhudak/workspace/github.com/TheHudat/bookbot/books/frankenstein.txt"))

main()