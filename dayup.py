import daydayup

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0,6]:
            dayup = 0.99*dayup
            
        else:
            dayup = (1+df)*dayup
            
    return dayup
dayfactor = 0.01
print(daydayup.daydayup())
while dayUP(dayfactor) < daydayup.daydayup():
    dayfactor += 0.001

print("工作日的努力参数是：{:.3f}".format(dayfactor))