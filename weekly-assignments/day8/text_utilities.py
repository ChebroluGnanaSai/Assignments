def word_count(text):
    words = text.split()
    return len(words)


def unique_words(text, case_sensitive=False):
    words = text.split()

    if not case_sensitive:
        words = [word.lower() for word in words]

    return list(set(words))


def reverse_string(text):
    return text[::-1]
