import itertools
import random
import copy
Available = [3, 3, 2]
Max = [[7, 5, 3],
       [3, 2, 2],
       [9, 0, 2],
       [2, 2, 2],
       [4, 3, 3]]
Allocation = [[0, 1, 0],
              [2, 0, 0],
              [3, 0, 2],
              [2, 1, 1],
              [0, 0, 2]]
Need = [[7, 4, 3],
        [1, 2, 2],
        [6, 0, 0],
        [0, 1, 1],
        [4, 3, 1]]
Work=[0,0,0]
Finish=[0,0,0,0,0]  # 五个进程完成度
Request=[0,0,0]  # 需求矩阵

def security(num,number):
    b = copy.deepcopy(Finish)
    for j in range(0, 3):  #  改变Work   # 二次work 问题
        Work[j] = Work[j] + Allocation[num][j]
        if Available[j]<Need[num][j]:
            return False

    b[num]=1  # 假定num进程执行成功
    dome = 5
    for _ in itertools.product('01234', repeat=dome):  # 排列找顺序     有问题要改返回值永真
        for n in _:
            i = int(n)
            if 0 == b[i]:
                for k in range(0, 3):
                    if Need[i][k] <= Work[k]:
                        b[i] = 1
                        for w in range(0,3):
                            Work[w] = Work[w]+ Allocation[i][w]   # 成功加Work
                        dome = dome - 1
        if 0 == dome:
            break
    for c in range(0,5):  # 返回值判断是否全部为 true
        if 0==b[c]:
            return False
    return True

def bank(number):
    result=[[0, 0, 0],  # 结果矩阵
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
    while True:
        for i in range(0, number):  # 五个进程循环
            print("进程%d正在请求资源"%i)
            if 0 == Finish[i]:  # 循环进程
                MAX = Need[i][0]  # 找出需求最大值
                for m in range(0,3):
                    if MAX<Need[i][m]:
                        MAX = Need[i][m]

                for j in range(0, 3):  # 随机定义需求任务   # 随机不全面  若全面计算量过大  优化
                    Request[j] = random.randint(0, MAX)

                # for j in range(0, 3):  # 随机定义需求任务   # 随机不全面  若全面计算量过大  优化
                #     Request[j] = eval(input("请输入需求资源："))

                flag = 0 # 判断申请资源量是否合适
                for j in range(0, 3):
                    if Request[j] > Need[i][j]:
                        flag = 1
                        print("进程%d需求量大于所需资源！"%i)
                        break
                    if Request[j] > Available[j]:
                        flag = 1
                        print("进程%d需求量超过现有资源"%i)
                        break
                if 1 == flag:  # 该进程退出  下一个进程上
                    continue

                # 系统分配资源
                for k in range(0, 3):
                    Work[k] = Work[k] + Available[k]  # 改变Work等于现有资源
                    Available[k] = Available[k] - Request[k]
                    Allocation[i][k] = Allocation[i][k] + Request[k]
                    Need[i][k] = Need[i][k] - Request[k]

                # 安全验证
                print("安全验证",security(i,number))

                if False==security(i,number):
                    for s in range(0,3):
                        Work[s] = 0  # Work重新初始化
                        Available[s] = Available[s] + Request[s]
                        Allocation[i][s] = Allocation[i][s] - Request[s]
                        Need[i][s] = Need[i][s] + Request[s]
                else:  # 分配资源不代表执行成功
                    alloca = 0
                    for a in range(0,3):
                        if Allocation[i][a] <Need[i][k]:  # 分配资源合理但仍不够执行条件
                            print("资源分配不合理")
                            alloca = 1
                            break
                    if 0==alloca:
                        Finish[i] = 1
                        for t in range(0,3):  # 可用资源增加
                            Available[t] = Available[t] + Allocation[i][t]
                        print("进程%d执行成功" % i)
                        print("分配资源数",Request[0],Request[1],Request[2])
                        print("执行完进程%d后可利用资源数"%i,Available[0],Available[1],Available[2])

        # 结束验证
        check=0
        for s in range(0,number):
            if 1 == Finish[s]:
                check = check + 1
        if 5==check:
            print("执行成功！")
            break

if __name__ == '__main__':
    number=5
    bank(number);









