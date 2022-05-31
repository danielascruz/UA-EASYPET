import matplotlib.pyplot as plt
import numpy as np


class SuvDisplayer:
    def __init__(self, data):
        self.data = data

    def graphic_organ(self):
        c = 1
        for i in ["Heart", "Brain (gray matter)", "Brain (white matter)", "Liver", "Kidney"]:
            plt.figure(c)
            plt.title(i)
            plt.bar("S. Zincirkeser et al \n 2007 \n Male values", self.data.df_study1_M[i]["SUV_mean"])
            plt.bar("S. Zincirkeser et al \n 2007 \n Female values", self.data.df_study1_F[i]["SUV_mean"])
            plt.bar("André H. Dias et al \n 2022 \n Male Values", self.data.df_study2_M[i]["SUV_mean"])
            plt.bar("André H. Dias et al \n 2022 \n Female Values", self.data.df_study2_F[i]["SUV_mean"])
            plt.bar("LTH Tan et al \n 2004", self.data.df_study3[i]["SUV_mean"])

            error_df1_M = [[self.data.df_study1_M[i]["SUV_min"]], [self.data.df_study1_M[i]["SUV_max"]]]
            error_df1_F = [[self.data.df_study1_F[i]["SUV_min"]], [self.data.df_study1_F[i]["SUV_max"]]]
            error_df2_M = [[self.data.df_study2_M[i]["SUV_min"]], [self.data.df_study2_M[i]["SUV_max"]]]
            error_df2_F = [[self.data.df_study2_F[i]["SUV_min"]], [self.data.df_study2_F[i]["SUV_max"]]]
            error_df3 = [[self.data.df_study3[i]["SUV_min"]], [self.data.df_study3[i]["SUV_max"]]]

            plt.errorbar("S. Zincirkeser et al \n 2007 \n Male values", self.data.df_study1_M[i]["SUV_mean"],
                         fmt='o', yerr=error_df1_M, color='k')
            plt.errorbar("S. Zincirkeser et al \n 2007 \n Female values", self.data.df_study1_F[i]["SUV_mean"],
                         fmt='o', yerr=error_df1_F, color='k')
            plt.errorbar("André H. Dias et al \n 2022 \n Male Values", self.data.df_study2_M[i]["SUV_mean"],
                         fmt='o', yerr=error_df2_M, color='k')
            plt.errorbar("André H. Dias et al \n 2022 \n Female Values", self.data.df_study2_F[i]["SUV_mean"],
                         fmt='o', yerr=error_df2_F, color='k')
            plt.errorbar("LTH Tan et al \n 2004", self.data.df_study3[i]["SUV_mean"],
                         fmt='o', yerr=error_df3, color='k')

            plt.xticks(rotation=90)
            plt.tight_layout()
            c += 1
        plt.show()

    def graphic_mean(self):
        plt.figure()
        plt.title("Average SUV Values")
        for i in ["Heart", "Brain (gray matter)", "Brain (white matter)", "Liver", "Kidney"]:

            total_mean_values = [self.data.df_study1_M[i]["SUV_mean"], self.data.df_study1_F[i]["SUV_mean"],
                                 self.data.df_study2_M[i]["SUV_mean"], self.data.df_study2_F[i]["SUV_mean"],
                                 self.data.df_study3[i]["SUV_mean"]]

            total_mean = [i for i in total_mean_values if i != 0]
            total_mean = np.mean(total_mean)

            error_df1_M = [[self.data.df_study1_M[i]["SUV_min"]], [self.data.df_study1_M[i]["SUV_max"]]]
            error_df1_F = [[self.data.df_study1_F[i]["SUV_min"]], [self.data.df_study1_F[i]["SUV_max"]]]
            error_df2_M = [[self.data.df_study2_M[i]["SUV_min"]], [self.data.df_study2_M[i]["SUV_max"]]]
            error_df2_F = [[self.data.df_study2_F[i]["SUV_min"]], [self.data.df_study2_F[i]["SUV_max"]]]
            error_df3 = [[self.data.df_study3[i]["SUV_min"]], [self.data.df_study3[i]["SUV_max"]]]

            error_min_value = [error_df1_M[0][0], error_df1_F[0][0], error_df2_M[0][0], error_df2_F[0][0],
                               error_df3[0][0]]
            error_min = [i for i in error_min_value if i != 0]
            total_error_min = np.max(error_min)

            error_max_value = [[error_df1_M[1][0], error_df1_F[1][0], error_df2_M[1][0], error_df2_F[1][0],
                                error_df3[1][0]]]
            error_max = [i for i in error_max_value if i != 0]
            total_error_max = np.max(error_max)

            plt.bar(i, total_mean, width=0.7)
            plt.xticks(rotation=90)
            plt.errorbar(i, total_mean, yerr=[[total_error_min], [total_error_max]], fmt='o', color='k')
            plt.tight_layout()
        plt.show()
