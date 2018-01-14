import bpy

class TF_Set_Cursor2d(bpy.types.Operator):
    bl_label = "Set le Cursor2D"
    bl_idname = "sequencer.tf_set_cursor2d"
    
    @classmethod
    def poll(cls, context):
        if (context.scene.sequence_editor and
            context.space_data.type == 'SEQUENCE_EDITOR' and
            context.region.type == 'PREVIEW' and
            context.scene.seq_pivot_type == '2'):
            return True
        return False
    
    def invoke(self, context, event):
        bpy.ops.sequencer.tf_initialize_pivot()
        
        mouse_x = event.mouse_region_x
        mouse_y = event.mouse_region_y
        
        pos = context.region.view2d.region_to_view(mouse_x, mouse_y)
        
        context.scene.seq_cursor2d_loc = [round(pos[0]),round(pos[1])]
        
        return {'PASS_THROUGH'}
