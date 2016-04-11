def calcTwoSum(arr, limit):
   h = {}
   for i in range(len(arr)):
      complementIndex = h.get(limit - arr[i])
      if (complementIndex != None):
         return [i, complementIndex]
      else:
         h[arr[i]] = i
   return -1

if __name__ == "__main__":
    print calcTwoSum([2,-3,4,7,9], 6)
