import csv
import os.path


#Read csv
def read_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found {file_path}")
    with open(file_path) as file:
        return list(csv.DictReader(file))

#write csv
def write_csv(file_path,data,fieldnames):

    with open(file_path) as file:
        writer =csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)

