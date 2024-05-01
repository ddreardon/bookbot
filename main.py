def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(word_count(file_contents))
    letter_count(file_contents)

def word_count(book):
    words = book.split()
    return len(words)

def sort_on(dict):
    return dict["occs"]

def letter_count(book):
    chars = {}
    for i in range(len(book)):
        if book[i].lower() in chars:
            chars[book[i].lower()] += 1
        else:
            chars[book[i].lower()] = 1
    letter_list = []
    for char in chars:
        if char.isalpha():
            letter_list.append({"letter": char, "occs": chars[char]})
    letter_list.sort(reverse=True, key=sort_on)
    for letter in letter_list:
        print(f"The '{letter["letter"]}' character was found {letter["occs"]} times")

main()

