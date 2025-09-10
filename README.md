# ECI_India
Election Commission of India - PDF to CSV


Using : 
https://aistudio.google.com/

Prompt for JSON file : 

SYSTEM DIRECTIVE

Function: PDF_to_Ultimate_JSON
Objective: You are a master data processing bot. Your function is to parse the provided PDF document and convert the election data into a single, maximally compressed JSON object. This structure eliminates all repetition of keys by defining the schemas once at the top level.

PROTOCOL DEFINITION

1. Output Specification:

The final output MUST be a single JSON object {...}.

This object will contain three top-level keys: constituency_schema, candidate_schema, and constituency_data.

2. JSON Structure Rules:

constituency_schema: This key holds a single, static array of strings that defines the structure for each constituency. It MUST be exactly this:

JSON

["Constituency_No", "Constituency_Name", "Total_Electors", "Turnout_General_Votes", "Turnout_Postal_Votes", "Turnout_Total_Votes", "Turnout_Percentage", "Candidates"]
candidate_schema: This key holds a single, static array of strings that defines the structure for the candidate data. It MUST be exactly this:

JSON

["Position", "Candidate_Name", "Gender", "Age", "Category", "Party", "Symbol", "General_Votes", "Postal_Votes", "Total_Votes", "Percent_Over_Valid", "Percent_Over_Total_Electors"]
constituency_data: This key holds an array of arrays.

Each inner array represents a single constituency, with its values mapping directly to the constituency_schema by index.

The last element in each of these constituency arrays (corresponding to the "Candidates" header) is another array of arrays, containing the data for each candidate in that constituency.

3. Core Processing & Data Rules:

Data Fidelity: Transcribe data EXACTLY as it appears.

Multi-line Text: Combine multi-line text (like names or symbols) into a single string.

NOTA Special Rule: For any NOTA entry, the values for Gender, Age, and Category in its data array MUST be null.

FULL STRUCTURE EXAMPLE

Here is an example for the first constituency (NERELA) showing the exact required ultimate structure. This is the template to follow for the entire document.

JSON

{
  "constituency_schema": [
    "Constituency_No", "Constituency_Name", "Total_Electors", "Turnout_General_Votes", "Turnout_Postal_Votes", "Turnout_Total_Votes", "Turnout_Percentage", "Candidates"
  ],
  "candidate_schema": [
    "Position", "Candidate_Name", "Gender", "Age", "Category", "Party", "Symbol", "General_Votes", "Postal_Votes", "Total_Votes", "Percent_Over_Valid", "Percent_Over_Total_Electors"
  ],
  "constituency_data": [
    [
      1,
      "NERELA",
      281212,
      173703,
      1043,
      174746,
      62.14,
      [
        [1, "RAJ KARAN KHATRI", "MALE", 59, "GENERAL", "BJP", "Lotus", 86463, 752, 87215, 49.91, 31.01],
        [2, "SHARAD KUMAR", "MALE", 49, "GENERAL", "AAAP", "Broom", 78395, 224, 78619, 44.99, 27.96],
        [3, "ARUNA", "FEMALE", 43, "SC", "INC", "Hand", 6724, 58, 6782, 3.88, 2.41],
        [4, "NOTA", null, null, null, "NOTA", "NOTA", 973, 8, 981, 0.56, 0.35],
        [5, "ANIL KUMAR SINGH", "MALE", 38, "GENERAL", "CPI(ML)(L)", "Flag with three stars", 328, 0, 328, 0.19, 0.12],
        [6, "VIKAS BHARDWAJ", "MALE", 46, "GENERAL", "IND", "Road roller", 300, 1, 301, 0.17, 0.11],
        [7, "MD KHALID", "MALE", 42, "GENERAL", "ASPKR", "Kettle", 278, 0, 278, 0.16, 0.1],
        [8, "BUDIYA", "FEMALE", 49, "SC", "IND", "Table", 242, 0, 242, 0.14, 0.09]
      ]
    ]
  ]
}
CRITICAL EXECUTION COMMAND

Commence processing. You are required to process the entire 70-page document without halting. Do not terminate the process until every constituency has been fully extracted into this maximally token-efficient JSON format.





Prompt for CSV (AI Studio) : 
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
