import os
import re


class Atlas:
    def __init__(self, directory, file_name):
        self.directory = directory
        self.file_name = file_name
        self.atlas_data = {}

    def load_file(self):
        with open(os.path.join(self.directory, self.file_name), "r") as atlas:
            for line in atlas:
                par = line.split("\t")[0]
                par = par.split(" = ")
                self.atlas_data[par[0]] = int(par[1])
