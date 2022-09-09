
#Parent class
class Animal:
    snake='serpents'
    spider='arachnids'

    def Quiz(self):
        entry_name=input("Please enter your name to begin: ")
        entry_snake=input("What species does the snake belong to?\n ")
        entry_spider=input("What species does the spider belong to?\n ")
        if (entry_snake ==self.snake and entry_spider==self.spider):
            print("Correct {}! the answer is {} and {}!".format(entry_name,entry_snake,entry_spider))
        else:
            print("Incorrect. Please try again.")


#Child class
class Spider(Animal):
    legs='8'
    eyes='8'
    dance='yes'

    def Quiz(self):
        entry_name=input("Please enter your name to begin: ")
        entry_dance=input("Do spiders dance? ")
        if(entry_dance==self.dance):
            print("Correct, {}!".format(entry_name))
        else:
            print("Incorrect. Please try again.")

class Snake(Animal):
    legs='0'
    arms='0'
    limbs='no'

    def Quiz(self):
        entry_name=input("Please enter your name to begin: ")
        entry_limbs=input("Do snakes have limbs?\n ")
        if(entry_limbs==self.limbs):
            print("Correct, {}! You are very smart".format(entry_name))
        else:
            print("Incorrect.Please try again.")



    


    
animal=Animal()
animal.Quiz()

spider=Spider()
spider.Quiz()

snake=Snake()
snake.Quiz()




