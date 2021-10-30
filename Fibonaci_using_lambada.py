def fibonacci():

    nterms=int(input("How many terms? "))
    fibonacci_list=[0,1]
    
    if nterms <= 0:
        print("Please enter a positive integer")

    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":",end=" ")
        print(fibonacci_list[0])


    # generate fibonacci sequence

    else:
        
        (any(map(lambda x,: fibonacci_list.append(sum(fibonacci_list[-2:])),range(nterms))))
        print( * fibonacci_list[:nterms])


fibonacci()