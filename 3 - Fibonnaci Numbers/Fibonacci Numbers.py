while True:
    # Main Fibonacci Function
    def fib(n):
        # Seed Numbers
        print("0")
        print("1")
        a = 0
        b = 1
        # Correct Value Checker
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return a
        elif n == 1:
            return b
        else:
            # Loop
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)


    # User Input
    n = int(input("n = "))
    # Function Caller
    fib(n)

    continue
