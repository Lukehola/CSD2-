import simpleaudio as sa
import numpy as np 

frequency = float(input("What frequency do you want to be played?"))
fs = 44100
seconds = int(input("And for how many seconds should I play it?"))
t = np.linspace(0, seconds, seconds*fs, False)

number_of_times_played = int(input("How many times do you want it to be played?"))

##def number_of_times_function(): 

note = np.sin(frequency*t*2*np.pi)

audio = note * (2**15 - 1) / np.max(np.abs(note)) 

audio = audio.astype(np.int16)

for i in (range(number_of_times_played)): 
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    print(i)