import pandas as pd
import chart

masculinity_df = pd.read_csv('masculinity_survey.csv')
demographics_df = masculinity_df[['racethn4', 'educ3' , 'educ4', 'age3', 'kids', 'orientation', 'weight']]


columns_chosen=['q0001', 'q0002', 'q0004_0001',
       'q0004_0002', 'q0004_0003', 'q0004_0004', 'q0004_0005', 'q0004_0006',
       'q0005', 'q0007_0001', 'q0007_0002', 'q0007_0003', 'q0007_0004',
       'q0007_0005', 'q0007_0006', 'q0007_0007', 'q0007_0008', 'q0007_0009',
       'q0007_0010', 'q0007_0011', 'q0008_0001', 'q0008_0002', 'q0008_0003',
       'q0008_0004', 'q0008_0005', 'q0008_0006', 'q0008_0007', 'q0008_0008',
       'q0008_0009', 'q0008_0010', 'q0008_0011', 'q0008_0012', 'q0009',
       'q0010_0001', 'q0010_0002', 'q0010_0003', 'q0010_0004', 'q0010_0005',
       'q0010_0006', 'q0010_0007', 'q0010_0008', 'q0011_0001', 'q0011_0002',
       'q0011_0003', 'q0011_0004', 'q0011_0005', 'q0024', 'q0025_0001', 
       'q0025_0002', 'q0025_0003', 'q0026', 'q0034', 'q0035', 'q0036',
       'educ4', 'age3', 'kids', 'orientation']

#print(masculinity_df.columns)

reduced_df=masculinity_df[columns_chosen]
print(reduced_df.head(6))

Q4={"father" : (demographics_df['q0004_0001'] == 'Father or father figure(s)').sum(),
    "mother" : (demographics_df['q0004_0002'] == 'Mother or mother figure(s)').sum(),
    "other family" : (demographics_df['q0004_0003'] == 'Other family members').sum(),
    "pop culture" : (demographics_df['q0004_0004'] == 'Pop culture').sum(),
    "friends" : (demographics_df['q0004_0003'] == 'Friends').sum(),
    "other" : (demographics_df['q0004_0003'] == 'Other (please specify)').sum()
    }


Q4_pie = chart.Chart('pie',reduced_df,'Q4',pie_arr=list(Q4))
Q4_pie.__make_pie_chart()


# question 3 is not in the database






# print(demographics_df.head(20))


# We use a loop to go through every single column name in your DataFrame
# for column in demographics_df.columns:
#     temp_chart=chart.Chart('bar',demographics_df,column)
#     temp_chart.make_chart()
    



# temp_chart=chart.Chart('histogram',demographics_df,'weight',bins=100)
# temp_chart.make_chart()