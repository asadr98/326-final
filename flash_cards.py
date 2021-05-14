"""This program is designed to parse through a set of flash cards for the user studying.
    
    INST326 Final Project
    """
import re
import sys
from argparse import ArgumentParser
from pprint import PrettyPrinter
pp = PrettyPrinter()
class Flash:
    
    """This class stores the individual questions and answers for each flash card and gets user input.
    
    Attr:
    cards (list): all the flash cards
    path: path to read in txt file
    """
    def __init__(self, path):
        """Initializes a Flash object.

        Args:
            cards (list): List of the flash cards
            path: path to read in txt file
        """
        self.cards = []
        self.path = path
        
        
    def get_text(self):
        """This function reads in text file
        Driver: Asad Raheem
        Navigator: Sana Hassan
        Args:
        text: object to read in text file
        
        Returns:
            text
        """
        text = ''
        with open(self.path, "r", encoding = "utf-8") as f:
            text = f.read()
        return text
    
    def split_text_into_cards(self, text):
        """This function splits the list of all cards into individual cards.
        Driver: Sana Hassan
        Navigator: Asad Raheem

        Args:
            individ_cards (list): Each individual card split

        Side effects:
            Modifies cards list to include each individual card
        """
        individ_cards = text.split('End"')
       
        for maybe_card in individ_cards:
            question_re = re.compile(r'Question:\s(.+)')
            answer_re = re.compile(r'Answer:\s(.+)')
            
            maybe_question = question_re.search(maybe_card)
            maybe_answer = answer_re.search(maybe_card)
           
            if maybe_question and maybe_answer: 
                question = maybe_question.group(1)
                answer =     maybe_answer.group(1)
                card = Card(question, answer)
                self.cards.append(card)
              
        return self.cards
    '''
    +------------------------------+
    |  question: bla bla           |
    |  what is your answer:        |
    |            some answer       |
    '''
    def go_thru(self, cards):
        """This function outputs each question one by one and then 
        allows the user to input their answer. It then informs them if they are correct or not.
        If incorrect it outputs the correct answer. It does this for each individual card in the set.
        Driver: Asad Raheem
        Navigator: Sana Hassan

        Args:
            cards (list): List of cards
            question_text (str): String of each question
            answer_prompt (str): String to inform user to input answer
            user_answer (input): User input of their answer.
        
        Side effects:
            Prints each question, user answer, whether answer is correct or not, and correct answer.
        
        """
        for card in cards:
            print('+' + ('-'*60) + '+')
            question_text = f'question; "{card.question}"'
            print(f'| {question_text:<59}|')
            answer_prompt = "Enter your answer:"
            user_answer = input(f'| {answer_prompt:<59}|\n| ')
            
            
            
            if user_answer == "cheat":
                print(f'answer: "{card.answer}"')
                user_answer = input("Enter your answer:\n")
                
            print(f'you answered "{user_answer}"')
            if user_answer == card.answer:
                print('Correct answer')

            else:
                print('Wrong answer')
                print(f'correct answer:"{card.answer}"')

class Card:
    """This class stores each question and answer.
    Driver: Sana Hassan
    Navigator: Asad Raheem
    
    Args:
    question: hold each question
    answer: holds each answer
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def main(f):
    """Calls functions from Flash class to output each card and allow user answers.
    Driver: Asad Raheem
    Navigator: Sana Hassan
    
    Args:
    flash (variable): Instance of Flash card
    text (variable): Instance of get_text() function from Flash class
    
    Returns:
    f: Instance of Flash card
    
    """
    
    flash = Flash(f)
    text = flash.get_text()
    
    cards = flash.split_text_into_cards(text)
    flash.go_thru(cards)
    
    return f

   

def parse_args(arglist):
    """ Parse command-line arguments.
    Driver: Sana Hassan
    Navigator: Asad Raheem
    Args:
    parser
    parser.add_argument
    
    Returns:
    arglist"""
    parser = ArgumentParser(arglist)
    parser.add_argument("path")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    """Runs function.
    Attr:
    args
    Prints:
    Main function
    "Thank you for studying. Great job!"
    """

    args = parse_args(sys.argv[1:])
    print(main(args.path))
    print("Thank you for studying. Great job!")
