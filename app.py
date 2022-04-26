from flask import Flask

#Flask instance
app = Flask(__name__)

# flask root of routes
@app.route('/')

# practice function
def hello_world():
    return 'Hello World!'

    
