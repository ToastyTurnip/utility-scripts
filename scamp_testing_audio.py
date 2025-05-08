from scamp import *

s = Session()

piano = s.new_part('piano')

s.start_transcribing()
pitches = """
58 62 65 65 63 62 60 60 58 58 62 65 65 63 62 63 62 
58 62 65 65 63 62 60 60 58 58 62 65 65 63 62 63 62
58 58 58 55 58 58 55 58 55
62 60 58 62 60 60 58 58
"""
pitches = [int(x) for x in pitches.split()]
for pitch in pitches:
    p = input()
    piano.play_note(pitch, 1, 0.2)

s.stop_transcribing()#.to_score().show_xml()




