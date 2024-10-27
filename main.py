book_dir = "books/"
frankenstein_filename = "frankenstein.txt"

def main():
    with open(book_dir + frankenstein_filename, "r") as f:
        text = f.read()
    
    no_chars = get_num_characters(text)
    no_words = get_num_words(text)
    print_report(no_words, no_chars)

def print_report(no_words, no_chars):
    print(f"--- Begin report of {book_dir + frankenstein_filename} ---")
    print(f"There are {no_words} words found in the document\n")
    for c in no_chars:
        print(f"The '{c} character was found {no_chars[c]} times'")


    print(f"--- End report ---")

def get_num_characters(text:str):
    d = {}
    for c in text.lower():
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1

    return d




def get_num_words(text:str):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    main()
