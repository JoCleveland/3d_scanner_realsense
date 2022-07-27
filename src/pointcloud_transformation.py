from math import radians
import numpy as np
import json
from plyfile import PlyData, PlyElement
import glob
import pathlib
from numpy import cos, sin, pi
import open3d


class PointcloudTransformation():
        def __init__(self, folder_location, json=None):
                self.file_directory = str(pathlib.Path(__file__).parent.resolve())
                if json==None:
                        matrix_values = self.read(f'{self.file_directory}/matrices.json')
                else:
                        matrix_values = self.read(json)
                self.transformation_matrices = self.create_matrices(matrix_values)
                self.main(folder_location)


        def read(self, file):
                with open(file, "r") as read_file:
                    location = json.load(read_file)
                return location


        def create_matrices(self, matrix_values):

                transformation_matrices = {}
                for key in matrix_values.keys():
                        translation = np.identity(4)
                        translation[:3,3] = matrix_values[key][1:]
                        angle = pi*matrix_values[key][0]/180
                        rotation = np.array([[cos(angle), 0, sin(angle), 0], [0, 1, 0, 0], [-sin(angle), 0, cos(angle), 0], [0, 0, 0, 1]])

                        transformation_matrices[key] = [translation, rotation]

                return transformation_matrices


        def ply_read(self, file):
                ply_data = open3d.io.read_point_cloud(file)
                points_matrix = np.asarray(ply_data.points)
                return points_matrix


        def ply_data_transform(self, points_matrix):
                


        def main(self, folder_location):
                for file in glob.glob(f'{folder_location}/*.ply'):
                        # naming format: object_posenumber_date.ply
                        pose_number = int(file.split('/')[-1].split('_')[1][4:])



# class pointcloud(object):

        # def __init__(self, ply):
        #         self.pointcloud = self.read(ply)
        #         self.ply = ply


if __name__ == "__main__":


        matrix_info = transformations("/home/cleveland/python_training/3d_scanner/matrices.json")


        
                