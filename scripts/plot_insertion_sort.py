"""Plot insertion sort benchmark results.

Reads benchmark_results/insertion_sort.csv (columns: n, time_ms) and
saves a line/scatter plot showing how the runtime grows with n to
benchmark_results/insertion_sort.png.
"""

import csv
import pathlib

import matplotlib.pyplot as plt

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "benchmark_results" / "insertion_sort.csv"
PNG_PATH = BASE_DIR / "benchmark_results" / "insertion_sort.png"


def read_results(csv_path):
    n_values = []
    time_values = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            n_values.append(int(row["n"]))
            time_values.append(float(row["time_ms"]))
    return n_values, time_values


def plot_results(n_values, time_values, output_path):
    fig, ax = plt.subplots()
    ax.plot(n_values, time_values, marker="o")
    ax.set_xlabel("n, listans längd")
    ax.set_ylabel("t, körtid i millisekunder")
    ax.set_title("Insertion sort performance")
    ax.grid(True)
    fig.savefig(output_path)
    plt.close(fig)


def main():
    n_values, time_values = read_results(CSV_PATH)
    plot_results(n_values, time_values, PNG_PATH)


if __name__ == "__main__":
    main()
