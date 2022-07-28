import copy
import numpy as np
import open3d as o3d

test = o3d.io.read_point_cloud('src/stairs.ply')
T = np.eye(4)
T[:3, :3] = test.get_rotation_matrix_from_xyz((0, np.pi / 3, np.pi / 2))
T[0, 3] = 1
T[1, 3] = 1.3
print(T)
test_t = copy.deepcopy(test).transform(T)
o3d.visualization.draw_geometries([test, test_t])