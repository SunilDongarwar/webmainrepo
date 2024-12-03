
### 1. `webapp.py`
# Set the secret key for session management
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your actual secret key



@app.route('/')

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Your email address
app.config['MAIL_PASSWORD'] =  os.getenv('MAIL_PASSWORD')  # Your email password or app password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')  # Default sender

mail = Mail(app)

def index():
 return render_template('index.html')

@app.route('/services')
def services():
 return render_template('services.html')

@app.route('/about')
def about():
 return render_template('about.html')

@app.route('/contact')
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create and send the email
        msg = Message(subject=f'New message from {name}',
                      recipients=['recipient@example.com'])  # Replace with your recipient's email
        msg.body = f'From: {name} <{email}>\n\n{message}'
        mail.send(msg)

        flash('Your message has been sent successfully!', 'success')
        return redirect('/contact')  # Redirect to the contact page after submission

    return render_template('contact.html')

if __name__ == '__main__':
 app.run(debug=True)
