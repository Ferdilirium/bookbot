import sys
from stats import get_words_number, count_characters, sort_dict, sort_on, report



def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path=sys.argv[1]
    dict=count_characters(get_book_text(path))
    sorted=sort_dict(dict)
    report(sorted,get_words_number(path),path)
main()
