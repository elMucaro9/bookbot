def main():
    libro = "/home/edr9/escuela/github.com/elMucaro9/bookbot/books/frankenstein.txt"
    contenido_del_libro = get_book_text(libro)
    num_palabras = get_num_words(contenido_del_libro)
    char_count = count_characters(contenido_del_libro)

    #Area de Print
    print(f"{contenido_del_libro}")
    print("\n=========================================")
    print(f"\n{num_palabras} palabras found in the document")
    print("\n=========================================")
    print(f"Total Count Characters is {char_count}")


def get_num_words(contenido_del_libro):
    palabras = contenido_del_libro.split()
    return len(palabras)


def get_book_text(libro):
    with open(libro) as f:
        return f.read()

def count_characters(contenido_del_libro):
    # Convert the entire texto to lowercase to avoid duplicates for case sensitivity
    texto = contenido_del_libro.lower()
    
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the texto
    for char in texto:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If it's not in the dictionary, add it with a count of 1
            char_count[char] = 1
    
    return char_count

main()