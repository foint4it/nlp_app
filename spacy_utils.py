import subprocess
cmd = ['python','-m','spacy download en_core_web_sm']
subprocess.run(cmd)
print("Trabajando")