# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision G, 09/24/2023

Verified working on: Python 3.8 for Windows 10 64-bit.
'''

__author__ = 'reuben.brewer'

#########################################################
import os
import sys
from copy import * #for deepcopy of dicts
from stdlib_list import stdlib_list #"pip install stdlib_list"
#########################################################

##########################################################################################################
##########################################################################################################
def SortListAlphabetically(InputList):
    try:
        OutputList = sorted(InputList, key=lambda v: v.lower())
        return OutputList
    except:
        exceptions = sys.exc_info()[0]
        print("SortListAlphabetically, exceptions: %s" % exceptions)
        return list()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def IsModuleNameStringInPythonStdLibrary(ModuleNameStringToCheck, PythonVersion = -1): #Requires"pip install stdlib_list"

    try:
        PythonVersion = str(PythonVersion)

        if PythonVersion == "-1":
            ListOfAllModuleNameStringInPythonStdLibrary = stdlib_list('.'.join([str(v) for v in sys.version_info[0:2]])) #Uses version of current Python interpreter running this code.
        else:
            ListOfAllModuleNameStringInPythonStdLibrary = stdlib_list(PythonVersion)

        if ModuleNameStringToCheck in ListOfAllModuleNameStringInPythonStdLibrary:
            return 1
        else:
            return 0
    except:
        exceptions = sys.exc_info()[0]
        print("IsModuleNameStringInPythonStdLibrary, exceptions: %s" % exceptions)
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def ExtractDependenciesFromFile(ClassFileFullPath):

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ListOfDependencies = list()

    try:

        with open(ClassFileFullPath, 'r', encoding=FileEncoding) as ClassFileToParse:

            for line in ClassFileToParse:

                line = line.strip()
                #print("ExtractDependenciesFromFile, line = ")

                # 'import' must be in the line and it (or 'from') must appear first.
                # This prevents catching ''' random text import '''
                # Finding 'import' or 'from' at index 0 requires .strip() to be applied to line first!
                if line.find("import") != -1 and (line.find("import") == 0 or line.find("from") == 0):

                    ##########################################################################################################
                    ##########################################################################################################
                    ##########################################################################################################

                    if ClassName in PrintOnlyTheseClassNamesList:
                        pass
                        #print("line: " + line) #FOR DEBUGGING

                    line = line.replace("import ","").replace("from ","").replace(" import *","")

                    ###################################################### To remove comments, as in 'import cv2 #"pip install opencv-python==3.2.0.6"'
                    CommentStartingIndex = line.find("#")
                    if CommentStartingIndex != -1:
                        line = line[:CommentStartingIndex]
                    ######################################################

                    ###################################################### To handle situations like 'import tkinter.font as tkFont #Python 3'
                    AsStartingIndex = line.find(" as ")
                    if AsStartingIndex != -1:
                        line = line[:AsStartingIndex]
                    ######################################################

                    ###################################################### To handle situations like the left-over 'tkinter ttk'
                    SpaceStartingIndex = line.find(" ")
                    if SpaceStartingIndex != -1:
                        line = line[:SpaceStartingIndex]
                    ######################################################

                    line = line.replace("*", "") #To handle situations like 'from tkinter import * #Python 3'
                    line = line.strip()

                    LineSplitIntoList = line.split(',')

                    for IndividualImportName in LineSplitIntoList:

                        ################
                        IndividualImportName = IndividualImportName.strip()

                        if IndividualImportName.find("Phidget22") != -1:
                            IndividualImportName = "Phidget22" #Get rid of all sub modules of Phidget22 (e.g. 'Phidget22.Devices.DigitalOutput', 'Phidget22.Devices.Log', 'Phidget22.LogLevel', 'Phidget22.Phidget', 'Phidget22.PhidgetException')
                        ################

                        ##########################################################################################################
                        ##########################################################################################################
                        if IndividualImportName != "":

                            ##########################################################################################################
                            if USE_IncludeOnlyModulesNotInPythonStdLibrary_FLAG == 1:

                                if IsModuleNameStringInPythonStdLibrary(IndividualImportName) == 1 or IsModuleNameStringInPythonStdLibrary(IndividualImportName, "2.7") == 1:  # Is in the std library
                                    ShouldWeIncludeThisImportBasedOnPythonStdLibraryFlag = 0
                                else:
                                    ShouldWeIncludeThisImportBasedOnPythonStdLibraryFlag = 1

                            else:
                                ShouldWeIncludeThisImportBasedOnPythonStdLibraryFlag = 1
                            ##########################################################################################################

                            ##########################################################################################################
                            if ShouldWeIncludeThisImportBasedOnPythonStdLibraryFlag == 1:

                                ######################################################
                                if USE_IncludeOnlyReubenPythonModules_FLAG == 1:

                                    ShouldWeIncludeThisImportBasedOnIncludeOnlyReubenPythonModulesFlag = 1
                                    for Keyword in ReubenFilterKeywordsThatMustBePresentInLowerCase:
                                        if IndividualImportName.lower().find(Keyword) == -1:  # Keyword not found
                                            ShouldWeIncludeThisImportBasedOnIncludeOnlyReubenPythonModulesFlag = 0

                                else:
                                    ShouldWeIncludeThisImportBasedOnIncludeOnlyReubenPythonModulesFlag = 1
                                ######################################################

                                ######################################################
                                if ShouldWeIncludeThisImportBasedOnIncludeOnlyReubenPythonModulesFlag == 1:
                                    if IndividualImportName != ClassName: #Don't include yourself!
                                        ListOfDependencies.append(IndividualImportName)
                                ######################################################

                            ##########################################################################################################

                        ##########################################################################################################
                        ##########################################################################################################

                    ##########################################################################################################
                    ##########################################################################################################
                    ##########################################################################################################

    except:
        exceptions = sys.exc_info()[0]
        print("Could not open file " + ClassFileFullPath + ", Exceptions: %s" % exceptions) #unicorn UNCOMMENT THIS TO PRINT ERRORS

    return ListOfDependencies
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

########################################################################################################## Start of if __name__ == '__main__':
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ########################################################################################################## Start of setting main filepaths and parameters
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    reuben_python_imports_list_Python3path_FullPath = "C:\\Anaconda3\\Lib\\site-packages\\reuben_python_imports_list_Python3.pth" #unicorn
    ReubenFilterKeywordsThatMustBePresentInLowerCase = ["reuben", "python"] #"class"
    FileEncoding = "utf-8" #Otherwise we can't open files with the # -*- coding: utf-8 -*- header that prevents 'SyntaxError: Non-ASCII character '\xe2' in file"'.

    PrintOnlyTheseClassNamesList = [] #Blank means that we'll print everything!
    #PrintOnlyTheseClassNamesList = ["CameraStreamerClass_ReubenPython2and3Class"]

    USE_ExamineOnlyReubenPythonClasses_FLAG = 1
    USE_IncludeOnlyModulesNotInPythonStdLibrary_FLAG = 1
    USE_IncludeOnlyReubenPythonModules_FLAG = 0

    SpecialFilesFullPathList = ["G:\\My Drive\\CodeReuben\\Dependencies\\CreateListOfDependenciesForReubenClasses.py",
                                "G:\\My Drive\\CodeReuben\\UR5arm_ReubenPython2and3Class\\Teleop_UR5arm.py",
                                "G:\\My Drive\\CodeReuben\\UR5arm_ReubenPython2and3Class\\ExcelPlot_CSVfileForTrajectoryData.py",
                                "G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\SelfBalancingRobot1.py",
                                "G:\\My Drive\\CodeReuben\\TransducerTechniquesSSIloadCellReader_ReubenPython3Class\\test_program_for_TransducerTechniquesSSIloadCellReader_ReubenPython3Class_MultipleSensors.py"]

    USE_SpecialFiles_FLAG = 1

    MasterClassDependencies_DictOfDicts = dict()
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ########################################################################################################## End of setting main filepaths and parameters

    ########################################################################################################## Start of populating MasterClassDependencies_DictOfDicts for standard
    ########################################################################################################## MyClassName_ReubenPython2and3Class.py --> ListOfModuleDependencies and
    ########################################################################################################## test_program_for_MyClassName.py --> ListOfModuleDependencies_TestProgram
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    with open(reuben_python_imports_list_Python3path_FullPath, 'r', encoding=FileEncoding) as PTHfileToParse:

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        for ClassFileFullPath in PTHfileToParse:

            ClassFileFullPath = ClassFileFullPath.strip()
            LastSlashIndex = ClassFileFullPath.rfind("\\")
            ClassName = ClassFileFullPath[LastSlashIndex + 1:]
            CodeDirectoryFullPath = ClassFileFullPath

            ClassFileFullPath_ClassPY = CodeDirectoryFullPath + "\\" + ClassName + ".py"
            ClassFileFullPath_TestProgram = CodeDirectoryFullPath + "\\test_program_for_" + ClassName + ".py"

            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            if USE_ExamineOnlyReubenPythonClasses_FLAG == 1:
                ShouldWeOpenAndParseThisClassFlag = 1
                for Keyword in ReubenFilterKeywordsThatMustBePresentInLowerCase:
                    if ClassName.lower().find(Keyword) == -1: #Keyword not found
                        ShouldWeOpenAndParseThisClassFlag = 0
            else:
                ShouldWeOpenAndParseThisClassFlag = 1
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            if ShouldWeOpenAndParseThisClassFlag == 1:

                ListOfModuleDependencies = ExtractDependenciesFromFile(ClassFileFullPath_ClassPY)
                #print("ListOfModuleDependencies: type = " + str(type(ListOfModuleDependencies)) + ", value = " + str(ListOfModuleDependencies))

                ListOfModuleDependencies_TestProgram = ExtractDependenciesFromFile(ClassFileFullPath_TestProgram)
                #print("ListOfModuleDependencies_TestProgram: type = " + str(type(ListOfModuleDependencies)) + ", value = " + str(ListOfModuleDependencies))

                MasterClassDependencies_DictOfDicts[ClassName] = dict([("ListOfModuleDependencies", ListOfModuleDependencies),
                                                         ("ListOfModuleDependencies_TestProgram", ListOfModuleDependencies_TestProgram),
                                                         ("ListOfModuleDependencies_NestedLayers", list()),
                                                         ("ListOfModuleDependencies_All", list())])

            else:
                continue
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ########################################################################################################## End of populating MasterClassDependencies_DictOfDicts for standard
    ########################################################################################################## MyClassName_ReubenPython2and3Class.py --> ListOfModuleDependencies and
    ########################################################################################################## test_program_for_MyClassName.py --> ListOfModuleDependencies_TestProgram

    ########################################################################################################## Start of populating MasterClassDependencies_DictOfDicts for SpecialFiles
    ########################################################################################################## (hard-coded full filename paths, can by name anything ending in .py)
    ########################################################################################################## MyClassName_ReubenPython2and3Class.py --> ListOfModuleDependencies
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if USE_SpecialFiles_FLAG == 1:

        for SpecialFilesFullPathString in SpecialFilesFullPathList:

            with open(SpecialFilesFullPathString, 'r', encoding=FileEncoding) as SpecialfileToParse:

                SpecialFilesFullPathString = SpecialFilesFullPathString.strip()
                LastSlashIndex = SpecialFilesFullPathString.rfind("\\")
                ClassName = SpecialFilesFullPathString[LastSlashIndex + 1:]

                ListOfModuleDependencies = ExtractDependenciesFromFile(SpecialFilesFullPathString)
                #print("ListOfModuleDependencies: type = " + str(type(ListOfModuleDependencies)) + ", value = " + str(ListOfModuleDependencies))

                MasterClassDependencies_DictOfDicts[ClassName] = dict([("ListOfModuleDependencies", ListOfModuleDependencies),
                                                         ("ListOfModuleDependencies_TestProgram", list()),
                                                         ("ListOfModuleDependencies_NestedLayers", list()),
                                                         ("ListOfModuleDependencies_All", list())])

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ########################################################################################################## End of populating MasterClassDependencies_DictOfDicts for SpecialFiles
    ########################################################################################################## (hard-coded full filename paths, can by name anything ending in .py)
    ########################################################################################################## MyClassName_ReubenPython2and3Class.py --> ListOfModuleDependencies

    #print("MasterClassDependencies_DictOfDicts: " + str(MasterClassDependencies_DictOfDicts) + ", type: " + str(type(MasterClassDependencies_DictOfDicts)))
    #sys.exit()

    ########################################################################################################## Start of recursively-finding nested layers
    ########################################################################################################## --> ListOfModuleDependencies_NestedLayers,
    ########################################################################################################## removing duplicates within (but not across) lists
    ########################################################################################################## to form --> ListOfModuleDependencies_All, and
    ########################################################################################################## printing final results
    ##########################################################################################################
    ##########################################################################################################
    for ClassName in MasterClassDependencies_DictOfDicts:

        ########################################################################################################## Recursively find nested layers
        try:

            ModuleNamesToInspect = MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies"] + MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_TestProgram"] #ListOfModuleDependencies_All doesn't exist yet
            #print(ClassName + ", ModuleNamesToInspect = " + str(ModuleNamesToInspect))

            while len(ModuleNamesToInspect) > 0:
                ModuleName = ModuleNamesToInspect.pop(0)

                if ModuleName in MasterClassDependencies_DictOfDicts:

                    ListOfModules_NestedLayers = MasterClassDependencies_DictOfDicts[ModuleName]["ListOfModuleDependencies"] #DON'T INCLUDE "ListOfModuleDependencies_TestProgram"
                    ModuleNamesToInspect = ModuleNamesToInspect + ListOfModules_NestedLayers #Recursive
                    MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"] = MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"] + ListOfModules_NestedLayers

        except:
            exceptions = sys.exc_info()[0]
            print("Creating nested layers, exceptions for ClassName = '" + ClassName + "': %s" % exceptions)
        ##########################################################################################################

        ########################################################################################################## Remove duplicates within (but not across) lists
        try:

            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies"] = list(set(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies"]))
            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_TestProgram"] = list(set(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_TestProgram"]))
            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"] = list(set(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"]))

            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies"] = SortListAlphabetically(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies"])
            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_TestProgram"] = SortListAlphabetically(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_TestProgram"])
            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"] = SortListAlphabetically(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"])

            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_All"] = MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies"]  + \
                                                                                MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_TestProgram"] + \
                                                                                MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"]


            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_All"] = list(set(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_All"]))
            MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_All"] = SortListAlphabetically(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_All"])

        except:
            exceptions = sys.exc_info()[0]
            print("Removing duplicate values, sort alphabetically, and calculate ALL list, exceptions: %s" % exceptions)
        ##########################################################################################################

        ########################################################################################################## Printing final results
        try:

            ##################
            if len(PrintOnlyTheseClassNamesList) > 0:
                if ClassName in PrintOnlyTheseClassNamesList:
                    PrintInfoOnThisClassNameFlag = 1
                else:
                    PrintInfoOnThisClassNameFlag = 0
            else:
                PrintInfoOnThisClassNameFlag = 1
            ##################

            ##################
            if PrintInfoOnThisClassNameFlag == 1:
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print(ClassName + ", ListOfModuleDependencies: " + str(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies"]))
                print(ClassName + ", ListOfModuleDependencies_TestProgram: " + str(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_TestProgram"]))
                print(ClassName + ", ListOfModuleDependencies_NestedLayers: " + str(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_NestedLayers"]))
                print(ClassName + ", ListOfModuleDependencies_All:" + str(MasterClassDependencies_DictOfDicts[ClassName]["ListOfModuleDependencies_All"]))
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
            ##################

        except:
            exceptions = sys.exc_info()[0]
            print("Printing final results, exceptions: %s" % exceptions)
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ########################################################################################################## End of recursively-finding nested layers
    ########################################################################################################## --> ListOfModuleDependencies_NestedLayers,
    ########################################################################################################## removing duplicates within (but not across) lists
    ########################################################################################################## to form --> ListOfModuleDependencies_All, and
    ########################################################################################################## printing final results

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
########################################################################################################## End of if __name__ == '__main__':