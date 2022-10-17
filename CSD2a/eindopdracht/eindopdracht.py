import time
from tracemalloc import start 
import simpleaudio as sa 
import random 

samp1 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
samp2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")
samp3 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/CHEF_snare_07_v2.wav")

gridTotal1 = 14
numNotes1 = 3
offset1 = 1

gridValue1 = gridTotal1//numNotes1
gridList1Xtra = 0 

def make_list_values(gridValue, numNotes): 
    gridList = [] 
    for i in range(numNotes): 
        gridList.append(gridValue)
        if i != 0:
            gridList[i] = gridList[i] + gridList[i-1]
    return gridList

def make_grid_list(gridTotal,numNotes,gridValue,gridList): 
    if gridValue * numNotes != gridTotal: 
        for i in range(gridTotal - gridValue*numNotes): 
            gridList[i]= gridList[i] + 1 

def make_offset_list(gridList):
    global gridTotal1
    for i in gridList: 
        gridList[i] = gridList[i] + 1 
        if gridList[i] > gridTotal1:  
            gridList[i] = 0


gridList1 = make_list_values(gridValue1,numNotes1)
make_grid_list(gridTotal1, numNotes1, gridValue1,gridList1)
    
print(gridList1)
