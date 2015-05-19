import os
import unittest
import tempfile
from app import app
import json

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def test_list_entries_in_phone_book(self):
        directory = self.app.get('/phonebook')
        self.assertEqual(directory.status, "200 OK")
        self.assertIn('"done": false', directory.data)    
    	
    def test_create_new_entry_in_phone_book_with_no_address(self):
        url = "/phonebook"
        data = {'Surname': 'Butcher', 'Firstname': 'Luke', 'Phone number': '07944938828'}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        entry = self.app.post(url, data=json.dumps(data), headers=headers)
        self.assertIn('Butcher', entry.data)

    def test_error_insert_missing_surname(self):
        url = "/phonebook"
        data = {'Firstname': 'Mike', 'Phone number': '07959483958'}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        entry = self.app.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(entry.status, '400 BAD REQUEST')

    def test_error_insert_missing_firstname(self):
        url = "/phonebook"
        data = {'Surname': 'Cross', 'Phone number': '07959433333'}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        entry = self.app.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(entry.status, '400 BAD REQUEST')

    def test_error_insert_missing_phone_number(self):
        url = "/phonebook"
        data = {'Surname': 'Smalling', 'Firstname': 'Ben'}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        entry = self.app.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(entry.status, '400 BAD REQUEST')

    def test_error_instert_not_json_data(self):
        url = "/phonebook"
        data = 'Jones, John, 07839488339'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        entry = self.app.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(entry.status, '400 BAD REQUEST')

    def test_remove_existing_entry_in_phone_book(self):
        url = '/phonebook/Smiths'
        self.app.delete(url)
        st = self.app.get('/phonebook/2')
        self.assertEqual(st.status, '404 NOT FOUND')

    def test_update_existing_entry_in_phone_book(self):
        url = 'phonebook/Aldridge'
        data = {'Address': '5 Smith Close, CM29 3JJ'}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        updatePage = self.app.put(url, data=json.dumps(data), headers=headers)
        print updatePage.data
        self.assertIn('5 Smith Close', updatePage.data)

    def test_search_entries_in_phone_book_for_surname(self):
    	surnameSearch = self.app.get('/phonebook/Aldridge')
    	self.assertIn('Aldridge', surnameSearch.data)

if __name__ == '__main__':
    unittest.main()