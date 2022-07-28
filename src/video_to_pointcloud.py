import glob
import numpy as np
import matplotlib.pyplot as plt
import pyrealsense2 as rs



class VideoToPointcloud():
    def __init__(self, folder_directory):
        self.folder_directory = folder_directory
        self.pipe = rs.pipeline()
        self.cfg  = rs.config()
        self.main()

    def open(self, file):
        
        self.cfg.enable_device_from_file(file)
        self.pipe.start(self.cfg)


        for x in range (5):
            self.pipe.wait_for_frames()


        frameset = self.pipe.wait_for_frames()
        color_frame = frameset.get_color_frame()
        depth_frame = frameset.get_depth_frame()


        self.pipe.stop()

        return color_frame, depth_frame

    
    def save_pointcloud(self, color_frame, depth_frame, name):
        pc = rs.pointcloud()
        pc.map_to(color_frame)
        pointcloud = pc.calculate(depth_frame)
        pointcloud.export_to_ply(f'{name}.ply', color_frame)


    def main(self):
        for file_name in glob.glob(f'{self.folder_directory}/*.bag'):
            color_frame, depth_frame = self.open(file_name)
            temp_name = file_name.split('/')
            self.save_pointcloud(color_frame, depth_frame, f'{self.folder_directory}/{temp_name[-1][:-4]}')

            

if __name__ == "__main__":
    VideoToPointcloud('/home/cleveland/python_training/3d_scanner')