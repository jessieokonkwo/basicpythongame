print("Welcome to my first game!")
name = input("Before we begin, what is your name? ")
age = int(input ("How old are you? "))

lives = 10

if age >= 16:
    print("Perfect, you are old enough to play!  ")

    want_to_play = input("Are you sure you want to play? ").lower()
    if want_to_play == "yes":
        print("You are starting with", lives, "lives")
        print ("Let's play! ")

        left_or_right = input("First choice...Left or Right (left/right) ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reached a lake... Do you swim across or walk around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across, but got bit by a dog and lost 5 lives")
                lives -=5

            ans = input("You notice a house and a river. Which do you go to? (river/house)")
            if ans == "house":
                print("You go to the house and the owner sends you away because he doesnt like your haircut. As you leave, he takes 5 lives")
                lives -=5

                if lives <= 0:
                    print("Oh no, you have 0 lives left. You lost the game...Do better haha")
                else:
                    print("You have survived to the end...Kudos to you, you won!")
                
            else:
                print("You fell in the river and lost...")
                
        else:
             print("You fell on a rock and lost the game...lmaoo")
            
    else:
        print("okay then, cya... ")
else: 
    print("Sorry, you are not old enough to play this game... ")


















'''
Triple quotations comment out a block of code, the hashtag comments out a line 
Here are a few key things to remember:
string - "hello", 'hi', '4'
int - 6, 7, -9, 19000
float - 6.4, 4.0, -9.7
bool - True, False
'''