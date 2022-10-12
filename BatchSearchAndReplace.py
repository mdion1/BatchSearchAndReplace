import os
import searchReplaceInputs
from typing import List,Dict

def textReplace(filename: str, findReplaceDict: Dict[str, str]):
    try:
        fin = open(filename, "rt")
        data = fin.read()
        fin.close()

        found = False
        for key in findReplaceDict.keys():
            if data.find(key) != -1:
                found = True
                data = data.replace(key, findReplaceDict[key])
        if found:
            print("Entries found in " + filename)
            fin = open(filename, "wt")
            fin.write(data)
            fin.close()
    except:
        print("Could not open " + filename)
        return

if __name__ == "__main__":
    #Get filename list

    filepathList: List[str] = []
    for (dirpath, dirnames, filenames) in os.walk(searchReplaceInputs.BaseDir):
        for filename in filenames:
            filepath =  os.path.join(dirpath, filename)

            # apply filename filters
            # parse = (exclusive filters AND'ed together) && (inclusive filters OR'ed together)
            parse = True # if filter list is empty, parse all files
            for filterStr in searchReplaceInputs.filePathFilters_exclusive:
                parse &= (filterStr in filepath)

            exclusiveFilt = True
            inclusiveFilt = 0 == len(searchReplaceInputs.filePathFilters_inclusive) # if list is empty, ignore by setting True
            for filterStr in searchReplaceInputs.filePathFilters_exclusive:
                exclusiveFilt &= (filterStr in filepath)
            for filterStr in searchReplaceInputs.filePathFilters_inclusive:
                inclusiveFilt |= (filterStr in filepath)
            
            if exclusiveFilt and inclusiveFilt:
                textReplace(filepath, searchReplaceInputs.searchReplaceDict)
                filepathList.append(filepath)



'''
    #parse the arguments
    if False:
    #if len(sys.argv) != 3:
        print("Provide two arguments: the filepath/name of the find/replace text list, and the path to the search directory.")
    else:
        #read the find/replace entries into a list
        #BatchfindReplaceDictFilename = sys.argv[1]
        BatchfindReplaceDictFilename = 'C:/Users/Matt Dion/mdion1.github.com/BatchSearchAndReplace/searchAndReplaceText.txt'
        ListRawData = open(BatchfindReplaceDictFilename, "rt").readlines()
        findReplaceEntryList = []
        for row in ListRawData:
            row = row.strip('\n')
            findReplaceEntryList.append(row.split(','))

        #open each file in the search directory and replace each item in the find/replace list
        #SearchDirectory = sys.argv[2]
        SearchDirectory = 'C:/PCBA-Squidstat_Plus/PCBA'
        if (SearchDirectory[-1] != '/'):
            SearchDirectory = SearchDirectory + '/'
        filelist = []
        for (dirpath, dirnames, filenames) in walk(SearchDirectory):
            filelist.extend(filenames)
            break
        for singleFile in filelist:
            searchFileName = SearchDirectory + singleFile
            if BatchfindReplaceDictFilename != searchFileName:
                textReplace(SearchDirectory + singleFile, findReplaceEntryList)
'''