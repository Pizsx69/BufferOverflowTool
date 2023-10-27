#usage python searchinrop.py csrop.txt "push esp" "pop" 
import argparse
import numpy
 

list = []
def Sorting(lst):
 
    # list for storing the length of each string in list 
    lenlist=[]   
    for x in lst:
         lenlist.append(len(x))     
 
    # return a list with the index of the sorted
    # items in the list
    sortedindex = numpy.argsort(lenlist)  
 
    # creating a dummy list where we will place the 
    # word according to the sortedindex list 
    lst2 = ['dummy']*len(lst)   
 
    # print(sortedindex,lenlist)
    for i in range(len(lst)):    
 
        # placing element in the lst2 list by taking the
        # value from original list lst where it should belong 
        # in the sorted list by taking its index from sortedindex
        lst2[i] = lst[sortedindex[i]]     
                                         
    return lst2
     
# Driver code



def search_strings_in_file(file_path, search_strings):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if all(search_string in line for search_string in search_strings):
                    list.append(line)
                    #print(line, end='')

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Search for lines containing all specified strings in a text file")
    parser.add_argument("file_path", help="Path to the text file")
    parser.add_argument("search_strings", nargs='+', help="Strings to search for in the file (all must be present)")

    args = parser.parse_args()
    file_path = args.file_path
    search_strings = args.search_strings

    search_strings_in_file(file_path, search_strings)
    p = Sorting(list)
    for x in p:
        print(x,end='')

