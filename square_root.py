number = int(input("\nEnter a Number: "))

if number < 2:
    print("\nSquare Root: ", number)
else:
    previous_guess = number
    current_guess = (previous_guess + (number / previous_guess)) / 2
    
    while abs(current_guess - previous_guess) >= 0.000001:
        previous_guess = current_guess
        current_guess = (previous_guess + (number / previous_guess)) / 2

    print("\nSquare Root: ", current_guess)
