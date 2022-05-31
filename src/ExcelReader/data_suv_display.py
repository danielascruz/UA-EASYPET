import matplotlib.pyplot as plt
import numpy as np


class SuvDisplayer:
    def __init__(self, data):
        self.data = data

    def read_file(self):
        file_name = self.data.excel_file.split('\\')[-1]
        if file_name == "SUV_values_backup.xlsx":
            self.graphic_organ_human()
            self.graphic_mean_human()
        elif file_name == "SUV_values_brain.xlsx":
            self.graphic_organ_mice()

    def graphic_organ_human(self):
        c = 1
        for i in ["Heart", "Brain (gray matter)", "Brain (white matter)", "Liver", "Kidney"]:
            plt.figure(c)
            plt.title(i)
            if self.data.df_study1_M[i]["SUV_mean"] != 0:
                plt.bar("S. Zincirkeser et al \n 2007 \n Male values", self.data.df_study1_M[i]["SUV_mean"], zorder=3)
                error_df1_M = [[self.data.df_study1_M[i]["SUV_mean"] - self.data.df_study1_M[i]["SUV_min"]],
                               [self.data.df_study1_M[i]["SUV_max"] - self.data.df_study1_M[i]["SUV_mean"]]]
                plt.errorbar("S. Zincirkeser et al \n 2007 \n Male values", self.data.df_study1_M[i]["SUV_mean"],
                             fmt='o', yerr=error_df1_M, color='k', zorder=3)

            if self.data.df_study1_F[i]["SUV_mean"] != 0:
                plt.bar("S. Zincirkeser et al \n 2007 \n Female values", self.data.df_study1_F[i]["SUV_mean"], zorder=3)
                error_df1_F = [[self.data.df_study1_F[i]["SUV_mean"] - self.data.df_study1_F[i]["SUV_min"]],
                               [self.data.df_study1_F[i]["SUV_max"] - self.data.df_study1_F[i]["SUV_mean"]]]
                plt.errorbar("S. Zincirkeser et al \n 2007 \n Female values", self.data.df_study1_F[i]["SUV_mean"],
                             fmt='o', yerr=error_df1_F, color='k', zorder=3)

            if self.data.df_study2_M[i]["SUV_mean"] != 0:
                plt.bar("André H. Dias et al \n 2022 \n Male Values", self.data.df_study2_M[i]["SUV_mean"], zorder=3)
                error_df2_M = [[self.data.df_study2_M[i]["SUV_mean"] - self.data.df_study2_M[i]["SUV_min"]],
                               [self.data.df_study2_M[i]["SUV_max"] - self.data.df_study2_M[i]["SUV_mean"]]]
                plt.errorbar("André H. Dias et al \n 2022 \n Male Values", self.data.df_study2_M[i]["SUV_mean"],
                             fmt='o', yerr=error_df2_M, color='k', zorder=3)

            if self.data.df_study2_F[i]["SUV_mean"] != 0:
                plt.bar("André H. Dias et al \n 2022 \n Female Values", self.data.df_study2_F[i]["SUV_mean"], zorder=3)
                error_df2_F = [[self.data.df_study2_F[i]["SUV_mean"] - self.data.df_study2_F[i]["SUV_min"]],
                               [self.data.df_study2_F[i]["SUV_max"] - self.data.df_study2_F[i]["SUV_mean"]]]
                plt.errorbar("André H. Dias et al \n 2022 \n Female Values", self.data.df_study2_F[i]["SUV_mean"],
                             fmt='o', yerr=error_df2_F, color='k', zorder=3)

            if self.data.df_study3[i]["SUV_mean"] != 0:
                plt.bar("LTH Tan et al \n 2004", self.data.df_study3[i]["SUV_mean"], zorder=3)
                error_df3 = [[self.data.df_study3[i]["SUV_mean"] - self.data.df_study3[i]["SUV_min"]],
                             [self.data.df_study3[i]["SUV_max"] - self.data.df_study3[i]["SUV_mean"]]]
                plt.errorbar("LTH Tan et al \n 2004", self.data.df_study3[i]["SUV_mean"],
                             fmt='o', yerr=error_df3, color='k', zorder=3)

            plt.xticks(rotation=90)
            plt.ylabel("SUV values (g/mL)")
            plt.grid(linestyle='--', zorder=0)
            plt.tight_layout()
            c += 1
        plt.show()

    def graphic_mean_human(self):
        plt.figure()
        plt.title("Average SUV Values")
        plt.ylabel("SUV values (g/mL)")
        plt.grid(linestyle='--', zorder=0)
        for i in ["Heart", "Brain (gray matter)", "Brain (white matter)", "Liver", "Kidney"]:

            total_mean_values = [self.data.df_study1_M[i]["SUV_mean"], self.data.df_study1_F[i]["SUV_mean"],
                                 self.data.df_study2_M[i]["SUV_mean"], self.data.df_study2_F[i]["SUV_mean"],
                                 self.data.df_study3[i]["SUV_mean"]]

            total_mean = [i for i in total_mean_values if i != 0]
            total_mean = np.mean(total_mean)

            error_df1_M = [[self.data.df_study1_M[i]["SUV_mean"] - self.data.df_study1_M[i]["SUV_min"]],
                           [self.data.df_study1_M[i]["SUV_max"] - self.data.df_study1_M[i]["SUV_mean"]]]
            error_df1_F = [[self.data.df_study1_F[i]["SUV_mean"] - self.data.df_study1_F[i]["SUV_min"]],
                           [self.data.df_study1_F[i]["SUV_max"] - self.data.df_study1_F[i]["SUV_mean"]]]
            error_df2_M = [[self.data.df_study2_M[i]["SUV_mean"] - self.data.df_study2_M[i]["SUV_min"]],
                           [self.data.df_study2_M[i]["SUV_max"] - self.data.df_study2_M[i]["SUV_mean"]]]
            error_df2_F = [[self.data.df_study2_F[i]["SUV_mean"] - self.data.df_study2_F[i]["SUV_min"]],
                           [self.data.df_study2_F[i]["SUV_max"] - self.data.df_study2_F[i]["SUV_mean"]]]
            error_df3 = [[self.data.df_study3[i]["SUV_mean"] - self.data.df_study3[i]["SUV_min"]],
                         [self.data.df_study3[i]["SUV_max"] - self.data.df_study3[i]["SUV_mean"]]]

            # Low Error
            error_min_value = [error_df1_M[0][0], error_df1_F[0][0], error_df2_M[0][0], error_df2_F[0][0],
                               error_df3[0][0]]
            error_min = [i for i in error_min_value if i != 0]
            total_error_min = np.max(error_min)

            # High Error
            error_max_value = [error_df1_M[1][0], error_df1_F[1][0], error_df2_M[1][0], error_df2_F[1][0],
                               error_df3[1][0]]
            error_max = [i for i in error_max_value if i != 0]
            total_error_max = np.max(error_max)

            plt.bar(i, total_mean, width=0.7, zorder=3)
            plt.xticks(rotation=90)
            plt.errorbar(i, total_mean, yerr=[[total_error_min], [total_error_max]], fmt='o', color='k', zorder=3)
            plt.tight_layout()
        plt.show()

    def graphic_organ_mice(self):
        plt.figure()
        plt.ylabel("SUV values (g/mL)")
        plt.grid(linestyle='--', zorder=0)
        plt.title("Robert A. Coleman et al \n 2017")
        for i in ["Cerebellum", "Hypothalamus", "Internal capsule"]:
            if self.data.df_Wild_Type[self.data.Study1][i]["SUV_mean"] != 0:
                plt.bar(i, self.data.df_Wild_Type[self.data.Study1][i]["SUV_mean"], zorder=3)
            plt.xticks(rotation=90)
            plt.tight_layout()
        plt.show()
