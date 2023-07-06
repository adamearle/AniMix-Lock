# Define information about the add-on
bl_info = {
    "name": "AniMix Header Button", # The name of the add-on
    "author": "Adam Earle", # The author of the add-on
    "version": (2, 5), # The version of the add-on
    "blender": (2, 91, 0), # The Blender version required by the add-on
    "location": "3D Viewport Header" # The location where the add-on is accessible
    "description": "Adds a button with functionality to toggle viewport lock in the 3D viewport header",  # The description of the add-on
    "category": "3D View" # The category of the add-on
}

import bpy

# Define a custom operator class
class CustomOperator(bpy.types.Operator):
    bl_idname = "object.custom_operator" # The unique ID of the operator
    bl_label = "Custom Operator" # The label displayed for the operator

    def execute(self, context):
        # Toggle viewport lock
        context.space_data.region_3d.lock_rotation = not context.space_data.region_3d.lock_rotation
        return {'FINISHED'}

# Define a custom draw function for the 3D viewport header
def draw_custom_button(self, context):
    layout = self.layout
    layout.operator("object.custom_operator", text="", icon=get_lock_icon(context))

# Function to determine the lock icon based on the viewport lock status
def get_lock_icon(context):
    if context.space_data.region_3d.lock_rotation:
        return "LOCKED" # Return the "LOCKED" icon if viewport is locked
    else:
        return "UNLOCKED" # Return the "UNLOCKED" icon if viewport is unlocked

# Register the operator and draw function
def register():
    bpy.utils.register_class(CustomOperator) # Register the custom operator
    bpy.types.VIEW3D_HT_header.append(draw_custom_button) # Append the custom draw function to the 3D viewport header

def unregister():
    bpy.utils.unregister_class(CustomOperator) # Unregister the custom operator
    bpy.types.VIEW3D_HT_header.remove(draw_custom_button) # Remove the custom draw function from the 3D viewport header

if __name__ == "__main__":
    register() # Call the register() function to initialize the add-on
