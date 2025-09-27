# BLAST Database Extraction & Conversion

## Steps Followed

### 1. Downloaded BLAST Dataset
I downloaded the required BLAST database files from [NCBI FTP](https://ftp.ncbi.nlm.nih.gov/blast/db/).

### 2. Installed BLAST+
Installed the **BLAST+** toolkit to interact with the downloaded databases.

### 3. Extracted the Dataset
Unpacked the `.tar.gz` files to get BLAST binary database files (`.nsq`, `.nin`, `.nhr` etc.).

### 4. Converted to FASTA & SQLite
Used BLAST+ utilities to generate:
- A **FASTA file** for sequence access.
- A **SQLite3 file** for structured querying.

### 5. Wrote Python Script to Explore Database
Created a Python script that:
- Connects to the SQLite3 database.
- Retrieves the available **table names**.

### 6. Exported Tables to CSV
Another Python script was written that:
- Reads a given table from SQLite.
- Converts it into a **CSV file** for analysis.

---

## Output
- FASTA file ✅  
- SQLite3 database ✅  
- CSV files for each table ✅
