
#total count of the string calculated

def count(data):
    count=0

    for i in data:
        print(i)
        count=count+1

    return count


data="ramakrishnacollege"

print(count(data))


#2.To count the duplicate letters in string

def count_duplicate(duplicate):
      dataset={}

      for i in duplicate:
          if i not in dataset:
            dataset[i]=0
          dataset[i]=dataset[i]+1
      return dataset

duplicate="ramakrishnacollege"

print(sorted(count_duplicate(duplicate).items()))


#sort a words in order without using sort method
#unsorted=["s","a","r","a","n"]
def sortletters(unsorted):

    for l in range(len(unsorted)-1):
        for m in range(l+1,len(unsorted)):
            if unsorted[l]>unsorted[m]:
                temp=unsorted[l]
                unsorted[l]=unsorted[m]
                unsorted[m]=temp

    print("sorted_arr:{}".format(unsorted))

unsorted=["s","a","r","e","n"]

sortletters(unsorted)

print(unsorted)
