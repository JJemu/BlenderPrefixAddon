bl_info = {
    "name": "Prefix Adder",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Tool",
    "description": "Adds a prefix to the names of selected objects",
    "category": "Object",
}

import bpy

class OBJECT_OT_add_prefix(bpy.types.Operator):
    """Add a prefix to selected objects"""
    bl_idname = "object.add_prefix"
    bl_label = "Add Prefix"
    bl_options = {'REGISTER', 'UNDO'}

    # This property will be displayed as a text box in the dialog
    prefix: bpy.props.StringProperty(
        name="Prefix",
        description="Prefix to add to object names",
        default="PREFIX_"
    )

    def execute(self, context):
        for obj in context.selected_objects:
            # Only add the prefix if it's not already there
            if not obj.name.startswith(self.prefix):
                obj.name = self.prefix + obj.name
        return {'FINISHED'}

    # The invoke method displays a pop-up dialog with the text box
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    # The draw method defines the layout of the pop-up dialog
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "prefix")

class VIEW3D_PT_prefix_adder(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport Sidebar"""
    bl_label = "Prefix Adder"
    bl_idname = "VIEW3D_PT_prefix_adder"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Add prefix to object names:")
        layout.operator("object.add_prefix")

def register():
    bpy.utils.register_class(OBJECT_OT_add_prefix)
    bpy.utils.register_class(VIEW3D_PT_prefix_adder)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_prefix_adder)
    bpy.utils.unregister_class(OBJECT_OT_add_prefix)

if __name__ == "__main__":
    register()
