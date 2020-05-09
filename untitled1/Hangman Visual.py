import random

def random_word():
    words = ['blue', 'orange', 'yellow', 'purple', 'white']
    return random.choice(words)

def hangman_game():
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    word = random_word()
    letters_guessed = []
    shots = 5
    guessed = False

    print('Please guess a color that has', len(word), 'letters in it.')
    print(len(word) * 'X')
    print("""
        |----|
        |
        |
        |
        |
        |
        |-----""")
    while guessed == False and shots > 0:
        if shots == 5:
            print('The game is on, you have 5 shots in order to guess the right color, good luck!')
        elif shots > 1 < 5:
            print('You have ' + str(shots) + ' shots left')
        else:
            print('It\'s your last chance buddy!')
        guess = input('Please enter one letter or full word: ').lower()
        already_used = []
        already_used = guess.split(' ')
        already_used_list = list(already_used)
        print("you have already entered:")
        #already_used_list.append(guess)
        print(already_used_list)
        if len(guess) == 1:
            if guess not in ABC:
                print('Sorry, but it is not a letter.')
            elif guess in letters_guessed:
                print('That letter was already entered')
            elif guess not in word:
                print('That\'s not one of the letters you\'re looking for. You have one shot less.')
                letters_guessed.append(guess)
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
            #already_used.append(guess)

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += 'X'
            print(status)
            if shots == 5:
                print("""
                |----|
                |
                |
                |
                |
                |
                |-----""")
            elif shots == 4:
                print("""
                |----|
                |    0
                |
                |
                |
                |
                |-----""")
            elif shots == 3:
                print("""
                |----|
                |    0
                |   /|\\
                |
                |
                |
                |-----""")
            elif shots == 2:
                print("""
                |----|
                |    0
                |   /|\\
                |    |
                |
                |
                |-----""")
            elif shots == 1:
                print("""
                |----|
                |    0
                |   /|\\
                |    |
                |   /
                |
                |-----""")
            else:
                RED = '\033[31m'
                print(RED + """
                |----|
                |    0
                |   /|\\
                |    |
                |   / \\
                |THIS IS THE END!!!
                |-----""")

        if status == word:
            print('Yes, ' + word + ' is the color you were looking for!!! You guessed letter by letter but it\'s still a win!')
            guess = True
            break
        elif shots == 0:
            print('Sorry, it\'s over! Try again later!')

hangman_game()
