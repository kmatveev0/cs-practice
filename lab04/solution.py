names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names, scores):
    n = 0
    m = 0
    for i in range(len(scores)):
        if scores[i] > m:
            m = scores[i]
            n = i
    return names[n]

def average(scores):
    if scores != 0:
        return f'{(sum(scores) / len(scores)):.2f}'
    else:
        return 0.0

def ranking(names, scores):
    n = len(names)
    sorted_names = names
    sorted_scores = scores
    for i in range(len(scores)-1):
        if sorted_scores[i] < sorted_scores[i + 1]:
            sorted_scores[i], sorted_scores[i + 1] = sorted_scores[i + 1], sorted_scores[i]
            sorted_names[i], sorted_names[i + 1] = sorted_names[i + 1], sorted_names[i]
    return sorted_names

def above_average(names, scores):
    l = []
    av = float(average(scores))
    for i in range(len(scores)):
        if scores[i] > av:
            l.append(names[i])
    return l

print(winner(names,scores))
print(average(scores))
print(ranking(names,scores))
print(above_average(names,scores))
