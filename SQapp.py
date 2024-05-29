import sqlite3



conn = sqlite3.connect('book_db.sqlite')
cursor = conn.cursor()



############################## 1 ##################################
# cursor.execute("SELECT * FROM books")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 2 ##################################
# cursor.execute("SELECT * FROM books WHERE author='William Shakespeare' ")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 3 ##################################
# cursor.execute("SELECT * FROM books WHERE author='William Shakespeare' or author='Rowling' ")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 4 ##################################
# cursor.execute("SELECT * FROM books WHERE price<=20")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 5 ##################################
# cursor.execute("SELECT DISTINCT author FROM books")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 6 ##################################
# cursor.execute("SELECT * FROM users WHERE balance>100")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 7 ##################################
# cursor.execute("SELECT * FROM purchase WHERE purchase_date<'2018-01-01'")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 8 ##################################
# cursor.execute("SELECT * FROM purchase WHERE purchase_date BETWEEN '2018-01-01' AND '2018-12-31'")
# records = cursor.fetchall()
# for record in records:
#     print(record)



############################## 9 ##################################
# cursor.execute("SELECT DISTINCT user_id FROM purchase")
# records = cursor.fetchall()
# user_ids = [record[0] for record in records]
# user_names = []
# if user_ids:
#     user_query = "SELECT username FROM users WHERE id IN ({seq})".format(
#         seq=','.join(['?']*len(user_ids))
#     )
#     cursor.execute(user_query, user_ids)
#     user_names = cursor.fetchall()
# for name in user_names:
#     print(name[0])



############################## 10 ##################################
# cursor.execute("SELECT DISTINCT book_id FROM purchase")
# records = cursor.fetchall()
# book_ids = [record[0] for record in records]
# user_names = []
# book_titles = []
# if book_ids:
#     book_query = "SELECT title FROM books WHERE id IN ({seq})".format(
#         seq=','.join(['?']*len(book_ids))
#     )
#     cursor.execute(book_query, book_ids)
#     book_titles = cursor.fetchall()
# for title in book_titles:
#     print(title[0])


conn.close()