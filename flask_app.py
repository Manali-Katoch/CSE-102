from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dummy user data
USER_DATA = {
    'username': 'Admin',
    'password': 'Admin'
}

@app.route('/')
def index():
    return render_template('lab2.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USER_DATA['username'] and password == USER_DATA['password']:
        return render_template('data.html', username=username)
    else:
        return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
