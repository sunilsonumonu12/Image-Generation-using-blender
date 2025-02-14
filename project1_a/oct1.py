from flask import Flask, request, render_template, send_file
import subprocess
import os

app = Flask(__name__)

# Ensure the output directories exist
output_directory = "output"
image_directory = "static/images"  # Directory where images are stored

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML template with buttons

@app.route('/show-image', methods=['POST'])
@app.route('/show-image', methods=['POST'])
def show_image():
    # Correct the path to your image location
    image_path = 'static/images/imagine.jpg'  # Make sure this file exists
    return send_file(image_path, mimetype='images/jpeg')  # Correct MIME type

@app.route('/handle-buttons', methods=['POST'])
def handle_buttons():
    action = request.form['action']  # Get which button was clicked

    try:
        if action == 'run_script1':
            subprocess.run(['python', 'script1.py'], check=True)
            return "Script 1 executed successfully!"
        
        elif action == 'run_script2':
            subprocess.run(['python', 'script2.py'], check=True)
            return "Script 2 executed successfully!"
        
        elif action == 'run_script3':
            subprocess.run(['python', 'script3.py'], check=True)
            return "Script 3 executed successfully!"
        
        elif action == 'run_script4':
            subprocess.run(['python', 'script4.py'], check=True)
            return "Script 4 executed successfully!"
        
        elif action == 'run_script5':
            subprocess.run(['python', 'script5.py'], check=True)
            return "Script 5 executed successfully!"

    except subprocess.CalledProcessError as e:
        return f"Error occurred: {e}"

@app.route('/save-text', methods=['POST'])
def save_text():
    input_text = request.form['input_text']

    # Save the text to input_text.txt
    with open('input_text.txt', 'w') as file:
        file.write(input_text)

    return f'Text "{input_text}" has been saved successfully!'

if __name__ == "__main__":
    app.run(debug=True)
