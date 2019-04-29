def main():
    def first_last(a,b):
        b.append(a[0])
        b.append(a[-1])

    a = [5, 10, 15, 20, 25] 
    b= []
    first_last(a,b)
    print b     

if __name__ == '__main__':
    main()