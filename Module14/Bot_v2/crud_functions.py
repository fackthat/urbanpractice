import sqlite3

def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.close()
    return products


# connection = sqlite3.connect('not_telegram.db')
# cursor = connection.cursor()
#
# products_data = [
#     ("Product1", "Описание 1", 100),
#     ("Product2", "Описание 2", 200),
#     ("Product3", "Описание 3", 300),
#     ("Product4", "Описание 4", 400),
# ]
#
# cursor.execute("SELECT COUNT(*) FROM Products")
# if cursor.fetchone()[0] == 0:
#     cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", products_data)
# connection.commit()
# connection.close()
