import pypyodbc

server = 'DOM\SQLEXPRESS'
database = 'b_library'
username = 'Administrator'
password = 'Qq123456'

connection = pypyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=' + server + ';'
                            'DATABASE=' + database + ';'
                            'Trusted_connection=yes')

cursor = connection.cursor()

mySQLQuery = ('''
                INSERT INTO dbo.tAuthors (AuthorFirstName, AuthorLastName, Authorage) 
                VALUES ('Максим', 'Горький', '55')
              ''')

mySQLQuery1 = ('''
                SELECT *
                FROM dbo.tAuthors            
              ''')

cursor.execute(mySQLQuery)
connection.commit()
cursor.execute(mySQLQuery1)
results = cursor.fetchall()
print(results)
with open('data_from_MSSQL.txt', 'w', encoding='UTF-8') as f:
    for row in results:
        print('Welcome :' + str(row[0]) + ' Name: ' + str(row[1]) + ' LastName: '
          + str(row[2]) + ' Age: ' + str(row[3]), file=f)

cursor.close()
connection.close()
