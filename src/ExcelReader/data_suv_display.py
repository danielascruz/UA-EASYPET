import matplotlib.pyplot as plt


class SuvDisplayer:
    def __init__(self, data):
        self.data = data

    def graphic_organ_mice(self):
        plt.figure()
        plt.ylabel("SUV values (g/mL)")
        plt.grid(linestyle='--', zorder=0)
        # plt.title("Robert A. Coleman et al \n 2017")
        for i in self.data.keys():
            if self.data[i]["SUV_mean"] != 0:
                plt.bar(i, self.data[i]["SUV_mean"], zorder=3)
            plt.xticks(rotation=90)
            plt.tight_layout()
        plt.show()
