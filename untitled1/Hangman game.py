#dwie uwagi
#1.pojawia sie poprawny komunikat, gdy uzytkownik poda cyfre,
# ale gdy poda sie liczbe komunikat jest juz taki, jak w przypadku dluzszego lub krotszego slowa.
# Narazie dajemy sobie spokoj z poprawieniem tego, zostawilem wyhaszowany kod, ktorego probowalismy uzyc

#2.sa dwa rozne komunikaty w przypadku wygranej, jeden, gdy zgadujemy literka po literce, a drugi gdy wpiszemy cale slowo

#3. Niestety nie wiemy jak zrobic ostatnia czesc zadania, dlatego podsylamy bez .json'a


import random

def random_word():
    words = ['blue', 'orange', 'yellow', 'purple', 'white']
    return random.choice(words)

def hangman_game():
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    word = random_word()
    letters_guessed = []
    shots = 10
    guessed = False

    print('Please guess a color that has', len(word), 'letters in it.')
    print(len(word) * 'X')
    while guessed == False and shots > 0:
        if shots == 10:
            print('The game is on, you have 10 shots in order to guess the right color, good luck!')
        elif shots > 1 < 10:
            print('You have ' + str(shots) + ' shots left')
        else:
            print('It\'s your last chance buddy!')
        guess = input('Please enter one letter or full word: ').lower()
        if len(guess) == 1:
            if guess not in ABC:
                print('Sorry, but it is not a letter.')
            # elif guess is int or float:
            #     print('You need a letter, not a digit/number')
            elif guess in letters_guessed:
                print('That letter was already entered')
            elif guess not in word:
                print('That\'s not one of the letters you\'re looking for. You have one shot less.')
                letters_guessed.append(guess) # czy to jest tu potrzebne?
                shots -= 1
            elif guess in word:
                print("Yes, you got it, it\'s one of the letters!")
                letters_guessed.append(guess)
        elif len(guess) == len(word):
            if guess == word:
                print('Nice, you got the color by typing the whole word! Indeed it\'s ' + word + "!")
                guessed = True
            else:
                print('Sorry but you\'re wrong!')
                shots -= 1
        else:
            print('Incorrect number of letters; it\'s either to short or too long. It counts as an incorrect letter!')
            shots -= 1

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += 'X'
            print(status)

        if status == word:
            print('Yes, ' + word + ' is the color you were looking for!!! You guessed letter by letter but it\'s still a win!')
            guess = True
            break
        elif shots == 0:
            print('Sorry, it\'s over! Try again later!')

hangman_game()

# if __name__ == '__main__':
#     data = open("hangman.json")
#     word = random.choice(list(data.keys())).lower()