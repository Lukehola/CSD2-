import time
from tracemalloc import start 
import simpleaudio as sa 
import random 

samp1 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")
samp2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.enpassant.wav")
samp3 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/CHEF_snare_07_v2.wav")

gridTotal = 14
numNotes1 = 3
offset1 = 1


gridList1 = 14//3
gridList1Xtra = 0 
if gridList1 * numNotes1 != gridTotal: 
    for i in range(gridTotal - gridList1*numNotes1): 
        gridList1Xtra = gridList1Xtra + 1 


print(gridList1)
print(gridList1Xtra)