import sys
# if sys.version_info > (2,7):
import sqlite3

class Database:
	def __init__(self):
		self.conn = sqlite3.connect('cav.db')
		self.cursor = self.conn.cursor()
	
	def __del__(self):
		self.conn.close()
	
	def createDB(self):
		try:
			self.cursor.execute(
			''' 
			CREATE TABLE calendar
			(name text, date text, time text)
			'''
			)
		except: 
			return
	
	def insertRow(self, name, date, time):
		toExecute = "INSERT INTO calendar VALUES ('%s', '%s', '%s')" % (name, date, time)
		self.cursor.execute(toExecute)
		self.conn.commit()
	
	def getRow(self, name):
		self.cursor.execute("SELECT * FROM calendar WHERE name=?", (name,))
		print(self.cursor.fetchall())
	

if __name__ == "__main__":
	db = Database()
	db.createDB()
	# db.insertRow("Jeff", "date", "time")
	db.getRow("Jeff")
