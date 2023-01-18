import csv
import pymysql

# Connect to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    db='database'
)

# Create the 'quotes' table
with connection.cursor() as cursor:
    cursor.execute('''
        CREATE TABLE quotes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            quote VARCHAR(255) NOT NULL,
            source VARCHAR(255) NOT NULL,
            dob_dod VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL
        )
    ''')

# Open the CSV file and read the data
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Insert the data into the 'quotes' table
with connection.cursor() as cursor:
    for i, row in enumerate(data[1:]):
        cursor.execute(f'''
            INSERT INTO quotes (quote, source, dob_dod, category)
            VALUES ("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}")
        ''')

# Close the connection to the database
connection.close()