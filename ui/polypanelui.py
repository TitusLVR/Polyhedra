import bpy
from bpy.types import Panel
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector



class UI_PT_polyhedra(Panel):
    """Generate Archimedean Polyhedrons"""
    bl_label = "Polyhedra"
    bl_idname = "UI_PT_polyhedra"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    
    #-----------------------
    # Draw UI
    #-----------------------
    def draw(self,context):
        layout = self.layout
        box = layout.box()
        box.label(text="Archimedean solid", icon='GROUP')
        row = box.row()
        row.operator("mesh.add_cuboctahedron")
        row.operator("mesh.add_icosidodecahedron")
        row = box.row()
        row.operator("mesh.add_snubdodecahedron")
        row.operator("mesh.add_rhombicuboctahedron")
        row = box.row()
        row.operator("mesh.add_truncated_cuboctahedron")
        row.operator("mesh.add_truncated_icosidodecahedron")
        row = box.row()
        row.operator("mesh.add_rhombicosidodecahedron")
        box.label(text="Truncated Platonic solids")
        row = box.row()
        row.operator("mesh.add_truncated_icosahedron")
        row.operator("mesh.add_truncated_cube")
        row = box.row()
        row.operator("mesh.add_truncated_dodecahedron")
        row.operator("mesh.add_truncated_octahedron")
        row = box.row()
        row.operator("mesh.add_truncated_tetrahedron")
        box.label(text="Snub cube")
        row = box.row()
        row.operator("mesh.add_snub_cube_left")
        row.operator("mesh.add_snub_cube_right")
        row = box.row()
        ###########
        box = layout.box()
        box.label(text="Kepler-Poinsot polyhedron", icon='GROUP')
        row = box.row()
        row.operator("mesh.add_great_dodecahedron")
        row.operator("mesh.add_great_stellated_dodecahedron")
        row = box.row()
        row.operator("mesh.add_great_icosahedron")
        row.operator("mesh.add_small_stellated_dodecahedron")
        row = box.row()
