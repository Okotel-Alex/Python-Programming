from flask import Flask #Import the Flask Class
app = Flask(__name__) #Create an Instance of the Flask Class

@app.route('/') #Route the function
def main(): #Run the function
  return "Hello World"

app.run(host='0.0.0.0', port=5000, debug=True) #Run the Application (in debug mode)
