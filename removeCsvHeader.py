#!python3
#removeCsvHeader.py--Remove the header from all CSV files in the current
import csv,os
os.chdir('d:\\python\\study')
os.makedirs('headerRemoved',exist_ok=True)
#loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue #skip non-csv file
    print('Removing header from ' + csvFilename +'...')
    #TODO: read the csv file in (skipping first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    csvReaderRows = csv.reader(csvFileObj)
    for row in csvReaderRows:
        if csvReaderRows.line_num == 1:
            continue #skip first row
        csvRows.append(row)
    csvFileObj.close()
    #TODO: write out the CSV file
    csvFileObj = open(os.path.join('headerRemoved',csvFilename),'w',newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
print('Done')
