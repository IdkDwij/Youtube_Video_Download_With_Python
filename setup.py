import os

codefile = """
"""
#codefile comment: still working on it
print('installing packages')
os.system('pip install pytube')
print('setting up file')
f = open("VideoDownloader.py", "w)
f.write(codefile)
f.close()
print("job done")
os.system("del setup.py")
