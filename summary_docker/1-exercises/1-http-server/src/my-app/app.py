# Import necessary modules from Flask
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm  # FlaskForm class for handling forms
from wtforms import StringField, SubmitField  # Import form fields
from wtforms.validators import DataRequired  # Validator for input fields

# Import pymongo for MongoDB interaction
from pymongo import MongoClient

# Initialize the Flask application
app = Flask(__name__)
# Configure a secret key for security purposes (CSRF protection)
app.config["SECRET_KEY"] = "wow-such-secret-much-security"

# MongoDB connection setup
client = MongoClient(
    "mongodb://root:root@mongo-db/?retryWrites=true&w=majority"
)
db = client["1_demo_flask_mongodb"]  # Replace with your database name
collection = db["onlyname"]  # Replace with your collection name


# Define a form class using FlaskForm
class MyForm(FlaskForm):
    # Define a text field with label 'Name' and a DataRequired validator
    name = StringField("Name", validators=[DataRequired()])
    # Define a submit button
    submit = SubmitField("Submit")


# Define the route for the root URL
@app.route("/", methods=["GET", "POST"])
def index():
    # Create an instance of MyForm
    form = MyForm()

    # Check if the form is submitted correctly
    if form.validate_on_submit():
        # Display the submitted data into the form and terminal
        name = form.name.data
        print("Name:", name)

        # Save the name to MongoDB
        collection.insert_one({"name": name})

        # Redirect to the index page after submission
        return redirect(url_for("index"))

    # Render the form template if GET request or form validation fails
    return render_template("form.html", form=form)


# Check if the script is executed directly (not imported)
if __name__ == "__main__":
    # Run the Flask app in debug mode for development
    app.run(debug=True, host="0.0.0.0")
