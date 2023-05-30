import random
import time


elements = ['piatra', 'hartie', 'foarfeca']


def verify_user_element(user_element):
    global x 
    
    x = bool
    if(user_element == 'piatra' or user_element == 'hartie' or user_element == 'foarfeca'):
        x = True
    else:
        x = False


def verify_elements(ai_element,user_element):
    global winner
    winner = str
    print(f'User Element : {user_element} ')
    print(f'Ai Element : {ai_element}')
    if(ai_element == 'piatra' and user_element == 'foarfeca' ):
        winner = 'AI'
    if(user_element == 'piatra' and ai_element == 'foarfeca'):
        winner = 'User'
    if(ai_element == 'foarfeca' and user_element == 'hartie'):
        winner = 'AI'
    if(user_element == 'foarfeca' and ai_element == 'hartie'):
        winner = 'User'
    if(user_element == 'hartie' and ai_element == 'piatra'):
        winner = 'User'
    if(ai_element == 'hartie' and user_element == 'piatra'):
        winner = 'AI'
    if(ai_element == user_element):
        winner = 'Remiza'
    
        

def AI_choice():
    global choice
    choice = random.choice(elements)
    #print(choice)
    if(element_user == choice):
        choice = random.choice(elements)    
        #print(choice)

def main_game():
    global element_user
    element_user = input('Alege ti element ul (piatra , hartie, foarfeca): ')
    print('Verificam Daca Element ul tau este corect')
    time.sleep(1)
    verify_user_element(element_user)
    if(x == True):
        AI_choice()
        print('Element ul este corect')
        game()
       
    else:
        print('Elementul este incorect')
        return main_game()
    
    








def game():
        verify_elements(choice, element_user)
        if(winner == 'AI'):
            re_match = input('Robotul Este Castigator! Doresti sa re-joci? (y/n) : ')
            if(re_match == 'y'):
                return main_game()
            else:
                quit()
        if(winner == 'User'):
         re_match = input('Tu Esti Castigator! Doresti sa re-joci? (y/n) : ')
         if(re_match == 'y'):
          return main_game()
         else:
             quit()  
        if( winner == 'Remiza'):
            re_match = input('Remiza ! Doresti sa re-joci? (y/n) : ')
            if(re_match == 'y'):
             return main_game()
            else:
                quit(200)
            
            
    
    
if __name__ == '__main__':
    main_game()