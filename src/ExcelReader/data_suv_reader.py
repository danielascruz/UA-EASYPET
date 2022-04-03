import pandas as pd


class SuvReader:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.df_study1_M = None
        self.df_study1_F = None
        self.df_study2_M = None
        self.df_study2_F = None
        self.df_study3 = None

    def read_file(self):
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
