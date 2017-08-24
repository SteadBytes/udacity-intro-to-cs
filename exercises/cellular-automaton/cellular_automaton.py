def cellular_automaton(source, pattern_num, n):
    patterns = get_patterns(pattern_num)
    for i in range(n):
        result = ''
        for k in range(len(source)):
            p = source[k - 1] + source[k] + source[(i + 1) % n]
            result += patterns[p]
        source = result
    return result


def get_patterns(pattern_num):
    patterns = {}
    for i in range(7, -1, -1):
        if pattern_num // (2**i) == 1:
            patterns[ruleset[i]] = 'x'
            pattern_num -= 2**i
        else:
            patterns[ruleset[i]] = '.'
    return patterns


ruleset = ['...',  '..x',  '.x.', '.xx',
           'x..',  'x.x',  'xx.', 'xxx']
print(cellular_automaton('.x.x.x.x.', 17, 2))
#>>> xxxxxxx..
print(cellular_automaton('.x.x.x.x.', 249, 3))
# #>>> .x..x.x.x
# print cellular_automaton('...x....', 125, 1)
# #>>> xx.xxxxx
# print cellular_automaton('...x....', 125, 2)
# #>>> .xxx....
# print cellular_automaton('...x....', 125, 3)
# #>>> .x.xxxxx
# print cellular_automaton('...x....', 125, 4)
# #>>> xxxx...x
# print cellular_automaton('...x....', 125, 5)
# #>>> ...xxx.x
# print cellular_automaton('...x....', 125, 6)
# #>>> xx.x.xxx
# print cellular_automaton('...x....', 125, 7)
# #>>> .xxxxx..
# print cellular_automaton('...x....', 125, 8)
# #>>> .x...xxx
# print cellular_automaton('...x....', 125, 9)
# #>>> xxxx.x.x
# print cellular_automaton('...x....', 125, 10)
# #>>> ...xxxxx
