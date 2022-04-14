from matplotlib import projections
import open3d as o3d
import numpy as np


pcd = o3d.io.read_point_cloud("./leaf_voxelizedMAIS.pcd")
plane_model, inliers = pcd.segment_plane(distance_threshold=1000,
                                         ransac_n=3,
                                         num_iterations=1000,
                                         
                                         )

print(f"PCD: {pcd}")
print(f"Plane Model: {plane_model}")
print(f"Inliers: {inliers}")



[a, b, c, d] = plane_model
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

inlier_cloud = pcd.select_by_index(inliers)
temp = np.asarray(inlier_cloud)
print(f"Inliers CLoud: {temp}")
inlier_cloud.paint_uniform_color([1.0, 0, 0])
outlier_cloud = pcd.select_by_index(inliers, invert=True)
print(f"Outliers CLoud: {outlier_cloud}")
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


p1 = np.array([43, 53, 97])
p2 = np.array([55, 43, 116])
p3 = np.array([107, 33, 93])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-2, 14, 5)
y = np.linspace(-2, 14, 5)
X, Y = np.meshgrid(x, y)

Z = (d - a * X - b * Y) / c

# plot the mesh. Each array is 2D, so we flatten them to 1D arrays
ax.plot(X.flatten(),
        Y.flatten(),
        Z.flatten(), 'bo ')

# plot the original points. We use zip to get 1D lists of x, y and z
# coordinates.
ax.plot(*zip(p1, p2, p3), color='r', linestyle=' ', marker='o')

# adjust the view so we can see the point/plane alignment
ax.view_init(0, 22)
plt.tight_layout()
plt.savefig('plane.png')
plt.show()