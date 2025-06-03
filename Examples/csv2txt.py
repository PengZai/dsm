import csv

# Input and output file paths
data_dir = "/root/dsm/Examples/polytunnel/Timestamps"
csv_file = 'easy_bag_zed_left.csv'
txt_file = 'easy_bag_zed_left.txt'

with open(data_dir+"/"+csv_file, 'r') as infile, open(data_dir+"/"+txt_file, 'w') as outfile:
    reader = csv.reader(infile)
    next(reader)  # Skip header
    for row in reader:
        outfile.write(row[0] + '\n')
