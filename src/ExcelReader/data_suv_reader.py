import pandas as pd


class SuvReader:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.df_study1_M = None
        self.df_study1_F = None
        self.df_study2_M = None
        self.df_study2_F = None
        self.df_study3 = None
        self.df_Tg2576 = None
        self.df_Wild_Type = None
        self.df_Wild_Type1 = None
        self.df_Wild_Type2 = None
        self.Study1 = "Brain and Brown Adipose Tissue Metabolism in Transgenic Tg2576 Mice Models of Alzheimer " \
                      "Disease Assessed Using 18F-FDG PET Imaging"
        self.Study2 = "Study of an image-derived SUV and a modified SUV using mouse FDG-PET"
        self.mice_dict = None

    def read_file(self):
        file_name = self.excel_file.split('\\')[-1]
        if file_name == "SUV_values_backup.xlsx":
            self.read_human_file()
        elif file_name == "SUV_values_brain.xlsx":
            self.read_mice_file()
        elif file_name == "SUV_mice.xlsx":
            self.read_mice()

    def read_human_file(self):
        xls = pd.ExcelFile(self.excel_file)  # Read excel with pandas
        self.df_study1_M = xls.parse(xls.sheet_names[0], header=1)  # turns sheet into a data frame
        self.df_study1_F = xls.parse(xls.sheet_names[1], header=1)
        self.df_study2_M = xls.parse(xls.sheet_names[2], header=1)
        self.df_study2_F = xls.parse(xls.sheet_names[3], header=1)
        self.df_study3 = xls.parse(xls.sheet_names[4], header=1)

        self.df_study1_M = self.df_study1_M.set_index('organs').to_dict(orient="index")
        self.df_study1_F = self.df_study1_F.set_index('organs').to_dict(orient="index")
        self.df_study2_M = self.df_study2_M.set_index('organs').to_dict(orient="index")
        self.df_study2_F = self.df_study2_F.set_index('organs').to_dict(orient="index")
        self.df_study3 = self.df_study3.set_index('organs').to_dict(orient="index")

        for j in [self.df_study1_M, self.df_study1_F, self.df_study2_M, self.df_study2_F, self.df_study3]:
            for i in j.keys():
                if j[i]["SUV_mean"] == "None":
                    j[i]["SUV_mean"] = 0
                    j[i]["SUV_min"] = 0
                    j[i]["SUV_max"] = 0

    def read_mice_file(self):
        xls = pd.ExcelFile(self.excel_file)  # Read excel with pandas
        self.df_Tg2576 = xls.parse(xls.sheet_names[0], header=1)  # turns sheet into a data frame
        self.df_Tg2576 = self.df_Tg2576.set_index('organs').to_dict(orient="index")

        self.df_Wild_Type1 = xls.parse(xls.sheet_names[1], header=1)
        self.df_Wild_Type1 = self.df_Wild_Type1.set_index('organs').to_dict(orient="index")

        self.df_Wild_Type2 = xls.parse(xls.sheet_names[2], header=1)
        self.df_Wild_Type2 = self.df_Wild_Type2.set_index('organs').to_dict(orient="index")

        for j in [self.df_Tg2576, self.df_Wild_Type1, self.df_Wild_Type2]:
            for i in j.keys():
                if j[i]["SUV_mean"] == "None":
                    j[i]["SUV_mean"] = 0

        self.df_Wild_Type = {self.Study1: self.df_Wild_Type1, self.Study2: self.df_Wild_Type2}

    def read_mice(self):
        xls = pd.ExcelFile(self.excel_file)  # Read excel with pandas
        self.mice_dict = xls.parse(xls.sheet_names[0])  # turns sheet into a data frame
        self.mice_dict = self.mice_dict.set_index('organs').to_dict(orient="index")

        for j in [self.mice_dict]:
            for i in j.keys():
                if j[i]["SUV_mean"] == "None":
                    j[i]["SUV_mean"] = 0
