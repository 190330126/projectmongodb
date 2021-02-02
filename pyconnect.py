from pymongo import MongoClient # import mongo client to connect
import pprint
# Creating instance of mongoclient
client = MongoClient()
# Creating database
db = client.employee

employee = [{"empid": 1009,"name": "RAJU","dept": "CSE","salary": 200000,"age": 24},
            {"empid": 1008,"name": "LAVI","dept": "ESE","salary": 20000,"age": 25},
            {"empid": 1001,"name": "GANAPTHY","dept": "EEE","salary": 20000,"age": 26}]

# Creating document
employees = db.employees
# Inserting data
employees.insert_many(employee)
# Fetching data

for i in employees.find():
    pprint.pprint(i)