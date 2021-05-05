# import the library
from appJar import gui


# variables

questions = [
["Trash","Good","Bad","1"],
["Plastic","Love","Hate","1"]
]

quiz_progress = 0

# handle button events
def press(button):
    global quiz_progress
    for question in range(len(questions)):
        if button == "1":
            if questions[quiz_progress][3] == "1":
                print("Correct")
                app.setLabel("Question","Correct")
                app.hideButton("1")
                app.hideButton("2")
                app.showButton("Next")
        if button == 2:
            print("Incorrect")
            app.setLabel("Question","Correct")
            app.hideButton("1") 
            app.hideButton("2")
            
        if button == "Next":
            
            quiz_progress = 1
            display_question(quiz_progress)
    

def display_question(quiz_progress):
    app.setLabel("Question",questions[quiz_progress][0])
    app.setButton("1",questions[quiz_progress][1])
    app.setButton("2",questions[quiz_progress][2])
    
# create a GUI variable called app
app = gui("Enviro quiz", "400x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to enviroQuiz")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabel("Question")

# link the buttons to the function called press=

app.addButton("1",press)
app.addButton("2",press)
app.addButton("Next",press)
app.hideButton("Next")

display_question(quiz_progress)

# start the GUI
app.go()