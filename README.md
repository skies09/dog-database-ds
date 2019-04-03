# **K9 Collection**
---

## DEMO - https://dog-database-ds.herokuapp.com

This is the Data Centric milestone project for CodeInstitute.
This is an open sourced dog database which anyone and everyone can contribute to.





## Strategy for the project
### What the project does
* This is a dog breed database

### The need it fulfills
* There has yet to be a database showing all the dog breeds along with statistical information regarding each breed.
* This database can show every dog breed if needs be with as much information about the breeds to give users of the website as much information about the different dog breeds before purchasing/adopting a dog.
* Being open sourced this database has the potential to be changed by people who already own dogs, to give more and up to date information to potential dog owners.
* This in turn has the potential to reduce the number of rejected and homeless dogs as people will more likely get a breed they are more suited to.

### Target audience
* Dog owners, dog fanatics and potential dog adopters.

### Expansion strategy
* More categories such as 'cost to keep', 'good with children', 'amount of shedding' and 'tolerates being alone'
* Links to dog rescue homes to encourage smart and researched adoption and reduce the number of dogs in kennels.


# How the website is setup
---
## The body of the website is set up into

### Navigation Bar

Includes the website __brand__ along with a button to add a breed and a button linked to a page that shows all the breeds which are right aligned. 

### Introduction Container

Includes website banner and website title.

## Block content

### Home page

On the home page there is a carousel which can be scrolled through and shows links to each of the 7 dog groups.

### The group pages

The table below shows what is included in the section content on each page 

|Page         |  Section content|
|-------------|-----------------|
|Hound Group  |Title- The group that is shown. Multiple cards showing the different breeds with statistics and picture. There is also edit and delete buttons for each dog.|
|Gundog Group |Title- The group that is shown. Multiple cards showing the different breeds with statistics and picture. There is also edit and delete buttons for each dog.|
|Pastoral Group|Title- The group that is shown. Multiple cards showing the different breeds with statistics and picture. There is also edit and delete buttons for each dog.|
|Terrier Group|Title- The group that is shown. Multiple cards showing the different breeds with statistics and picture. There is also edit and delete buttons for each dog.|
|Toy Group    |Title- The group that is shown. Multiple cards showing the different breeds with statistics and picture. There is also edit and delete buttons for each dog.|
|Utility Group|Title- The group that is shown. Multiple cards showing the different breeds with statistics and picture. There is also edit and delete buttons for each dog.|
|Working Group|Title- The group that is shown. Multiple cards showing the different breeds with statistics and picture. There is also edit and delete buttons for each dog.|

### The all breeds page

The section content of this page has all the dog breeds regardless of dog group.
This list can be sorted using the buttons, depending on which statistic the user is looking for.

### The add breeds page

The section content of this page is a form that can be filled in by the user to add a dog breed to the collection.

### The edit breed page

If a user feels the data of a particular breed is inaccurate, they can update the information by clicking the edit button on the dog breed in question. The data of the dog appears in the form and the user has the option to change/update any of the data.

### Delete button

This button removes the dog breed in question.
There is a modal that appears when the delete button is clicked to make sure the breed is not deleted accidently by asking the user if they are sure to delete.

## Footer

Contains the copyright of the websites to the developer.


---

##### What was used in the website

* Google fonts
* Bootstrap 3.3.7
* Materialize 0.100.2
* cdnjs cloudflare
* jQuery 3.2.1
* Click==7.0
* Flask==1.0.2
* Flask-PyMongo==2.2.0
* Jinja2==2.10
* MarkupSafe==1.1.1
* Werkzeug==0.14.1
* dnspython==1.16.0
* itsdangerous==1.1.0
* pymongo==3.7.2
* MongoDB Atlas

---

### Ways of testing

#### Testing CRUD funtionality.
1. Edited beagle breed to test the edit page.
2. Deleted beagle breed to test the delete button.
3. Added beagle breed to test add page.
4. Checked every button on the all breeds page which does order the dogs by particular division. The drop downs for each dog also expand correctly.
5. The brand in the nav bar links to the home page from every page.

###### Browsers tested on

* Chrome
* Safari
* Firefox
* Mozilla

###### Responsive devices tested on
* iphone
* ipad
* Macbook air


## Deployment
1. Added requirements.txt file and Procfile.
2. Created Heroku app called dog-database-ds
3. Pushed to heroku.
4. Set scale, heroku ps:scale web=1
5. Heroku app settings, Config Vars - IP = 0.0.0.0 PORT = 5000

## Credits

### Content

Statistical information came from the pets4home.co.uk website.
