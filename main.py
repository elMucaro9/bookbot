def main():
    book = "/home/edr9/escuela/github.com/elMucaro9/bookbot/books/frankenstein.txt" # <--- this is the book path
    book_content = get_book_text(book)
    if book_content:
        num_words = get_num_words(book_content)
        char_count = count_characters(book_content)

        # Print area
        print(f"\n>>> Begin report of books/frankenstein.txt >>>")
        print(f"\n--- {num_words} palabras found in the document ---")
        print("\n=========================================")
        print("Character Counts:")
        for char, count in char_count.items():
            print(f"  '{char}': {count}")
        else:
            print("=========================================")
            print("\nNo content to process.")

# Splits the content into words and counts them.
def get_num_words(book_content):
    palabras = book_content.split()
    return len(palabras)

# It uses -get_book_text- to read the content of "frankenstein.txt", returning its content as a string..
def get_book_text(book):
    try:
        with open(book, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file {book} was not found.")
    except IOError:
        print(f"Error: Could not read the file {book}.")
    return ""

# Counts each character in the text, converting all to lowercase to avoid case sensitivity issues.
def count_characters(book_content):
    text = book_content.lower()
    char_count = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

main()