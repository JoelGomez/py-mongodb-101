"""
CRUD básico con MongoDB y Python
"""
from pymongo import MongoClient
from bson import ObjectId
from os import system

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)
db = client['test-store']
collection = db['products']

def add_product():
    """Agrega un producto a la BD"""
    p_name = input("Nombre del producto: ")
    p_price = input("Precio del producto: ")
    p_stock = input("Productos en stock: ")
    p_category = input("Categoría del producto: ")

    collection.insert_one({
        "name" : p_name,
        "price" : p_price,
        "stock" : p_stock,
        "category" : p_category
    })
    print("-" * 50)
    print("Producto agregado")
    print("-" * 50)
    print('\n')


def list_products():
    """Lista de todos los productos en BD"""
    results = collection.find({})
    for result in results:
        print("id: ", result['_id'])
        print("Nombre: ", result['name'])
        print("Precio: ", result['price'])
        print("Stock: ", result['stock'])
        print("-" * 20)

    print("-" * 50)
    print("\n")

def find_product(id):
    """Busca un producto mediante su _id"""
    result = collection.find_one({"_id" : ObjectId(id)})
    print("id: ", result['_id'])
    print("Nombre: ", result['name'])
    print("Precio: ", result['price'])
    print("Stock: ", result['stock'])
    print("-" * 20 ,"\n")


def update_product():
    """Actualiza los datos de un producto
       que se busca por su _id
    """
    id = input("Id del producto: ")
    find_product(id)
    n_name = input("Nuevo nombre: ")
    n_price = input("Nuevo precio: ")
    n_stock = input("Nuevo stock: ")

    collection.update_one({"_id":ObjectId(id)}, {"$set":{"name":n_name, "price": n_price, "stock":n_stock}})
    system('cls')
    print("Producto actualizado")
    find_product(id)
    print("-" * 50)

def delete_product(id):
    """Elimina un producto de la bd"""
    print("Seguro que quiere eliminar el siguiente producto?")
    find_product(id)
    print("Escriba SI o NO")

    while True:
        res = input(": ")
        if res == 'SI':
            collection.delete_one({"_id" : ObjectId(id)})
            print("El producto ha sido eliminado")
            print("-" * 50)
            break
        elif res == 'NO':
            break


while True:
    print("Elije alguna de las siguientes opciones")
    print("1 Nuevo producto")
    print("2 Listar todos los productos")
    print("3 Buscar un producto")
    print("4 Actualizar un producto")
    print("5 Eliminar un producto")
    print("0 Para terminar el programa \n")

    res = int(input(":"))
    print('\n')

    if res == 0:
        print("691h")
        break
    elif res == 1:
        system('cls')
        add_product()
        
    elif res == 2:
        system('cls')
        list_products()
    elif res == 3:
        system('cls')
        id = input("Id del producto: ")
        find_product(id)
    elif res == 4:
        system('cls')
        update_product()
    elif res == 5:
        system('cls')
        id = input("Id del producto:")
        delete_product(id)
