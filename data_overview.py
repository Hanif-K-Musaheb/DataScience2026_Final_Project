import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load your dataset
df = pd.read_csv('masculinity_survey.csv')

# 2. Create a folder to save all the graphs so they don't clutter your workspace
output_folder = "dataset_graphs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 3. Loop through every single column in the DataFrame
for column in df.columns:
    plt.figure(figsize=(8, 5))
    
    # Count the frequency of each value in the column and plot a bar chart
    # We use dropna=False to also see if there are any missing values
    value_counts = df[column].value_counts(dropna=False)
    
    # Create a bar plot
    value_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    
    # Add titles and labels
    plt.title(f'Distribution of {column}')
    plt.xlabel('Values')
    plt.ylabel('Count')
    
    # Adjust layout so labels don't get cut off
    plt.tight_layout()
    
    # Save the graph as a PNG image in the folder
    # We replace any slashes in the column name just in case to prevent file path errors
    safe_col_name = str(column).replace('/', '_')
    plt.savefig(f'{output_folder}/{safe_col_name}_graph.png')
    
    # Close the plot to free up memory
    plt.close()

print(f"All graphs have been successfully saved in the '{output_folder}' folder!")