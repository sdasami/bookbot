from stats import number_of_words
from stats import number_of_characters, sort_characters
import sys

def get_book_text(filepath): 
    #file_contents = ""
    with open(filepath) as f:
        return f.read()


def main():
    try:
        #book_path = "books/frankenstein.txt"
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = number_of_words(text)
        characters_and_numbers = number_of_characters(text)
        #print(characters_and_numbers)
        sort_char_and_number = sort_characters(characters_and_numbers)
        report(book_path, sort_char_and_number, num_words)

    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

    
    

def report(book_path, sort_char_and_number, num_words):
    #print(argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(sort_char_and_number)
    for c in sort_char_and_number:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")

main()