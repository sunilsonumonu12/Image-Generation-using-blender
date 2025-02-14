import bpy
import bmesh

# Create a new cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
cube = bpy.context.object

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
