class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        strings_1 = version1.split(".")
        strings_2 = version2.split(".")
        i = 0
        while i < min(len(strings_1), len(strings_2)):
            num1, num2 = strings_1[i], strings_2[i]
            n1, n2 = int(num1), int(num2)
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1

            i+=1
        if len(strings_1) == len(strings_2):
            return 0

        longer = strings_1 if len(strings_1) > len(strings_2) else strings_2
        while i < len(longer):
            n = int(longer[i])
            if n > 0:
                return 1 if longer == strings_1 else -1
            i += 1
        return 0
