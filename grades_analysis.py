#!/usr/bin/env python3
"""
Student Grades Data Analysis
Author: Hewad Rustom

Features:
- Load student grades from a CSV file
- Calculate average, highest, and lowest scores
- Count number of passed and failed students
- Visualize results (histogram + bar chart)
- Save summary report to a text file
"""

import pandas as pd
import matplotlib.pyplot as plt

# ------------------- Settings -------------------
DATA_FILE = "students.csv"
REPORT_FILE = "grades_summary.txt"
PASS_MARK = 40  # students with score >= 40 are considered passed


# ------------------- Load Data -------------------
def load_data(filename: str) -> pd.DataFrame:
    """Load student grades CSV into a DataFrame"""
    try:
        df = pd.read_csv(filename)
        print(f"✅ Loaded {len(df)} records from {filename}")
        return df
    except FileNotFoundError:
        print(f"❌ File {filename} not found.")
        exit(1)


# ------------------- Analysis -------------------
def analyze(df: pd.DataFrame) -> dict:
    """Compute key statistics from grades"""
    results = {}
    results["average"] = df["Grade"].mean()
    results["highest"] = df["Grade"].max()
    results["lowest"] = df["Grade"].min()
    results["passed"] = (df["Grade"] >= PASS_MARK).sum()
    results["failed"] = (df["Grade"] < PASS_MARK).sum()
    results["total"] = len(df)

    return results


def save_report(results: dict, filename: str):
    """Save analysis results to a text file"""
    with open(filename, "w") as f:
        f.write("=== Student Grades Summary ===\n")
        f.write(f"Total students : {results['total']}\n")
        f.write(f"Average score  : {results['average']:.2f}\n")
        f.write(f"Highest score  : {results['highest']}\n")
        f.write(f"Lowest score   : {results['lowest']}\n")
        f.write(f"Passed         : {results['passed']}\n")
        f.write(f"Failed         : {results['failed']}\n")
    print(f"📄 Report saved to {filename}")


# ------------------- Visualization -------------------
def visualize(df: pd.DataFrame):
    """Generate charts for grade distribution and subject averages"""

    # Histogram of grades
    plt.figure(figsize=(6, 4))
    plt.hist(df["Grade"], bins=10, color="skyblue", edgecolor="black")
    plt.title("Grade Distribution")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("grades_histogram.png")
    plt.show()

    # Bar chart: average per subject (if multiple subjects exist)
    if "Subject" in df.columns:
        subject_avg = df.groupby("Subject")["Grade"].mean()
        plt.figure(figsize=(6, 4))
        subject_avg.plot(kind="bar", color="coral", edgecolor="black")
        plt.title("Average Grade per Subject")
        plt.ylabel("Average Grade")
        plt.tight_layout()
        plt.savefig("subject_avg.png")
        plt.show()


# ------------------- Main -------------------
def main():
    df = load_data(DATA_FILE)
    results = analyze(df)
    save_report(results, REPORT_FILE)
    visualize(df)


if __name__ == "__main__":
    main()
