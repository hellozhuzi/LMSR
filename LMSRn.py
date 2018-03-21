import math
#固定参与人数2
# e:事件创建者自行定义的整数
e=300
#选项个数
n=4

#准备金
def F():
    return e*math.log(n,math.e)
def C(qs):
    v=0
    for q in qs:
        v=v+math.exp(q/e)
    c= e*(math.log(v,math.e))
    return c
def P(qs,i):
    sum = 0
    for q in qs:
        sum = sum+math.exp(q/e)
    p = math.exp(qs[i]/e)/sum
    return p

#假设第一个正确，庄家盈利
def win(qs):
    w = C(qs)-qs[0]-F
    buyinfo = '购买比例'
    for q in qs:
        buyinfo+=str(int(q))+':'
    print(buyinfo,'盈利情况',w)
    return

def allWins(qs):
    print('F 成本', F())
    for q in qs:
        w = C(qs) - q - F()
        l = C(qs)-q
        print('剩余',l,'盈利',w)
    return


def test():

    # 当前选项个数
    qs = [110, 10, 10, 10]
    total = 0
    for q in qs:
        total = total + q
    print('假定亏算界', e, '选项', n, '售出份额', total, '第一个选项正确')
    i = 0
    for q in qs:
        print('选项', str(i + 1), '即时价格', P(qs, i))
        i = i + 1
    # 每个选项对应的盈利情况
    allWins(qs)

    return

test()
