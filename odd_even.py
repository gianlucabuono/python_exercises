def main():
    number = int(raw_input('Please, enter a number: '))
    if  number%4 == 0:
        print "\nThat's an even number and, moreover, a multiple of 4!"
    elif number%2 == 0:
        print  "\nThat's an even number!"   
    elif number%2 != 0:
        print "\nThat's an odd number!"    

if __name__ == '__main__':
    main()    