import os

def discoverFiles(start):
    extensions = ['pdf','txt', 'docx']
    for dirpath, dirs, files in os.walk(start):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

# x = discoverFiles('/')
x = discoverFiles(r'D:\\')
for j in x:
    print (j)