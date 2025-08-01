# Last updated: 8/1/2025, 2:12:46 AM
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # fizz = "Fizz"
        # buzz = "Buzz"
        # result = [""]*n
        # print(n)
        # for i in range(n):
        #     temp = i+1
        #     if temp%3 == 0 and temp%5==0:
        #         result[i] ="FizzBuzz"
        #     elif temp%3 ==0:
        #         result[i] = "Fizz"
        #     elif temp%5 == 0:
        #         result[i] = "Buzz"
        #     else:
        #         result[i] = str(temp)
        # return result

        result = []
        print(n)
        for i in range(n):
            temp = i+1
            if temp%3 == 0 and temp%5==0:
                result.append("FizzBuzz")
            elif temp%3 ==0:
                result.append("Fizz")
            elif temp%5 == 0:
                result.append("Buzz")
            else:
                result.append(str(temp))
        return result
