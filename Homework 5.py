
lst2 = []
lst3 = []

def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return [] 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
    # Find the permutations for lst if there are more than 1 characters
    l = [] # empty list that will store current permutation 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 #ลองเล่นๆๆๆๆๆ
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
def jjoin (d):
    raum =""
    for j in range(0,len(d)):
        raum= raum + str(d[j])
    return int(raum)

#Get a number from user
for i in range(0,4) :
    get_num = int(input("Enter thenumber : "))
    lst2.append(get_num)


for p in permutation(lst2):
    lst3.append(jjoin(p))

print(max(lst3))