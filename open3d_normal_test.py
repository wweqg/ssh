import open3d as o3d

def load_point_cloud_from_ply(ply_file):
    return o3d.io.read_point_cloud(ply_file)

# Replace "path_to_your_ply_file.ply" with the actual path to your PLY file
point_cloud = load_point_cloud_from_ply("./longdress_vox10_1051.ply")

def compute_normals(point_cloud):
    # Set the number of nearest neighbors to consider when computing normals
    # You can adjust this value based on your requirements
    num_neighbors = 30

    # Compute normals using Open3D's KDTree method
    o3d.geometry.PointCloud.estimate_normals(
        point_cloud, search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=num_neighbors)
    )

normals = point_cloud.normals

def write_normals_to_ply(point_cloud, ply_file):
    # Add normals to the point cloud
    o3d.io.write_point_cloud(ply_file, point_cloud)

# Replace "path_to_output_ply_file.ply" with the path where you want to save the updated PLY file
write_normals_to_ply(point_cloud, "./path_to_output_ply_file.ply")
