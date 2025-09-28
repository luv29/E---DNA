import tarfile

file_path = "taxdb.tar.gz"

with tarfile.open(file_path, "r:gz") as tar:
    tar.extractall()

print("taxdb extraction complete!")
