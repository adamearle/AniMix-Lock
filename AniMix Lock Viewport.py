bl_info = {
    "name": "AniMix Lock Viewport Rotation",
    "author": "Adam Earle",
    "version": (2, 5),
    "blender": (2, 91, 0),
    "location": "3D Viewport Header",
    "description": "Adds a button with functionality to toggle viewport lock in the 3D viewport header",
    "category": "3D View"
}

import bpy

class CustomOperator(bpy.types.Operator):
    bl_idname = "object.custom_operator"
    bl_label = "Custom Operator"

    def execute(self, context):
        context.space_data.region_3d.lock_rotation = not context.space_data.region_3d.lock_rotation
        return {'FINISHED'}

def draw_custom_button(self, context):
    layout = self.layout
    lock_status = context.space_data.region_3d.lock_rotation
    layout.operator("object.custom_operator", text="", icon=get_lock_icon(context), depress=lock_status)

def get_lock_icon(context):
    if context.space_data.region_3d.lock_rotation:
        return "LOCKED"
    else:
        return "UNLOCKED"

def register():
    bpy.utils.register_class(CustomOperator)
    bpy.types.VIEW3D_HT_header.append(draw_custom_button)

def unregister():
    bpy.utils.unregister_class(CustomOperator)
    bpy.types.VIEW3D_HT_header.remove(draw_custom_button)

if __name__ == "__main__":
    register()
