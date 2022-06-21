
import os
from unicodedata import name;
import cv2 as cv;
#step1: negitive file
def negtivefile_generator(file_name,negitive_file_name):
    file_name_arr= os.listdir(file_name) 
    with open(negitive_file_name,'w+') as f: 
        for path in file_name_arr:
            f.write('cats/'+path+'\n')
def rename_file(filename):
    file_path_arr=os.listdir(filename) 
    i=1;
    for path in file_path_arr:
         with open(path,'w+') as f: 
            img=cv.imread('cats/'+path)
            cv.imwrite('img'+str(i)+'.jpg',img);
            i=i+1;
            
                
if __name__=="__main__":
    rename_file('cats') 
           #negtivefile_generator('cats','D:/Work/Code/Python/OpenCV/cats/negetive.txt')
           