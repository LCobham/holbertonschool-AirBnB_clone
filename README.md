# Hbnb : *The Airbnb Clone*

The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://intranet.hbtn.io/rltoken/FrRTcvuF5L9wWDzFE9k01A "AirBnB website"). This project will have multiples features, but the first one has to be **The Console**

## Learning objetives:

 With this project we will have the power of:

> ° Have a parent class called BaseModel that will be useful for   
> Initialization, seralization and deserialization: Instance <->   
> Dictionary <-> JSON string <-> file
> ° Create all classes used for Airbnb
>        ° How to handle **File storage**
>        ° Unittests to validate all our classes and storage engine


The good performance of our console system is very important because we are going to handle and store a powerful amount of data that will be necessary throughout the entire project, so a good storage system will make us don´t  have to pay attention of how the objects are stored.

##  Requirements

- [x] All the files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- [x] `README.md`  file must exist
 - [x] All the files use the  `pycodestyle (version 2.7.)`  standard guidelines, including class and functions documentation
 - [x] All tests are execute using the  `unittest`  module
 - [x] List item

All the files and folders are presented as a tree in the file explorer. It can be switch from one to another by clicking a file in the tree.

## The main file: `Console.py`

This program will have the entry point of the command interpreter. The allowed commands you can use are:

|       FUNCTIONS     |USAGE                        |  INPUT                     |
|----------------|-------------------------------|-----------------------------|
|*do_quit*|To end the file           |`quit`            |
|*do_EOF*          |End of file            |ctrl + d           |
|*do_create*          |Creates a new instance of a given class|`create` + `class name`|
|*do_show*| Display the string representation of a model with a specific ID. |`show` + `class name` + `ID`. 
|*do_destroy*|Destroys an instance of a a given model.|`destroy` + `class name` + `ID`
| *do_all* | Prints all instances of a given class. If no arguments are given, prints every instance. |`all` + `class name` or `all`
|*do_update*| Updates an instance of a model, adds attributes| `update` + `class name`+ `ID`+`attribute name`+`attribute value`

## `./console.py`

Clone this repository:

```
git clone https://github.com/mattowsh/holbertonschool-AirBnB_clone.git

```

Execute the console in interactive mode:

    $ ./console.py
    (hbnb) help
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit



Execute the console in non-interactive mode: 

```
	$ echo "help" | ./console.py
	(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
Unit testing:
```
python3 -m unittest discover tests
```

## `file_storage.py`
	
This is the main responsable to make safe all the data in the storage system, it is also important do serialization and deserialization of JSON files
The file contains:

 - *all*: Returns all the '__objects' dictionary
 - *new*: Creates new entry in the '__objects' dictionary
 - *save*: Serializes the '__objects' dictionary to the JSON file with path = __file_path
 - *reload*: Deserializes the JSON file to __objects if the path specified in __file_path exists.

## Classes

BaseModel is our parent class, all of the future classes will inherit from this one, here are all common attributes and methods, but there are others classes:
| NAME OF THE CLASS | ATTRIBUTES |
|--|--|
| User| `email` `password` `first name` `last name`
| State | `name` |
|City  | `state_id` `name` |
| Amenity |`name`  |
| Place |  `city_id` `user_id` `name` `description` `number_rooms` `number_bathrooms` `max_guest` `max_guest` `latitude` `longitude` `amenity_ids` |
|Review  |  `place_id` `user_id` `text`|



 

***AUTHORS***:
[Lucas Cobham](https://github.com/LCobham)
[Romina Benitez](https://github.com/Blingblinggiirl)