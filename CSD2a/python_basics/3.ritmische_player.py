import time 
import simpleaudio as sa 
import math 
import sys 
import array as array_module 

wave_obj = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/python_basics/SFX_schaak.wav")
##wave_obj_2 = sa.WaveObject.from_wave_file("/Users/521459/Desktop/CSD2-/CSD2a/python_basics/enpassant.wav")
##play_obj = wave_obj.play()
##play_obj.wait_done()

true_time_tobeadded = 0 



input_list = [4, 1, 0.5, 1.5, 0.5, 120]
bpm = input_list[-1]
lines_amount = input_list[0]

second_apart_list = input_list[1:-1] 
print(second_apart_list)

##echte BPM waarde

true_time_list = []

##remove line amount and bpm from the list 




##BPM calculation, decides how fast it should be played 

for i in range(len(second_apart_list)): 
    true_time_tobeadded = 60 / bpm * second_apart_list[i] 
    true_time_list.append(true_time_tobeadded)


##plays the slicer, repeating for the amount of lines given 

def number_of_measures(): 
        for seconds in true_time_list: 
            play_obj = wave_obj.play()
            time.sleep(seconds)

for i in range(input_list[0]): 
    number_of_measures()
