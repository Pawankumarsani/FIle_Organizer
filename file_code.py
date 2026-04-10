import os

base_path= r"C:\Users\admin\abc"

files = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path,f))]

filetypes=set([os.path.splitext(file)[1].lower().strip('.') for file in files if  '.' in file ])

for filetype in filetypes:
    folder_path=os.path.join(base_path,filetype.upper()) 
    os.makedirs(folder_path,exist_ok=True)
    
    for file in files:
        ext=os.path.splitext(file)[1].lower().strip('.')
        
        if ext==filetype:
            
            src=os.path.join(base_path,file)
            dst=os.path.join(folder_path,file)
            
            if not os.path.exists(dst):
                os.rename(src,dst)
            else:
                print(f'skipped(already exists):{file}')
                
    print("file succesfully organised")    