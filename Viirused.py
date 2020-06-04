import os 
if __name__ == "__main__":
    print('virus-chan activated')
    for (root,dirs,files) in os.walk('.', topdown=True):
        for victim in files:
            if(victim[-3:] == '.py'):
                print(root)
                print(victim)
