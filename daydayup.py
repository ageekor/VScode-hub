def daydayup():
    dayup = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup = 1.01*dayup
        else:
            dayup = 1.01*dayup
    return dayup

print("{:.3f}".format(daydayup()))
