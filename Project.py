import random



rand = random.randint(0,100)
# def AutoGenerateRandom():
for i in range(1, 99):
        guess = int(input('Please enter your guess: '))
        

        if guess == rand:
            print("Perfect!!")
            print(f"You guessed perfectly, it is {rand}")
            

        # elif guess < rand:
        #     print(f'You are close')

        # elif guess > rand:
        #     print(f"Try again") 

        else:
            guess != rand
            print(f"Your guess is Wrong, it is {rand}")



# def Guess(action: int):
                
#     if action == 1:
#         print(guess)
#     else: 
#         if action == 0:
#             print("was it fun?")