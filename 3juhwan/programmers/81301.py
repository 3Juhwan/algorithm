digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def solution(s):
    answer = ''
    while s:
        if s[0] in '0123456789':
            answer += s[0]
            s = s[1:]
            continue
        for x in digit:
            if len(s) >= len(x) and s[:len(x)] == x:
                answer += digit[x]
                s = s[len(x):]
                break
    return int(answer)