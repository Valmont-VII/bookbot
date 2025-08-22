from stats import get_num_words, letter_counter, list_of_dicts
import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}") # This line goes here
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words") # This line goes here
    print("--------- Character Count -------")


    
    my_dict = letter_counter(text)
    dddddddddd = list_of_dicts(my_dict)
    for dd in dddddddddd:
        if dd["char"].isalpha():
            print(f"{dd["char"]}: {dd["num"]}")


    print("============= END ===============")

    
    



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
