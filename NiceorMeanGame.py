

#Python: 3.10.5

#Author: Elise Snow

#Purpose:  Create Nice or Mean simple game from Tech Academy



def start(nice=0,mean=0,name=""):
    #get users name
    name= describe_game(name)
    nice,mean,name= nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if it is a new game or not
        if its new, get users name
        if its not new, thank player
        and ask to play again
    """
    if name!="":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop=True
        while stop:
            if name =="":
                name=input("\nWhat is your name? \n>>> ").capitalize()
                if name !="":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be introduced to several different people. \nYou ca choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be decided by your actions")
                    stop=False
    return name




def nice_mean(nice,mean,name):
    stop=True
    while stop:
        show_score(nice,mean,name)
        pick=input("\nA stranger approches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick== "n":
            print("\nThe stranger walks away smiling...")
            nice= (nice+1)
            stop=False
        if pick == "m":
            print("\nThe stanger glares at you \nand storms off...")
            mean= (mean+1)
            stop=False
    score(nice,mean,name) # pass the 3 var to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passes the value stored within the 3 var
    if nice >2: # if condition is valid, call win function
        win(nice,mean,name)
    if mean>2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # sub the {} wildcard with our var
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nToo bad! Game Over! \n{}, you shall live in a dirty beat-up van by the river and die alone.".format(name))
    again(nice,mean,name)
                          
def again(nice,mean,name):
    stop=True
    while stop:
        choice =input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice=="y":
            stop=False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, sad to see you go!")
            stop=False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO'\n>>> ")
            
def reset(nice,mean,name):
    nice=0
    mean=0
    start(nice,mean,name)




if __name__=="__main__":
    start()
