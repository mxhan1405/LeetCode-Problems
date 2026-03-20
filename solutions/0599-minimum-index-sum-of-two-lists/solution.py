class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Map each restaurant in list1 to its index
        lookup = {res: i for i, res in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        # Check restaurants in list2
        for j, res in enumerate(list2):
            if res in lookup:
                current_sum = j + lookup[res]
                
                # If we found a new, smaller index sum, reset the result list
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [res]
                # If it matches the current minimum, add it to the list
                elif current_sum == min_sum:
                    result.append(res)
                    
        return result

