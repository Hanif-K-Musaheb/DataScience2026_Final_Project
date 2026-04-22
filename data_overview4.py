import pandas as pd
import matplotlib.pyplot as plt

q1=['q0001']
q2=['q0002']
q4=['q0004_0001', 'q0004_0002', 'q0004_0003', 'q0004_0004', 'q0004_0005', 'q0004_0006']
q5=['q0005']
q7=['q0007_0001', 'q0007_0002', 'q0007_0003', 'q0007_0004',
       'q0007_0005', 'q0007_0006', 'q0007_0007', 'q0007_0008', 'q0007_0009',
       'q0007_0010', 'q0007_0011']
q8=['q0008_0001', 'q0008_0002', 'q0008_0003',
       'q0008_0004', 'q0008_0005', 'q0008_0006', 'q0008_0007', 'q0008_0008',
       'q0008_0009', 'q0008_0010', 'q0008_0011', 'q0008_0012']
q9=['q0009']




masculinity_df = pd.read_csv('masculinity_survey.csv')


percentage_data = masculinity_df[q2].value_counts(normalize=True) * 100

percentage_data.plot(kind='barh')
plt.xlabel('Percentage (%)') 

plt.tight_layout()
plt.show()