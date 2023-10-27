#usage python searchinrop.py csrop.txt "push esp" "pop" 
import argparse

def search_strings_in_file(file_path, search_strings):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if all(search_string in line for search_string in search_strings):
                    print(line, end='')

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Search for lines containing all specified strings in a text file")
    parser.add_argument("file_path", help="Path to the text file")
    parser.add_argument("search_strings", nargs='+', help="Strings to search for in the file (all must be present)")

    args = parser.parse_args()
    file_path = args.file_path
    search_strings = args.search_strings

    search_strings_in_file(file_path, search_strings)
