Image Generation Using Blender (3D Text Rendering)
Overview
This project generates 3D images of text using Blender 4.2. The script runs Blender in the background, automates the creation of 3D text, and renders the image according to your specifications. It uses Python to call Blender and run the rendering process.

Requirements
Before you begin, ensure that the following software is installed:

Blender 4.2: You can download Blender from here.

Python: Python is required to run the scripts. If you haven't already, download and install Python from here.

You also need to install the os and subprocess libraries, which are built into Python, so no extra installation is required for them.
Setup Instructions
Install Blender:

Install Blender 4.2 (or the required version) from the official website.
Make sure that Blender is added to your system PATH. This step is crucial to run Blender via the command line from your Python scripts.
Clone the Project:

Clone the GitHub repository to your local machine using the following command:

bash
Copy
git clone https://github.com/sunilsonumonu12/Image-Generation-using-blender.git
Replace your-username and your-repository with your actual GitHub username and repository name.

Modify the Script Paths:

Open the Python script files (e.g., oct12.py, july31ww5.py, etc.).

Change the hardcoded paths in the script files to point to the correct locations on your system.

Blender executable path (blender_executable).
Blender file path (blend_file_path).
Image file path (image_path).
For example, change this line:

python
Copy
blender_executable = 'C:/Program Files/Blender Foundation/Blender 4.2/blender.exe'
To the correct path of your Blender installation. Similarly, update the paths for the Python scripts and image files.

Example for image path:

python
Copy
image_path = r"C:/path/to/your/image.jpg"
Running the Scripts:

To generate the 3D text image, simply run the Python script corresponding to the task. For example:

bash
Copy
python oct12.py
This will run the script, call Blender in the background, and render the 3D image.
Each script works independently, so you can execute them separately as needed.
