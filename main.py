def count_words(book):
    words = book.split()
    return len(words)


def get_words(book):
    words = book.split()
    return words


def character_frequency(book):
    words = get_words(book)
    frequency = {}
    for word in words:
        for character in word.lower():
            if character.isalpha():
                if character in frequency:
                    frequency[character] += 1
                else:
                    frequency[character] = 1
    return frequency


def build_report(book, path):
    word_count = count_words(book)
    freq = character_frequency(book)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    report = f"--- Begin report of {path} --- \n"
    report += f"Word count: {word_count}\n"
    report += "Character frequency:\n"
    for character, count in freq:
        report += f"{character}: {count}\n"

    report += f"--- End report of {path} ---"
    return report


def main():
    path = "books/frankenstein.txt"
    with open(path) as file:
        book = file.read()
    print(build_report(book, path))


main()
