import subprocess
cmd = ['python3','-m','spacy download en_core_web_sm']
subprocess.run(cmd)
print("Working")