# Address Book

## Back-End

Based on Django and Python3

Codes are in the folder 'AddressBook'

URL '/Contact/' will return the index page

'/Contact/getContacts' will return all the data in JSON using GET

'/Contact/updateContact' will update/create/delete data using POST

if the request doesn't contain the address id, it will create one

if contains the key-value 'Function': 'Delete', that data will be deleted

otherwise it will be updated

## Front-End

Based on Angular 13 with the module angular2-smart-table 

(ng2-smart-table may have problems on dependence using Angular 13)

Codes are in the folder 'Contact'

## Database

sql file is in the folder 'database'