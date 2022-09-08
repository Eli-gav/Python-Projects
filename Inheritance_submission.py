
#Parent Class
class Player:
    user_name='No Name Provided'
    password='5679'
    points_scored=''
    total_deaths=''

#Child classes
class Enviroment(Player):
    time_played=''
    settings='normal'

class Transactions(Player):
    times_purchased=''
    total=''
    
    
    
