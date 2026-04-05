import pandas as pd
import matplotlib.pyplot as plt
import chart # Importing your teammate's chart class

# 1. Load the dataset
df = pd.read_csv('masculinity_survey.csv')

# 2. Identify the columns for Question 4 (Sources of Ideas)
# q0004_0001: Father, q0004_0002: Mother, q0004_0003: Other family
family_cols = ['q0004_0001', 'q0004_0002', 'q0004_0003']

# 3. Clean and Transform: Convert "Not selected" to 0 and the actual text to 1
for col in family_cols:
    # This replaces the specific text with 1 and "Not selected" with 0
    df[col] = df[col].apply(lambda x: 0 if x == 'Not selected' else 1)

# 4. Preliminary Analysis: Calculate the percentage of influence
print("Percentage of men influenced by:")
print(df[family_cols].mean() * 100)

# 5. Visualizing the 'Outcome' (How masculine they feel)
# Let's use the Chart class your teammate Hanif wrote to see the distribution
# We use 'q0001' which is "How masculine do you feel?"
perception_chart = chart.Chart('bar', df, 'q0001')
perception_chart.make_chart()