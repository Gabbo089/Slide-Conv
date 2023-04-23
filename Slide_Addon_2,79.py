import bpy

bl_info = {
    "name": "Slide Calculator",
    "author": "Gabbo",
    "version": (1, 0),
    "blender": (2, 70, 0),
    "description": "Slide Calculator for Whitehole",
    "category": "Convert Path",
    "doc_url": "https://github.com/Gabbo089/Slide",
}


class AddonPanel(bpy.types.Panel):
    bl_label = "Path Calculator"
    bl_idname = "OBJECT_PT_my_addon_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Slide"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.prop(context.scene, "my_selected_curve", icon='CURVE_DATA', text="Bezier")
        column = layout.column()
        column = layout.column()
        column.prop(context.scene, "my_float_vector", text="Slide's Coordinates")
        layout.scale_y = 1.1
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.prop(context.scene, "my_output_file", text="Output")
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.operator("myaddon.print_results")


class AddonPrintResultsOperator(bpy.types.Operator):
    bl_idname = "myaddon.print_results"
    bl_label = "Print Coordinates"

    def execute(self, context):
        curve = context.scene.my_selected_curve
        float_vector = context.scene.my_float_vector
        points = []
        for point in curve.data.splines[0].bezier_points:
            points.append((float_vector[0] + point.co[0], float_vector[1] + point.co[1], float_vector[2] + point.co[2]))
            points.append((float_vector[0] + point.handle_left[0], float_vector[1] +  point.handle_right[1], float_vector[2] + point.handle_right[2]))
            points.append((float_vector[0] + point.handle_right[0], float_vector[1] +  point.handle_right[1], float_vector[2] + point.handle_right[2]))
        filepath = bpy.path.abspath(context.scene.my_output_file)
        with open(filepath, "w") as f:
            for i, point in enumerate(points):
                if i % 3 == 0:
                    f.write("Path {} (Main Path):    (X {:.3f}, Y {:.3f}, Z {:.3f})\n".format(i//3 + 1, point[0], point[1], point[2]))
                elif i % 3 == 1:
                    f.write("Path {} (Controller 1): (X {:.3f}, Y {:.3f}, Z {:.3f})\n".format(i//3 + 1, point[0], point[1], point[2]))
                else:
                    f.write("Path {} (Controller 2): (X {:.3f}, Y {:.3f}, Z {:.3f})\n".format(i//3 + 1, point[0], point[1], point[2]))
        return {'FINISHED'}


class AddonBrowseFileOperator(bpy.types.Operator):
    bl_idname = "myaddon.browse_file"
    bl_label = "Browse for File"
    
    filepath: bpy.props.StringProperty(subtype="DIR_PATH") 

    def execute(self, context):
        context.scene.my_output_file = self.filepath
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def my_curve_filter(scene, pointer):
    return pointer.type == 'CURVE'

def my_pointer_prop_update(self, context):
    if context.scene.my_selected_curve:
        print("Selected curve:", context.scene.my_selected_curve.name)
    else:
        print("No curve selected.")

def register():
    bpy.types.Scene.my_selected_curve = bpy.props.PointerProperty(type=bpy.types.Object, poll=my_curve_filter, update=my_pointer_prop_update)
    bpy.types.Scene.my_float_vector = bpy.props.FloatVectorProperty(name="My Float Vector", subtype="TRANSLATION", size=3, precision=8)
    bpy.types.Scene.my_output_file = bpy.props.StringProperty(name="Output File Path", subtype='FILE_PATH', default="//Coordinates.txt")
    bpy.utils.register_class(AddonPanel)
    bpy.utils.register_class(AddonPrintResultsOperator)
    bpy.utils.register_class(AddonBrowseFileOperator)

def unregister():
    del bpy.types.Scene.my_selected_curve
    del bpy.types.Scene.my_float_vector
    del bpy.types.Scene.my_output_file
    bpy.utils.unregister_class(AddonPanel)
    bpy.utils.unregister_class(AddonPrintResultsOperator)
    bpy.utils.unregister_class(AddonBrowseFileOperator)


if __name__ == "__main__":
    register()