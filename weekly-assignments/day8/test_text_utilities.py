import unittest
from text_utilities import word_count, unique_words, reverse_string


class TestTextUtilities(unittest.TestCase):

    def test_word_count(self):
        self.assertEqual(word_count("Hello World"), 2)

    def test_unique_words(self):
        result = unique_words("apple apple banana")
        self.assertEqual(sorted(result), ["apple", "banana"])

    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)
        self.assertEqual(unique_words(""), [])
        self.assertEqual(reverse_string(""), "")

    def test_single_word(self):
        self.assertEqual(word_count("Python"), 1)
        self.assertEqual(unique_words("Python"), ["python"])

    def test_case_sensitive(self):
        result = unique_words("Hello hello", True)
        self.assertEqual(sorted(result), ["Hello", "hello"])

    def test_case_insensitive(self):
        result = unique_words("Hello hello", False)
        self.assertEqual(result, ["hello"])


if __name__ == "__main__":
    unittest.main()
