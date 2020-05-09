# ka1.py
xy  = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    10: (3, 0),
    0: (3, 1),
    11: (3, 2)
}
left = [1, 4, 7]
right = [3, 6, 9]
def solution(numbers, hand):
    answer = ''
    l, r = 10, 11
    for num in numbers:
        if num in left:
            l = num
            answer += "L"
        elif num in right:
            r = num
            answer += "R"
        else:
            dx, dy = xy[num]
            lx, ly = xy[l]
            rx, ry = xy[r]
            left_dist = abs(lx - dx) + abs(ly - dy)
            right_dist = abs(rx - dx) + abs(ry - dy)
            if left_dist < right_dist:
                l = num
                answer += "L"
            elif left_dist > right_dist:
                r = num
                answer += "R"
            else:
                if hand == "left":
                    l = num
                    answer += "L"
                else:
                    r = num
                    answer += "R"

    return answer

# numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"
# numbers, hand =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"
numbers, hand =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"
print(solution(numbers, hand))