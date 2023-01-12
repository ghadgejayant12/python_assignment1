lst1=[1,2,3,4,5,6]
print('Element from 2nd to 5th position :",lst1[1:4])
# Slicing : Get element from second position to fifth position from list - [1, 2, 3, 4, 5, 6]
# Q1 above


lst2=["ab","abc","aba"]
for st in lst2:
     left=0
     right=len(st)-1
     ans=True
     while left<right:
          if st[left]!=st[right]:
              ans=False
              break
      print(st,':',ans)
# Condition : Check if string palindrome or not “ab”, “abc”, “aba”
# Q2 above

lst3=["aab","abc","def"]
for i in lst3:
    freq=dict()
    rep=False
    for x in i:
        if x in freq.keys() and freq[x]==1:
           rep=True
           break
        else:
           freq[x]=1
    if rep==False:
       print('There are no repeating characters in',i)
    else:
       print('There are repeating characters in',i)
# Loop : Check if string contains repeated characters “aab”, “abc”, “def”
#Q3 above   
 
def palindrome(st):
     left=0
     right=len(st)-1
     ans=True
     while left<right:
          if st[left]!=st[right]:
              ans=False
              break
      return ans
def slice_list(lst1):
      return lst1[1:4]
for i in lst2:
   print(i,':',palindrome(i))
print('2nd to 5th element slice',slice_list(lst1))
# Function : Convert all the above to function which can work on variadic number of arguments
# Q4 above
