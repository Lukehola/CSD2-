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

numNotes2 = 9
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
    if len(gridList) != 0: 
        if gridList[checklistitem] == i: 
            Check = True 
        else: 
            Check = False
    else: 
        checklistitem = 0 

check_list(gridList1, 0)
check_list(gridList2, 0)
check_list(gridList3, 0)
print(Check)

combo_list12 = [] 
combo_list13 = [] 
combo_list23 = [] 

def make_double_samples(list1,list2,list3): 
    global combo_list12
    global combo_list13
    global combo_list23
    
    if len(list1) >= len(list2): 
        for i in list1: 
            if i in list2:
                combo_list12.append(i) 
    if len(list2) > len(list1): 
        for i in list2: 
            if i in list1:
                combo_list12.append(i) 

    if len(list1) >= len(list3): 
        for x in list1: 
            if x in list3: 
                combo_list13.append(x)
    if len(list3) > len(list1): 
        for x in list3: 
            if x in list1: 
                combo_list13.append(x)

    if len(list2) >= len(list3): 
        for x in list2: 
            if x in list3: 
                combo_list23.append(x)
    if len(list3) > len(list2): 
        for x in list3: 
            if x in list2: 
                combo_list23.append(x)
            
make_double_samples(gridList1,gridList2,gridList3)

print("Combo Lists:")
print(combo_list12)
print(combo_list13)
print(combo_list23)


def create_dict_steps(gridTotal, timestamps, samp): 
    global checklistitem
    global Check
    # event_dict = {}
    event_dict_stamps = {}
    event_list = [] 
    for i in range(gridTotal):
        check_list(gridList1, i)
        if Check == True : 
            event_dict_stamps = {"Timestamp": timestamps[checklistitem],"Instrument":samp}
            checklistitem = checklistitem + 1 
            event_list.append(event_dict_stamps.copy())
        else: 
            Check = False
    return event_list

dict1 = create_dict_steps(gridTotal1, gridList1,samp1)
dict2 = create_dict_steps(gridTotal1, gridList2,samp2)
dict3 = create_dict_steps(gridTotal1, gridList3,samp3)

print(dict1)
print(dict2)
print(dict3)


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

print(gridList1)
