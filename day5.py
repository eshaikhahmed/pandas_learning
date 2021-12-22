import pandas as pd 

# read your big file into df
df = pd.read_csv("student.csv");

# yahoo, yes head() : This function does the magic 
# select top 5 rows
top_5 = df.head(5);

# save those top 5 rows into new file named as top_5.csv
top_5.to_csv("top_5.csv", index=False);
