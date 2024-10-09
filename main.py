import os

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    low_text = get_lowercased(text)
    char_count = count_characters(low_text)
    report = run_count_report(book_path, num_words, char_count)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_lowercased(text):
    lowered_text = text.lower()
    return lowered_text

def count_characters(text):
    char_count = {}
    for char in text.lower():  # Assuming text is already lowercase
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    sorted_items = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_items

def run_count_report(book_path, num_words, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char, count in char_count:
        print(f"The '{char}' character was found {count} times.")


main()