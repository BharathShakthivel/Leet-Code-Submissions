class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Greedy Algorithm
        #Edge case - What if there are no plants at all
        if n==0:
            return True
        #Three Checks
        #Step 1 - The plant should be empty
        #Step 2 - Checking left neighbour -  If it is at the start or the element before is free to plant
        #Step 3 - Checking Right neighbour = If it is at the end or the next element is free to plant
        #If all satisfy we will plant the tree and decrement also we check if there are no plants to plant we just exit the loop and return True
        #If at the end there are still plants to plant iee., n>0, we just return False 
        for i in range(0,len(flowerbed)):
            if flowerbed[i]==0:
                if i == 0 or flowerbed[i-1]==0:
                    if i == len(flowerbed)-1 or flowerbed[i+1]==0:
                        flowerbed[i] = 1
                        n-=1 
                        if n==0:
                            return True
        return False


