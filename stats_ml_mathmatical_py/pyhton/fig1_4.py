import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

import fig1_2

def main():
    N = 100
    iter_num = 100
    fig, ax = plt.subplots(figsize=(10, 10))

    for _ in range(iter_num):
        x = np.random.randn(N)+2
        e = np.random.randn(N)
        y = x + 1 + e
        b_1, b_0 = fig1_2.min_sq(x, y)

        ax.scatter(b_0, b_1)
    ax.axhline(1.0, c="black", linewidth=0.5)
    ax.axvline(1.0, c="black", linewidth=0.5)
    ax.set_ylabel("beta_1")
    ax.set_xlabel("beta_0")
    fig.savefig(Path.cwd()/"stats_ml_mathmatical_py"/"fig"/"fig1_4_py.png")
    plt.show()
    plt.close(fig)
if __name__ == "__main__":
    main()