from validator_collection import checkers


email = checkers.is_email(input("What's your email? "))

if emaild == True:
    print("Valid")
else:
    print("Invalid")
