# AirBnB 
![](https://github.com/ThibautBernard/AirBnB_clone/blob/main/img_repo/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png)
* This project is from my cursus at Holberton School. 
* <br> The purpose of this project is to create a reproduction of the famous site *airbnb.com* from scratch.
* <br> The language used in this project is Python, Javascript and *HTML/CSS*.
* <br> The project will use also the framework **Flask** and will be hosted on **AWS**.
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
    * Main classes were every classes will inherit from
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

