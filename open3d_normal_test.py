import open3d as o3d

# Load the point cloud from .ply file
pcd = o3d.io.read_point_cloud("longdress_vox10_1051.ply")

# Compute normals for the point cloud
o3d.geometry.estimate_normals(pcd, search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# Save the point cloud with normals to a new .ply file
o3d.io.write_point_cloud("out", pcd)
