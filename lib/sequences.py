def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    # Generate the Fibonacci sequence
    fib_sequence = [0, 1]
    for _ in range(2, length):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Print the sequence as a list
    print(fib_sequence)
