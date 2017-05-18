from game import game, baudout
import sys

def main():
    """
    Main function, using two while true loop
    1, The first while loop check input of initial investment
       break until the input is in correct format
    2, The second while loop control the game play
       break if no more points(money) or no more cards left
    """
    while True:
        try:
            baudout("How much money do you want to invest?\n")
            init_invest = input()
        except EOFError:
            sys.exit(0)
            
        try: 
            game_obj = game(init_invest)
        except ValueError as error:
            print(error)
        else:
            break
            
    
    # Print the rules of the game
    baudout("Your investment is: %d\n" % game_obj.init_pts)
    baudout("Press press enter to continue.\n")
    input()
    print("===================== Play with Poker Card Game =======================\n")
    print("         Now, the game will begin, get ready!\n \
         1, - You have a standard deck of 52 cards facing down\n \
         2, - You can only draw one card at a time\n \
         3, - For each black card you draw, you earn $1\n \
         4, - For each red card you draw, you lose $1\n \
         5, - You may choose to stop drawing cards at any time by enter Quit\n \
         6, - When you have less than 1$, you can't play on and you lose!\n")
    print("========================================================================\n")
    baudout("Press press enter to continue.\n")
    input()
    
    while True:
        print("-------------------- Continue Game? ----------------------\n\n \
               Enter YES to continue\n \
               Enter No/Quit to exit\n \
               Enter Report to report current score\n \
               Enter hint to get recommendation.\n")
        print("----------------------------------------------------------\n ")
        draw = input()
        
        # Quit the game
        if draw.lower() == "no" or draw.lower() == "quit":
            baudout("Thanks for playing, ByeBye!")
            break
        
        # Cheat, get hint
        elif draw.lower() == "hint":
            game_obj.get_hint()
        
        # Report the current condition
        elif draw.lower() == "report":
            game_obj.report_current_condition()
        
        # Handle all other invalid input
        elif draw.lower() != "yes":
            baudout("Invalid Input! Enter Yes or No/Quit\n\n")
            continue
        
        # Input is yes, resume the game
        else:
            drawed_card = game_obj.draw_card()
            current_pts, change_in_point = game_obj.calc_pts(drawed_card)
            baudout("Your drawed card is %s, you get %d point.\nYour current points is %d\n\n" % (drawed_card,change_in_point,current_pts))
            end_flag = game_obj.end_condition()
            if end_flag == True:
                break

        
if __name__ == "__main__":
    main()        
            