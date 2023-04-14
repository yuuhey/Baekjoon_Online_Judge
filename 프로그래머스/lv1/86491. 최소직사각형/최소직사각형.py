def solution(sizes):
    w = []
    h = []
    for size in sizes:
        if size[0]<size[1]:
            size[0], size[1] = size[1], size[0]
        w.append(size[0])
        h.append(size[1])
    w_max = max(w)
    h_max = max(h)
    
    return w_max*h_max