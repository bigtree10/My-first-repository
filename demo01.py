print("这是develop中的demo01")


def avg(num1, num2):
    """计算两个数字的平均数"""
    avg_num = (num1+num2)/2
    print(f"{num1}和{num2}的平均数是{avg_num}")


new_num1 = float(input("请输入第一个数字："))
new_num2 = float(input("请输入第二个数字："))
avg(new_num1, new_num2)
