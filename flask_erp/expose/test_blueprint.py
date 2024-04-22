from flask import Blueprint, jsonify
from markupsafe import escape
from dependency_injector.wiring import inject, Provide
from flask_erp.cbv import cbv
from flask_erp.di.di import DI
from flask_erp.model.Todo import Todo
from flask_erp.service.todo_service import TodoService

blueprint = Blueprint('todo_routes', __name__, url_prefix="/api/todo")

class TodoController:

    @blueprint.route('/path/<path:subpath>')
    def show_subpath(subpath):
        # show the subpath after /path/
        return f'Subpath {escape(subpath)}'

    @blueprint.route("/")
    def index():
        """
        This is the landing page for the University of Stack Portal
        """
        return render_template('index.html', name=index)


    @blueprint.route("/signup")
    def signup():
        """
        This is the signup page for the University of Stack Portal. Here students can register and create a student account
        """    
        return render_template('signup.html', name=signup)


    @blueprint.route("/login")
    def login():
        """
        This is the login page for the University of Stack Portal. Here students can login once they have successfully register their account
        """
        return render_template('login.html', name=login)


    @blueprint.route("/validate", methods=["POST"])
    def validate():
        """
        This is the backend service which registers a new student and creates an account for them.
        """
        if request.method == 'POST':
            uname = request.form['uname']
            newpass = request.form['newpass']
            if uname in users.keys():
                print("User exists")
                value = users[uname]['pass']
                if newpass == value:
                    print("Password matches")
                    firstname = users[uname]['firstname']
                    lastname = users[uname]['lastname']
                    age = users[uname]['age']
                    course = users[uname]['course']
                    #return "Login Succeded"
                    return render_template('student.html', firstname=firstname, lastname=lastname, age=age, course=course)
                else:
                    return "Login Unsuccessfull"    


    @blueprint.route("/student/setdata", methods=["POST"])
    def setdata():
        """
        This is the backend service which captures the new student's data.
        """
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            age = request.form['age']
            course = request.form['course']
            users[firstname]['firstname'] = firstname
            users[firstname]['lastname'] = lastname
            users[firstname]['age'] = age
            users[firstname]['course'] = course
            print(firstname, lastname, age, course)
            print(users)
            #return "%s, %s, %s, %s" % (firstname, lastname, str(age), course)
            return render_template('student.html', firstname=firstname, lastname=lastname, age=age, course=course)


    @blueprint.route("/student/getdata")
    def getdata():
        """
        This is the backend service which can be used to retrieve the student's data.
        """
        return "Get Student Data"


    @blueprint.route("/saveuser", methods=["POST"])
    def saveuser():
        """
        This is the backend service which stores the new student's data in a dictionary database.
        """
        if request.method == 'POST':
            user = request.form['uname']
            newpass = request.form['newpass']
            repeatpass = request.form['repeatpass']

            print(user)
            print(newpass)
            print(repeatpass)
            if newpass == repeatpass:
                users[user] = {}
                users[user]['pass'] = newpass
                print(users)
                return render_template('setdata.html', user=user)
                #return setdata(user)
            else:
                return "User profile creation failed"