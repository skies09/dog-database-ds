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
    return render_template("dogs.html", group=mongo.db.group.find())
    
# add dog page
@app.route('/add_breed')
def add_breed():
    return render_template('add_breed.html',
    group=mongo.db.group.find(),
                           breed=mongo.db.breed.find())
                          

#this inserts the added dog into the database, this works!
@app.route('/insert_dog', methods=['POST'])
def insert_dog():
    breed = mongo.db.breed
    breed.insert_one(request.form.to_dict())
    return redirect(url_for('get_dogs'))    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)