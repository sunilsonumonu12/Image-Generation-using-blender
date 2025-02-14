import bpy
import math
import bmesh
from mathutils import Vector

mat2 = bpy.data.materials.new(name="GradientBlueMaterial")
mat2.use_nodes = True
nodes = mat2.node_tree.nodes
links = mat2.node_tree.links

# Clear default nodes
for node in nodes:
    nodes.remove(node)

# Add necessary nodes
output_node = nodes.new(type='ShaderNodeOutputMaterial')
principled_node = nodes.new(type='ShaderNodeBsdfPrincipled')
gradient_node = nodes.new(type='ShaderNodeTexGradient')
color_ramp_node = nodes.new(type='ShaderNodeValToRGB')
mapping_node = nodes.new(type='ShaderNodeMapping')
tex_coord_node = nodes.new(type='ShaderNodeTexCoord')

# Load the image for the Image Texture Node
image_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\simple6.jpeg"
image_texture_node = nodes.new(type='ShaderNodeTexImage')
image_texture_node.image = bpy.data.images.load(image_path)

# Set node locations
output_node.location = (400, 0)
principled_node.location = (200, 0)
gradient_node.location = (-600, 0)
color_ramp_node.location = (-400, 0)
mapping_node.location = (-200, 0)
tex_coord_node.location = (-800, 0)
image_texture_node.location = (-400, -200)  # Position it as desired

# Configure color ramp
color_ramp_node.color_ramp.elements[0].position = 0.0
color_ramp_node.color_ramp.elements[0].color = (1.0, 0.0, 0.0, 1.0)  # Cyan-like color
mid_element_1 = color_ramp_node.color_ramp.elements.new(0.333)
mid_element_1.color = (1.0, 0.549, 0.0, 1.0)  # Teal color
mid_element_2 = color_ramp_node.color_ramp.elements.new(0.666)
mid_element_2.color = (1.0, 0.9, 0.8, 1.0)  # Dark Blue
color_ramp_node.color_ramp.elements[1].position = 1.0
color_ramp_node.color_ramp.elements[1].color = (1.0, 0.0, 0.0, 1.0)  # Red

# Configure the Principled BSDF
principled_node.inputs['Metallic'].default_value = 0.5
principled_node.inputs['Roughness'].default_value = 0.3

# Link nodes
links.new(tex_coord_node.outputs['Generated'], mapping_node.inputs['Vector'])
links.new(mapping_node.outputs['Vector'], gradient_node.inputs['Vector'])
links.new(gradient_node.outputs['Color'], color_ramp_node.inputs['Fac'])
links.new(color_ramp_node.outputs['Color'], principled_node.inputs['Base Color'])
links.new(image_texture_node.outputs['Color'], principled_node.inputs['Base Color'])  # Link image texture to Principled BSDF
links.new(principled_node.outputs['BSDF'], output_node.inputs['Surface'])

# Assign material to the plane
#plane = bpy.context.object  # Assuming you have a plane object selected
#if plane.data.materials:
#    plane.data.materials[0] = mat2
#else:
#    plane.data.materials.append(mat2)

print("Gradient texture applied to the plane.")

# Function to create a plane with specified properties
def create_plane(location, scale_x, scale_y, scale_z, rotation):
    # Create the plane
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=location, rotation=rotation)
    
    # Access the created plane (it will be the last object created)
    plane = bpy.context.active_object
    
    # Scale the plane
    plane.scale = (scale_x, scale_y, scale_z)

# Specify location, scale for x, y, z axes, and rotation for the plane
create_plane(location=(1, 0, 0), scale_x=4, scale_y=3, scale_z=1, rotation=(0, 0, 0))

# Access the existing plane object
plane = bpy.data.objects.get("Plane")
if plane is None:
    print("No object named 'Plane' found.")
else:
    # Create a new material
    mat = bpy.data.materials.new(name="GradientBlueMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    for node in nodes:
        nodes.remove(node)

    # Add necessary nodes
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    principled_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    gradient_node = nodes.new(type='ShaderNodeTexGradient')
    color_ramp_node = nodes.new(type='ShaderNodeValToRGB')
    mapping_node = nodes.new(type='ShaderNodeMapping')
    tex_coord_node = nodes.new(type='ShaderNodeTexCoord')
    image_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\simple5.jpg"
    # Add Image Texture Node
    image_texture_node = nodes.new(type='ShaderNodeTexImage')
    image_texture_node.image = bpy.data.images.load(image_path)  # Load your image here

    # Set node locations
    output_node.location = (400, 0)
    principled_node.location = (200, 0)
    gradient_node.location = (-600, 0)
    color_ramp_node.location = (-400, 0)
    mapping_node.location = (-200, 0)
    tex_coord_node.location = (-800, 0)
    image_texture_node.location = (-400, -200)  # Position it as desired

    # Configure color ramp
    color_ramp_node.color_ramp.elements[0].position = 0.0
    color_ramp_node.color_ramp.elements[0].color = (1.0, 0.0, 0.0, 1.0)  # 00FFD9 (Cyan-like color)
    
    mid_element_1 = color_ramp_node.color_ramp.elements.new(0.333)
    mid_element_1.color = (1.0, 0.549, 0.0, 1.0)   # 34BCCB (Teal color)
    
    mid_element_2 = color_ramp_node.color_ramp.elements.new(0.666)
    mid_element_2.color = (1.0, 0.9, 0.8, 1.0)  # 0D5BBB (Dark Blue)
    
    color_ramp_node.color_ramp.elements[1].position = 1.0
    color_ramp_node.color_ramp.elements[1].color = (1.0, 0.0, 0.0, 1.0) 

    # Configure the Principled BSDF
    principled_node.inputs['Metallic'].default_value = 0.5
    principled_node.inputs['Roughness'].default_value = 0.3

    # Link nodes
    links.new(tex_coord_node.outputs['Generated'], mapping_node.inputs['Vector'])
    links.new(mapping_node.outputs['Vector'], gradient_node.inputs['Vector'])
    links.new(gradient_node.outputs['Color'], color_ramp_node.inputs['Fac'])
    links.new(color_ramp_node.outputs['Color'], principled_node.inputs['Base Color'])
    links.new(image_texture_node.outputs['Color'], principled_node.inputs['Base Color'])  # Link image texture to Principled BSDF
    links.new(principled_node.outputs['BSDF'], output_node.inputs['Surface'])

    # Assign material to the plane
    if plane.data.materials:
        plane.data.materials[0] = mat
    else:
        plane.data.materials.append(mat)

    print("Gradient texture applied to the plane.")

# Create a new material
material = bpy.data.materials.new(name="CustomMaterial")
material.use_nodes = True
nodes = material.node_tree.nodes

# Function to create a camera with specified properties

#"C:\Users\sunil\OneDrive\Desktop\input_text.txt"
# Set the created camera as the active camera
#bpy.context.scene.camera = camera
input_file_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\input_text.txt"
with open(input_file_path, 'r') as file:
    input_text = file.read().strip()
# Create text object
bpy.ops.object.text_add()
text_obj = bpy.context.active_object
text_obj.data.body = input_text
text_obj.name = "StyledText"
text_obj.data.extrude = 0.6
text_obj.data.bevel_depth = 0.03
font_path = "C:/Users/sunil/Downloads/love-days-love-font/LoveDays-2v7Oe.ttf"  # Update the path to your font file
bpy.ops.font.open(filepath=font_path)
text_obj.data.font = bpy.data.fonts[-1]
# Convert text to mesh
bpy.ops.object.convert(target='MESH')

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Select the text object
bpy.context.view_layer.objects.active = text_obj
text_obj = bpy.context.active_object
obj = bpy.context.active_object
# Switch to Edit Mode to unwrap the UVs
bpy.ops.object.mode_set(mode='EDIT')

# Unwrap the cube's UVs
bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)

# Get the mesh and a BMesh object (within Edit Mode)
obj = bpy.context.active_object
me = obj.data
bm = bmesh.from_edit_mesh(me)  # Use from_edit_mesh in Edit Mode

# Get the UV layer
uv_layer = bm.loops.layers.uv.verify()

# Select the faces you want to resize (replace with your selection logic)
selected_faces = [f for f in bm.faces if f.select]

# Define the scaling factor (e.g., double the size)
scale_factor = 5.0

# Scale the UVs of selected faces
for f in selected_faces:
    for l in f.loops:
        l[uv_layer].uv *= scale_factor

# Update the mesh with the modified BMesh (within Edit Mode)
bmesh.update_edit_mesh(me)  # Correct usage: call bmesh's update_edit_mesh with the mesh

# Free the BMesh data (optional, happens automatically when exiting Edit Mode)
bm.free() 

# Switch back to Object Mode (if needed)
bpy.ops.object.mode_set(mode='OBJECT')
# Enter Object mode to access mesh data
bpy.ops.object.mode_set(mode='OBJECT')

# Get the mesh data
mesh = text_obj.data
image_path = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\python_july19\simple2.png"

# Create a new material for the text object
material_z = bpy.data.materials.new(name="Material_Z")
material_z.use_nodes = True

# Clear any existing nodes
nodes = material_z.node_tree.nodes
for node in nodes:
    nodes.remove(node)

# Add the Image Texture node
image_texture_node = nodes.new(type='ShaderNodeTexImage')
image_texture_node.location = (-400, 0)
image_texture_node.image = bpy.data.images.load(image_path)

# Add the Emission shader
emission_node = nodes.new(type='ShaderNodeEmission')
emission_node.location = (0, 0)
emission_node.inputs['Strength'].default_value = 1.5  # Control emission intensity

# Add the Material Output node
output_node = nodes.new(type='ShaderNodeOutputMaterial')
output_node.location = (200, 0)

# Link the nodes
links = material_z.node_tree.links
links.new(image_texture_node.outputs['Color'], emission_node.inputs['Color'])
links.new(emission_node.outputs['Emission'], output_node.inputs['Surface'])
# Function to clean up the material node tree
def clean_material_nodes(material):
    if material.use_nodes:
        nodes = material.node_tree.nodes
        for node in nodes:
            nodes.remove(node)


# Create material for other directions (blue)
material_other = bpy.data.materials.get("Material_Other")
if material_other is None:
    material_other = bpy.data.materials.new(name="Material_Other")
material_other.use_nodes = True
clean_material_nodes(material_other)  # Clear any existing nodes

# Set a simple diffuse shader for material_other (blue)
nodes_other = material_other.node_tree.nodes
output_node_other = nodes_other.new(type='ShaderNodeOutputMaterial')
diffuse_node_other = nodes_other.new(type='ShaderNodeBsdfDiffuse')
diffuse_node_other.inputs['Color'].default_value = (0, 0, 1, 1)  # Blue color
material_other.node_tree.links.new(diffuse_node_other.outputs['BSDF'], output_node_other.inputs['Surface'])
#material_other
# Assign the materials to the mesh
if len(text_obj.data.materials) == 0:
    text_obj.data.materials.append(mat2)
    text_obj.data.materials.append(material_other)
    text_obj.data.materials.append(mat2)
else:
    text_obj.data.materials[0] = mat2
    text_obj.data.materials[1] = material_other
    text_obj.data.materials[2] = mat2

# Function to determine the direction of the face normal
def is_z_direction(normal):
    return abs(normal.z) > abs(normal.x) and abs(normal.z) > abs(normal.y)

# Assign materials based on the face normal direction
for poly in mesh.polygons:
    normal = poly.normal
    if is_z_direction(normal):
        poly.material_index = 2 # Assign Material_Z (yellow)
    else:
        poly.material_index = 1  # Assign Material_Other (blue)

# Return to object mode
#bpy.ops.object.mode_set(mode='OBJECT')

# Return to object mode
bpy.ops.object.mode_set(mode='OBJECT')
text_obj = bpy.context.active_object
#bpy.ops.uv.smart_project(angle_limit=66.0)
bpy.ops.object.mode_set(mode='EDIT')

# Unwrap the cube's UVs

# Switch back to Object Mode
bpy.ops.object.mode_set(mode='OBJECT')

bpy.context.area.ui_type = 'VIEW_3D'
#bpy.context.area.ui_type = 'UV'
## Select all UV vertices
#bpy.ops.uv.select_all(action='SELECT')

## Resize the UV vertices
#bpy.ops.transform.resize(value=(4, 4, 1)) 

## Translate the UV vertices
#bpy.ops.transform.translate(value=(-0.327357, -0.222823, 0))
#bpy.context.area.ui_type = 'VIEW_3D'
## Exit Edit Mode
bpy.ops.object.mode_set(mode='OBJECT')
print("Styled word 'palak' created with materials based on face direction.")
obj = bpy.data.objects.get("StyledText")
if obj is None:
    print("Object 'StyledText' not found in the scene.")
else:
    # Set location and rotation at frame 0
    bpy.context.scene.frame_set(0)
    obj.location.x = 0
    obj.location.y = 0.20759
    obj.location.z = 4.0575
    obj.rotation_euler.x = -14.669 * math.radians(1)  # Convert degrees to radians
    obj.rotation_euler.y = 0 * math.radians(1)        # Convert degrees to radians
    obj.rotation_euler.z = 0 * math.radians(1)        # Convert degrees to radians
    
    # Insert keyframes for location and rotation at frame 0
    obj.keyframe_insert(data_path="location", index=-1)
    obj.keyframe_insert(data_path="rotation_euler", index=-1)

    # Set location and rotation at frame 104
    bpy.context.scene.frame_set(104)
    obj.location.x = 0
    obj.location.y = -0.32082
    obj.location.z = 0.26421
    obj.rotation_euler.x = -5.1113 * math.radians(1)  # Convert degrees to radians
    obj.rotation_euler.y = 0 * math.radians(1)        # Convert degrees to radians
    obj.rotation_euler.z = 0 * math.radians(1)        # Convert degrees to radians
    
    # Insert keyframes for location and rotation at frame 104
    obj.keyframe_insert(data_path="location", index=-1)
    obj.keyframe_insert(data_path="rotation_euler", index=-1)

    print("Keyframes inserted for 'StyledText' at frames 0 and 104.")

bpy.ops.mesh.primitive_uv_sphere_add()
sphere = bpy.context.object

# Rename and scale the UV sphere
sphere.name = "Sphere.001"
sphere.scale = (0.15, 0.15, 0.15)  # Scale to 25% of the original size

# Create a new material for the sphere
material = bpy.data.materials.new(name="Material.002")
material.use_nodes = True

# Clear default nodes
nodes = material.node_tree.nodes
nodes.clear()

# Add nodes
output_node = nodes.new(type='ShaderNodeOutputMaterial')
emission_node = nodes.new(type='ShaderNodeEmission')
image_texture_node = nodes.new(type='ShaderNodeTexImage')

# Set node locations
output_node.location = (400, 0)
emission_node.location = (200, 0)
image_texture_node.location = (0, 0)

# Set emission node properties for a pink color
emission_node.inputs['Strength'].default_value = 5.9
emission_node.inputs['Color'].default_value = (1.0, 0.0, 0.75, 1.0)  # Simple pink color

# Load and set the image texture
image_path = r"C:\Users\sunil\OneDrive\Desktop\simple.jpg"
image = bpy.data.images.load(image_path)
image_texture_node.image = image

# Create links between nodes
links = material.node_tree.links
links.new(emission_node.outputs['Emission'], output_node.inputs['Surface'])
links.new(image_texture_node.outputs['Color'], emission_node.inputs['Color'])

# Assign material to the UV sphere
if sphere.data.materials:
    sphere.data.materials[0] = material
else:
    sphere.data.materials.append(material)

print("UV Sphere added, renamed to 'Sphere.001', scaled to 25%, and material assigned.")

# Create a new cube
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.object
cube.name = "ParticleCube"
cube.location.x = 0.881
cube.scale.x=2
# Create a new particle system
particle_system = cube.modifiers.new(name="ParticleSystem", type='PARTICLE_SYSTEM')
psys = particle_system.particle_system
psys.name = "ParticleSystem"
settings = psys.settings
settings.name = "ParticleSettings.001"
bpy.context.object.show_instancer_for_render = False
# Set the particle system settings
settings.type = 'EMITTER'
settings.count = 900
settings.frame_start = 1.0
settings.frame_end = 200.0
settings.lifetime = 50.0
settings.particle_size = 0.42
settings.size_random = 0.0
settings.physics_type = 'NEWTON'
settings.effector_weights.gravity = 0.0
settings.render_type = 'OBJECT'
settings.instance_object = bpy.data.objects.get("Sphere.001")  # Ensure "Sphere.001" exists
settings.material = 1
settings.use_dynamic_rotation = False
settings.rotation_mode = 'VEL'
settings.angular_velocity_mode = 'VELOCITY'
settings.angular_velocity_factor = 0.0

def create_area_light(name, location, rotation, color, energy, scale_x):
    # Add an area light
    bpy.ops.object.light_add(type='AREA', location=location)
    
    # Get the created light object
    light = bpy.context.object
    light.name = name
    light.data.energy = energy
    light.data.color = color
    light.scale = (scale_x, 1.0, 1.0)  # Set the scale along the X axis
    
    # Set the rotation
    light.rotation_euler = (math.radians(rotation[0]), 
                            math.radians(rotation[1]), 
                            math.radians(rotation[2]))

# Define the properties for the first area light
light1_location = (0.9985, 1.6031, 1.2696)
light1_rotation = (-44.6724, 0.0, 0.0)
light1_color = (1.0, 0.0, 0.9882)  # FF00FC in RGB
light1_energy = 150.0
light1_scale_x = 4.24731

# Define the properties for the second area light
light2_location = (0.9985, -0.967038 , 1.30326)
light2_rotation = (43.3499, 0.0, 0.0)
light2_color = (0.1373, 0.5765, 1.0)  # 2393FF in RGB
light2_energy = 150.0
light2_scale_x = 4.24731

# Create the two area lights with the specified properties
create_area_light("AreaLight1", light1_location, light1_rotation, light1_color, light1_energy, light1_scale_x)
create_area_light("AreaLight2", light2_location, light2_rotation, light2_color, light2_energy, light2_scale_x)


print("Two area lights created with the specified properties.")

# Set render resolution
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720
bpy.context.scene.render.resolution_percentage = 100

# Set output path and file format
bpy.context.scene.render.filepath = 'C:/Users/sunil/OneDrive/Desktop/organise/saiyan 5/rendered_image.png'
bpy.context.scene.render.image_settings.file_format = 'PNG'

# Set frame to render
bpy.context.scene.frame_set(1)
def create_spotlight(name):
    # Create a spotlight
    bpy.ops.object.light_add(type='SPOT')
    spotlight = bpy.context.object
    spotlight.name = name
    
    # Configure spotlight properties
    spotlight.data.energy = 800.0
    spotlight.data.spot_size = 0.4799656271934509
    spotlight.data.spot_blend = 0.15000000596046448
    spotlight.data.use_nodes = True  # Ensure the spotlight uses nodes

    return spotlight

# Function to set spotlight properties and keyframe them
def set_keyframes(spotlight, frame, location, rotation_euler):
    # Set spotlight location and rotation
    spotlight.location = location
    spotlight.rotation_euler = rotation_euler
    
    # Keyframe location and rotation
    spotlight.keyframe_insert(data_path="location", frame=frame)
    spotlight.keyframe_insert(data_path="rotation_euler", frame=frame)

# Create spotlight
spotlight = create_spotlight("Spotlight")

# Set keyframes for the specified frames
keyframes = [
    (73, (0.3464176654815674, 1.099352478981018, 1.5631004571914673), (-0.574514627456665, -1.2066512405740562e-16, 3.564789774589946e-17)),
    (101, (0.3464176654815674, -0.19072383642196655, 1.8704091310501099), (0.11429443955421448, 0.10471975803375244, 1.0177630256852453e-20)),
    (189, (2.407345771789551, -0.19072383642196655, 1.8704091310501099), (0.11429443955421448, -0.3839724361896515, 1.0177630256852453e-20))
]

# Apply keyframes
for frame, loc, rot in keyframes:
    set_keyframes(spotlight, frame, loc, rot)
# Select the object
object_name = "StyledText" # Replace with your object name
obj = bpy.data.objects[object_name]
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Go to Edit Mode
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')

# Unwrap the object
bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)

# Return to Object Mode
bpy.ops.object.mode_set(mode='OBJECT')

# Create a new material with an image texture
new_material = bpy.data.materials.new(name="ImageMaterial")
new_material.use_nodes = True
nodes = new_material.node_tree.nodes
links = new_material.node_tree.links

# Clear default nodes
for node in nodes:
    nodes.remove(node)

# Add necessary nodes
texture_node = nodes.new(type='ShaderNodeTexImage')
bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
output_node = nodes.new(type='ShaderNodeOutputMaterial')

# Load an image and assign it to the texture node
image_path = r"C:\Users\sunil\OneDrive\Desktop\simple.jpg"
  # Replace with the path to your image file
image = bpy.data.images.load(image_path)
texture_node.image = image

# Connect nodes
links.new(texture_node.outputs['Color'], bsdf_node.inputs['Base Color'])
links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])
# Create a new material
material = bpy.data.materials.new(name="CustomMaterial")
material.use_nodes = True
nodes = material.node_tree.nodes
links = material.node_tree.links

# Clear default nodes
for node in nodes:
    nodes.remove(node)

# Create Principled BSDF node
bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
bsdf.location = (400, 300)
bsdf.inputs['Metallic'].default_value = 0.5
bsdf.inputs['Roughness'].default_value = 0.6
bsdf.inputs['IOR'].default_value = 1.5
bsdf.inputs['Alpha'].default_value = 1.0

# Create Material Output node
material_output = nodes.new(type='ShaderNodeOutputMaterial')
material_output.location = (800, 300)

# Link Principled BSDF to Material Output
links.new(bsdf.outputs[0], material_output.inputs[0])

# Create Voronoi Texture node
voronoi_texture = nodes.new(type='ShaderNodeTexVoronoi')
voronoi_texture.location = (-800, 300)
voronoi_texture.feature = 'F1'
voronoi_texture.distance = 'EUCLIDEAN'
voronoi_texture.inputs['Scale'].default_value = 84.6
voronoi_texture.inputs['Randomness'].default_value = 1.0

# Create Color Ramp node
color_ramp = nodes.new(type='ShaderNodeValToRGB')
color_ramp.location = (-400, 300)
color_ramp.color_ramp.interpolation = 'LINEAR'
color_ramp.color_ramp.elements[0].position = 0.0
color_ramp.color_ramp.elements[0].color = (1, 1, 1, 1)
color_ramp.color_ramp.elements[1].position = 0.25
color_ramp.color_ramp.elements[1].color = (0.0, 0.176, 1.0, 1.0)
color_ramp.color_ramp.elements.new(0.5)
color_ramp.color_ramp.elements[2].position = 0.5
color_ramp.color_ramp.elements[2].color = (0.0, 1.0, 1.0, 1.0)
color_ramp.color_ramp.elements.new(0.75)
color_ramp.color_ramp.elements[3].position = 0.75
color_ramp.color_ramp.elements[3].color = (0.0, 0.0, 1.0, 1.0)

# Create Normal Map node
normal_map = nodes.new(type='ShaderNodeNormalMap')
normal_map.location = (0, 300)
normal_map.inputs['Strength'].default_value = 10.0

# Link nodes
links.new(voronoi_texture.outputs['Color'], color_ramp.inputs['Fac'])
links.new(color_ramp.outputs['Color'], bsdf.inputs['Base Color'])
links.new(color_ramp.outputs['Color'], normal_map.inputs['Color'])
links.new(normal_map.outputs['Normal'], bsdf.inputs['Normal'])

def create_area_light(name, location, rotation, color, energy):
    # Add an area light
    bpy.ops.object.light_add(type='AREA', location=location)
    
    # Get the created light object
    light = bpy.context.object
    light.name = name
    light.data.energy = energy
    light.data.color = color
    light.rotation_euler = (math.radians(rotation[0]), 
                            math.radians(rotation[1]), 
                            math.radians(rotation[2]))
    return light

# Define the properties for the first area light
light1_location = (0.9985, 1.6031, 1.2696)
light1_rotation = (-44.6724, -0.0002, 0.0003)  # Rotation angles in degrees
light1_color = (1.0, 1.0, 1.0)  # White color
light1_energy = 500  # Light intensity

# Create the first area light
#create_area_light("AreaLight1", light1_location, light1_rotation, light1_color, light1_energy)

# Define the properties for the second area light
light2_location = (-1.2, -0.8, 1.0)
light2_rotation = (-60.0, 0.0, 0.0)
light2_color = (0.8, 0.8, 1.0)  # Slightly bluish light
light2_energy = 300

# Create the second area light
#create_area_light("AreaLight2", light2_location, light2_rotation, light2_color, light2_energy)
# Assign the new material to the object
if obj.data.materials:
    obj.data.materials[0] = material
# Set the resolution
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720
bpy.context.scene.render.resolution_percentage = 100  # 100% of the set resolution

# Set the render engine to EEVEE
bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'

# Access the EEVEE settings
eevee_settings = bpy.context.scene.eevee

# Set the render samples for EEVEE
eevee_settings.taa_render_samples = 20  # Temporal Anti-Aliasing render samples

# Set the frame to 120
bpy.context.scene.frame_set(120)

# Define the output path and file format
#bpy.context.scene.render.filepath = r"C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\static\imagine.jpg"
imagepath=r'C:\Users\sunil\OneDrive\Desktop\Db2 Challenges\organise\Beuatiful\placement_19july\project1_a\static\images\imagine.jpg'
bpy.context.scene.render.filepath = imagepath
bpy.context.scene.render.image_settings.file_format = 'JPEG'  # You can choose other formats like 'JPEG'
def create_camera(location, scale, rotation):
    # Add a camera
    bpy.ops.object.camera_add(location=location)

    # Get the created camera object
    camera = bpy.context.object

    # Set the scale
    camera.scale = scale

    # Set the rotation (convert degrees to radians for Blender)
    camera.rotation_euler = (math.radians(rotation[0]), 
                             math.radians(rotation[1]), 
                             math.radians(rotation[2]))
    return camera

# Specify the location (x, y, z), scale (x, y, z), and rotation (x, y, z) in degrees
camera_location = (1.022431,0.0986078,5.101191)
camera_scale = (0.424, 0.424, 0.424)
camera_rotation = (0.13,0.4391,0.00096)

# Create the camera with the specified properties
camera = create_camera(camera_location, camera_scale, camera_rotation)
# Render only this frame
bpy.ops.render.render(write_still=True)
