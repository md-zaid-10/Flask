from flask import Flask

'''
It creates an instance of flask class, which will be your WSGI (web server gateway interface) application.
'''

# Initialize flask WSGI app
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this App. This is an amazing Framework"

@app.route("/index")
def index():
    return "Welcome to the index page"

# this is an entry point for your application
if __name__=="__main__":
    app.run(debug=True)