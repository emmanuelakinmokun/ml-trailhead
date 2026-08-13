# Microbiology Lab Notebook CLI

A command-line sample tracking system built in Python for recording, managing, and analyzing microbiological lab specimens. Designed for light weight, zero-dependency persistence using standard CSV files.

---

## Features

- ** Sample Inventory Management**: View all logged samples in a clean, human-readable index layout.
- ** Data Entry Validation**: Add new samples with built-in validation (e.g., enforcing positive integer inputs for Colony Forming Unit counts).
- ** Identifier Search**: Search records dynamically by Sample ID (`S001`, `S002`, etc.) with case-insensitive matching.
- ** Safe Deletion**: Delete records by their menu selection index with automatic synchronization to the underlying CSV file.
- ** Real-time Statistics**: Instantly view metrics across your data set:
  - Total records count
  - Average, minimum, and maximum CFU/mL
  - Isolated organism breakdown (Bacteria vs. Fungi)
- ** CSV Persistence**: Automatically initializes default data and saves all operations directly to `Micro_lab_sample_record.csv`.

---

