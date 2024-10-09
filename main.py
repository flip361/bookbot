import os

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    low_text = get_lowercased(text)
    char_count = count_characters(low_text)

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
    sorted_char_count = dict(sorted(char_count.items()))
    return sorted_char_count


main()