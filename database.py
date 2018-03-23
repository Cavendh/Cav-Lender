import sys
# if sys.version_info > (2,7):
import sqlite3

class Database:
	# constructor
	def __init__(self):
		self.conn = sqlite3.connect('cav.db')
		self.cursor = self.conn.cursor()

	# destructor
	def __del__(self):
		self.conn.close()

	def createDB(self):
		try:
			self.cursor.execute(
			'''
			CREATE TABLE calendar
			(name text, event text, date text)
			'''
			)
		except:
			return

	def insertRow(self, name, event, date):
		toExecute = "INSERT INTO calendar VALUES ('%s', '%s', '%s')" % (name, event, date)
		self.cursor.execute(toExecute)
		self.conn.commit()

	def getRow(self, name):
		self.cursor.execute("SELECT * FROM calendar WHERE name=?", (name,))
		print(self.cursor.fetchall())

	# time format = YYYY-MM-DD HH:MM:SS
	def getTime(self, date):
		self.cursor.execute("SELECT * FROM calendar WHERE date=?",(date,))
		print(self.cursor.fetchall())

	def getEvent(self, event):
		self.cursor.execute("SELECT * FROM calendar WHERE event=?",(event,))
		print(self.cursor.fetchall())

if __name__ == "__main__":
	db = Database()
	db.createDB()
	# db.insertRow("Jeff", "event", "time")
	db.getRow("Jeff")
	print("-----------")
	db.getTime("time")
	print("-----------")
	db.getEvent("event")
