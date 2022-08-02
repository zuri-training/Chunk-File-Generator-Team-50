import os
import random
from zipfile import ZipFile

def main():
    number_of_lines = 200000  # lines
    
    #create a new directory to store split files
    newpath = os.path.join('compress') 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
     #if the directory already exists, create a new folder with random numbers in the name
    else:
        newpath = os.path.join(f'compress{random.randint(1,1000000)}') 
        os.makedirs(newpath)
        
    #create the chunk files and write to it
    def write_chunk(part, lines):
            with open(os.path.join(newpath, f"data_part_{part}.csv"), 'w') as f_out:
                #write the header
                f_out.write(header)
                #write the remainder of the lines
                f_out.writelines(lines)

#open the file to be split in read mode
    with open('csv_data1.csv', 'r') as f:
        count = 0
        header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % number_of_lines == 0:
                write_chunk(count // number_of_lines, lines)
                lines = []
        # write remainder
        if len(lines) > 0:
            write_chunk((count // number_of_lines) + 1, lines)

#create a function to zip the split files
    #get the file paths of files to be zipped
    def get_all_file_paths(directory):
        file_paths = []
        
        for root, directories, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_paths.append(file_path)
        return file_paths
    
    def compress():
        #path to folder which needs to be zipped
        directory = newpath
        
        #call the function to get all file paths
        file_paths = get_all_file_paths(directory)
        
        #printing the list of all files to be zipped
        print('Following files will be zipped:')
        for file_name in file_paths:
            print(file_name)
            
            #write to a new file as zip
        with ZipFile(os.path.join(newpath, 'my_csv_files.zip'),'w') as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(file)
                #delete each file after it has been written to the zip archive
                os.remove(file)
                
        print('All files zipped successfully!')
    compress()
if __name__ == '__main__':
    main()
