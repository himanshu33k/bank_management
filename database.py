# Database management Bank
import mysql.connector as sql

mydb = sql.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="bank"
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                CREATE TABLE customers (
                username VARCHAR(20),
                password VARCHAR(20),
                name VARCHAR(20),
                age INT,
                city VARCHAR(20),
                balance DECIMAL(10, 2),
                account_number VARCHAR(20),
                balance DECIMAL(10, 2),
                status INT
);
    ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()