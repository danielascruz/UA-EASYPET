import pandas as pd


class SuvReader:
    def __init__(self, excel_file):
        self.excel_file = excel_file

    def read_mice(self):
        xls = pd.ExcelFile(self.excel_file)  # Read excel with pandas
        mice_dict = xls.parse(xls.sheet_names[0])  # turns sheet into a data frame
        mice_dict = mice_dict.set_index('organs').to_dict(orient="index")

        for j in [mice_dict]:
            for i in j.keys():
                if j[i]["name_moby"] == "None":
                    j[i]["SUV_mean"] = 0
        
        return mice_dict
