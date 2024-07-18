import random as rd
generated_number = rd.randint(1,100)
guess = int(input("Enter a number between 1-100: "))
#matching you number with generated number
while(generated_number!= guess):
   difference = generated_number - guess
   if 0> (difference) > -10  :
     print("\n Try a slighlty lower number!")
     guess = int(input("Enter a number between 1-100: "))
   elif 10 <= (difference) <= 100  :
     print("\n Try a higher number!")
     guess = int(input("Enter a number between 1-100: "))
   elif 0 < (difference) < 10 :
     print("\n Try a slightly higher number!")
     guess = int(input("Enter a number between 1-100: "))
   elif -10 >= (difference) >= -100  :
     print("\n Try a lower number!")
     guess = int(input("Enter a number between 1-100: "))
print("You got it! your number has matched")

