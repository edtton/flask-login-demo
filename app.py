from flask import Flask, render_template, request 
import sqlite3

# Flask constructor takes current module name as the parameter 
app = Flask(__name__)

def create_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')

    cursor.execute("INSERT INTO users VALUES (?, ?)", ('johndoe', 'password'))

    connection.commit()
    connection.close() 

def insert_users():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    username = 'gwashington'
    password = 'password'
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))

    connection.commit()
    connection.close()

def remove_users():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    username = "johndoe'--"

    query = f"DELETE FROM users WHERE username = '{username}'"

    cursor.execute(query) 

    connection.commit()
    connection.close() 

# define the URL path that triggers this method 
@app.route("/")
@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        result = cursor.fetchall() 

        connection.commit()
        connection.close() 

        return render_template('results.html', result = result )

    return render_template('login.html')

if __name__ == '__main__':
    # create_database()
    app.run(debug = True)
    # insert_users()
    # remove_users()
