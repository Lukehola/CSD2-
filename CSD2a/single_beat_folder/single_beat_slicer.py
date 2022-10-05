import simpleaudio as sa 
import time 
import random 

PlayBackLoop = True 

QtnoteDuration = [0.25, 0.5, 0.75, 0.5]
timeStamps16th = []
bpmNoteTrue = []
bpmNoteTrueTime = [] 
loopamount = 0 



startTime = time.time()

wave_obj = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
wave_obj_2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")

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

def bpm_note_true_fun(): 
    for i in bpmNoteTrue: 
        global timevalue 
        global currentTime
        timevalue = i + currentTime
        bpmNoteTrueTime.append(timevalue)
        currentTime = timevalue

bpm_note_true_fun()

print(bpmNoteTrueTime)

timestamp = bpmNoteTrueTime.pop(0)

## speelt de sample en popped de BPMNOTETRUETIME

while PlayBackLoop: 
    timeNow = time.time()
    if(timeNow - startTime >= timestamp): 
        wave_obj.play()
        print("playing!")
        if (len(bpmNoteTrueTime) > 0 ): 
            timestamp = bpmNoteTrueTime.pop(0)
    
    ## hier moeten alle elementen opnieuw de lijst in 
    ## zorg ervoor dat je de playbackloop kunt stoppen 

        else:
            if loopamount == 5: 
                PlayBackLoop = False
            else:   
                bpm_note_true_fun()
                change_it_up()
                loopamount = loopamount + 1 
                print(bpmNoteTrueTime)


    else: 
        time.sleep(0.001)

time.sleep(1)
