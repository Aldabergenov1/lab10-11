import psycopg2, csv
from config import host, user, password,db_name

connection = psycopg2.connect(
    host = host,
    database = db_name,
    user = user,
    password = password
)
connection.autocommit = True
cursor = connection.cursor()
arr = []
sql = '''
    INSERT INTO phonebook1
    VALUES(%s,%s,%s,%s);    
      '''
try:
    with open(r'C:\Users\Махарон\Desktop\ee\a.csv') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            row[0] = int(row[0])
            arr.append(row)
    for row in arr:
        cursor.execute(sql, row)

    pass
except:
    sql = '''
    INSERT INTO phonebook1
    VALUES(%s,%s,%s,%s);    
      '''
    id = int(input('ID: '))
    username = input('Username: ')
    number = input('Phone number: ')
    email = input('E-mail: ')
    cursor.execute(sql,(id,username,number,email))

cursor.close()
connection.close()
