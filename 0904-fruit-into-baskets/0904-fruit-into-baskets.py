class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        my_dict = {}
        left = 0
        right = 0
        maximum_fruits = 0

        while right < n:
            #First we are adding fruits in dictionary(basket).
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1
            
            #here we are checking if our dicitonary(basket) have more than two types of fruits.
            if len(my_dict) > 2:
                my_dict[fruits[left]] -= 1 #here we are decreasing the fruits value in dicitonary(basket).
                if my_dict[fruits[left]] == 0: #here we are checking if our fruit value became zero(0).
                    del my_dict[fruits[left]] #remove it from dicitionary(basket).
                left += 1
            
            if len(my_dict) <= 2:
                maximum_fruits = max(maximum_fruits, right - left + 1)

            right += 1
        
        return maximum_fruits
      