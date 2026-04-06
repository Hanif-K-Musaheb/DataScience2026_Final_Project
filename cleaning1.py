import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('masculinity_survey.csv')

#Filtering out people who didn't answer the main question
df = df[df['q0001'] != 'No answer'].copy()

#Targeted Binarization: Turning text into 1s and 0s
target_cols = ['q0004_0001', 'q0004_0002', 'q0008_0011']

for col in target_cols:
    df[col] = df[col].apply(lambda x: 0 if x == 'Not selected' else 1)


df.to_csv('masculinity_cleaned_focus.csv', index=False)
print("Targeted cleaning complete. Saved to 'masculinity_cleaned_focus.csv'")

#Chart 1: Family Impact
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='q0001', hue='q0004_0001', palette='Set2')
plt.title('Self-Perception of Masculinity vs. Father Influence')
plt.legend(title='Father Influence', labels=['No', 'Yes'])
plt.savefig('chart_family.png')

# Calculate the percentage of respondents who said 'Yes' to Father Influence
percentage_father_influence = df['q0004_0001'].mean() * 100

print(f"Percentage of respondents influenced by father figure: {percentage_father_influence:.1f}%")

#Chart 2: Money Impact
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='q0001', hue='q0008_0011', palette='coolwarm')
plt.title('Self-Perception of Masculinity vs. Provider Worry')
plt.legend(title='Worry about Providing', labels=['No', 'Yes'])
plt.savefig('chart_money.png')

