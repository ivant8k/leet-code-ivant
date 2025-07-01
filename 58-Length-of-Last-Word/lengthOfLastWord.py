class Solution(object):
    def lengthOfLastWord(self, s):
        pisah = s.split(' ')
        i = -1
        while pisah[i] == '':
            i -=1
        return len(pisah[i])
        