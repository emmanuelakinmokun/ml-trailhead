'''
Lab Notebook CLI” — a command-line Python program (no web/UI needed) that manages a small dataset via lists/dicts and reads/writes to a CSV file. - Spec: a program that lets a user (via terminal input) add,
view, search, and delete entries in a simple dataset — frame it as a “sample tracker” (e.g., tracking lab samples: ID, date, sample type, result) since it’s familiar territory from microbiology.
- Requirements: at least 4 functions, one dictionary-of-dictionaries or list-of-dictionaries data structure, CSV read/write persistence, basic error handling (e.g., invalid input doesn’t crash the program).
- Stretch goal: add simple statistics (count entries by type, average of a numeric field) using only built-in Python (no pandas yet).

'''


import csv
import os

filename = 'Micro_lab_sample_record.csv'

Sample_1 = {'ID': 'S001', 'Date':'2026-08-01','Organism_Type': 'Bacteria', 'Probable_organism':'Escherichia coli', 'Nutrient_media': 'Eosin-Methylene Blue Agar', 'CFU_count': 1500, 'Source': 'Niger River'}
Sample_2 = {'ID': 'S002', 'Date':'2026-03-23','Organism_Type': 'Fungi', 'Probable_organism':'Nil', 'Nutrient_media': 'Nutrient Agar','CFU_count': 45, 'Source': 'General Hospital Ward Air Sample'}
Sample_3 = {'ID': 'S003', 'Date':'2026-11-08','Organism_Type': 'Bacteria', 'Probable_organism':'Proteus vulgaris', 'Nutrient_media': 'MacConkeyAgar', 'CFU_count': 176, 'Source': 'Asa River'}
Sample_4 = {'ID': 'S004', 'Date':'2026-04-10', 'Organism_Type': 'Bacteria','Probable_organism':'Nil', 'Nutrient_media': 'Nutrient Agar', 'CFU_count': 345,  'Source': "MacDonald's waste water"}

Field_names = ['ID', 'Date', 'Organism_Type', 'Probable_organism', 'Nutrient_media', 'CFU_count','Source']


def initialize(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
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
    if not samples:
        print('\nNo samples recorded')
        return
    for index, row in enumerate(samples, start=1):
        print(f"[{index}] ID: {row['ID']} | Date: {row['Date']} | Type: {row['Organism_Type']} | Organism: {row['Probable_organism']} | Media: {row['Nutrient_media']} | CFU: {row['CFU_count']} | Source: {row['Source']}")

def add_sample(filename, samples):
    sample_id = input("Enter Sample ID: ").strip()
    date = input("Enter Date (YYYY-MM-DD): ").strip()
    organism_type = input("Enter Microorganism type: ").strip()
    organism = input("Enter Probable Organism: ").strip()
    media = input("Enter Nutrient Media: ").strip()
    cfu_ml = input('Enter Colony Count: ').strip()
    while not cfu_ml.isdigit():
        print("Invalid input. Colony Count must be a positive integer.")
        cfu_ml = input("Enter Colony Count: ").strip()
    source = input("Enter Source: ").strip()


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
    print("\nSample added successfully.")


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
        if sample_number < 0 or sample_number >= len(samples):
            raise IndexError
        delete_sample = samples.pop(sample_number)

        with open(filename, mode = 'w', newline='', encoding='utf-8') as file: 
            writer = csv.DictWriter(file, fieldnames = Field_names)
            writer.writeheader()
            writer.writerows(samples)

        print(f"\nSample {delete_sample['ID']} deleted successfully.")

    except (ValueError, IndexError):
        print('\nInvalid selection. Please enter a valid sample number')
              

def statistics(samples):
    cfu_counts = [int(sample['CFU_count']) for sample in samples if str(sample['CFU_count']).isdigit()]
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


def main():
    initialize(filename)
    samples = load_sample(filename)
    
    while True:
        print("\n" + "=" * 40)
        print('MICROBIOLOGY LAB BOOK CLI')
        print("=" * 40)
        print("1. View All Samples")
        print("2. Add New Sample")
        print("3. Search Sample")
        print("4. Delete Sample")
        print("5. View Statistics")
        print("6. Exit")
        print("=" * 40)

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            view_samples(samples)
        elif choice == '2':
            add_sample(filename, samples)
        elif choice == '3':
            search_sample(samples)
        elif choice == '4':
            delete_sample(filename, samples)
        elif choice == '5':
            statistics(samples)
        elif choice == '6':
            if confirm_exit():
                print("\nExiting Lab Notebook. Goodbye!")
                break
        else:
            print("\nInvalid selection. Please enter a number from 1 to 6.")

if __name__ == '__main__':
    main()    
    



