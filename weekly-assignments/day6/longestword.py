def finding_longest_word(text):
    splitted_word = text.split()
    longest_word = ""
    for word in splitted_word:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

text = input("Enter a sentence: ")
output = finding_longest_word(text)
print("Longest word:", output)
