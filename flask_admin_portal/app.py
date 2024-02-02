from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.secret_key = b'7c1d3ee755de95c54d9f345d0f630209'

# Define default admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')

def is_logged_in():
    return 'username' in session

@app.route('/')
def index():
    if is_logged_in():
        return render_template('index.html', username=session['username'])
    return render_template('login.html', form=LoginForm())

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        username = form.username.data
        password = form.password.data

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['username'] = username
            return redirect(url_for('index'))

    return render_template('login.html', form=form, error='Invalid credentials')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/users')
def list_users():
    if not is_logged_in():
        return redirect(url_for('index'))

    try:
        # Fetch users from JsonPlaceHolder API
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        users = response.json()
        return render_template('users.html', users=users, username=session['username'])
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e), username=session['username'])

@app.route('/create_user', methods=['POST'])
def create_user():
    if not is_logged_in():
        return redirect(url_for('index'))

    try:
        # Logic to create a new user using data from the request
        data = request.form
        response = requests.post('https://jsonplaceholder.typicode.com/users', data=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        new_user = response.json()
        message = 'User created successfully'
        return jsonify({'message': message, 'user': new_user})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})


# Number of photos to display per page
PHOTOS_PER_PAGE = 9

@app.route('/photos')
def list_photos():
    if not is_logged_in():
        return redirect(url_for('index'))

    try:
        # Fetch photos from JsonPlaceHolder API
        response = requests.get('https://jsonplaceholder.typicode.com/photos')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        photos = response.json()

        # Pagination logic
        page = request.args.get('page', 1, type=int)
        start_index = (page - 1) * PHOTOS_PER_PAGE
        end_index = start_index + PHOTOS_PER_PAGE
        paginated_photos = photos[start_index:end_index]

        # Calculate total pages
        total_pages = (len(photos) + PHOTOS_PER_PAGE - 1) // PHOTOS_PER_PAGE

        return render_template('photos.html', photos=paginated_photos, page=page, total_pages=total_pages, username=session['username'])
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e), username=session['username'])


if __name__ == '__main__':
    app.run(debug=True)
