import time
from tracemalloc import start 
import simpleaudio as sa 
import random 

samp1 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
samp2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")
samp3 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/CHEF_snare_07_v2.wav")

Check = True 
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

#floor division

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

#checks if floor division isnt accurate, adds remainder to list items 

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

#I need to compare the different lists, and when they fall on the same note, combine the two samples in one dict index 
#Also I need to make a new dictionary with all the events, of course 

checklistitem = 0 

def check_list(gridList, i):
    global checklistitem
    global Check
    if gridList[checklistitem] == i: 
        Check = True 
    else: 
        Check = False

check_list(gridList1, 0)
print(Check)


def create_dict_steps(gridTotal, timestamps): 
    global checklistitem
    global Check
    # event_dict = {}
    event_dict_stamps = {}
    event_list = [] 
    for i in range(gridTotal + 1):
        check_list(gridList1, i)
        if Check == True : 
            event_dict_stamps = {"Timestamp": timestamps[checklistitem],"Instrument":samp1}
            checklistitem = checklistitem + 1 
            event_list.append(event_dict_stamps.copy())
        else: 
            Check = False
    return event_list

dict1 = create_dict_steps(gridTotal1, gridList1)
print(dict1)

print(progress)

while Playbackloop: 
    timeNow = time.time() - startTime

    #defining when progress needs to be increased 
    if timeNow >= timeStep: 
        progress = progress + 1 
        startTime = time.time()
        timeNow = time.time()
        print(progress)
        if progress >= gridTotal1: 
            progress = 0 
            print(progress)
            make_offset_list(gridTotal1, gridList1, offset1)
            print(gridList1)

print(gridList1)
