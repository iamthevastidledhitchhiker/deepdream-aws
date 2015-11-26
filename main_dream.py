import os, subprocess
for f in os.listdir('Input'):
    subprocess.call(["python", "dream.py", 'Input/'+f, 'Output/'+f])