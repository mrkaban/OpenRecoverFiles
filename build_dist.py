import zipfile
from subprocess import *
import os
import shutil
import sys

VERSION = "1.5.5"
EXE_NAME = "KickassUndelete_{0}.exe".format(VERSION.replace(' ','_'))
ZIP_NAME = "KickassUndelete_{0}.zip".format(VERSION.replace(' ','_'))

FRAMEWORK = "C:\\Program Files (x86)\\Reference Assemblies\\Microsoft\\Framework\\.NETFramework\\v4.0"
MSBUILD = "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\msbuild.exe"
ILMERGE = "C:\\Program Files (x86)\\Microsoft\\ILMerge\\ILMerge.exe"

SOLUTION = "KickassUndelete/KickassUndelete.sln"
OUTPUT_DIR = "KickassUndelete/bin/Release/"
RELEASE_NOTES = "README.txt"

PUBLISH_FOLDER = "dist/"
TEMP_DIR = "temp/"

if not os.path.exists(MSBUILD):
    sys.exit("ERROR: MSBuild not found!")

if not os.path.exists(ILMERGE):
    sys.exit("ERROR: ILMerge not found!")


def executeProcess(command):
    p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    res = p.communicate()
    print "STDOUT:"
    print res[0]
    print "STDERR:"
    print res[1]
    return res[1] == ''


# Builds the KickassUndelete solution
def buildSolution():
    print "Building Kickass Undelete..."
    command = [MSBUILD, SOLUTION, "/p:Configuration=Release,Platform=Any CPU"]
    print command
    if not executeProcess(command):
        print "Build failed!"
        return False
    else:
        print "Build succeeded!"
        return True



# Merges the assemblies together
def mergeAssemblies(assemblies, outfile):
    print "Merging assemblies:"
    command = [ILMERGE, "/out:{0}".format(outfile), "/targetplatform:v4,{0}".format(FRAMEWORK)]
    command += assemblies
    print command
    if not executeProcess(command):
        print "Merging failed!"
        return False
    else:
        print "Merging succeeded!"
        return True


# Zip the result together with the release notes
def zipBinaries(files, outfile):
    print "Building zip archive..."
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
    zf = zipfile.ZipFile(outfile, mode='w')
    try:
        for f in files:
            zf.write(f, compress_type=compression)
    finally:
        zf.close()
    print "Zip archive complete!"



# Zip the source
def zipSource(dirs, outfile):
    # TODO: Write me
    pass


if buildSolution():
    mainassembly = [file for file in os.listdir(OUTPUT_DIR) if file.lower().endswith(".exe") and "vshost" not in file.lower()][0]
    assemblies = [OUTPUT_DIR + mainassembly] + [OUTPUT_DIR + file for file in os.listdir(OUTPUT_DIR) if file.lower().endswith(".dll")]
    print assemblies
    if not os.path.exists(TEMP_DIR):
        os.mkdir(TEMP_DIR)
    if mergeAssemblies(assemblies, TEMP_DIR + mainassembly):
        shutil.copy(TEMP_DIR + mainassembly, PUBLISH_FOLDER + EXE_NAME)
        shutil.copy(RELEASE_NOTES, TEMP_DIR + RELEASE_NOTES)
        os.chdir(TEMP_DIR)
        zipdest = "../" + PUBLISH_FOLDER + ZIP_NAME
        if os.path.exists(zipdest):
            os.remove(zipdest)
        zipBinaries([mainassembly, RELEASE_NOTES], zipdest)
        os.chdir("..")
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

