import os
from array import array
import numpy as np


class RawDataSetter:
    def __init__(self, file_name, volume=None, size_file_m=None, pixel_size=1, pixel_size_axial=1, offset=0):
        if size_file_m is None and volume is None:
            size_file_m = np.array(os.path.basename(file_name).split("(")[1].split(")")[0].split(","), dtype=np.int)
        if volume is not None:
            size_file_m = volume.shape
        self.file_name = file_name
        self.size_file_m = size_file_m
        self.pixel_size = pixel_size
        self.pixel_size_axial = pixel_size_axial
        self.size_file = self.size_file_m[0]*self.size_file_m[1]*self.size_file_m[2]
        self.offset = offset
        self.volume = volume

    def read_files(self):
        output_file = open(self.file_name, 'rb')  # define o ficheiro que queres ler
        a = array('f')  # define quantos bytes le de cada vez (float32)
        a.fromfile(output_file, self.size_file)  # lê o ficheiro binário (fread)
        output_file.close()  # fecha o ficheiro
        volume = np.array(a)  # não precisas
        self.volume = volume.reshape((self.size_file_m[0], self.size_file_m[1], self.size_file_m[2]), order='f')

    def write_files_simple_binary(self):
        """ """
        volume = self.volume.astype(np.float32)
        length = 1
        for i in volume.shape:
            length *= i
        # length = volume.shape[0] * volume.shape[2] * volume.shape[1]
        if len(volume.shape) > 1:
            data = np.reshape(volume, [1, length], order='F')
        else:
            data = volume
        output_file = open(self.file_name, 'wb')
        # output_file = open(os.path.join(self.study_path, file_folder, file_name_raw), 'wb')
        arr = array('f', data[0])

        arr.tofile(output_file)
        output_file.close()
