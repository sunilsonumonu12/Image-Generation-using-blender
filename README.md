# **Image Generation Using Blender (3D Text Rendering)**  

## **Overview**  
This project automates the generation of **3D text images** using *Blender 4.2*. The script runs Blender in the background, creates **3D text**, and renders the image according to specified settings using **Python**.

---

## **Requirements**  
Before you begin, ensure that the following software is installed:

- **Blender 4.2** – Download it from [Blender's official website](https://www.blender.org/download/).
- **Python** – Required to run the scripts. Download and install it from [Python's official website](https://www.python.org/downloads/).
- **Built-in Libraries:**  
  - `os`
  - `subprocess`  
  *(These are included with Python, so no extra installation is needed.)*

---

## **Setup Instructions**  

### **1. Install Blender**  
- Install **Blender 4.2** (or the required version) from the official website.  
- Ensure that **Blender is added to your system PATH**.  
  *(This step is crucial to run Blender via the command line from your Python scripts.)*

### **2. Clone the Project**  
Clone the GitHub repository to your local machine using the following command:  
## **3. Modify the Script Paths**  
Open the Python script files (e.g., `oct12.py`, `july31ww5.py`, etc.) and update the hardcoded paths to match your system.

### **Paths to Update**  
- **Blender Executable Path** (`blender_executable`)  
- **Blender File Path** (`blend_file_path`)  
- **Image Save Path** (`image_path`)  

---

### **Example: Updating Blender Executable Path**  
Change this line in your script:

```python
blender_executable = 'C:/Program Files/Blender Foundation/Blender 4.2/blender.exe'

```bash


git clone https://github.com/sunilsonumonu12/Image-Generation-using-blender.git

