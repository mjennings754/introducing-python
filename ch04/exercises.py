"""
4.1 Choose a number between 1 and 10 and assign it to the variable secret.
Then, select another number between 1 and 10 and assign it to the variable
guess. Next, write the conditional tests (if, else, and elif) to print the
string 'too low' if guess is less than secret,
'too high' if greater than
secret, and 'just right' if equal to secret.
"""
secret = 4
guess = 2

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")
