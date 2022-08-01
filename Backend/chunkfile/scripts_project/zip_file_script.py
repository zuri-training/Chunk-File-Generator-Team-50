from zipfile import ZipFile
import os

#get the file paths of files to be zipped
def get_all_file_paths(directory):
    file_paths = []
    
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)
    return file_paths

def main():
    #path to folder which needs to be zipped
    directory = '.\compress'
    
    #call the function to get all file paths
    file_paths = get_all_file_paths(directory)
    
    #printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
        
    with ZipFile('my_python_files.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
            
    
    print('All files zipped successfully!')

if __name__ == "__main__":
    main()