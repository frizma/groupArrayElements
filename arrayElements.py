from math import ceil
def groupArrayElements(arrayElements,n):
    try:
        listItemCount=ceil(len(arrayElements)/n) #number of items in final lists
        return [arrayElements[i:i+listItemCount] for i in range(0,len(arrayElements),listItemCount)]
        # for loop increment by "listItemCount"
        #spliting "arrayElements" into n lists where each list will have "listItenCount" elements 
    except Exception as e:
        if e.__class__==ZeroDivisionError:
            return "'n' should be greater than zero"
        elif len(arrayElements)==0:
           return "'arrayElements' should not be a empty list"
        else:
            return str(e)