import time
from tracemalloc import start 
import simpleaudio as sa 
import random 

samp1 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
samp2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")
samp3 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/CHEF_snare_07_v2.wav")

Playbackloop = True 
timeStep = float(input("How much time should there be between the steps? ")) 

startTime = time.time()
progress = 0 

gridTotal1 = int(input("How many steps should there be in the grid? "))

numNotes1 = 4
offset1 = 1

numNotes2 = 4
offset2 = 2

numNotes3 = 5
offset3 = 1

gridValue1 = gridTotal1//numNotes1
gridValue2 = gridTotal1//numNotes2
gridValue3 = gridTotal1//numNotes3

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

def make_offset_list(gridTotal, gridList,offset):
    for i in gridList: 
        gridList[i] = gridList[i] + offset
        if gridList[i] > gridTotal1:  
            gridList[i] = gridList[i] - gridTotal


gridList1 = make_list_values(gridValue1,numNotes1)
make_grid_list(gridTotal1, numNotes1, gridValue1,gridList1)

gridList2 = make_list_values(gridValue2,numNotes2)
make_grid_list(gridTotal1, numNotes2, gridValue2,gridList2)

gridList3 = make_list_values(gridValue3,numNotes3)
make_grid_list(gridTotal1, numNotes3, gridValue3,gridList3)

print(gridList1)
print(gridList2)
print(gridList3)


print(progress)

while Playbackloop: 
    timeNow = time.time() - startTime
    if timeNow >= timeStep: 
        progress = progress + 1 
        startTime = time.time()
        timeNow = time.time()
        print(progress)
        if progress >= gridTotal1: 
            progress = 0 
            print(progress)

print(gridList1)

