from text_utilities import word_count, unique_words, reverse_string


def main():
    text = input("Enter a sentence: ")

    print("\n----- Results -----")
    print("Word Count:", word_count(text))
    print("Unique Words (Case Insensitive):", unique_words(text))
    print("Unique Words (Case Sensitive):", unique_words(text, True))
    print("Reversed String:", reverse_string(text))


if __name__ == "__main__":
    main()
