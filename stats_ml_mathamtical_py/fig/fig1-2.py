import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

from typing import List, Union
Num = Union[int, float]
Vector = List[Num]

plt.style.use("ggplot")

def min_sq(x : Union[Vector, np.ndarray], y : Union[Vector, np.ndarray] ) -> np.ndarray:
    x_bar, y_bar = np.mean(x), np.mean(y)
    beta_1 : np.ndarray = np.dot(x-x_bar, y-y_bar) / np.linalg.norm(x-x_bar)**2 # (1.4)
    beta_0 : np.ndarray = y_bar - beta_1 * x_bar
    return beta_1, beta_0

def plot(x, y, x_seq, y_pre, yy_pre, out_dir, save=False, fig_name = None):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y)
    ax.axhline(0, c="black", linewidth=0.5)
    ax.axvline(0, c="black", linewidth=0.5)
    ax.plot(x_seq, y_pre, label="before Centering")
    ax.plot(x_seq, yy_pre, label="after Centering")
    ax.legend(loc="best")
    plt.show()
    if save:
        fig.savefig(out_dir / fig_name)

def run():
    base_dir = Path.cwd()
    out_dir = base_dir / "fig"
    N = 100
    a = np.random.normal(loc=2, scale=1, size=N) # mean = 2, std = 1
    b = np.random.randn(1)
    x = np.random.randn(N)
    y = a * x + b + np.random.randn(N) # データ生成

    a1, b1 = min_sq(x, y)
    xx = x - np.mean(x)
    yy = y - np.mean(y)
    a2, b2 = min_sq(xx, yy)

    x_seq = np.arange(-5, 5, 0.01)
    y_pre = x_seq*a1 + b1
    yy_pre = x_seq*a2 + b2
    plot(x, y, x_seq, y_pre, yy_pre, out_dir, save=True, fig_name="fig1-2")

if __name__ == "__main__":
    run()