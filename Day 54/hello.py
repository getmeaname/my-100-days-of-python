from flask import Flask

app = Flask(__name__)
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>"\
           '<p style="text-align:center"> This is GPT </p>' \
           "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExamRkcGRxMGczbGgyYTlreDM2dzBpZDM3c3Y4ZWhwdmQ3ZDFsM25neCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DFexVkRG7gX9oCy68r/giphy.gif', width=200>"

@app.route("/Bye")
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return "<p>Bye, World!</p>"
@app.route("/Hello/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}!, You are {number} years."


if __name__ == "__main__":
    app.run(debug=True)