import pandas as pd


class SuvReader:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.mice_dict = None

    def read_mice(self):
        xls = pd.ExcelFile(self.excel_file)  # Read excel with pandas
        self.mice_dict = xls.parse(xls.sheet_names[0])  # turns sheet into a data frame
        self.mice_dict = self.mice_dict.set_index('organs').to_dict(orient="index")

        for j in [self.mice_dict]:
            for i in j.keys():
                if j[i]["name_moby"] == "None":
                    j[i]["SUV_mean"] = 0
