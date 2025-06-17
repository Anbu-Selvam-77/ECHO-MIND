from flask import Flask, render_template

app = Flask(__name__)

# Route for the signup page
@app.route('/')
def signup():
    return render_template('index.html')

# Route for the chatbot page
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/signin.html')
def signin():
    return render_template('signin.html')

# Corrected main entry point
if __name__ == '__main__':
    app.run(debug=True)