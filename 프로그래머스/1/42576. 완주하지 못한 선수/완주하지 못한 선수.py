def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    else:
        answer=participant[-1]
            
    return answer