# ka3.py

def solution(gems):
    uniqe_gems = set(gems)
    N = len(uniqe_gems)
    gem_dict = {}
    for gem in uniqe_gems:
        gem_dict[gem] = 1e+10

    min_value = 1e+10
    ix = 0
    flag = True
    set_flag = True
    tmp_set = set()
    while flag:
        gem_dict[gems[ix]] = ix

        if ix == 0:
            _min = [0, gems[ix]]

        if set_flag:
            tmp_set.add(gems[ix])

        if gems[ix] == _min[1]:
            tmp = min(gem_dict.items(), key=lambda x: x[1])
            _min = [tmp[1], tmp[0]]
        if len(tmp_set) == N:
            set_flag = False
            _max = ix
            diff = _max - _min[0]
            if diff < min_value:
                min_value = diff
                answer = [_min[0] + 1, _max + 1]
                if min_value == N:
                    flag = False

        ix += 1
        if ix == len(gems):
            flag = False

    return answer

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))