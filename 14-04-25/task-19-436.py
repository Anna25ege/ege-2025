def f(x, y, s):
    if x + y >= 44:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x + y, y, s - 1),
         f(x, y + x, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 100) if f(11, s, 1)])
print('20)', [s for s in range(1, 100) if f(11, s, 2)])
print('21)', min([(abs(s - s2), s, s2) for s in range(1, 100) for s2 in range(1, 100) if f(s2, s, 3)]))
