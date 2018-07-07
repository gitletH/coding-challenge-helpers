import glob
import re
import os

srcDir = 'src/'
outDir = 'out/'

if not os.path.exists(outDir):
    os.makedirs(outDir)

txtfiles = []
for file in glob.glob("%s*.py" % srcDir):
    with open(file, 'r') as fin:
        with open(file.replace(srcDir, outDir), 'w+') as fout:
            for line in fin:
                if not re.match(r'(?:^\s*$)|(?:^#.*$)', line):
                    fout.write(line)
                    