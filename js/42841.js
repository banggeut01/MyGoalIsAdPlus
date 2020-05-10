function solution(s) {
    var answer = s.length;
    for (var i = 1; i <= parseInt(s.length / 2); i++) {
        var chars = ""
        var prev = ""
        var cnt = 0
        for (var j = 0; j < s.length; j += i) {
            // 문자열 같으면 
            if (s.substr(j, i) === prev) {
                // 반복 시작
                if (cnt === 0) {
                    cnt = 2
                }
                // 두번째 반복부터
                else {
                    cnt++
                }
            }
            // 문자열 다르면
            else {
                if (cnt != 0) {
                    chars += cnt + ""
                }
                chars += prev
                prev = s.substr(j, i)
                cnt = 0
            }
        }
        if (cnt != 0) {
            chars += cnt + ""
        }
        chars += prev
        answer = Math.min(answer, chars.length)
    }
    return answer;
}

console.log(solution("3"))