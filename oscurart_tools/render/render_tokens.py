# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

import bpy
import os
from bpy.app.handlers import persistent


@persistent
def replaceTokens(dummy):
    global renpath
    # global nodeDict
    tokens = {
        "<scene>": bpy.context.scene.name,
        "<file>": os.path.basename(bpy.data.filepath).split(".")[0],
        "<viewlayer>": bpy.context.view_layer.name,
        "<camera>": (
            "NoCamera"
            if bpy.context.scene.camera == None
            else bpy.context.scene.camera.name
        ),
        "<version>": os.path.basename(bpy.data.filepath).split(".")[0][-4:],
    }

    print(bpy.context.view_layer.objects.active.name)

    renpath = bpy.context.scene.render.filepath

    # nodeDict = []
    # # compositor nodes
    # if bpy.context.scene.use_nodes:
    #     for node in bpy.context.scene.node_tree.nodes:
    #         if node.type == "OUTPUT_FILE":
    #             nodeDict.append([node, node.base_path])
    #             node.base_path = (
    #                 node.base_path.replace("<scene>", tokens["<scene>"])
    #                 .replace("<file>", tokens["<file>"])
    #                 .replace("<viewlayer>", tokens["<viewlayer>"])
    #                 .replace("<camera>", tokens["<camera>"])
    #                 .replace("<version>", tokens["<version>"])
    #             )

    bpy.context.scene.render.filepath = (
        renpath.replace("<scene>", tokens["<scene>"])
        .replace("<file>", tokens["<file>"])
        .replace("<viewlayer>", tokens["<viewlayer>"])
        .replace("<camera>", tokens["<camera>"])
        .replace("<version>", tokens["<version>"])
    )
    print(bpy.context.scene.render.filepath)


@persistent
def restoreTokens(dummy):
    global renpath
    bpy.context.scene.render.filepath = renpath

    # # restore nodes
    # for node in nodeDict:
    #     node[0].base_path = node[1]


# //RENDER/<scene>/<file>/<viewlayer>/<camera>
