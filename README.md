# AirBnB 
![](https://github.com/ThibautBernard/AirBnB_clone/blob/main/img_repo/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png)
👉 This project is from my cursus at Holberton School. 
The purpose of this project is to create a reproduction of the famous site *airbnb.com* from scratch.
<br> The language used in this project is Python, Javascript and *HTML/CSS*.
<br> The project will use also the framework **Flask** and will be hosted on **AWS**.
* UnitTest ``` python3 -m unittest discover tests ```

## Back-End : 
![](https://github.com/ThibautBernard/AirBnB_clone/blob/main/img_repo/d2d06462824fab5846f3.png)
### First step of the Back-end part
#
* Create all classes
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
* Create a command line interpreter to manage our objects 
  * Create a new object (ex: a new User or a new Place)
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
* Create a new object ``` (hbtn) create <class_name> ```
* List all the current object of all classes instanced ``` (hbtn) all ```
  * List only current object instanced of one classes ``` (hbtn) all <class_name> ```
* Quit the console ``` (hbtn) quit ```

