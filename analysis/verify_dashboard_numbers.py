"""
HR Analytics Dashboard — Verification Analysis
Answers the same ten questions the Power BI dashboard's own panels raise,
using pandas only. No new charts are generated here on purpose — the
dashboard (HR.pbix / dashboard_full.png) is the single source of visuals
for this project; this script just proves the numbers behind it.
"""

import pandas as pd

df = pd.read_csv("../data/HR_Analytics-4__2_.csv", encoding="utf-8-sig")
df.columns = df.columns.str.strip()

print("Rows, Cols:", df.shape)

# Q1. Headline KPIs (Total Employees / Active / Attrition Count / Attrition Rate)
total = len(df)
attrition_yes = (df["Attrition"] == "Yes").sum()
attrition_no = (df["Attrition"] == "No").sum()
rate = attrition_yes / total * 100
print(f"\nQ1 - Total: {total} | Active: {attrition_no} | Attrition: {attrition_yes} | Rate: {rate:.1f}%")

# Q2. Average Age & Average Experience (dashboard uses YearsatCompany, not TotalExperience)
print(f"\nQ2 - Avg Age: {df['Age'].mean():.1f} | Avg Years at Company: {df['YearsatCompany'].mean():.2f}")

# Q3. Attrition by Department
q3 = df[df["Attrition"] == "Yes"]["Department"].value_counts()
print("\nQ3 - Attrition count by Department:\n", q3)

# Q4. Attrition by Salary Slab
q4 = pd.crosstab(df["SalarySlab"], df["Attrition"])
print("\nQ4 - Attrition by Salary Slab:\n", q4)

# Q5. Age Group Distribution
q5 = df["AgeGroup"].value_counts()
print("\nQ5 - Employee count by Age Group:\n", q5)

# Q6. Attrition by Gender
q6 = df[df["Attrition"] == "Yes"]["Gender"].value_counts()
print("\nQ6 - Attrition count by Gender:\n", q6)

# Q7. Attrition Trend by Experience (Total Experience in years)
q7 = df[df["Attrition"] == "Yes"]["TotalExperience(Years)"].value_counts().sort_index()
print("\nQ7 - Attrition count by Total Experience (years):\n", q7.head(12))

# Q8. Attrition by Job Role & Job Satisfaction
q8 = pd.crosstab(df[df["Attrition"] == "Yes"]["JobRole"],
                  df[df["Attrition"] == "Yes"]["JobSatisfaction"], margins=True)
print("\nQ8 - Attrition by JobRole x JobSatisfaction:\n", q8)

# Q9. Department-wise Employee Count
q9 = df["Department"].value_counts()
print("\nQ9 - Employee count by Department:\n", q9)

# Q10. Does overtime relate to attrition? (extra cut not on the dashboard,
# computed here purely to sanity-check the story, no chart produced)
q10 = pd.crosstab(df["OverTime"], df["Attrition"], normalize="index") * 100
print("\nQ10 - Attrition rate by OverTime status (%):\n", q10)
