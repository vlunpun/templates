from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)                                                       # this gets the name of the file so Flask knows it's name
proxied = FlaskBehindProxy(app)  
app.config['SECRET_KEY'] = '131a00f696ccda7414d2354a43800ba8'

# Disable redirect interception
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# Enable debug mode
app.debug = True

# Set up the Flask-DebugToolbar
toolbar = DebugToolbarExtension(app)

@app.route("/register", methods=['GET', 'POST'])                            # this tells you the URL the method below is related to
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)    # this prints HTML to the webpage

@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')
    
@app.route("/about")
def second_page():
    return render_template('about.html', subtitle='About us', text='This is the about page')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")