def main():
    import random as ran
    def sort_list_gen(min,max,len_list):
        a=[]
        for l in range(0,len_list):
            a.append(ran.randint(min,max))
        return sorted(a)

    def find_list_elem(list_name, elem_value):
        first_idx = 1
        last_idx = len(list_name) - 1
        if elem_value not in list_name:
            print 'There is not such a number in this list'
        else:
            while True:
                middle_idx = int(round((last_idx - first_idx)/2))
                middle_elem = list_name[middle_idx]
                if middle_elem == elem_value:
                    print '\nGenerated list: ' + str(lista), 'Found it! Element value: ' + str(middle_elem) 
                    break
                elif middle_elem < elem_value:
                    first_idx = middle_idx
                    continue
                elif middle_elem > elem_value:
                    last_idx = middle_idx
                    continue                           
    
    lenght = int(raw_input('Choice the lenght of the list: '))
    minimum = int(raw_input('\nChoice the minimum number in the list: '))
    maximum = int(raw_input('\nChoice the maximum number in the list: '))
    num = int(raw_input('\nPick a number: '))
    lista = sort_list_gen(minimum,maximum,lenght)
    print lista
    #value = int(raw_input('Choice a number to check in the list: '))
    find_list_elem(lista, num)
    #if num in lista:
    #    print '\nGenerated list: ' + str(lista), "\nYou're right!"
    #else:
    #    print '\nGenerated list: ' + str(lista), "\nYou're wrong!"

if __name__=='__main__':
    main()