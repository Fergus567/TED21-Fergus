# Fergus Earl
# Environmental Quiz

'''An environmentally aware quiz on 5 relevant global topics and issues.'''

# imports
import json
import random
import easygui
from collections import OrderedDict

# functions
def get_quiz():
    '''Loads the quiz data from questions.json as a dictionary'''
    with open('questions.json', 'r') as f:
        return json.load(f, object_pairs_hook=OrderedDict) # returns the quiz dictionary and orders it with the collections input
                                                            #(fixes questions sometimes being out of order on load)

# initial variable declarations
condition = True
quiz = get_quiz() 

print(quiz)

# main routine
if easygui.msgbox("Welcome to the EnviroQuiz!\ncoded and maintained by Fergus Earl", "EnviroQuiz | Welcome") != 'OK':
    exit() # means the close window button was pressed

while condition: # loops the script until the condition is set to false
    score = 0


    for question in quiz:
        answers = quiz[question]["answers"]
        answer = quiz[question]["answer"]
        fact = quiz[question]["fact"]

        random.shuffle(answers) # shuffle the list to create a different order of answers each time

        user_answer = easygui.buttonbox(question, "EnviroQuiz | Score {}".format(score), answers)

        if user_answer not in answers:
            exit() # means the close window button was pressed

        if user_answer == answer:
            score += 1
            statement = 'Correct!'
        else:
            statement = 'Incorrect! The right answer was {}'.format(answer)

        if easygui.msgbox("{}\n\n{}".format(statement, fact), 'EnviroQuiz | Score {}'.format(score), ('Continue')) != 'Continue':
            exit() # means the close window button was pressed
    
    if not easygui.boolbox('Good effort! Your final score was {}'.format(score), 'EnvrioQuiz | Play again?', ['Play again', 'Exit']):
        condition = False # break the loop by changing the condition
