import subprocess
import os
#"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\july31ww.py"
#"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\july20d.blend"
# Path to the Blender executable
blender_executable = 'C:/Program Files/Blender Foundation/Blender 4.2/blender.exe'  # Adjust if Blender is not in your PATH
python_script_path = 'C:/Users/sunil/OneDrive/Desktop/Db2 Challenges/organise/Beuatiful//placement_19july/python_july19/oct12.py'
# Path to the Blender file you want to open
#"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\july20d.blend"
blend_file_path = 'C:/Users/sunil/OneDrive/Desktop/Db2 Challenges/organise/Beuatiful/placement_19july/python_july19/july20d.blend'  # Change this to your .blend file path

# Command to open the Blender file
command = [blender_executable, blend_file_path, '--python', python_script_path]

# Run the command
subprocess.run(command)