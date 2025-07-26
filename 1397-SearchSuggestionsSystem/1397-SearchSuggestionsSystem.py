# Last updated: 7/26/2025, 2:32:11 PM
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Approach - First sort the products list, then with search word maintain a list of list and append it with new list for each char added to the searchWord Binary Search
        # nlogn + n*w + m
        # TC - O(nlogn + n + w + m) SC - O(m) where m is iterations for search word

        # sorting the products
        products.sort()
        n = len(products)
        result = []
        left = 0
        right = n - 1

        for i in range(len(searchWord)):
            c = searchWord[i]

            while left <= right and (len(products[left]) <= i or products[left][i] != c):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != c):
                right -= 1
            
            result.append([])

            remain = right - left + 1

            for j in range(min(3, remain)):
                result[-1].append(products[left + j])
        return result