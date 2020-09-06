import numpy as np
import os
import glob

#Naming Convention
#Use full English words for variables and functions.
#Seperate words by a underscore
#Use common sense to shorten if the word is too long
#Class names are also words seperated by underscores, however first letter must be capitalized.

class Data_Manager:
    def __init__(self, dir_paths,prefix_list):
        ###Mandatory inputs
        self.dir_paths = dir_paths #This is a list of text with folder names
        self.prefix_list = prefix_list #This is a list of text with prefix

        self.descriptions = []
        
        for i in range(len(self.dir_paths)):
            os.chdir(self.dir_paths[i])
            for file in glob.glob('*.txt'):
                try :
                    opened_file = open(file, encoding ="utf8").read() 
                    self.descriptions.append([self.prefix_list[i]+file,opened_file]) 
                except:
                    print('Something went wrong with file ',file,'Therefore, skipping that file.')    
        
#####################################
#This function loads data from text files in a folder
    def read_from_folders():
        
        #return 1 if successfull 0 if there is a problem
        
#This function loads data from a DB
    def read_from_db():
    
        return 1 or 0
    
#This function scraope data from online artile and load to the data manager
    def read_from_online_article():
        return 1 or 0
        

    def get_text(self): 
        return np.array(self.descriptions)
    
    
#This function reads data in the datammanager, then rokenize and return a 2D array in the following format
#[[dummy, token 1, token 2, token 3, ], [article name, token 1 freq, token 2 freq, ....],[],.....]
   def get_tokens():
        
    return the tokenized array
        
        