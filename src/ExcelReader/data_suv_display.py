import matplotlib.pyplot as plt


class SuvDisplayer:
    def __init__(self, data):
        self.data = data
        # self.error_df1_M = None
        # self.error_df1_F = None
        # self.error_df2_M = None
        # self.error_df2_F = None
        # self.error_df3 = None

    def graphic(self):
        plt.figure()
        c = 1
        for i in ["Stomach", "Lung (R)", "Lung (L)", "Heart"]:
            plt.subplot(3, 2, c)
            plt.title(i, fontsize=9)
            plt.bar("S1: M", self.data.df_study1_M[i]["SUV_mean"], width=0.7)
            plt.bar("S1: F", self.data.df_study1_F[i]["SUV_mean"], width=0.7)
            plt.bar("S2: M", self.data.df_study2_M[i]["SUV_mean"], width=0.7)
            plt.bar("S2: F", self.data.df_study2_F[i]["SUV_mean"], width=0.7)
            plt.bar("S3", self.data.df_study3[i]["SUV_mean"], width=0.7)

            error_df1_M = [[self.data.df_study1_M[i]["SUV_min"]], [self.data.df_study1_M[i]["SUV_max"]]]
            error_df1_F = [[self.data.df_study1_F[i]["SUV_min"]], [self.data.df_study1_F[i]["SUV_max"]]]
            error_df2_M = [[self.data.df_study2_M[i]["SUV_min"]], [self.data.df_study2_M[i]["SUV_max"]]]
            error_df2_F = [[self.data.df_study2_F[i]["SUV_min"]], [self.data.df_study2_F[i]["SUV_max"]]]
            error_df3 = [[self.data.df_study3[i]["SUV_min"]], [self.data.df_study3[i]["SUV_max"]]]

            plt.errorbar("S1: M", self.data.df_study1_M[i]["SUV_mean"], fmt='o', yerr=error_df1_M, color='k')
            plt.errorbar("S1: F", self.data.df_study1_F[i]["SUV_mean"], fmt='o', yerr=error_df1_F, color='k')
            plt.errorbar("S2: M", self.data.df_study2_M[i]["SUV_mean"], fmt='o', yerr=error_df2_M, color='k')
            plt.errorbar("S2: F", self.data.df_study2_F[i]["SUV_mean"], fmt='o', yerr=error_df2_F, color='k')
            plt.errorbar("S3", self.data.df_study3[i]["SUV_mean"], fmt='o', yerr=error_df3, color='k')
            c += 1
        plt.show()
