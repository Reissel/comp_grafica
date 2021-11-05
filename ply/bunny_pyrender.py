import trimesh
import pyrender

fuze_trimesh = trimesh.load('C:/Users/Reissel/Desktop/Computação Gráfica/obj/bunny_ply/bun_zipper.ply')
mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
scene = pyrender.Scene()
scene.add(mesh)
pyrender.Viewer(scene, use_raymond_lighting=True)