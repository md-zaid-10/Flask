## integrate html files in web framework



from flask import Flask, render_template, request

'''
It creates an instance of flask class, which will be your WSGI (web server gateway interface) application.
'''

# Initialize flask WSGI app
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')


# this is an entry point for your application
if __name__=="__main__":
    app.run(debug=True)