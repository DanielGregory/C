'''
Name: Daniel Gregory
Section: 006
Date: 11/18/2022
Email: DannyTGregory@uky.edu
'''
#Purpose: ask the player (pname) whether they want to pass the die or roll
# invalid answers are rejected until the player enters either P or R
#   upper or lower case
#precondition: the player's name (string)
#postcondition: either P or R (string) based on player's answer (always uppercase)
from graphics import *
def pass_or_roll(name, window: GraphWin):
    
   #ask player to enter R or P(upper and lowercase)
    prompt = Text(Point(250, 230), name + " what do you want to do?")
    prompt.setSize(20)
    prompt.draw(window) 
    
    #draw two rectangles that say pass or roll
    r1 = Rectangle(Point(120, 300), Point(220, 400))
    r1.draw(window)
    r1_text = Text(r1.getCenter(), "Pass")
    r1_text.draw(window)
    r2 = Rectangle(Point(270, 300), Point(370, 400))
    r2.draw(window)  
    r2_text = Text(r2.getCenter(), "Roll")
    r2_text.draw(window)
    
    #save where user clicks
    click = window.getMouse()
      # while the click in not inside any boxes
    while (not inbetween(Point(120, 300), click, Point(220, 400)) and not inbetween(Point(270, 300), click,Point(370, 400))):
        # get the player's next click
        click = window.getMouse() 
    #undraw everything
    prompt.undraw()
    r1.undraw()
    r1_text.undraw()
    r2.undraw()
    r2_text.undraw()        

    #check if user clicked in pass or roll box
    if inbetween(Point(120, 300), click, Point(220, 400)):
        choice = 'P'
    else:
        choice = 'R'
    return choice
#Purpose: to draw a die in the window
#preconditions: roll, window
#postconditions: returns gif corresponding to roll
def draw_die(roll, window: GraphWin):
    die_pic = Image(Point(250, 250), str(roll) + ".gif")
        # draw image
    die_pic.draw(window)
        
        # return die image
    return die_pic    

#Purpose: to do one player's turn, performing rolls or passes as player chooses
#Precondition: player name (string), player roll total (int), player's pass count (int)
#Postcondition: player roll total and player's pass count, both int, modified as needed
#  if player passed, pass count reduced, if player rolled, roll total increased
def play_turn(choice, name, roll, passcount, window: GraphWin ):
  
    # if player decided to roll, roll dice and display roll
    if choice == 'R':
        roll = random.randint(1,6)
        result = (name+ ' rolled a %i' %roll)
    #make sure passcount doesnt increase
        passcount = 0
    
   # if player decided to pass make sure passcount is great than 0
    elif choice == 'P':
        #check if passcount is greater than 0
        if passcount >=0:
            passcount = -1
    #           state that the player passed the roll
            result = (name + ' passed the roll')
    #          make sure total roll does not move
            roll=0
        else:
            #if no more pass's automatically roll for player
            roll = random.randint(1,6)
            result = (name+ ' rolled a %i' %roll)
            passcount =0
            
    #  prints what the user rolled  
    turn = Text(Point(250, 150), result)
    turn.draw(window)
    
    #call draw die and draw the gif in the window 
    die_image = draw_die(roll, window)
    window.getMouse()
    
    #undraw everything
    turn.undraw()
    die_image.undraw()
    
    #return roll and passcount
    return roll, passcount

def inbetween (pt1, pt2, pt3):
    '''
    Purpose:  detect whether a Point pt2 is between Points pt1 and pt3
       assumes that pt1 is to the left of pt3 (x of pt1 is <= x of pt3)
       and that pt1 is above pt3 (y of pt1 is <= y of pt3)
    Preconditions:  pt1 and pt3 are the boundary Points, forming a rectangle.
       pt2 is the Point which is being tested for "betweenness".
    Postconditions:
       returns True if the Point pt2 lies in the rectangle formed by pt1 and pt3.
          This includes pt2 being exactly ON one side of the rectangle.
       returns False if this is not true.  
    '''
    between = False
    if (pt1.getX() <= pt2.getX() <= pt3.getX()) and (pt1.getY() <= pt2.getY() <= pt3.getY()):
        between = True
    return between

import random
def main():
 # Purpose: 2 players take turns rolling a die - 6-sided
# the first player to total rolls to 21 or greater loses.
# a player can pass a roll but only 3 times
# Preconditions: player names (strings), decisions to roll or pass (strings)
# Postconditions: prompts, display of totals and pass counts, rolls of the die
#      statement of who wins
    win = GraphWin('Twenty One', 500,500)

#print title prompts
    msg = Text(Point(250, 60), "Don't get to 21!\n")
    msg.draw(win)
    msg1 = Text(Point(250, 200),"Each player tries not to get to 21")
    msg1.draw(win)
    msg2 =Text(Point(250, 230),'Each player has 3 passes, which allow them to not roll on a round.')
    msg2.draw(win)
        
    
#User input player one
    player1prompt = Text(Point(100,300),'Who is player 1?')
    player1prompt.draw(win)
    user_input = Entry(Point(190,300),5)
    user_input.setText("")
    user_input.draw(win)
        
       
#user input player two
    player2prompt = Text(Point(300,300),'Who is player 2?')
    player2prompt.draw(win)
    user_input1 = Entry(Point(390,300),5)
    user_input1.setText("")
    user_input1.draw(win)
    win.getMouse()
    player1 = str(user_input.getText()) 
    player2 = str(user_input1.getText()) 
    
#undraw all prompts
    msg.undraw()
    msg1.undraw() 
    msg2.undraw()
    player1prompt.undraw()
    player2prompt.undraw()
    user_input1.undraw()
    user_input.undraw()
#initialize total roll variables and passes for players
    counter =1
    player1_total=0
    player2_total=0
    passcount1 =3
    passcount2 = 3
    
#create counters for both players at the top of the window
    name1 = Text(Point(100, 15), "Player " + player1)
    rolls1 = Text(Point(100, 35), "Total Rolls: " + str(player1_total))
    pass1 = Text(Point(100, 55), "Passes: " + str(passcount1))
    name2 = Text(Point(400, 15), "Player " + player2)
    rolls2 = Text(Point(400, 35), "Total Rolls: " + str(player2_total))
    pass2 = Text(Point(400, 55), "Passes: " + str(passcount2))
    name1.draw(win)
    name2.draw(win)
    rolls1.draw(win)
    rolls2.draw(win)
    pass1.draw(win)
    pass2.draw(win)  
    
#While loop for when neither player has 21
    while player1_total <21 and player2_total <21:
  #print round 
        msg.setText('Round '+ str(counter)+ ':')  
        
    #Call pass_or_roll function
        if passcount1 >0:
            choice = pass_or_roll(player1, win)
        else:
            choice = 'R'
      #player plays call play_turn function
        total = play_turn(choice, player1, player1_total, passcount1, win)
      #if player one does not lose do same steps for player two's turn
        player1_total += total[0]
        passcount1 += total[1]
        if player1_total < 21:
            #give player the choice to pass or roll if they have passes left otherwise just roll for them
            if passcount2 >0:
                choice=  pass_or_roll(player2, win)
            else:
                choice = 'R'
            total = play_turn(choice, player2, player2_total, passcount2, win)
            player2_total +=total[0]
            passcount2 += total[1]
#add to the round counter
        counter +=1
        #print after every round the scores and passes for both playes
        rolls1.setText("Total Rolls: " + str(player1_total))
        pass1.setText("Passes: " + str(passcount1))
        rolls2.setText("Total Rolls: " + str(player2_total))
        pass2.setText("Passes: " + str(passcount2))

        #print who won
    if player1_total >= 21:
        won = (player2+ ' won!')
    elif player2_total >=21:
        won = (player1+ ' won!')
    Final = Text(Point(250,160), won)
    Final.setSize(35)
    Final.setFill('yellow')
    Final.draw(win)
    
    #print message that tells user to click to close window with a mouse click
    end_msg =  Text(Point(250, 200), "Click to close")
    end_msg.draw(win)
    win.getMouse()
    win.close()
main()