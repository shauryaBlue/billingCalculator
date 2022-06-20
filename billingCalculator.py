#Function to determine bill by iterating over all slabs
def billCalculator(slabsDictionaryList,totalUnits):
    billAmount = 0
    for slab in slabsDictionaryList:
        #if totalUnits is greater than highest of slab -- cost for that slab is calculated, then loop iterates to next slab
        #if it is the highest slab (as shown by -1) or totalUnits is less than highest of slab -- cost for that slab is calculated, then loop is exited
        if totalUnits>slab['high']:
            if slab['high']==-1:
                billAmount+=(totalUnits-slab['low'])*slab['unitCost']
                break
            else:
                billAmount+=(slab['high']-slab['low']+1)*slab['unitCost']
        else:
            billAmount+=(totalUnits-slab['low']+1)*slab['unitCost']
            break
    return billAmount

#Function to read input from billingInput.txt and call secondary function to create dictionaries
def inputFileReader():
    #mention path to input file below
    with open('billingInput.txt') as inputFile:
        slabs = inputFile.readlines()
        slabs = [slab.rstrip() for slab in slabs]
    slabsDictionaryList = createDictionaryList(slabs)
    return slabsDictionaryList

#Function to create dictionary per slab and append them to a list
#Also gets values of totalUnits from billingInput.txt file
def createDictionaryList(slabs):
    totalUnits = 0
    slabDictionaryList=[]
    for slab in slabs:
        if "Total Units:" in slab:
            totalUnits = int(slab.replace('Total Units: ','').strip())
            continue
        slabArray = slab.replace(',','').split(' ')
        slabDictionary = {"low":int(slabArray[0]),"high":int(slabArray[1]),"unitCost":int(slabArray[2])}
        slabDictionaryList.append(slabDictionary)
    #totalUnits is the number of units consumed
    #slabDictionaryList is an array containing one dictionary per slab
    #slabDictionaryList --> [{"low":x,"high":y,:"value":z},{"low":x,"high":y,:"value":z},{"low":x,"high":y,:"value":z}...]
    return totalUnits,slabDictionaryList


def main():
    #Read values from input file
    totalUnits,slabsDictionaryList = inputFileReader()
    #Copy value of totalUnits
    totalUnitsCopy=totalUnits
    #Calculate bill amount
    billAmount = billCalculator(slabsDictionaryList,totalUnits)
    #Print bill amount
    print("Bill is {} for {} units".format(billAmount,totalUnitsCopy))

if __name__ == "__main__":
    main()