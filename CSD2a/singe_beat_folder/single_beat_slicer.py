import simpleaudio as sa 
import time 


noteDuration = [0.25, 0.5, 1, 2.25]
timeStamps16th = []
bpmNoteTrue = []

wave_obj = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
wave_obj_2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")

bpm = 100
bpm_adjust = 60/bpm

def note_to_16():
    for i in noteDuration: 
        timeStamps16th.append(i*4)



def bpm_adjust_16(): 
    for i in noteDuration: 
        bpmNoteTrue.append(i*bpm_adjust)
        

bpm_adjust_16()
note_to_16()

print(bpmNoteTrue)
print(timeStamps16th)