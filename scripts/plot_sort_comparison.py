"""Plot a comparison of insertion sort vs. merge sort benchmark results.

Reads benchmark_results/insertion_sort.csv and benchmark_results/merge_sort.csv
(columns: n, time_ms) and saves a combined plot to
benchmark_results/sort_comparison.png so the difference in scaling
between the two algorithms is clearly visible.
"""

import csv
import pathlib

import matplotlib.pyplot as plt

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
INSERTION_SORT_CSV = BASE_DIR / "benchmark_results" / "insertion_sort.csv"
MERGE_SORT_CSV = BASE_DIR / "benchmark_results" / "merge_sort.csv"
PNG_PATH = BASE_DIR / "benchmark_results" / "sort_comparison.png"


def read_results(csv_path):
    n_values = []
    time_values = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            n_values.append(int(row["n"]))
            time_values.append(float(row["time_ms"]))
    return n_values, time_values


def plot_comparison(insertion_data, merge_data, output_path):
    fig, ax = plt.subplots()

    insertion_n, insertion_time = insertion_data
    merge_n, merge_time = merge_data

    ax.plot(insertion_n, insertion_time, marker="o", label="Insertion sort")
    ax.plot(merge_n, merge_time, marker="o", label="Merge sort")

    ax.set_xlabel("n, listans längd")
    ax.set_ylabel("t, körtid i millisekunder")
    ax.set_title("Insertion sort vs. merge sort performance")
    ax.legend()
    ax.grid(True)
    fig.savefig(output_path)
    plt.close(fig)


def main():
    insertion_data = read_results(INSERTION_SORT_CSV)
    merge_data = read_results(MERGE_SORT_CSV)
    plot_comparison(insertion_data, merge_data, PNG_PATH)


if __name__ == "__main__":
    main()
