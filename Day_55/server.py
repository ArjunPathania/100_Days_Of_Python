from flask import Flask
from random import randint

lucky_number = randint(0, 9)
print(lucky_number)

app = Flask('__main__')

@app.route('/')
def index():
    return """<h1>Guess a number between 0 and 9</h1>
    <img src ="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGd4MTA2dnhmMnNqYXdza2Fzdmc3YzlkZmJpbjJzaDB1dDkzaDluZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.webp"/ alt="numbers gif" width="500" height="600">
     """

@app.route('/<int:guess>')
def guess_page(guess):

    if guess < lucky_number:
        return """<h1 style="color:red;">Too Low ,Try Again</h1>
    <img src ="https://i.giphy.com/jD4DwBtqPXRXa.webp"/ alt="Too Low" width="500" height="600">
     """
    elif guess > lucky_number:
        return """<h1 style="color:purple";>Too High ,Try Again</h1>
            <img src ="https://i.giphy.com/3o6ZtaO9BZHcOjmErm.webp"/ alt="Too High" width="500" height="600">
             """
    else:
        return """<h1 style="color:green";>You found me!</h1>
    <img src ="https://i.giphy.com/4T7e4DmcrP9du.webp"/ alt="Correct" width="500" height="600">
     """

if __name__=="__main__":
    app.run(debug=True)