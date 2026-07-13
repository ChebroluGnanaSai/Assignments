def count_vowels(text):
    vowels="aeiou"
    special_characters="@!#$%^&*()"
    count=0
    count_special_characters=0
    text=text.lower()
    for ch in text:
        if ch in vowels:
            count=count+1
        elif ch in special_characters:
            count_special_characters=count_special_characters+1
    return count,count_special_characters
text=input("Enter an Input")
count,count_special_characters=count_vowels(text)
print(f'Vowels "{count}"')
print(f'Special Characters : "{count_special_characters}"')
