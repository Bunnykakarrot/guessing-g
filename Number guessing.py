import random
import math
#inputs
lower =int(input("enter number for lower bound ="))
upper =int(input("enter number for upper bound ="))
#Selecting random number in range of upper and lower bounds
t = random.randint(lower,upper)
print("\n\t You've only ",round(math.log(upper-lower+1,2)),"chances to guess the number \n")
# starting with number of guesses
c=0
#calculation of minimum number of
#gusses upon range
while c<math.log(upper-lower+1,2):
    c=c+1
    #guess input
    g=int(input("enter number for the guess"))

     #checking condition with if condition
    if t==g:
         print ("You've guess the number in ",c,"try")
         #now loop  should break
         break
    elif t>g:
         print("You guessed too small")
    elif t<g:
         print("You guessed too high")
         
# if guess is more than requied guesses then
if c>math.log(upper-lower+1,2):
    print("\nNumber is = ",t)
    print("\tBetter luck next time")
      
           
