import pandas as pd  
import re  
import sys  
from datetime import date  
import shutil  

centre="12345"  


#dataframe  
df=pd.read_csv('pupils.csv')  
df['Surname','Forename']=df['Full Name'].str.split(', ')  
df=df.drop(['Full Name','Year Group','Reg Group'], axis=1)  
pupils=df.values.tolist()  
print(df)  

#set up folder to store zip files  
today=date.today()  
folder=today.strftime("%Y%m%d")  
os.mkdir(f"./{folder}")  

for pupil in pupils:  
    #pupil[0]=examnumber  
    #pupil[1]=controlassessfolder  
    #pupil[2]=name as [surname,firstname]  
    #filename: CENTRENUMBER_CANDIDATE NUMBER_SURNAME_FORENAME  
    #remove apostrophes   
    surname=re.sub("[^A-Za-z- ]",'',"".join(pupil[2][0]))  
    firstname=re.sub("[^A-Za-z- ]",'',"".join(pupil[2][1]))  
    filename=(f"{centre}_{pupil[0]}_{surname}_{firstname}.7z").upper()  

    try:  
        os.rename(f".\{pupil[1]}\completedcoding.7z",f".\{pupil[1]}\{filename}")  
    except:  
        print(f"Error renaming .\{pupil[1]} to {filename}")  
    else:  
        print(f"{pupil[1]} succeeded")  

    #copy file to folder store  
    try:  
        shutil.copyfile(f".\{pupil[1]}\{filename}",f".\{folder}\{filename}")  
    except:  
        print(f"Error copying {filename} to .\{folder}")  
    else:  
        print(f"Copied {filename} to .\{folder}")      
