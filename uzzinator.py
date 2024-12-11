import pyphen

vowels = "aeiou"
def convert_to_syllables(word):
    # Create a Pyphen dictionary for English
    dic = pyphen.Pyphen(lang='en')
    # Insert hyphens into the word at syllable breaks
    hyphenated = dic.inserted(word)
    # Split on the hyphens to get a list of syllables
    return hyphenated.split('-')

def cut_word(syllable):
    # Find the first vowel in the syllable
    for index, letter in enumerate(syllable):
        if letter.lower() in vowels:
            # Return everything before the vowel + "uzz"
            return syllable[:index] + "uzz"
    # If no vowel is found, just append "uzz"
    return syllable + "uzz"

def uzzinator(word):
    syllables = convert_to_syllables(word)
    print(syllables)
    if len(syllables) == 1:  
        return cut_word(syllables[0])
    last_syllable = syllables[-1]
    second_last_syllable = syllables[-2]
    if second_last_syllable[-1] in vowels:
        return "".join(syllables[:-2]) + cut_word(second_last_syllable)
    return "".join(syllables[:-1]) + cut_word(last_syllable)

print('To exit, enter: quit')
while True:
    user_input = input("Enter a word: ").strip().lower()
    if (user_input == "quit"):
        break
    print(uzzinator(user_input))
