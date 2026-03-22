import pandas as pd
import chart

masculinity_df = pd.read_csv('masculinity_survey.csv')
demographics_df = masculinity_df[['racethn4', 'educ4', 'age3', 'kids', 'orientation', 'weight']]


# print(masculinity_df.columns)

# print(demographics_df.head(20))


# # We use a loop to go through every single column name in your DataFrame
# for column in demographics_df.columns:
#     temp_chart=chart.Chart('bar',demographics_df,column)
#     temp_chart.make_chart()
    



temp_chart=chart.Chart('histogram',demographics_df,'weight',bins=100)
temp_chart.make_chart()