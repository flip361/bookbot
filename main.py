import os

def main():
    path_to_file = "books/frankenstein.txt"
    #print("Current working directory:", os.getcwd())
    #print("'books' directory exists:", os.path.exists("books"))
    #print("Files in 'books' directory:", os.listdir("books"))
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

main()