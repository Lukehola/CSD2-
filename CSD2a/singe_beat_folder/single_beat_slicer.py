import simpleaudio as sa 
import time 
import random 

PlayBackLoop = True 

noteDuration = [0.25, 0.5, 1, 2.25]
timeStamps16th = []
bpmNoteTrue = []

startTime = time.time()

wave_obj = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
wave_obj_2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")

bpm = 30
bpm_adjust = 60/bpm

def note_to_16():
    for i in noteDuration: 
        timeStamps16th.append(i*4)



def bpm_adjust_16(): 
    for i in noteDuration: 
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
change_it_up()

# print(bpmNoteTrue)
# print(timeStamps16th)
# timestamp = bpmNoteTrue.pop(0)
# print(len(bpmNoteTrue))

timestamp = bpmNoteTrue.pop(0)

while PlayBackLoop: 
    timeNow = time.time()
    if(timeNow - startTime >= timestamp): 
        wave_obj.play()
        if (len(bpmNoteTrue) > 0 ): 
            timestamp = bpmNoteTrue.pop(0)
    
        else:
            PlayBackLoop = False  

    else: 
        time.sleep(0.001)

time.sleep(1)
