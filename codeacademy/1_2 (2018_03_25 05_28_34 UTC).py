def root(x, tol = 0.1):
    lower = 0.0
    upper = x
    guess = (upper + lower) / 2
    while (abs(x - guess * guess) > tol):
        if guess * guess > x:
            upper = guess
        else:
            lower = guess
        guess = (upper + lower) / 2
    return guess

print(root(7))