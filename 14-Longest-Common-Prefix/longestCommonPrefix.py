class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = strs[0]
        pref_length = len(pref)

        for i in strs[1:]:
            while pref != i[0:pref_length]:
                pref_length -= 1
                if pref_length == 0:
                    return ""
                pref = pref [0:pref_length]
        return pref