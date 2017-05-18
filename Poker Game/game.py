from sys import stdout
from time import sleep

class game(object):
    '''
    this class contains variables and functions will be called during the game
    '''
    
    def __init__(self, init):
        """
        Construct, Initialize the object and check correctness of the input
        1, initial invest input should be a number
        2, initial invest input should be positive
        3, convert the float to int, since as long as you don't have 1 point
           you can play the game any more.
        """
        try:
            init = int(init)
        except ValueError:
            raise ValueError("Initial money should be a integer!")
        
        if init <= 0:
            raise ValueError("Initial money should be positive")
        
        self.red_curr = 26
        self.black_curr = 26
        self.init_pts = init
        self.current_pts = init
        self.in_hand_red = 0
        self.in_hand_black = 0
        self.drawed_card = None
    
    
    def calc_pts(self, drawed_card):
        """
        This function calculate the current points after draw
        Return current points and change in points
        """
        if drawed_card == "red":
            self.current_pts -= 1
            self.in_hand_red += 1
            change = -1
        if drawed_card == "black":
            self.current_pts += 1
            self.in_hand_black += 1
            change = 1
            
        return self.current_pts, change
            
    
    def draw_card(self):
        """
        This function will simulate the drawing process with dynamic probability
        and update the records of the remaining cards number.
        """
        # Simulate card drawing 
        import numpy as np
        red_prob = float(self.red_curr/(self.red_curr+self.black_curr))
        black_prob = 1-red_prob
        drawed_card = np.random.choice(np.array(["red","black"]), p=[red_prob,black_prob])
        
        # Update card numbers
        if drawed_card == "red":
            self.red_curr -= 1
        if drawed_card == "black":
            self.black_curr -= 1    
        
        return drawed_card
    
    
    def report_current_condition(self):
        """
        This function will report the current condition
        1, Your current points
        2, your wining/losing points
        """
        if self.current_pts > self.init_pts:
            baudout("Your current points is %d, you win %d points\n\n" % (self.current_pts, self.current_pts-self.init_pts))
        elif self.current_pts == self.init_pts:
            baudout("Your current points is %d, Drew\n\n" % (self.current_pts))
        elif self.current_pts < self.init_pts:
            baudout("Your current points is %d, you lose %d points\n\n" % (self.current_pts, self.init_pts-self.current_pts))
        
        
    
    def end_condition(self):
        """
        This function check if the game should be terminated
        1, player have no money
        2, no more card to draw
        If terminated, report condition.
        """
        if self.current_pts==0:
            baudout("You ran out of money, Game over!")
            self.report_current_condition()
            return True
        if self.black_curr+self.red_curr==0:
            baudout("There's no more card, Game over!")
            self.report_current_condition()
            return True
        
        
    def get_hint(self):
        """
        Cheating method
        1, Check how many red/black card left
        2, Calculate the wining expectation
        """
        win_rate = float((26-self.in_hand_black)/(52-self.in_hand_black-self.in_hand_red))
        exp_return = float((self.in_hand_red-self.in_hand_black)/(52-self.in_hand_black-self.in_hand_red))
        baudout("You have %d red cards and %d black cards in hand.\nThe probability of wining is %.2f, expected return is %.2f\n\n" % (self.in_hand_red,self.in_hand_black,win_rate, exp_return))


"""
Printing control, print the line character by character
Make the program looks like a old fashion game.
"""
BAUD = 1000
def baudout(str):
    for character in str:
        sleep(9. / BAUD)
        stdout.write(character)
        stdout.flush()
    
    