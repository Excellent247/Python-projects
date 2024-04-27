password = "Secret1"
guess = ""
guess_count = 0
guess_limit = 3
limit_passed = False
while guess != password and not(limit_passed):
    if guess_count != guess_limit:
        guess = input("Password: ")
        guess_count += 1
        print("Incorrect Password")
    else:
        limit_passed = True
if limit_passed:
    print("Number of trial exceeded")
else:
    print("You are now logged in!")