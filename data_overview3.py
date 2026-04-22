import pandas as pd
import os

# Load your data
masculinity_df = pd.read_csv('masculinity_survey.csv')

# Grab the first 20 rows of the entire dataset
df_head_20 = masculinity_df.head(20)

# Initialize variables for column scrolling
start_col = 0
window_size = 6
step = 3
# Calculate the maximum starting column index
max_col = len(masculinity_df.columns) - window_size 

def print_current_view():
    # Clear the terminal for a clean UI
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Enter 's' for next 3 columns | 'w' for previous 3 columns | 'q' to quit")
    print("-" * 80)
    # Use iloc to slice all rows (:), but only 6 columns at a time
    print(df_head_20.iloc[:, start_col : start_col + window_size])
    print("-" * 80)

# Print the initial view
print_current_view()

# Listen for user input
while True:
    # Wait for the user to type a key and hit Enter
    user_input = input("Command (w/s/q): ").strip().lower()
    
    if user_input == 's':
        # Move forward by 3 columns, capped at max_col
        start_col = min(start_col + step, max_col)
        print_current_view()
        
    elif user_input == 'w':
        # Move backward by 3 columns, floored at 0
        start_col = max(start_col - step, 0)
        print_current_view()
        
    elif user_input == 'q':
        print("Exiting viewer.")
        break