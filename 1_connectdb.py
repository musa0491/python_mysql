import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="restart" )
cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()