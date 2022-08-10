import re
def solution(new_id):
    answer = ""
    #1,2
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
	#3
    answer = re.sub('\.\.+', '.', answer)
    #4
    answer = answer.strip(".")
    #5
    if len(answer) == 0:
        answer = "a"
    #6
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip(".")
   	#7
    while len(answer) < 3:
    	answer += answer[-1]
    return answer