def main():
    import random as ran 
    from datetime import datetime
    start = datetime.now()
    n = ran.randint(1,9)
    c=0
    while True:
        u = int(raw_input('\nPick a number between 1 and 9: ')) 
        c += 1
        if u < n:
            ans = raw_input('Too low! Do you want to continue? ')
            if ans == 'yes':
                continue
                #print 'Pick a number between 1 and 9: '
            elif ans == 'no':
                print 'Ok, bye!'
                break
            while ans != 'yes' or ans != 'no':
                raw_input('Can you repeat? ')    
            #else:
            #    print 'Can you repeat?'   
        elif u > n:
            ans = raw_input('Too high! Do you want to continue? ')
            if ans == 'yes':
                continue
                #print 'Pick a number between 1 and 9: '
            elif ans == 'no':
                print 'Ok, bye!'
                break
            #else:
            #    print 'can u rep'
            #    ans = raw_input('Can you repeat?')            
        elif u == n:
            print "\nYou're right!"
            print 'You tried ' + str(c) + ' times'
            break


    stop = datetime.now()
    print 'The program ran for ' + str((stop-start)) + ' (hrs : min : sec)'     



if __name__ == '__main__':
    main()