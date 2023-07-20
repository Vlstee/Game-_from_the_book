print('Введите английский тект для перевода на поросячьею латынь: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    suffixNonletters = ''
    while not word[-1].isalpha():
        suffixNonletters += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    prefixNonConsonant = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixNonConsonant += word[0]
        word = word[1:]

    if prefixNonConsonant != '':
        word += prefixNonConsonant + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
        
    pigLatin.append(prefixNonLetters + word + suffixNonletters)

    print(''.join(pigLatin))