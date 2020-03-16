from os import walk
import sys

def textReplace(filename: str, findReplaceList: list):
    try:
        fin = open(filename, "rt")
        data = fin.read()
        fin.close()

        nothingFound = True
        for entry in findReplaceList:
            if len(entry) == 2:
                if data.find(entry[0]) != -1:
                    nothingFound = False
                    data = data.replace(entry[0], entry[1])
        if nothingFound:
            print("No entries found in " + filename)
        else:
            fin = open(filename, "wt")
            fin.write(data)
            fin.close()
    except:
        print("Could not open " + filename)
        return

if __name__ == "__main__":
    #parse the arguments
    if len(sys.argv) != 3:
        print("Provide two arguments: the filepath/name of the find/replace text list, and the path to the search directory.")
    else:
        #read the find/replace entries into a list
        BatchFindReplaceListFilename = sys.argv[1]
        ListRawData = open(BatchFindReplaceListFilename, "rt").readlines()
        findReplaceEntryList = []
        for row in ListRawData:
            row = row.strip('\n')
            findReplaceEntryList.append(row.split(','))

        #open each file in the search directory and replace each item in the find/replace list
        SearchDirectory = sys.argv[2]
        if (SearchDirectory[-1] != '/'):
            SearchDirectory = SearchDirectory + '/'
        filelist = []
        for (dirpath, dirnames, filenames) in walk(SearchDirectory):
            filelist.extend(filenames)
            break
        for singleFile in filelist:
            searchFileName = SearchDirectory + singleFile
            if BatchFindReplaceListFilename != searchFileName:
                textReplace(SearchDirectory + singleFile, findReplaceEntryList)