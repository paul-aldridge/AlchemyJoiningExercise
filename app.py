#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

#Inital data structure for phone book
phonebook = [
	{
		'id': 1,
		'Surname': u'Aldridge',
		'Firstname': u'Paul',
		'Phone number': '07636727223',
		'Address': 'Brassey Road'
	},
	{
		'id': 2,
		'Surname': u'Smith',
		'Firstname': u'Andy',
		'Phone number': '07637747746',
		'Address': 'Clarent Street'
	}
]

#Return phone book contents
@app.route('/phonebook')
def get_phonebook():
    return jsonify({'phonebook': phonebook})

#Search phone book for a surname
@app.route('/phonebook/<string:surname>', methods=['GET'])
def get_task(surname):
    entry = [entry for entry in phonebook if entry['Surname'] == surname]
    if len(entry) == 0:
        abort(404)
    return jsonify({'Entry found': entry[0]})

#Add new entry to phone book
@app.route('/phonebook', methods=['POST'])
def create_task():
    if not request.json or not 'Surname' in request.json or not 'Firstname' in request.json or not 'Phone number' in request.json:
        abort(400)
    entry = {
        'id': phonebook[-1]['id'] + 1,
        'Surname': request.json['Surname'],
        'Firstname': request.json['Firstname'],
        'Phone number': request.json['Phone number'],
        'Address': request.json.get('Address', ""),
        'done': False
    }
    phonebook.append(entry)
    return jsonify({'New entry': entry}), 201

#Update an existing entry in phone book
@app.route('/phonebook/<string:surname>', methods=['PUT'])
def update_task(surname):
    entry = [entry for entry in phonebook if entry['Surname'] == surname]
    if len(entry) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'Surname' in request.json and type(request.json['Surname']) is not unicode:
        abort(400)
    if 'Firstname' in request.json and type(request.json['Firstname']) is not unicode:
        abort(400)
    if 'Phone number' in request.json and type(request.json['Phone number']) is not unicode:
        abort(400)
    if 'Address' in request.json and type(request.json['Address']) is not unicode:
        abort(400)
    entry[0]['Surname'] = request.json.get('Surname', entry[0]['Surname'])
    entry[0]['Firstname'] = request.json.get('Firstname', entry[0]['Firstname'])
    entry[0]['Phone number'] = request.json.get('Phone number', entry[0]['Phone number'])
    entry[0]['Address'] = request.json.get('Address', entry[0]['Address'])
    return jsonify({'Updated entry': entry[0]})

#Remove existing entry from phone book
@app.route('/phonebook/<string:surname>', methods=['DELETE'])
def delete_task(surname):
    entry = [entry for entry in phonebook if entry['Surname'] == surname]
    if len(entry) == 0:
        abort(404)
    phonebook.remove(entry[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)