import open3d as o3d
import numpy as np

# pcd = o3d.io.read_point_cloud("./voxel_grid.pcd")

# voxel = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, 1024) #Voxel size specification
# o3d.visualization.draw_geometries([pcd])

print('input')
N = 2000
#TXT FORMAT pcd = o3d.io.read_point_cloud("./Mais.txt" ,format='xyz')
pcd = o3d.io.read_point_cloud("../MAIS.pcd")
# fit to unit cube
pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
          center=pcd.get_center())
pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
o3d.visualization.draw_geometries([pcd])

print('voxelization')
pcd.paint_uniform_color([1, 0.706, 0])
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                            voxel_size=0.005)
print(voxel_grid)
o3d.io.write_voxel_grid("leaf_voxel.ply", voxel_grid)
# voxel_grid.paint_uniform_color([1, 0.706, 0])
pcd = o3d.io.read_point_cloud("leaf_voxel.ply")
o3d.io.write_point_cloud("leaf_voxelizedMAIS.pcd", pcd)


o3d.visualization.draw_geometries([voxel_grid])
