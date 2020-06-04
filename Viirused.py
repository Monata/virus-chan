import os 
if __name__ == "__main__":
    print('virus-chan activated')
    for (root,dirs,files) in os.walk('.', topdown=True):
        print(root)
        print(dirs)
        print(files)
        print('--------------------------------')