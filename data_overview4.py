import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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




# masculinity_df = pd.read_csv('masculinity_survey.csv')

# percentage_data = masculinity_df[q4].value_counts(normalize=True) * 100

# percentage_data.plot(kind='barh')
# plt.xlabel('Percentage (%)')

# plt.tight_layout()
# plt.show()


import pandas as pd
import plotly.express as px

# Load your data
masculinity_df = pd.read_csv('masculinity_survey.csv')

q4 = ['q0004_0001', 'q0004_0002', 'q0004_0003', 'q0004_0004', 'q0004_0005', 'q0004_0006']

# 1. Run value_counts on all 6 columns individually using 'apply', fill missing with 0, and get percentages
df_percentages = masculinity_df[q9].apply(pd.Series.value_counts, normalize=True).fillna(0) * 100

# 2. Convert the row labels (the actual survey answers) into a standard column named 'Response'
df_percentages = df_percentages.reset_index().rename(columns={'index': 'Response'})

# 3. 'Melt' the data so it has exactly 3 columns: Response, Question, and Percentage
df_plot = df_percentages.melt(id_vars='Response', var_name='Question', value_name='Percentage')

# 4. Create the interactive grouped bar chart
fig = px.bar(df_plot, 
             x='Percentage', 
             y='Question', 
             color='Response', 
             barmode='group', # Groups the bars side-by-side instead of stacking them
             title='Q4 Responses (Hover for details)')

# Open the interactive chart
fig.show()