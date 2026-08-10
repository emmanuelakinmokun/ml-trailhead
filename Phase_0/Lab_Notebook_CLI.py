'''
Lab Notebook CLI” — a command-line Python program (no web/UI
needed) that manages a small dataset via lists/dicts and reads/writes to
a CSV file. - Spec: a program that lets a user (via terminal input) add,
view, search, and delete entries in a simple dataset — frame it as a “sample
tracker” (e.g., tracking lab samples: ID, date, sample type, result) since it’s
familiar territory from microbiology. - Requirements: at least 4 functions, one
dictionary-of-dictionaries or list-of-dictionaries data structure, CSV read/write
persistence, basic error handling (e.g., invalid input doesn’t crash the program).
- Stretch goal: add simple statistics (count entries by type, average of a numeric
field) using only built-in Python (no pandas yet).

'''


import csv

Sample_1 = {'ID': 'S001', 'Date':'2026-08-01', 'Probable_organism':'Escherichia coli', 'Nutrient_media': 'Eosin-Methylene Blue Agar', 'Source': 'Niger River'}
Sample_2 = {'ID': 'S002', 'Date':'2026-03-23', 'Probable_organism':'Nil', 'Nutrient_media': 'Nutrient Agar', 'Source': 'General Hospital Ward Air Sample'}
Sample_3 = {'ID': 'S003', 'Date':'2026-11-08', 'Probable_organism':'Proteus vulgaris', 'Nutrient_media': 'MacConkeyAgar', 'Source': 'Asa River'}
Sample_4 = {'ID': 'S004', 'Date':'2026-04-10', 'Probable_organism':'Nil', 'Nutrient_media': 'Nutrient Agar', 'Source': "MacDonald's waste water"}

Field_names = ['ID', 'Date', 'Probable_organism', 'Nutrient_media', 'Source']

with open('Micro_Lab_Notebook.csv', mode = 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=Field_names)
    writer.writeheader()
    writer.writerows([Sample_1, Sample_2, Sample_3, Sample_4])




