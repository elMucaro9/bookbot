def main():
    # Open the file and read its contents
    with open("/home/edr9/escuela/github.com/elMucaro9/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Count the words in the file
    word_count = count_words(file_contents)
    
    # Print the file contents and the word count
    print(file_contents)
    print("\n=========================================")
    print(f"The book contains {word_count} words.")
    print("=========================================")

def count_words(text):
    """
    Count the number of words in a given text.

    Args:
        text (str): The input string.
    
    Returns:
        int: The number of words in the string.
    """
    words = text.split()  # Split the text into words based on whitespace
    return len(words)
main()
