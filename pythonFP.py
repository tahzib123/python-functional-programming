def head(list):
    return list[0]

def tail(list):  #return list????
    return list[1:]

def sum(list):
    if len(list) == 1:
        return list[0] #or head(list)
    else:
        return head(list) + sum(tail(1))

def append_to_list(list,x):
    return list+[x]


#lambda function that returns added value of 2 datatypes for strings, ints, lists etc
add  = lambda itemToSearch, y:itemToSearch+y
def del_list(list,e):
    if len(list) == 0:
        return list
    elif list[0] == e:
        return []+del_list(list[1:],e)
    else:
        return [list[0]]+ del_list(list[1:],e)


list_head = lambda list: list[0]
list_tail = lambda list: list[1:]

add = lambda x,y:x+y

#min in function call will be 0th index of list, assuming that is the smallest, swap if necessary
def findMin(list,index,min):
    if len(list) == index:
        #del_list(list,min)
        return min
    else:
        if min > list[index]:
            return findMin(list,index+1,list[index])
        elif min == list[index]:
            return findMin(list,index+1,min)
        else:
            return findMin(list,index+1,min)

#deletes only first occurrence of e, variation of the del function professor gave us
def del1(list,e,index):
    if len(list) == index:
        return list
    elif index == len(list)-1:
        if list[index] == e:
            return list[0:index]
        else:
            return del1(list, e, index + 1)

    elif list[index] == e:
        return list[0:index]+list[index+1:]
    else:
        return del1(list,e,index+1)

def recurSelectionSort(a, n, index,newlist):
    if index == n:
        return newlist
    else:
        #k = findMin(a, 0, a[0])     <------- that was mutation to function call is embedded in return statement where k should be
        return recurSelectionSort(del1(a,findMin(a, 0, a[0]),0), n, index + 1, append_to_list(newlist, findMin(a, 0, a[0])))


# call function as lowercase(originalString) other parameters are default
def stop_lowercase(originalstring, currentIndex = 0, lowerstring=""):
    if (currentIndex > len(originalstring) - 1):
        return lowerstring
    else:
        # convert letter to ascii value
        lettervalue = ord(originalstring[currentIndex])
        # if the ascii val corresponds to a capital letter which is 65-90
        if 65 <= lettervalue <= 90:
            computelettervalue = lambda itemToSearch: itemToSearch + 32
            # call the lambda expression with lettervalue as parameter and convert it back to a char add to lowerstring
            return stop_lowercase(originalstring, currentIndex + 1, lowerstring + chr(computelettervalue(lettervalue)))
        # the current character is either already lowercase or is some type of symbol so it doesnt get changed
        else:
            return stop_lowercase(originalstring, currentIndex + 1, lowerstring + originalstring[currentIndex])


# call function as lowercase(originalString) other parameters are default
def stop_uppercase(originalstring, currentIndex = 0, upperstring=""):
    if (currentIndex > len(originalstring) - 1):
        return upperstring
    else:
        lettervalue = ord(originalstring[currentIndex])
        # if the ascii val corresponds to a lowercase letter which is 97-122
        if 97 <= lettervalue <= 122:
            computelettervalue = lambda itemToSearch: itemToSearch - 32
            return stop_uppercase(originalstring, currentIndex + 1, upperstring + chr(computelettervalue(lettervalue)))
        # the current character is either already uppercase or is some type of symbol so it doesnt get changed
        else:
            return stop_uppercase(originalstring, currentIndex + 1, upperstring + originalstring[currentIndex])


def lowercase(originalstring, currentIndex = 0, lowerstring=""):
    if (currentIndex > len(originalstring) - 1):
        return lowerstring
    else:
        # convert letter to ascii value
        lettervalue = ord(originalstring[currentIndex])
        # if the ascii val corresponds to a capital letter which is 65-90
        if 65 <= lettervalue <= 90:
            computelettervalue = lambda x: x + 32
            # call the lambda expression with lettervalue as parameter and convert it back to a char add to lowerstring
            return lowercase(originalstring, currentIndex + 1, lowerstring + chr(computelettervalue(lettervalue)))
        # the current character is either already lowercase or is some type of symbol so it doesnt get changed
        elif 97 <= lettervalue <=122 or lettervalue == 32:
            return lowercase(originalstring, currentIndex + 1, lowerstring+originalstring[currentIndex])
        elif lettervalue == 46 or originalstring[currentIndex] =='\n' :
            return lowercase(originalstring, currentIndex + 1, lowerstring+" ")
        else:
            return lowercase(originalstring, currentIndex + 1, lowerstring)





def uppercase1(originalstring, currentIndex = 0, upperstring=""):
    if (currentIndex > len(originalstring) - 1):
        return upperstring
    else:
        # convert letter to ascii value
        lettervalue = ord(originalstring[currentIndex])
        # if the ascii val corresponds to a capital letter which is 97-122
        if 97 <= lettervalue <= 122:
            computelettervalue = lambda x: x - 32
            # call the lambda expression with lettervalue as parameter and convert it back to a char add to upperstring
            return uppercase1(originalstring, currentIndex + 1, upperstring + chr(computelettervalue(lettervalue)))
        # the current character is either already uppercase or is some type of symbol so it doesnt get changed
        elif 65 <= lettervalue <=90 or lettervalue == 32:
            return uppercase1(originalstring, currentIndex + 1, upperstring+originalstring[currentIndex])
        elif lettervalue == 46 or originalstring[currentIndex] =='\n':
            return uppercase1(originalstring, currentIndex + 1, upperstring+" ")
        elif originalstring[currentIndex] == '\r':
            return uppercase1(originalstring, currentIndex + 1, upperstring)
        else:
            return uppercase1(originalstring, currentIndex + 1, upperstring)




def stopWordsFunction(file, index,word,list): #file is stopwords, index will be 0, word is empty string, list is empty

    if file=="": #if file is empty, then itll return after printing explanation
        print("Error: Input was empty")
        return
    elif index == len(file): #reached the end of the file, append the last word and return
        return append_to_list(list,word)

    elif file[index] != '\n': #concatenate each character of each word

        return stopWordsFunction(file,index+1,add (word,file[index]),list)
    elif file[index] == '\n': #an entire word is stored in my variable, append it to the list
        #list.append(word)
        #word=""
        return stopWordsFunction(file,index+1,"",append_to_list(list,word))







def input_function(file,index,word,list,stopwords):
    if file=="": #if file is empty, then itll return after printing explanation
        print("Error: Input was empty")
        return
    # reached the end of the file, append the last word and return
    elif index > len(file)-1:
        # prevent an empty word from being appended
        if word == '':
            return list
        #otherwise, please append
        if searchItemIndex(stopwords, word, 0, len(stopwords)) == -1:
            return input_function(file, index + 1, "", append_to_list(list, word),stopwords)
        else:
            return list
            #return append_to_list(list, word)

    # concatenate each character of each word
    elif file[index] != ' ':
        # get rid of \n
        if file[index] == '\n':
            # prevent empty words from being appended
            if word =='':
                return input_function(file, index + 1, "", list,stopwords)
            # otherwise, append
            if searchItemIndex(stopwords,word,0,len(stopwords))==-1:
                return input_function(file, index + 1, "", append_to_list(list,word),stopwords)
            else:
                return input_function(file,index+1,"",list,stopwords)

        else: #if file[index] == \n
            return input_function(file,index+1,add(word,file[index]),list,stopwords)
    elif file[index] == ' ': #an entire word is stored in my variable, append it to the list
        if searchItemIndex(stopwords, word, 0, len(stopwords)) == -1 and len(word)!=0:
            return input_function(file, index + 1, "", append_to_list(list, word),stopwords)
        else:
            return input_function(file, index + 1, "", list,stopwords)








def searchItemIndex(list, itemToSearch, left, right):
    if right >= left:

        mid = left + (right - left) // 2

        if list[mid] == itemToSearch:
            return mid

        elif list[mid] > itemToSearch:
            return searchItemIndex(list, itemToSearch, left, mid - 1)

        else:
            return searchItemIndex(list, itemToSearch, mid + 1, right)
    else:
        return -1

def isValueInList(list, itemToSearch):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if list[mid] == itemToSearch:
            return True
        elif itemToSearch < list[mid]:
        # slicing list left side to mid(search left side)
            return isValueInList(list[:mid], itemToSearch)
        else:
        # slicing list  mid + 1 to end of list(search right side)
            return isValueInList(list[mid + 1:], itemToSearch)

# usage numOccurences(list,itemToSearch)
def numOccurences(list, itemToSearch, counter=0):
    indexOfItem = searchItemIndex(list, itemToSearch, 0, len(list) - 1)
    # not in the list
    if (indexOfItem == -1):
        return counter
    else:
    # removeFromList returns new list with an index removed
        return numOccurences(removeFromList(list, indexOfItem), itemToSearch, counter + 1)

# creates 2 copies of the list using python slice and then combines them then returns the #list without the element to be removed
def removeFromList(list, indexOfItem):
    if len(list) == 0:
        return list
    elif indexOfItem > len(list) - 1:
        return list
    else:
        return list[:indexOfItem] + list[indexOfItem + 1:]

# usage calculateFrequencies(list,frequencyList)
# currentIndex is the index whos frequency is being calculated.
def calculateFrequencies(list, frequencyList, currentIndex=0):
    if currentIndex > len(list) - 1:
        return frequencyList
    else:
        return calculateFrequencies(list,append_to_list(frequencyList, numOccurences(list, list[currentIndex])),currentIndex + 1)



def findduplicates(origList, freqList, currentIndex, counter, length):
    if currentIndex >= length - 1:
        return origList, freqList
    elif counter >= length:
        return findduplicates(origList, freqList, currentIndex + 1, currentIndex + 2, length)
    else:
        if origList[currentIndex] == origList[counter]:
            return findduplicates(removeFromList(origList,counter), removeFromList(freqList,counter), currentIndex, counter, length - 1)
        else:
            return findduplicates(origList, freqList, counter, counter + 1, length)



def findMaxKTimes(maxValue, k, origList, freqList, length, counter, outputfile):
  if k <= 0:
    return
  else:
    #passed through entire list so max should be computed
    if counter >= length:
      newWords, newFreq = printMax(maxValue, origList, freqList, len(freqList), 0, outputfile)

      return findMaxKTimes(0, k -1, newWords, newFreq, len(newFreq), 0, outputfile)
    else:
      if freqList[counter] > maxValue:
        return findMaxKTimes(freqList[counter], k, origList, freqList, len(freqList), counter + 1, outputfile)
      else:
        return findMaxKTimes(maxValue, k, origList, freqList, len(freqList), counter + 1, outputfile)


# prints everything with max value return the new listS without the max elements
def printMax(maxValue, origList, freqList, length, currentIndex,outputfile):
  # return updated list without max element(s)
  if currentIndex >= length:
    return origList, freqList
  else:
    if freqList[currentIndex] == maxValue:
      printToFile(origList,freqList,currentIndex,outputfile)
      return printMax(maxValue, removeFromList(origList,currentIndex), removeFromList(freqList,currentIndex), len(freqList) - 1, currentIndex,outputfile)
    else:
      return printMax(maxValue, origList, freqList, len(freqList), currentIndex + 1,outputfile)

def printToFile(origList, freqList, currentIndex, outputfile):
  writeStream = open(outputfile, "a")
  writeStream.write(origList[currentIndex] + " " + str(freqList[currentIndex]) + "\n")
  #writeStream.close()


def findMinKTimes(minValue, k, origList, freqList, length, counter, outputfile):
  if k <= 0:
    return
  else:
    #passed through entire list so max should be computed
    if counter >= length:
      newWords, newFreq = printMax(minValue, origList, freqList, len(freqList), 0, outputfile)

      return findMinKTimes(1000, k -1, newWords, newFreq, len(freqList), 0, outputfile)
    else:
      if freqList[counter] < minValue:
        return findMinKTimes(freqList[counter], k, origList, freqList, len(freqList), counter + 1, outputfile)
      else:
        return findMinKTimes(minValue, k, origList, freqList, len(freqList), counter + 1, outputfile)



import sys

def main():
    #sys.setrecursionlimit(1500)
    if(len(sys.argv)<2):
        print("Error: Not enough paramters were given, please try again")
        exit(1)

#***********************************************INPUT FILE**************************************************************
    split = sys.argv[1].split(';')
    input = split[0].split('=')
    input = input[1]
    #print(input)
#*******************************************K IS HOW MANY WORDS TO OUTPUT***********************************************
    k=split[1].split('=',1)
    k=k[1]
    k=int(k)
    #print(k)
#*****************************************MOST FREQUENT OR LEAST FREQUENT***********************************************
    frequent = split[2].split('=',1)
    if(frequent[1] == 'Y' or frequent[1] == 'y' ):
        frequent = "most_frequent"
    else:
        frequent = "least_frequent"
    #print(frequent)
#*****************************************************UPPERCASE OR LOWERCASE********************************************
    uppercase = split[3].split('=',1)
    if(uppercase[1] == 'N' or uppercase[1] == 'n'):
        uppercase = "no"
    else:
        uppercase = "yes"
    #print(uppercase)
#*************************************************OUTPUT FILE***********************************************************
    output = split[4].split('=',1)
    output = output[1]
    #print(output)
    open(output,'w').close()

    file = open(input,'r')
    input_contents = file.read()
    # if there is no input a blank output file is made and the program ends
    if len(input_contents) == 0:
        sys.exit()
    
    stopwords_file = open("stopwords.txt",'r')
#print("STOPWORDS -----------------------------------------")
    stopword_content = stopwords_file.read()
#print(stopword_content)




    line=""
    if uppercase == "yes":
        edited_stop_words = stop_uppercase(stopword_content,0,"")
        stopwords = stopWordsFunction(edited_stop_words, 0, line, [])
        input1 = uppercase1(input_contents, 0, "")
        input_list = input_function(input1, 0, line, [], stopwords)
    else:
        edited_stop_words = stop_lowercase(stopword_content, 0, "")
        stopwords = stopWordsFunction(edited_stop_words, 0, line, [])
        input1 = lowercase(input_contents, 0, "")
        input_list = input_function(input1, 0, line, [], stopwords)



    size = len(input_list)
    sorted_list = recurSelectionSort(input_list,size,0,[])
   # print("this is sorted")
    #print(sorted_list)

    frequencyList = calculateFrequencies(sorted_list, [])
   # print(sorted_list)
   # print(frequencyList)
    unique, newfreq = findduplicates(sorted_list,frequencyList,0,1,len(sorted_list))
   # print("This is final list")
    #print(unique)
    #print("this is frequncies")
    #print(newfreq)
    if frequent == "most_frequent":
        #print(k)
        findMaxKTimes(0,k,unique,newfreq,len(unique),0,output)
    else:
        #print(k)
        findMinKTimes(10000, k, unique, newfreq,len(unique), 0, output)
    #output.close()



sys.setrecursionlimit(50000)
main()
