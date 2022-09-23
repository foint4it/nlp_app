import subprocess
cmd = ['python','-m','spacy download en_core_web_trf']
subprocess.run(cmd)
print("Trabajando")