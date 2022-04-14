from pyntcloud import PyntCloud

cloud = PyntCloud.from_file("./leaf_voxelizedMAIS.pcd")

leaf = cloud.add_scalar_field("plane_fit")

cloud.points[leaf].plot(kind="hist")

cloud.plot(use_as_color=leaf,cmap="cool")