def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq
