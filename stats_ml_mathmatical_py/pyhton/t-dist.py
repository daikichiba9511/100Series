import numpy as np
import matplotlib.pyplot as plt

from scipy import stats
from pathlib import Path

plt.style.use("ggplot")

def main():
    x = np.arange(-10, 10, 0.01)
    normal_pdf = stats.norm.pdf(x, 0, 1)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(x, normal_pdf, label="gaussian distribution")
    for i in range(1, 11):
        t_dist_pdf = stats.t.pdf(x,i)
        ax.plot(x, t_dist_pdf, label="free degree of t distribution = " + str(i))
    ax.legend(loc="best")
    plt.show()
    fig.savefig(Path.cwd()/"stats_ml_mathmatical_py"/"fig"/"t-dist_py.png")

if __name__ == "__main__":
    main()