# AlchemyJoiningExercise

Phonebook
=========

This web service allows you to view and interact with a phonebook directory. 


How To Use
----------

There are five ways to interact with the service:

1. Viewing the conents of the phonebook: 
	http://localhost:5000/phonebook

2. Searching the phonebook for an entry matching a given Surname: 
	http://localhost:5000/<Surname>

3. Adding a new entry to the phonebook: 
	Making a POST request to http://localhost:5000/phonebook with data in json
	format including a Surname, Firstname, Phone number and (optionally) a 
	address (all should be in unicode) will insert a new entry into the phonebook. 
	
	For example (using curl):
	
	curl -i -H "Content-Type: application/json" -X POST -d '{"Surname":"West", 
	"Firstname":"Bill", "Phone number":"078483333"}' http://localhost:5000/phonebook

4. Updating an existing entry in the phonebook:
	Making a PUT request to http://localhost:5000/phonebook/<Surname> will update
	the entry corresponding to the given Surname. The data must be in json fomat
	and contain any combination of Surname, Firstname, Phone number and address 
	(all must be in unicode).

	For example (using curl):

	curl -i -H "Content-Type: application/json" -X PUT -d '{"Firstname":"Jenny"}' 
	http://localhost:5000/phonebook/West	

5. Delete an existing entry from the phone book
	curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/phonebook/West


How To Install
--------------

Create a new directory on your machine and copy all files from the github project
into it (file list below)


Flie List
---------

app.py
testSequence.py
README.md
flask (direcory)

