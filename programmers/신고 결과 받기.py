def solution(id_list, report, k):
    answer = [0] * len(id_list) 
    dict = {}
    for id in id_list:
        dict[id] = []
    for r in report:
        user = r.split()[0]
        reported = r.split()[1]
        
        tmp = dict.get(reported) 
        if user not in tmp:
            dict[reported].append(user)
    
    for key in dict.keys():
        if len(dict[key]) >= k:
            for a in dict[key]:
                idx = id_list.index(a)
                answer[idx] += 1
    
    return answer

#ref
def solution(id_list, report, k):
    answer = [0] * len(id_list) 
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports.[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer