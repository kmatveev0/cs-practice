def winner(names, scores):
    n = 0
    for i in range(len(scores)):
        if scores[i] > scores[n]:
            n = scores[i]
    return names[n]

def average(scores):
    if len(scores) != 0:
        return float(f'{(sum(scores) / len(scores)):.2f}')
    elif len(scores) == 1:
        return float(scores[0])
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
    av = average(scores)
    for i in range(len(scores)):
        if scores[i] > av:
            l.append(names[i])
    return l
