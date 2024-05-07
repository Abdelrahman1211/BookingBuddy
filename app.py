import os
from flask import Flask, render_template, jsonify, json, request, flash,redirect,url_for
from flask_mail import Mail, Message
from postdata import reviews, posts


app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/home.html')
def home():
    return render_template('home.html', reviews=reviews)

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/flight')
@app.route('/flight.html')
def flight():
    return render_template('flight.html')

@app.route('/contact', methods = ['GET', 'POST'])
@app.route('/contact.html', methods= ['GET', 'POST'])
def contact():
    return render_template('contact.html')

# Email Functionality
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your SMTP server address
app.config['MAIL_PORT'] = 465  # Replace with the appropriate port number
app.config['MAIL_USE_TLS'] = False  # Enable TLS encryption, set to False if using SSL
app.config['MAIL_USE_SSL'] = True 
app.config['MAIL_USERNAME'] = 'YOUR_EMAIL'  # Replace with your email address
app.config['MAIL_PASSWORD'] = 'YOUR_PASSWORD'  # Replace with your email password


mail = Mail(app)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == "POST":
        email = request.form['email']
        message = request.form['message']
        name = request.form['name']

        msg = Message('New Contact Form Submission',
                      sender=email,
                      recipients=['YOUR_EMAIL'])

        msg.body = f"Name: {name}\nEmail: {email}\n\n{message}"

        mail.send(msg)

        success = "Message sent successfully."

        flash(success)
        return redirect(url_for('contact'))
    

@app.route('/booked_flight', methods=['POST'])
def booked_flight():
    if request.method == 'POST':
        # Retrieve the form data
        origin = request.form['origin']
        destination = request.form['destination']
        departure_date = request.form['departuredate']
        return_date = request.form['returndate']
        email = request.form['email']
        passengername = request.form['passengername']
        preferredclass = request.form['preferredclass']
        airline = request.form['airline']

        # Create and send the email
        msg = Message('Flight Booking Confirmation',
                      sender='su1tancoding03@gmail.com',
                      recipients=[email])

        msg.body = f"Thank you for booking a flight with us!\n\n" \
           f"Flight details:\n" \
           f"Origin: {origin}\n" \
           f"Destination: {destination}\n" \
           f"Airline: {airline}\n" \
           f"Departure Date: {departure_date}\n" \
           f"Return Date: {return_date}\n" \
           f"Passenger Name: {passengername}\n" \
           f"Preferred Class: {preferredclass}"
                   

        mail.send(msg)

        # Flash a success message and redirect
        flash("Flight booked successfully!")
        return redirect(url_for('flight'))

    return render_template('flight.html')

@app.route("/users")
@app.route("/recqres-data.html")
def users():
    return render_template('recqres-data.html')

@app.route('/mobiles')
def mobiles():
    return render_template('mobiles.html')

@app.route('/get_mobiles')
def get_mobiles():
    # Construct the file path to the JavaScript file in the js folder
    file_path = os.path.join(os.path.dirname(__file__), 'js', 'mobile-data.js')
    
    try:
        # Read the content of the JavaScript file
        with open(file_path) as file:
            javascript_content = file.read()
        return javascript_content, 200, {'Content-Type': 'application/javascript'}
    except FileNotFoundError:
        return jsonify({'error': 'JavaScript file not found'}), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/post/<int:post_id>")
def single_post(post_id):
    post = posts[post_id - 1]  # Retrieve the post from the 'posts' list based on the URL
    return render_template('single-post.html', post=post)

@app.route("/post")
def all_post():
    return render_template('post-all.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
