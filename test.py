import pandas as pd


def get_top_5_data(csv_file, column_name, min_value, max_value, other_column_min_value):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Filter the DataFrame based on the conditions for the "dance" column and the other specified column
    filtered_df = df[(df['dnce'] >= min_value) &
                     (df['dnce'] <= max_value) &
                     (df['nrgy'] > other_column_min_value)]

    # Sort the filtered DataFrame by the specified column in descending order
    # sorted_df = filtered_df.sort_values(by=column_name, ascending=False)
    sorted_df = filtered_df

    # Get the top 5 rows
    # top_5_data = sorted_df.head(5)
    top_5_data = sorted_df

    return top_5_data


# Example usage
csv_file = 'songs.csv'  # Specify your CSV file path
# Specify the name of the column you want to get the largest values from
column_name = 'Column_Name'
min_value = 30  # Specify the minimum value for the dance column
max_value = 40  # Specify the maximum value for the dance column
other_column_min_value = 80  # Specify the minimum value for the other column

top_5_data = get_top_5_data(csv_file, column_name,
                            min_value, max_value, other_column_min_value)
print("Top 5 data:")
# Use to_string() method to print DataFrame without index
print(top_5_data.to_string(index=False))
