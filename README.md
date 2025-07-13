# ECI_India
Election Commission of India - PDF to CSV


Using : 
https://aistudio.google.com/

Prompt : 
You are an expert data entry specialist. Your task is to extract all election result data from the attached PDF file and format it perfectly into a single, complete CSV format.

Follow these rules precisely:
1.  The CSV columns must be exactly: `Constituency_No`, `Constituency_Name`, `Constituency_Type`, `Total_Electors`, `Candidate_S_No`, `Candidate_Name`, `Gender`, `Age`, `Category`, `Party`, `Symbol`, `General_Votes`, `Postal_Votes`, `Total_Votes`, `Percentage_of_Valid_Votes`, `Percentage_of_Total_Electors`, `Turnout_General`, `Turnout_Postal`, `Turnout_Total`, `Turnout_Percentage`.
2.  Go through the entire PDF and extract the data for every candidate in every constituency.
3.  **TURN OUT DATA:** For each constituency, find the "TURN OUT" row and its corresponding totals. Add this data to the new columns (`Turnout_General`, `Turnout_Postal`, `Turnout_Total`, `Turnout_Percentage`) for EVERY candidate in that same constituency.
4.  The constituency information (No, Name, etc.) and the Turnout data will be the same for all candidates in that constituency and must be repeated on each row.
5.  Combine multi-line candidate names into a single field (e.g., "DR. HEENA VIJAYKUMAR GAVIT").
6.  Treat "NOTA" as a candidate. If data for a field (like Gender or Age) is missing, leave it blank.
7.  If Candidate_Name = NOTA, keep the "Symbol" column empty.
8.  Handle messy or misaligned rows by correctly matching the data to the right column based on the table's overall structure.
9.  Do not add any commentary or explanations. Only output the raw CSV data, starting with the header row.

CSV files : 
Delhi 2025 - 10-Detailed_Results_1744913508.pdf
Maharashtra 2024 - 10-Detailed_Results_1744893339.pdf

Output CSV needs to be cleaned (use cleaned_csv.py)
