import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dog_database'
app.config["MONGO_URI"] = 'mongodb+srv://admin:admin1@myfirstcluster-oj81k.mongodb.net/dog_database?retryWrites=true'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_dogs')
def get_dogs():
    return render_template("dogs.html")
    
#Group navigation
#Hound group navigation
@app.route('/hound_group')
def hound_group():
    return render_template('hound_group.html',
    breed=mongo.db.breed.find({"group": "Hound"}))
    
#Gundog group navigation
@app.route('/gundog_group')
def gundog_group():
    return render_template('gundog_group.html',
    breed=mongo.db.breed.find({"group": "Gundog"}))
    
#Pastoral group navigation
@app.route('/pastoral_group')
def pastoral_group():
    return render_template('pastoral_group.html',
    breed=mongo.db.breed.find({"group": "Pastoral"}))
    
#Terrier group navigation
@app.route('/terrier_group')
def terrier_group():
    return render_template('terrier_group.html',
    breed=mongo.db.breed.find({"group": "Terrier"}))
    
#Toy group navigation
@app.route('/toy_group')
def toy_group():
    return render_template('toy_group.html',
    breed=mongo.db.breed.find({"group": "Toy"}))
    
#Utility group navigation
@app.route('/utility_group')
def utility_group():
    return render_template('utility_group.html',
    breed=mongo.db.breed.find({"group": "Utility"}))
    
#Working group navigation
@app.route('/working_group')
def working_group():
    return render_template('working_group.html',
    breed=mongo.db.breed.find({"group": "Working"}))

    
# add dog page
@app.route('/add_breed')
def add_breed():
    return render_template('add_breed.html',
    group=mongo.db.group.find(),
                           breed=mongo.db.breed.find())
                          

#this inserts the added dog into the database
@app.route('/insert_dog', methods=['POST'])
def insert_dog():
    breed = mongo.db.breed
    breed.insert_one(request.form.to_dict())
    return redirect(url_for('get_dogs'))    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)