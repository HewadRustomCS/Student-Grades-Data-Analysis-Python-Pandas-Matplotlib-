# 📊 Student Grades Data Analysis (Python + Pandas + Matplotlib)

A Python project that analyzes **student grades** using Pandas and visualizes the results with Matplotlib. It loads grades from a CSV file, calculates statistics, generates reports, and produces visual charts.

## 🚀 Features
- Load student grades from a CSV file (`students.csv`)
- Calculate:
  - Average, highest, and lowest score
  - Number of passed/failed students
- Save summary to `grades_summary.txt`
- Visualize:
  - Histogram of grade distribution
  - Bar chart of average grade per subject

## 🛠️ Setup & Run
1. Clone this repository  
2. Install requirements:
   ```bash
   pip install pandas matplotlib
Make sure students.csv is in the same folder as grades_analysis.py

Run:

bash
Copy code
python grades_analysis.py
📂 Example Dataset (students.csv)
csv
Copy code
Name,Subject,Grade
Alice,Math,78
Bob,Math,55
Charlie,Math,32
Diana,Science,88
Ethan,Science,47
Fiona,History,65
George,History,29
Helen,Math,92
📌 Example Output
css
Copy code
✅ Loaded 8 records from students.csv
📄 Report saved to grades_summary.txt
grades_summary.txt

yaml
Copy code
=== Student Grades Summary ===
Total students : 8
Average score  : 60.75
Highest score  : 92
Lowest score   : 29
Passed         : 6
Failed         : 2
📈 Visualizations
grades_histogram.png → Histogram of grades

subject_avg.png → Bar chart of subject averages

📖 What I Learned
Using Pandas for data manipulation

Applying Matplotlib for visualizations

Reading/writing CSV & text files in Python

Creating a clean and reproducible data pipeline
