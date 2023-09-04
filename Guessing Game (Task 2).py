import random
generated_number=random.randrange(0,20,1)
count=0
i=0
while i<=10:
    guess=int(input("Enter your guessed number: "))
    if guess == generated_number:
        print("You have guessed correct")
        print("You have guessed correct in",count,"attempts")
        break
    elif guess > generated_number:
        print("Too High")
    elif guess < generated_number:
        print("Too Low")
    count+=1

