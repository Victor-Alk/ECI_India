import pandas as pd

# Load raw file
df = pd.read_csv('code.csv')

# Step 1: Fix column misalignment for NOTA rows
nota_mask = df['Candidate_Name'].astype(str).str.upper().str.strip() == 'NOTA'
cols_to_shift = df.columns[df.columns.get_loc('Symbol'):]  # From 'Symbol' onward
df.loc[nota_mask, cols_to_shift[::-1]] = df.loc[nota_mask, cols_to_shift].shift(periods=1, axis=1)
df.loc[nota_mask, 'Symbol'] = ''

# Step 2: Add fixed metadata columns
df['State_Name'] = 'Delhi'
df['Year'] = 2025
df['Assembly_No'] = 12
df['Election_Type'] = 'State Assembly Election (AE)'
df['Month'] = 2
df['Poll_No'] = 0
df['DelimID'] = 4

# Step 3: Convert vote and turnout columns to integer
int_cols = ['General_Votes', 'Postal_Votes', 'Total_Votes', 'Turnout_General', 'Turnout_Postal', 'Turnout_Total']
for col in int_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Step 4: Convert Age to integer, but leave empty for NOTA
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # convert to float
df.loc[nota_mask, 'Age'] = pd.NA  # blank for NOTA
df['Age'] = df['Age'].astype('Int64')  # nullable integer

# Step 5: Rename 'Category' to 'Candidate_Type'
df = df.rename(columns={'Category': 'Candidate_Type'})

# Save cleaned file
df.to_csv('code_updated.csv', index=False)
