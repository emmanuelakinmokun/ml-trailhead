'''Lab Sample Database - Purpose: turn the SQL you just learned into
muscle memory against data you already know, before Project 0 asks for something bigger
- Spec: take the CSV your Phase 0 “Lab Notebook CLI” produces
(or generate a synthetic version with ~200 rows if you didn’t keep the original),
load it into a local SQLite database with 2 related tables (e.g., samples and
results, linked by a sample ID) instead of one flat table. 
- Deliverables:
write and save 8–10 queries covering: a multi-table JOIN, a GROUP BY with an
aggregate, a subquery, and a window function (e.g., ranking samples by a result value within a group). Save them as a .sql file with a one-line comment
above each explaining what it answers. 
 - Stretch goal: wrap 2–3 of the queries
in a tiny Python script using sqlite3 that prints a formatted report — this
previews the Python+SQL combination you’ll use constantly later.'''

import sqlite3
import pandas as pd

df = pd.read_csv(r"C:\Users\emman\OneDrive\Documents\GitHub\Machine Learning\Phase_0\Micro_lab_sample_record.csv")

conn = sqlite3.connect('my_database.db')

df.to_sql('my_table', conn, if_exists='replace', index=False)

conn.close()

