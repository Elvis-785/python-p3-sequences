#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  # empty list when the length is 0
        return
    elif length == 1:
        print([0])  #[0] when the length is 1
        return

    first = 0
    second = 1
    fib_list = [first, second]  # Start with the first two Fibonacci numbers

    # Decreasing the length by two because the first 2 Fibonacci numbers already included
    length -= 2    

    while length > 0:
        next_fib = first + second
        fib_list.append(next_fib)  
        
        # Updating the first and second variables for finding the next number
        first, second = second, next_fib
        length -= 1

    print(fib_list)  

print_fibonacci(7)

if __name__ == "__main__":
    print_fibonacci(10)
    pass


