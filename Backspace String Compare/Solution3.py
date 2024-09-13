class Solution3:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def validChar(str, index):
            backspace = 0
            
            while index >= 0:

                if backspace == 0 and str[index] != '#':
                    break
                elif str[index] == '#':
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1

            return index

        s_index, t_index = len(s) - 1, len(t) - 1
        while s_index >= 0 or t_index >= 0:
            s_index = validChar(s, s_index)
            t_index = validChar(t, t_index)

            char_s = s[s_index] if s_index >= 0 else ''
            char_t = t[t_index] if t_index >= 0 else ''

            if char_s != char_t:
                return False
            
            s_index -= 1
            t_index -= 1
            
        return True