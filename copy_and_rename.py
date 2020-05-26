# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:43:45 2020

@author: fym2020
"""

#操作文件夹，将每个字文件夹中的某个特定文件拷贝出来，并且使用相关文件夹名称重命名
rootdir = 'd:/need/'

def list_and_copy(rootdir):
    import os
    import shutil
    list_file = os.listdir(rootdir)
    
    for i in range(0,len(list_file)):
        path = os.path.join(rootdir, list_file[i])
      
        if os.path.isdir(path):            
            list_sub = os.listdir(path)
            for i in range(0, len(list_sub)):
                if list_sub[i] == 'photo_org.jpg':
                    shutil.copyfile(path+'/'+list_sub[i], path+'_'+list_sub[i])
                elif list_sub[i] == 'share.jpg':
                    shutil.copyfile(path+'/'+list_sub[i], path+'_'+list_sub[i])
                
    #print(list_file)
    
 
if __name__ == '__main__':
    list_and_copy(rootdir)