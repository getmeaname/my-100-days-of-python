from flask import Flask
import random
app = Flask(__name__)

ans = random.randint(0,9)

@app.route("/")
def home_page():
    return '<h1>"Guess a number between 0 and 9"</h1>'\
           "<img src='https://www.defytvnet.com/'>"

@app.route("/<int:number>")
def user_generated_numbers(number):
    if number < ans:
        return "<h1>'Your guess is too low, try again'<h1>"\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > ans:
        return "<h1>'Your guess is too high, try again'<h1>" \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g">'
    elif number == ans:
        return "<h1>'Congrats, you've guessed the correct answer!'</h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)