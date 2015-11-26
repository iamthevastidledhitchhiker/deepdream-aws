import os, subprocess
for f in os.listdir('Input'):
    subprocess.call(["python", "dreamify.py", 'Input/'+f, 'Output/'+f])