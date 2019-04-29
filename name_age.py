import datetime as date

now = date.datetime.now()
def main():
    name=raw_input('Please, enter your name: ')
    age=raw_input('and age: ')
    print '\nYour name is ' + name 
    print 'Your age is ' + age
    print 'Hi ' + name + ', you will be 100 in ' + str( now.year + (100-int(age)) ) 

if __name__ == '__main__':
    main()