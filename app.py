from flask import Flask, render_template

import keys

app = Flask(__name__)
@app.route("/")
def index():
    old_fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    fruits = []
    for fruit in old_fruits:
        if fruit["name"][0].lower() == 'o' and fruit["quantity"] < 3:
            fruits.append(fruit)
        else:
            continue


    return render_template("index.html", fruits=fruits)

print(keys.MY_SECRET_API_KEY)
print(keys.MY_SECRET_API_KEY2)