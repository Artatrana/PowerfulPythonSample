import pandas as pd
import glob

# Check for alphanumeric character by looking ASCII codes between 65(A) and 122(z)

def is_alphabatic(string):
    return all(65<=ord(character) <= 122 for character in string )

all_files = glob.glob(storage_location + 'cleaned/treatments/*.csv')

df_list =[]

for filename in all_files:
    temp_df= pd.read_csv(filename)
    df_list.append(temp_df)

df = pd.concat(df_list, ignore_index=True)

df = df[len(df['PatientName']) > 0 and (is_alphabatic(df['PatientName']))]
df.to_parquet(storage_location+ 'curated/treatment.parquet')

