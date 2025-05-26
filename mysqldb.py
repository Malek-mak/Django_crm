import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    user = 'malek',
    password = 'Mak123mak@',
)

cursore = database.cursor()
cursore.execute('CREATE DATABASE crmdb')

print('all done')