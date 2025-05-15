def solution(answers):
    no_1 = [1,2,3,4,5]
    no_2 = [2,1,2,3,2,4,2,5]
    no_3 = [3,3,1,1,2,2,4,4,5,5]
    no_1 = no_1*2000
    no_2 = no_2*1250
    no_3 = no_3*1000
    answer1=0
    for i in range(len(answers)):
        if no_1[i] == answers[i]:
            answer1 += 1
    answer2=0
    for i in range(len(answers)):
        if no_2[i] == answers[i]:
            answer2 += 1
    answer3=0
    for i in range(len(answers)):
        if no_3[i] == answers[i]:
            answer3 += 1
    answer_dict={1 : answer1, 2: answer2, 3: answer3}
    answer_max = max(answer_dict.values())
    answer=[]
    for k, v in answer_dict.items():
        if v == answer_max:
            answer.append(k)
    answer.sort()
    return answer