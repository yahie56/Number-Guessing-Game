def get_user_guess():
    while True:
        try:
            guess=int(input("enter your gues (1-100):"))
            if 1<=guess <=100:
                return guess 
            else:
                print("please enter numbar between 1 and 100.")
        except ValueError:
            print("invalid input !Please enter a number.")