from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year)
@app.route("/guess/<name>")
def guess(name):
    AGE_URL = f'https://api.agify.io?name={name}'
    GENDER_URL = f'https://api.genderize.io/?name={name}'
    age_response = requests.get(AGE_URL)
    gender_response = requests.get(GENDER_URL)
    gender_data = gender_response.json()
    gender = gender_data['gender']
    age_data = age_response.json()
    age = age_data['age']
    return render_template("guess.html", age=age, gender=gender, name=name)
@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
