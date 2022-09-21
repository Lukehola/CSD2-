import time 
import simpleaudio as sa
from datetime import datetime

time_begin = datetime.now()

seconds = [1,1,2,1,1]

#calculate the distance between the notes 

for i in range(len(seconds)): 
    if i == 0: 
        seconds[i] = seconds[i]
    else:
        seconds[i] = seconds[i] + seconds[i - 1] 

print(seconds)

wave_obj = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/ritmische_player_folder/3a.SFX_schaak.wav")

##check if the sample is allowed to play, compare the allowed playtime to the current time 

seconds.reverse()
print(seconds)

for item in seconds: 
    t = time_begin - datetime.now() * -1 
    if t <= item:
        wave_obj.play()
    print(t)

