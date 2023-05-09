"""
MongoDB test from python
"""

from pymongo import MongoClient
from bson import ObjectId

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)
db = client['test-store']
collection = db['products']


# collection.insert_one({
#     "name" : "Mouse Gamer",
#     "price": 70
# })

# results = collection.find({"price|": 70})
# for result in results:
#     print(result['_id'], result['name'])


# producto1 = {"name" : "Teclado", "price" : 24}
# producto2 = {"name" : "Monitor 27", "price" : 70}

# collection.insert_many([producto1, producto2])

result = collection.find_one({"price": 70})
print(result)
print("-" * 50)


results = collection.find({"price": 70})
for result in results:
    print(result['_id'], result['name'])
print("-" * 50)

result = collection.find_one({'_id': ObjectId('64595066f1af6380130d26c7') })
print ("Objeto: " , result)


# eliminar un registro
#collection.delete_one({'_id': ObjectId('64595066f1af6380130d26c6') })

#eliminar todos los registros
#collection.delete_many({})

#atualizar un registro
#collection.update_one({"name": "laptop"}, {"$set": {"name": "keyboard", "price":300}})

#contar cuantos documentos hay en la colección
number_of_products = collection.count_documents({})
print(number_of_products)
