from math import radians
import numpy as np
import json
import glob
import pathlib
from numpy import cos, sin, pi
import open3d as o3d


class PointcloudTransformation():
        def __init__(self, folder_location, json=None):
                self.file_directory = str(pathlib.Path(__file__).parent.resolve())
                if json==None:
                        self.matrix_values = self.read(f'{self.file_directory}/matrices.json')
                else:
                        self.matrix_values = self.read(json)
                        
                self.ply_data_transform(folder_location)


        def read(self, file):
                with open(file, "r") as read_file:
                    location = json.load(read_file)
                return location


        def ply_data_transform(self, folder_location):
                
                for file in glob.glob(f'{folder_location}/*.ply'):
                        # naming format: object_posenumber_date.ply
                        pose_number = int(file.split('/')[-1].split('_')[1][4:])

                        pcd = o3d.io.read_point_cloud(file)

                        transformation_matrix = np.eye(4)
                        transformation_matrix[:3, :3] = pcd.get_rotation_matrix_from_xyz((self.matrix_values[pose_number][0], 0, 0))
                        transformation_matrix[0, 3] = self.matrix_values[pose_number][1]
                        transformation_matrix[1, 3] = self.matrix_values[pose_number][2]
                        transformation_matrix[2, 3] = self.matrix_values[pose_number][3]

                        pcd.transform(transformation_matrix)
                        o3d.visualization.draw_geometries([pcd])

                        pcd.export_to_ply('combined_point_cloud.ply')


        # def create_matrices(self, matrix_values):

        #         transformation_matrices = {}
        #         for key in matrix_values.keys():
        #                 transformation = 

        #                 # translation = np.identity(4)
        #                 # translation[:3,3] = matrix_values[key][1:]
        #                 # angle = pi*matrix_values[key][0]/180
        #                 # rotation = np.array([[cos(angle), 0, sin(angle), 0], [0, 1, 0, 0], [-sin(angle), 0, cos(angle), 0], [0, 0, 0, 1]])

        #                 # transformation_matrices[key] = [translation, rotation]

        #         return transformation_matrices


        # def ply_read(self, file):
        #         ply_data = open3d.io.read_point_cloud(file)
        #         points_matrix = np.asarray(ply_data.points)
        #         return points_matrix



# class pointcloud(object):

        # def __init__(self, ply):
        #         self.pointcloud = self.read(ply)
        #         self.ply = ply


if __name__ == "__main__":
        point_cloud = PointcloudTransformation('/home/cleveland/3d_scanner_realsense/src/Object1')

        point_cloud.ply_data_transform('/home/cleveland/3d_scanner_realsense/src/Object1')

