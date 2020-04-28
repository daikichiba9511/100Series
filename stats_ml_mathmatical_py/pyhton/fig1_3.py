import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

def main():
    base_dir = Path.cwd()
    x = np.arange(0, 20, 0.1)
    for i in range(1, 11):
        plt.plot(x, stats.chi2.pdf(x, i), label=str(i))
    plt.legend(loc="best")
    plt.show()
    plt.savefig(base_dir/"stats_ml_mathmatical_py"/"fig"/"fig1-3_py.png")
if __name__ == "__main__":
    main()