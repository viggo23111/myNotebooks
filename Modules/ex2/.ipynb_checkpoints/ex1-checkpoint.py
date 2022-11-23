import csv
import platform
import argparse 
def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))
                
def write_list_to_file(output_file, *strings):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        
        output_writer.writerow(['header'])
        
        for string in strings:
            output_writer.writerow([string])
            
def read_csv():
    parser = argparse.ArgumentParser(description='First write the path to read from, then it is optional to enter a file name that will get the data from the first file.')
    parser.add_argument('path', help='The path to process')
    parser.add_argument('--file', help='file to write to')
    args = parser.parse_args()
    with open(args.path) as f:
        content=f.readlines()
    lst = [line.strip() for line in content]
   
    if (args.file == None):
        print(lst)
    else:
        with open(args.file, 'w') as output_file:
            output_writer = csv.writer(output_file)
            for string in lst:
                output_writer.writerow([string])       
    
            
if __name__=='__main__':
  #  print_file_content('employees.csv')
   # write_list_to_file('test.csv','test','test2','test3')
    read_csv()
    