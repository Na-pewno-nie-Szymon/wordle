import random
import sys
import string

def wordset_loader(path: str) -> list:
    '''
        reading wordset (specified with path: str)
    '''
    with open(path, 'r') as file:
        file_wordlist = file.readlines()
    wordlist = []
    for word in file_wordlist:
        wordlist.append(word.rstrip('\n'))
    return wordlist

def random_word(wordlist: list) -> str:
    '''
        random.choise from wordlist dataset
    '''
    todays_word = random.choice(wordlist)
    return todays_word

def main_screen() -> bool:
    print()
    print('Hello to my simply wordle like game (with a stats)')
    print('For future me: try to make a prediction program that will try to win this game with average of under 4 rounds')
    print()
    print('Press enter to start playing!')
    _ = input()

    return True

def word_validation(player_word: str, ans_word: str) -> str:
    ans = ''
    for player_idx in range(len(player_word)):
        player_letter = player_word[player_idx]
        if player_letter == ans_word[player_idx]:
            ans += '+'
            ans_word[player_idx] = ''
        elif player_letter in ans_word:
            ans += '/'
        else:
            ans += '-'
    return ans


def get_player_word(wordlist: list) -> str:
    guessed_word = str(input())
    if guessed_word in wordlist:
        return guessed_word
    else:
        while guessed_word not in wordlist:
            print("Word not in a 5 letter word dictionary! Try again:")
            guessed_word = str(input())
        return guessed_word

def game(possibleW_data_path: str, allowedW_data_path: str, test_word = None) -> None:
    '''
        W O R L D
        + - / / -

        +: letter in a word and in a good place
        -: letter not i a word
        /: letter in a word but in a wrong place
    '''
    if test_word != None:
        todays_word = test_word
    else:
        possible_wordlist = wordset_loader(possibleW_data_path)
        todays_word = random_word(possible_wordlist)

    allowed_wordlist = wordset_loader(allowedW_data_path)
    max_rounds = 6

    main_screen()
    print('Let the game begin! Enter your first try:\n')
    for tries in range(1, max_rounds + 1):
        guessed_word = get_player_word(allowed_wordlist)
        ans = word_validation(player_word=guessed_word, ans_word=todays_word)
        print(ans + '\n')

        if ans == '+++++':
            print(f'You won! Good job, the word was: {todays_word}!')
            return None
    print(f"Try again! The word was: {todays_word}")
    return None

def run_wordle():
    flags = ['-p', '-a']
    try:
        if sys.argv[1] == flags[0]:
            possPATH = str(sys.argv[2])
        elif sys.argv[1] == flags[1]:
            alloPATH = str(sys.argv[2])
        
        if sys.argv[3] == flags[0]:
            possPATH = str(sys.argv[4])
        elif sys.argv[3] == flags[1]:
            alloPATH = str(sys.argv[4])

        return [possPATH, alloPATH]
    except IndexError:
        print('wordle.py takes 2 arguments')
        print('-p: path to possible words')
        print('-a: path to allowed words')
        exit()
    return MemoryError('Report this bug if occures to Na-pewno-nie-Szymon on Github :(')        
if __name__=="__main__":
    possPATH = run_wordle()[0]
    alloPATH = run_wordle()[1]
    try:
        test_word = sys.argv[2]
        game(possPATH, alloPATH, test_word)
    except IndexError:
        game(possPATH, alloPATH)
    exit()