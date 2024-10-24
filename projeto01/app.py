import os
from tqdm import tqdm
import time 

directory = os.listdir ('D:\Documentos Usuário\Documents\GitHub')
for item in tqdm (directory, colour= 'blue'):
    print(item)
    time.sleep(1)