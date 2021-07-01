import os
import subprocess
import pathlib
import time

LOCATION = str(pathlib.Path(__file__).parent.resolve())

folder = LOCATION + "\\projects"

sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]


def copyToMain(files, absolutePath, studentPath):
    absolutePath = "/".join(absolutePath.split("\\"))
    studentPath = "/".join(studentPath.split("\\"))

    import shutil
    for f in files:
        # print("copying "+studentPath+f, absolutePath)
        shutil.copy(studentPath + f, absolutePath)


def deleteFromMain(files, absolutePath, studentPath):
    studentPath = "/".join(studentPath.split("\\"))
    absolutePath = "/".join(absolutePath.split("\\"))
    for f in files:
        # print("deleting ",studentPath+f)
        os.remove(studentPath + f)
        # print("deleting ", absolutePath +"/" + f)
        os.remove(absolutePath + "/" + f)


# vider le fichier du résultat
open(LOCATION + "/javaClasses/resultat.json", "w").close()

for student in sub_folders:
    print(student)
    files = [name for name in os.listdir(folder + "/" + student) if
             os.path.isfile(os.path.join(folder + "/" + student, name)) and ".java" in name]
    for javaFile in files:
        subprocess.Popen("cd " + folder + "/" + student, shell=True)
        res = subprocess.Popen("cd " + folder + "/" + student + " && javac " + javaFile, shell=True,
                               stdout=subprocess.PIPE)
        if (len(res.stdout.read().decode("cp850")) == 0):
            print(javaFile + " compiled successfully")
        else:
            print("Error compiling file : " + javaFile)

    files = [name for name in os.listdir(folder + "/" + student) if
             os.path.isfile(os.path.join(folder + "/" + student, name)) and ".class" in name]
    copyToMain(files, LOCATION + "/javaClasses", folder + "/" + student + "/")

    print("\nexecuting java test...")
    res = subprocess.Popen("cd " + LOCATION + "/javaClasses" + " && java TestTP1 \"" + student + "\"", shell=True,
                           stdout=subprocess.PIPE)
    print("resultat :", end="\t")
    print(res.stdout.read().decode("cp850"))

    deleteFromMain(files, LOCATION + "/javaClasses", folder + "/" + student + "/")

resultat = open("resultat.json", "w")
resJava = open("./javaClasses/resultat.json", "r")
resultat.write("[" + "\n".join(resJava.readlines())[1:] + "]")
resJava.close()
resultat.close()

subprocess.Popen("start  " + LOCATION+"/resultat.json", shell=True)