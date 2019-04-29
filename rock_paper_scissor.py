def main():
    import random
    choices = ['paper','rock','scissor']
    while True:
        game = random.choice(choices)
        ur_c = raw_input('Select between rock, paper and scissor: ')
        if ur_c == 'rock' and game == 'scissor':
           print '\nYou win'
           break
        elif ur_c == 'scissor' and game == 'paper':
            print '\nYou win'
            break
        elif ur_c == 'paper' and game == 'rock':
            print '\nYou win'
            break         
        else:
            yon= raw_input('\nYou lost! Do you want to play again? ')
            if yon == 'no':
               break
            else:    
                print '\nTry again: '
            



if __name__ == '__main__':
   main()