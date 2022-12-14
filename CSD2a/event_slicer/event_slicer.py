
import time
from tracemalloc import start 
import simpleaudio as sa 
import random 

samp1 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
samp2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")
samp3 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/CHEF_snare_07_v2.wav")

samp1_dict = {
    "Name" : "Samp 1", 
    "Instrument" : samp1,
}
samp2_dict = {
    "Name" : "Samp 2", 
    "Instrument" : samp2,
}
samp3_dict = {
    "Name" : "Samp 3", 
    "Instrument" : samp3,
}

PlayBackLoop = True 

QtnoteDuration = [0.25, 0.5, 0.5, 0.5]
timeStamps16th = []
bpmNoteTrue = []
bpmNoteTrueTime = [] 
loopamount = 0 

startTime = time.time()

#------------------------------------------------------------------------------------------------------------------------
# wave_obj = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
# wave_obj_2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")
#------------------------------------------------------------------------------------------------------------------------

bpm = 30
bpm_adjust = 60/bpm

def note_to_16():
    for i in QtnoteDuration: 
        timeStamps16th.append(i*4)

#Adjust time 

def bpm_adjust_16(): 
    for i in QtnoteDuration: 
        bpmNoteTrue.append(i*bpm_adjust)
        
def change_it_up():     
    random_number = random.uniform(0,3)

    if 0 <= random_number <= 1: 
        bpmNoteTrue.reverse()

    elif 1 <= random_number <= 2:
        random.shuffle(bpmNoteTrue)

    else: 
        bpmNoteTrue.pop(2)
        bpmNoteTrue.append(random_number)

bpm_adjust_16()
note_to_16()
#change_it_up()


currentTime = 0

#makes sure previous item is added to current, to make sure it increases. Basically, a distance of 0.5 seconds and
#1.5 seconds becomes 2 in the bpmNoteTrueTime 

def bpm_note_true_fun(): 
    for i in bpmNoteTrue: 
        global timevalue 
        global currentTime
        timevalue = i + currentTime
        bpmNoteTrueTime.append(timevalue)
        currentTime = timevalue

bpm_note_true_fun()

print(bpmNoteTrueTime)


def create_dictio(sample, bpmNoteTrueTime, name): 
    event_dictio = {}
    total_event_list = [] 
    for i in range(len(bpmNoteTrueTime)): 
        event_dictio = {"Sample": sample, "Timestamp": bpmNoteTrueTime[i], "Name": name}
        total_event_list.append(event_dictio.copy())
    return total_event_list

samp1_events = create_dictio(samp1_dict["Instrument"],bpmNoteTrueTime,samp1_dict["Name"])
samp2_events = create_dictio(samp2_dict["Instrument"],bpmNoteTrueTime,samp2_dict["Name"])
samp3_events = create_dictio(samp3_dict["Instrument"],bpmNoteTrueTime,samp3_dict["Name"])


def sortByTimestamp(event):
    return event["Timestamp"]
    
all_samp_events = samp1_events + samp2_events + samp3_events
all_samp_events.sort(key = sortByTimestamp)

print(all_samp_events)

playValueEvent = 0 

while PlayBackLoop: 
    timeNow = time.time() - startTime
    if playValueEvent < len(all_samp_events) - 1:
        if timeNow >= all_samp_events[playValueEvent]["Timestamp"]: 
            all_samp_events[playValueEvent]["Sample"].play()
            playValueEvent = playValueEvent + 1 
    else: 
        time.sleep(0.001)




        # if timeNow >= all_samp_events[-1]["Timestamp"]: 
        #     PlayBackLoop == False 
        #     startTime = time.time()
        #     time.sleep(0.1)
        #     PlayBackLoop == True 



#------------------------------------------------------------------------------------------------

#playbackloop vorige opdracht 

#timestamp = bpmNoteTrueTime.pop(0)


# while PlayBackLoop: 
#     timeNow = time.time()
#     if(timeNow - startTime >= timestamp): 
#         wave_obj.play()
#         print("playing!")
#         if (len(bpmNoteTrueTime) > 0 ): 
#             timestamp = bpmNoteTrueTime.pop(0)
    
#     ## hier moeten alle elementen opnieuw de lijst in 
#     ## zorg ervoor dat je de playbackloop kunt stoppen 

#         else:
#             if loopamount == 2: 
#                 PlayBackLoop = False
#             else:   
#                 bpm_note_true_fun()
#                 change_it_up()
#                 loopamount = loopamount + 1 
#                 print(bpmNoteTrueTime)


#     else: 
#         time.sleep(0.001)

# time.sleep(1)

