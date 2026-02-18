
possible_hours = [1,2,4,8]
possible_minutes = [1,2,4,8,16,32]

class Solution:
    def readBinaryWatch(self, turnedOn: int):
        possible_strings = generateStrings(turnedOn, 10)
        ans = []
        for s in possible_strings:
            mins, hours = getTime(s)
            if hours is not None:
                hour_string = str(hours)
                mins_string = f"{mins:02d}"
                full_string = hour_string + ":" + mins_string
                ans.append(full_string)
        return ans

def getTime(s):
    hours = 0
    minutes = 0
    for i, char in enumerate(s):
        if i <= 3:
            if char == "1":
                hours += possible_hours[i]
        else:
            if char == "1":
                minutes += possible_minutes[i-4]
    if hours > 11 or minutes > 59:
        return None, None
    return minutes, hours

def generateStrings(numOnes, L):
    # generates all strings of length L with numOnes 1s in them.
    if numOnes == 0:
        return ["0"*L]
    
    ans = []
    for i in range(0, L - numOnes+1):
        possible_string = "0"*i
        possible_string += "1"
        remaining_strings = generateStrings(numOnes-1, L-i-1)
        for s in remaining_strings:
            ans.append(possible_string + s)
    
    return ans

mySol = Solution()
print(sorted(mySol.readBinaryWatch(5)))