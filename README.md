[![HitCount](http://hits.dwyl.com/ThibautBernard/AirBnB_clone.svg)](http://hits.dwyl.com/ThibautBernard/AirBnB_clone)
[![Python Style Guide: Good](https://img.shields.io/badge/code%20style-goodparts-brightgreen.svg?style=flat)](https://github.com/dwyl/goodparts "Python Good")
[![Inline docs](http://inch-ci.org/github/ThibautBernard/AirBnB_clone.svg?branch=master)](http://inch-ci.org/github/ThibautBernard/AirBnB_clone)

# AirBnB 

![](https://github.com/ThibautBernard/AirBnB_clone/blob/main/img_repo/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png)
## Description 
* This project is from my cursus at Holberton School. 
* The purpose of this project is to create a reproduction of the famous site *airbnb.com* from scratch.
* The language used in this project is Python, Javascript and *HTML/CSS*.
* The project will use also the framework **Flask** and will be hosted on **AWS**.
* 3 parts (Back-end, Front-end, Hosting)
* Launch UnitTest ``` python3 -m unittest discover tests ```

## :large_blue_circle: Back-End : 
![](https://github.com/ThibautBernard/AirBnB_clone/blob/main/img_repo/d2d06462824fab5846f3.png)
### :pushpin: First step of the Back-end part
#
* :large_blue_diamond: Create all classes
  * FileStorage 
    * Reload objects from a Json file
    * Save objects into Json file
    * Serialize
    * Deserialize
    * Return all current object
  * BaseModel
    * Main class were every classes will inherit from
    * unique id
    * created_at
    * updated_at
    * Representation of the object
  * User, State...
#
* :large_blue_diamond: Create a command line interpreter to manage our objects 
  * That create a new object (ex: a new User or a new Place)
  * Retrieve an object from a file, a database etc…
  * Do operations on objects (count, compute stats, etc…)
  * Update attributes of an object
  * Destroy an object
  * Store and persist objects to a file (JSON file)

### Knowledge (first part)
* Create a Python package
* How to create a command interpreter in Python using the cmd module
* What is an UUID
* How to serialize and deserialize a Class
* How to write and read a JSON file
* Use Unit testing and how to implement it in a large project
* *args and how to use it
* What is **kwargs and how to use it

### Usage of the console
* Firstly ``` git clone https://github.com/ThibautBernard/AirBnB_clone ```
* Secondly ``` ./console.py ```
### Classes 
* BaseModel
* User
* State
* City
* Place
* Review 
* Amenity
### Commands 
* Create (create a new object) ``` (hbtn) create <class_name> ```
* All (list all the current object of all classes instanced) ``` (hbtn) all ```
  * List only current object instanced of one classes ``` (hbtn) all <class_name> ```
* Show (Prints the string representation of an instance based on the class name) ``` (hbtn) show <class_name> <object_id> ```
  * Other way ``` (hbtn) <class_name>.show(<object_id>) ```
* Destroy (deletes an instance based on the class name and id (save the change into the JSON file)) ``` (hbtn) destroy <class_name> <object_id> ```
  * Other way ``` (hbtn) <class_name>.destroy(<object_id>) ```
* Update (updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) ``` (hbtn) update <class name> <id> <attribute name> "<attribute value>" ```
  * Other way ``` (hbtn) <class_name>.update(<object_id>, <attribute_name>, <value>) ```
* Count (return the count of all instances from a class) ``` (hbtn) <class_name>.count() ```
* Help ``` (hbtn) help ```
  * Help on one command ``` (hbtn) all <command_name> ```
* Quit the console ``` (hbtn) quit ```
### Interactive mode
``` echo "create <class_name>" | ./console.py ```
### Non interactive mode
``` (hbtn) create <class_name>  ```
### Examples
* Create a new user 
``` 
    (hbtn) create User  
    (hbtn) 2b8b754e-5fc4-40e0-bd92-3524ae7e60cf
    (hbtn) show User 2b8b754e-5fc4-40e0-bd92-3524ae7e60cf
    (hbtn) [User] (7a872431-b5b5-4522-a9d5-6c46c55ce4c8) {'id': '7a872431-b5b5-4522-a9d5-6c46c55ce4c8', 'created_at': datetime.datetime(2021, 2, 18, 14, 19, 1, 817111), 'updated_at': datetime.datetime(2021, 2, 18, 14, 19, 1, 817184)}

```
#### This project was done by Thibaut
#
