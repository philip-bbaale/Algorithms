def mergeTwoLists(l1, l2):
  l3 = []
  l1_index, l2_index = 0, 0
  while l1_index <= len(l1)-1 and l2_index <= len(l2)-1:
      if l1[l1_index] < l2[l2_index]:
          l3.append(l1[l1_index])
          l1_index +=1
      else:
          l3.append(l2[l2_index])
          l2_index +=1

  if l1_index < len(l1):
      l3 += l1[l1_index:]
  elif l2_index < len(l2):
      l3 += l2[l2_index:]

  return l3


l1 = [1,3, 4, 20]
l2 = [2,5,6, 7, 8]


res = mergeTwoLists(l1, l2)
print(res)


"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""