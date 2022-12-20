bl_info = {
    "name": "Polyhedra",
    "author": "Larionov_Alexey, updated to 3.xx by Titus",
    "version": (0, 22),
    "blender": (3, 00, 0),
    "location": "View3D > Add > Mesh > Polyhedra",
    "description": "Generate mesh Archimedean solids and Kepler-Poinsot_solids",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }

import bpy
import sys
import os
from .operators.archimedean_solid import (CreateCuboctahedron,
										  CreateIcosidodecahedron,
										  CreateSnubDodecahedron,
										  CreateRhombicuboctahedron,										  
										  CreateTruncatedCuboctahedron,
										  CreateTruncatedIcosidodecahedron,
										  CreateRhombIcosIdodecahedron,
										  CreateTruncatedIcosahedron,
										  CreateTruncatedCube,
										  CreateTruncatedDodecahedron,
										  CreateTruncatedOctahedron,
										  CreateTruncatedTetrahedron,
										  CreateSnubCubeLeft,
										  CreateSnubCubeRight)
from .operators.kepler_poinsot_solid import (CreateGreatDodecahedron,
											 CreateGreatStellatedDodecahedron,
											 CreateGreatIcosahedron,
											 CreateSmallStellatedDodecahedron)
from .ui.polypanelui import (UI_PT_polyhedra)

classes = (CreateCuboctahedron,
		   CreateIcosidodecahedron,
		   CreateSnubDodecahedron,
		   CreateRhombicuboctahedron,
		   CreateTruncatedCuboctahedron,
		   CreateTruncatedIcosidodecahedron,
		   CreateRhombIcosIdodecahedron,
		   CreateTruncatedIcosahedron,
		   CreateTruncatedCube,
		   CreateTruncatedDodecahedron,
		   CreateTruncatedOctahedron,
		   CreateTruncatedTetrahedron,
		   CreateSnubCubeLeft,
		   CreateSnubCubeRight,
		   CreateGreatDodecahedron,
		   CreateGreatStellatedDodecahedron,
		   CreateGreatIcosahedron,
		   CreateSmallStellatedDodecahedron,
		   UI_PT_polyhedra)

reg_cls, unreg_cls = bpy.utils.register_classes_factory(classes)

def register():
	reg_cls()
	print("Polyhedra Registered!")

def unregister():
	unreg_cls()
	print("Polyhedra Unregistered!")

if __name__ == "__main__":
    register()
