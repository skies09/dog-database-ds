import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dog_database'
app.config["MONGO_URI"] = 'mongodb+srv://admin:admin1@myfirstcluster-oj81k.mongodb.net/dog_database?retryWrites=true'

mongo = PyMongo(app)

#home page
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

#all dogs
@app.route('/all_group')
def all_group():
    return render_template('all_group.html', reverse="true",
     breed=mongo.db.breed.find())
    
# add dog page
@app.route('/add_breed')
def add_breed():
    return render_template('add_breed.html',
    group=mongo.db.group.find(),
                           breed=mongo.db.breed.find(),
                           size=mongo.db.breed.find(),
                           lifespan=mongo.db.breed.find(),
                           exercising_needs=mongo.db.breed.find(),
                           grooming_needs=mongo.db.breed.find(),
                           intelligence=mongo.db.breed.find())
                          

#this inserts the added dog into the database
@app.route('/insert_dog', methods=['POST'])
def insert_dog():
    breed = mongo.db.breed
    breed.insert_one(request.form.to_dict())
    return redirect(url_for('get_dogs'))    
    
    
#Edit dog section
@app.route('/edit_breed/<breed_id>')
def edit_breed(breed_id):
    breed =  mongo.db.breed.find_one({"_id": ObjectId(breed_id)})
    return render_template('edit_breed.html', breed=breed)

@app.route('/update_breed/<breed_id>', methods=["POST"])
def update_breed(breed_id):
    breed = mongo.db.breed
    breed.update( {'_id': ObjectId(breed_id)},
    {
        'breed':request.form.get('breed'),
        'group':request.form.get('group'),
        'size':request.form.get('size'),
        'lifespan': request.form.get('lifespan'),
        'exercising_needs': request.form.get('exercising_needs'),
        'grooming_needs':request.form.get('grooming_needs'),
        'intelligence':request.form.get('intelligence')
    })
    return redirect(url_for('get_dogs'))
    
#This deletes the dog
@app.route('/delete_breed/<breed_id>', methods=["GET","POST"])
def delete_breed(breed_id):
    mongo.db.breed.remove({'_id': ObjectId(breed_id)})
    return redirect(url_for('get_dogs'))

#sort dogs by size
@app.route('/sort_by_size/<reverse>/', methods=["GET","POST"])
def sort_by_size(reverse):
    print(reverse, type(reverse))
    if reverse.lower() == "true":
        reverse = True
        breed=mongo.db.breed.find().sort("size", 1)
    else:
        breed=mongo.db.breed.find().sort("size", -1)
        reverse = False
    return render_template('all_group.html', breed=breed, reverse = str(not reverse).lower())
    
#sort dogs by exercise_needs
@app.route('/sort_by_exercise_needs/<reverse>/', methods=["GET","POST"])
def sort_by_exercise_needs(reverse): 
    print(reverse, type(reverse))
    if reverse.lower() == "true":
        reverse = True
        breed=mongo.db.breed.find().sort("exercise_needs", -1)
    else:
        breed=mongo.db.breed.find().sort("exercise_needs", 1)
        reverse = False
    return render_template('all_group.html', breed=breed, reverse = str(not reverse).lower())

#sort dogs by grooming_needs
@app.route('/sort_by_grooming_needs/<reverse>/', methods=["GET","POST"])
def sort_by_grooming_needs(reverse): 
    print(reverse, type(reverse))
    if reverse.lower() == "true":
        reverse = True
        breed=mongo.db.breed.find().sort("grooming_needs", -1)
    else:
        breed=mongo.db.breed.find().sort("grooming_needs", 1)
        reverse = False
    return render_template('all_group.html', breed=breed, reverse = str(not reverse).lower())

#sort dogs by intelligence
@app.route('/sort_by_intelligence/<reverse>/', methods=["GET","POST"])
def sort_by_intelligence(reverse): 
    print(reverse, type(reverse))
    if reverse.lower() == "true":
        reverse = True
        breed=mongo.db.breed.find().sort("intelligence", -1)
    else:
        breed=mongo.db.breed.find().sort("intelligence", 1)
        reverse = False
    return render_template('all_group.html', breed=breed, reverse = str(not reverse).lower())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)