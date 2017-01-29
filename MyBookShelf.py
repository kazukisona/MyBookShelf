import pymysql

def add_book(db, title, author, publisher, published, isbn, buying):
	# making a cursor to a table
	cur = db.cursor()

	# execute INSERT command
	cur.execute("""INSERT INTO tb_book (title, author, publisher, published_date, isbn, buying_date) 
		    VALUES (%s, %s, %s, %s, %s, %s)""", (title, author, publisher, published, isbn, buying,))

	# select a new entry from the table
	cur.execute("SELECT * FROM tb_book ORDER BY id DESC LIMIT 1")

	# show the new entry
	result = cur.fetchone()
	print result


if __name__ == "__main__":

	# get inputs from a user
	title = raw_input("What is the title?: ")
	author = raw_input("Who is the author? (the first author): ")
	publisher = raw_input("Who is the publisher?: ")
	published = raw_input("When is the book published? (YYYY-MM-DD): ")
	isbn = raw_input("What is ISBN ?(000-0000000000): ")
	buying = raw_input("When did you buy it? (YYYY-MM-DD): ")

	# make a connection to database
	db = pymysql.connect(host='localhost',
						 user='username',
						 passwd='password',
						 db='books',
						 charset='utf8mb4')

	# add a new entry
	add_book(db, title, author, publisher, published, isbn, buying)

	# commit a change to a database
	db.commit()

	# close the connection
	db.close()
