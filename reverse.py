def main():
    string = raw_input('Write a word to check if it is a palindrome: ')
    if string == string[::-1]: 
        print "\nYes " + string + ' is a palindrome!'
    else:
        print '\nNope! ' + string + ' is not a palindrome.'

if __name__ == '__main__':
   main()