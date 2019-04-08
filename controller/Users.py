import mysql.connector
import os

class Users:

	def __init__(self):
		self.__localhost     = os.environ.get('LOCALHOST')
		self.__username      = os.environ.get('USER')
		self.__password      = os.environ.get('PASSWORD')
		self.__database_name = os.environ.get('DATABASE')
		self.__table_name 	 = os.environ.get('TABLE_NAME')
		self.createConnection()

	def create(self, name, address):
		cursor = self.__db.cursor()

		val = (name, address)
		cursor.execute("INSERT INTO "+self.__table_name+" (name, address) VALUES (%s, %s)", val)

		self.__db.commit()

		return {
	    	"status": "success",
	    	"messge": str(cursor.rowcount)+ "record inserted."
	    }

	def read(self):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+"")

		myresult = cursor.fetchall()

		return myresult

	def get(self, id):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+" WHERE id=%s LIMIT 1", (id,))
		myresult = cursor.fetchone()

		print(myresult)

		if myresult != None:
			return {
				"status": 1,
				"id": myresult[0],
				"name": myresult[1],
				"address": myresult[2]
			}	
		else:
			return {
				"status": 0,
				"message": "The ID that your looking for is not in the database or has already been deleted"
			}	


	def update(self, id, name, address):

		if id is "":
			return "Leaving id empty will cause an error like this."

		if name is "":
			return "Leaving name empty will update the value to empty as well."

		if address is "":
			return "Leaving address empty will update the value to empty as well."

		cursor = self.__db.cursor()

		cursor.execute("UPDATE "+self.__table_name+" SET name=%s, address=%s WHERE id=%s ", (name, address, id))
		self.__db.commit()

		user = self.get(id)

		return user


	def delete(self, id):
		cursor = self.__db.cursor()

		user = self.get(id)

		if user["status"]:
			cursor.execute("DELETE FROM "+self.__table_name+" WHERE id = %s", (id,))
			self.__db.commit()
		

		return user

	def createConnection(self):
		db = mysql.connector.connect(
		  host     = self.__localhost,
		  user     = self.__username,
		  passwd   = self.__password,
		  database = self.__database_name
		)

		self.__db = db