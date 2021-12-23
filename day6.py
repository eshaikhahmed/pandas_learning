
import pandas as pd 

# read your big file into df
df = pd.read_csv("student.csv");

# sort_values(): sort column 
sort_df = df.sort_values(by="student_name",
                         ascending=False,
                         kind="mergesort");

# save file
sort_df.to_csv("sort.csv", index=False);
