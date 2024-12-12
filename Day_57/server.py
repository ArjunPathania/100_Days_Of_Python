from flask import Flask,render_template
# import random,datetime
import requests
app = Flask(__name__)

@app.route('/')
def index():
    # random_number= random.randint(0,9)
    # current_year = datetime.datetime.now().year
    return render_template('index.html')

@app.route('/guess/<string:name>')
def guesser(name):
    # random_number= random.randint(0,9)
    # current_year = datetime.datetime.now().year
    age = requests.get(url=f'https://api.agify.io?name={name}')
    age.raise_for_status()
    result = age.json()
    gender = requests.get(url=f'https://api.genderize.io?name={name}')
    gender.raise_for_status()
    gender_result = gender.json()
    return render_template('guess.html',name=name,age = result['age'],gender=gender_result['gender'])

if __name__=='__main__':
    app.run(debug=True)