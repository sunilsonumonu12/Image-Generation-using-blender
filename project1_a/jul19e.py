from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Route to display the form
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle the form submission
@app.route("/process", methods=["POST"])
def process_input():
    user_input = request.form['user_input']
    
    # Process the input - for example, you could call a Python script
    # subprocess.run(['python', 'your_script.py', user_input])  # Optional for running an external Python script
    
    # Here, we just process the input inside this function for demonstration
    processed_output = user_input.upper()  # Sample processing (convert to uppercase)

    return f"<h1>Processed Output: {processed_output}</h1>"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
