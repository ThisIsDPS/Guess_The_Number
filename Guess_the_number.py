import random # random module

win_num = random.randint(0, 100) # generates random integer numbers b/w 1-100
guesses = 10 # maximum number of guesses
print("Guess the number between 1-100. You have",guesses,"Guesses only")

while(guesses):
    inp_num = int(input("Enter a number: "))
    if (win_num-inp_num)<=5 and (win_num-inp_num)>0:
        guesses-=1
        print("You are very close!!! Go little up\t\t{ Guesses left:",guesses,"}")
    elif (inp_num-win_num)<=5 and (inp_num-win_num)>0:
        guesses-=1
        print("You are very close!!! Go little down\t\t{ Guesses left:",guesses,"}")
    elif inp_num<win_num:
        guesses-=1
        print("HaHaHa!!! Go Up\t\t\t\t\t{ Guesses left:",guesses,"}")
    elif inp_num>win_num:
        guesses-=1
        print("HaHaHa!!! Go Down\t\t\t\t{ Guesses left:",guesses,"}")
    elif inp_num==win_num:
        print("\t\t\t\t\t\t\t\tCongratulations!!! You have Guessed Right!!!")
        break
if guesses==0:
    print("Try again next time :( , Your guesses are over.")