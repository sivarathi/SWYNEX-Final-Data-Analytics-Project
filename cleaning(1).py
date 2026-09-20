import pandas as pd

# Load the raw dataset
df = pd.read_csv("student_performance.csv")

# Replace missing values with Unknown
df = df.fillna("Unknown")

# Remove duplicate rows
df = df.drop_duplicates()

# Correct invalid exam scores
if "Exam_Score" in df.columns:
    df["Exam_Score"] = pd.to_numeric(df["Exam_Score"], errors="coerce")
    df.loc[df["Exam_Score"] > 100, "Exam_Score"] = 100

# Save cleaned dataset
df.to_csv("cleaned_student_performance.csv", index=False)
print("Cleaning completed successfully.")
