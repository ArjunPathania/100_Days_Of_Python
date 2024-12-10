from flask import Flask

app = Flask('__main__')

def make_bold_decorator(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper

def make_italics_decorator(function):
    def wrapper():
        return "<em>"+function()+"</em>"
    return wrapper


def make_underlined_decorator(function):
    def wrapper():
        return "<u>"+function()+"</u>"
    return wrapper

@app.route('/')
@make_bold_decorator
@make_italics_decorator
@make_underlined_decorator
def home_page():
    return 'Index'

@app.route('/users/<username>')
def index(username):
    return f"<h1>Hello {username}</h1>"


if __name__=='__main__':
    app.run(debug=True)