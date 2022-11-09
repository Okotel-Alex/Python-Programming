from flask import Flask, redirect # Import Flask Class, and redirect
app = Flask(__name__) # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function
    return redirect('https://sushipython.us', 302) # Call upon the redirect with status code 302

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)