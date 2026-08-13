'''
Lab Notebook CLI” — a command-line Python program (no web/UI needed) that manages a small dataset via lists/dicts and reads/writes to a CSV file. - Spec: a program that lets a user (via terminal input) add,
view, search, and delete entries in a simple dataset — frame it as a “sample tracker” (e.g., tracking lab samples: ID, date, sample type, result) since it’s familiar territory from microbiology.
- Requirements: at least 4 functions, one dictionary-of-dictionaries or list-of-dictionaries data structure, CSV read/write persistence, basic error handling (e.g., invalid input doesn’t crash the program).
- Stretch goal: add simple statistics (count entries by type, average of a numeric field) using only built-in Python (no pandas yet).

'''


import csv

Sample_1 = {'ID': 'S001', 'Date':'2026-08-01','Organism_Type': 'Bacteria', 'Probable_organism':'Escherichia coli', 'Nutrient_media': 'Eosin-Methylene Blue Agar', 'CFU_count': 1500, 'Source': 'Niger River'}
Sample_2 = {'ID': 'S002', 'Date':'2026-03-23','Organism_Type': 'Fungi', 'Probable_organism':'Nil', 'Nutrient_media': 'Nutrient Agar','CFU_count': 45, 'Source': 'General Hospital Ward Air Sample'}
Sample_3 = {'ID': 'S003', 'Date':'2026-11-08','Organism_Type': 'Bacteria', 'Probable_organism':'Proteus vulgaris', 'Nutrient_media': 'MacConkeyAgar', 'CFU_count': 176, 'Source': 'Asa River'}
Sample_4 = {'ID': 'S004', 'Date':'2026-04-10', 'Organism_Type': 'Bacteria','Probable_organism':'Nil', 'Nutrient_media': 'Nutrient Agar', 'CFU_count': 345,  'Source': "MacDonald's waste water"}

Field_names = ['ID', 'Date', 'Organism_Type', 'Probable_organism', 'Nutrient_media', 'CFU_count','Source']

with open('Micro_Lab_Notebook.csv', mode = 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=Field_names)
    writer.writeheader()
    writer.writerows([Sample_1, Sample_2, Sample_3, Sample_4])


def load_sample(filename):
    samples = []
    with open(filename, mode = 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            samples.append(row)
    return samples

def view_samples(samples):
    for row in samples:
        print(row)

def add_sample(filename, samples):
    sample_id = input("Enter Sample ID: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    organism_type = input("Enter Microorganism type: ")
    organism = input("Enter Probable Organism: ")
    media = input("Enter Nutrient Media: ")
    cfu_ml = input('Enter Colony Count: ')
    source = input("Enter Source: ")

    new_sample = {
        'ID' : sample_id,
        'Date' : date,
        'Organism_Type' : organism_type,
        'Probable_organism': organism,
        'Nutrient_media': media,
        'CFU_count':cfu_ml,
        'Source': source
    }

    with open(filename, mode = 'a', newline='', encoding='utf-8') as file: 
        writer = csv.DictWriter(file, fieldnames=Field_names)
        writer.writerow(new_sample)

    samples.append(new_sample)


def search_sample(samples):
# Searching by sample name
    search_input = input('Search for sample name (for example: S001): ').strip().lower()
    search_result = [sample for sample in samples if sample.get('ID', '').lower() == search_input]

    if search_result:
        print("\nFound matching sample(s):")
        for sample in search_result:
            print(sample)

    else:
        print("\nSample doesn't exist.")
   

def delete_sample(samples, filename):
    sample_number = input('Input sample number to be deleted (for example S001 is 1):')
    try:
        sample_number = int(sample_number) - 1
        delete_sample = samples.pop(sample_number)

        with open(filename, mode = 'w', newline='', encoding='utf-8') as file: 
            writer = csv.DictWriter(file, fieldnames = Field_names)
            writer.writeheader()
            writer.writerows(samples)

        print(f"\nSample {delete_sample['ID']} deleted successfully.")

    except (ValueError, IndexError):
        print('\nInvalid selection. Please enter a valid sample number')
              
# Statistics, Exit.. main function....

def statistics(samples):
    cfu_counts = [int(sample['CFU_count']) for sample in samples if sample['CFU_count'].isdigit()]
    if not cfu_counts:
        print("\nNo numeric CFU data available to calculate statistics.")
        return

    average_cfu = sum(cfu_counts)/len(cfu_counts)

    org_types = [sample.get('Organism_Type', '').title() for sample in samples]
    bacteria_count = org_types.count('Bacteria')
    fungi_count = org_types.count('Fungi')


    print("\n--- Lab Notebook Statistics ---")
    print(f"Total Samples Recorded: {len(samples)}")
    print(f"Average CFU Count: {average_cfu:.2f} CFU/mL")
    print(f"Minimum CFU Count: {min(cfu_counts)}")
    print(f"Maximum CFU Count: {max(cfu_counts)}")
    print(f'\nBacteria Isolated: {bacteria_count}')
    print(f'Fungi Isolated: {fungi_count}')


def confirm_exit():
    exit_request = input("Are you sure you want to exit? (yes/no): ").strip().lower()
    return exit_request in ['yes', 'y', 'exit']





    



