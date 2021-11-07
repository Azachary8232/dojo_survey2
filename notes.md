## \_\_init__
```py

from flask import Flask
app = Flask(__name__)
app.secret_key = "skittles"

```

## Server
```py
from flask import Flask
app = Flask(__name__)
app.secret_key = "skittles"
```
## Config
```py
import pymysql.cursors
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', # change the user and password as needed
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        self.connection = connection
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # if the query is an insert, return the id of the last row, since that is the row we just added
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # if the query is a select, return everything that is fetched from the database
                    # the result will be a list of dictionaries
                    result = cursor.fetchall()
                    return result
                else:
                    # if the query is not an insert or a select, such as an update or delete, commit the changes
                    # return nothing
                    self.connection.commit()
            except Exception as e:
                # in case the query fails
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# this connectToMySQL function creates an instance of MySQLConnection, which will be used by server.py
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

```
## Models
```py
# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 


class (User)/no():
    def __init__(self,data):
        self.id = data['id']

# C ****************************************
# C ****************************************
# C ****************************************

    @classmethod
    def create(cls,data):
        query = "INSERT INTO (users/no()) (*something*, *something*) VALUES (%(*something*)s, %(*something*)s;"
        (user/no())_id = connectToMySQL('(userS/no())').query_db(query,data)
        return (user/no())_id

# R ****************************************
# R ****************************************
# R ****************************************

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM (users)/no());"
        (userS/no()) = connectToMySQL('*userS*').query_db(query)
        (userS/no()) = []
        for user in (userS/no()):
            (userS/no()).append(cls(user))
        return (userS/no()) 

	# (joining two groups)  
    # add... from .model_(user/no()) import (User/no()) **to top of page 
	# add... self.(users/no()) = [] **to class(User/no()):
    @classmethod
    def get_one_with_ninjas(cls, data ):
        print(data)
        query = "SELECT * FROM (userS/no()) LEFT JOIN ninjas on (userS/no()).id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('***userS***').query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            # users = [] in self dictionary
            dojo.(userS/no()).append( ***User***(n) )
        return dojo

# U ****************************************
# U ****************************************
# U ****************************************

# D ****************************************
# D ****************************************
# D ****************************************

```
## Controllers
```py
# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.(user/no()) import (User/no())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    data = {
        # 'id' : id
        "(something/no())" : requestform['(somethong/no())']
    }
    Sample.create(data)
    return redirect('/sample')

# Left Join --- Works with models 'get_one_with_....'
@app.route('/sample/<int:id>')
def sample(id):
    data = {
    "id": id
    }
    return render_template('dojo_info.html', dojo=Dojo.get_one_with_ninjas(data))   
```

## Bootstrap CSS
```py
# Name Input

<div class="input-group mb-3">
    <span class="input-group-text" id="inputGroup-sizing-default">First Name</span>
    <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" name="first_name">
</div>  

# Button
 
	Blue-*** <button type="button" class="btn btn-primary">Primary</button>
```
## Validation
```py
@staticmethod
def vaildate_user(user):
    is_valid = True # we assume this is true
    if len(user['first_name]) < 0: 
        flash("first_name must be included.")
        is_valid = False  #-- use different if statement for all inputs
        
    return is_valid    