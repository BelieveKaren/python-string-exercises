
# Exercise 1: Name Tag

def exercise1():
    name = input("Full name: ")

    name = name.strip().title()

    words = name.split()

    initials = ""

    for word in words:
        initials += word[0] + "."

    print("Name tag:", name)
    print("Initials:", initials)
    print("Characters:", len(name))


# Exercise 2: Username Generator

def exercise2():
    while True:
        name = input("Full name: ").strip()
        words = name.split()

        if len(words) < 2:
            print("Please type a first name and a last name.")
        else:
            break

    first_name = words[0]
    last_name = words[-1]

    username = (first_name[0] + last_name).lower()
    email = username + "@school.example"

    print("Username:", username)
    print("Email:", email)


# Exercise 3: Text Statistics

def exercise3():
    sentence = input("Sentence: ")

    words = sentence.split()

    characters = len(sentence)
    word_count = len(words)

    letters = 0
    vowels = 0
    capitals = 0

    for ch in sentence:
        if ch.isalpha():
            letters += 1

            if ch.lower() in "aeiou":
                vowels += 1

            if ch.isupper():
                capitals += 1

    longest = ""

    for word in words:
        clean_word = ""

        for ch in word:
            if ch.isalpha():
                clean_word += ch

        if len(clean_word) > len(longest):
            longest = clean_word

    print("Characters:", characters)
    print("Words:", word_count)
    print("Letters:", letters)
    print("Vowels:", vowels)
    print("Capital letters:", capitals)
    print("Longest word:", longest)


# Exercise 4: Palindrome Checker

def exercise4():
    checked = 0
    palindromes = 0

    while True:
        text = input("Text (or stop): ")

        if text.strip().lower() == "stop":
            break

        cleaned = ""

        for ch in text.lower():
            if ch.isalnum():
                cleaned += ch

        if cleaned == "":
            print("Please type some letters or digits.")
            continue

        checked += 1

        if cleaned == cleaned[::-1]:
            print(f'"{text}" is a palindrome.')
            palindromes += 1
        else:
            print(f'"{text}" is not a palindrome.')

    print(f"You checked {checked} texts, {palindromes} palindromes.")
    print("Bye!")


# Exercise 5: Word Censor

def exercise5():
    BANNED = ["bad", "ugly", "hate", "men"]

    sentence = input("Sentence: ")

    words = sentence.split()

    result = []
    censored = 0

    for word in words:
        clean_word = ""

        for ch in word:
            if ch.isalpha():
                clean_word += ch

        if clean_word.lower() in BANNED:
            stars = "*" * len(clean_word)
            new_word = word.replace(clean_word, stars)
            result.append(new_word)
            censored += 1
        else:
            result.append(word)

    new_sentence = " ".join(result)

    print(new_sentence)
    print("Words censored:", censored)

exercise1()