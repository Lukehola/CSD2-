import time 
import simpleaudio as sa 
import math 
import sys 
import array as array_module 

wave_obj = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/python_basics/SFX_schaak.wav")
##play_obj = wave_obj.play()
##play_obj.wait_done()



input_list = [4, 1, 0.5, 1.5, 0.5, 120]
second_apart_list = input_list 
second_apart_list.pop(0)
second_apart_list.pop(-1)

##remove line amount and bpm from the list 

lines_amount = input_list[0]
bpm = input_list[-1]

##BPM calculation, decides how fast it should be played 

for i in range(len(second_apart_list)): 
    bpm/60*second_apart_list[i]

##plays the slicer, repeating for the amount of lines given 

for i in range(input_list[0]): 
    for seconds in second_apart_list: 
        play_obj = wave_obj.play()
        time.sleep(seconds)