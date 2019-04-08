
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   maxi = 0
   if int_list is None:
      raise ValueError
   elif len(int_list) != 0:
      for i in int_list:
         if maxi < i:
            maxi = i
      return maxi
   else:
      return None

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
       raise ValueError
   elif len(int_list) == 0:
       return []
   elif len(int_list) == 1:
       n = [int_list[0]]
       return n
   else:
       return reverse_rec(int_list[1:]) + [int_list[0]]



def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
       raise ValueError
   elif len(int_list) == 0:
       return None
   elif target == int_list[(low + high) // 2]:
       return (low + high) // 2
   elif low == high:
       return None

   if target > int_list[(low + high) // 2]:
       low = (low + high) // 2 + 1
   elif target < int_list[(low + high) // 2]:
       high = (low + high) // 2 - 1
   #if low == high - 1:
       #return None
   return bin_search(target, low, high, int_list)

