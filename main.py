def sort_dict(dict):
    return dict["val"]

def count_words(text):
    return len(text.split())

def read_file(path):
    with open(path) as f:
        return f.read()

def letter_count(text):
    char_dict = {}
    for char in text:
        lowercase_char = char.lower()
        if (lowercase_char in char_dict):
            char_dict[lowercase_char] += 1
        else:
            char_dict[lowercase_char] = 1
    return char_dict
    
def print_report(path, word_count, sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for char in sorted_list:
        print(f"The '{char["name"]}' character was found {char["val"]} times")
    print("--- End report")

def main():
    path = "books/frankenstein.txt"
    file_contents = read_file(path)
    word_count = count_words(file_contents)
    char_dict = letter_count(file_contents)
    sorted_list = []
    for entry in char_dict:
        if entry.isalpha() == True:
            sorted_list.append({"name": entry, "val": char_dict[entry]})
    sorted_list.sort(reverse=True, key=sort_dict)
    print_report(path, word_count, sorted_list)

main()