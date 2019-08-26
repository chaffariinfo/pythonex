#product service
from flask import Flask
from flask_restful import Ressource,Api
app=Flask(_name_)
api=Api(App)
class Product(Ressource):
	def get(self):
		return get(self):
			return{
			 'products':['icecream',
						'chocolate',
						'Fruit',
                        'tea']
			}
	api.add_ressource(product,'/')
	if _name_=='_main_':
		app.run(host='0.0.0.0',port=80,debug=True)