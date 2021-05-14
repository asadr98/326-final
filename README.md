This program allows a user to read in a text file containing a set of questions and their corresponding answers. It then displays the question, allows the user to input their guess, and then informs them if they are correct or not. It is essentially a study tool in the form of flash cards.

It is designed to run from the command line in this format:
          python flashcards.py "textfile".txt
          *An example txt file is included in this repository. 
So this program can be run as 
          python flashcards.py sat_questions.txt

When this is run in the python terminal the question will be displayed, the user is given a chance to input their answer, and they are informed if their answer were correct or not. If user guesses the wrong answer the correct answer will be displayed. 
The program iterates through each question in the txt file. 

*There is also a test file called test_flashcards.py for unit tests.
