def main():
    def fibonacci(n):
        a = [0,1,] 
        for i in range(1,n):
            a.append(a[i] + a[i-1])
        a.pop(0)
        return a    



    number = int(raw_input('How many number in Fibonacci series do you want? '))
    series = fibonacci(number)
    print '\nFibonacci series with ' + str(number) + ' elements: ' + str(series)         




if __name__ == '__main__':
    main()