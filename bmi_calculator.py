# -*- coding: utf-8 -*-
"""
程序 1：BMI 身体质量指数计算器
功能：输入身高（米）和体重（千克），计算 BMI，并按中国成人标准给出健康分类。
作者：Python 课程练习
"""


def calc_bmi(height, weight):
    """根据身高(米)和体重(千克)计算 BMI 值。"""
    return weight / (height * height)


def bmi_category(bmi):
    """按中国成人标准返回 BMI 分类。"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24.0:
        return "正常"
    elif bmi < 28.0:
        return "超重"
    else:
        return "肥胖"


def main():
    # 演示数据：也可改为从键盘输入
    height = 1.75  # 身高，单位：米
    weight = 68.0  # 体重，单位：千克

    # 若需手动输入，可取消下面两行注释：
    # height = float(input("请输入身高（米）："))
    # weight = float(input("请输入体重（千克）："))

    bmi = calc_bmi(height, weight)
    category = bmi_category(bmi)

    print("===== BMI 计算器 =====")
    print(f"身高：{height} 米")
    print(f"体重：{weight} 千克")
    print(f"BMI 指数：{bmi:.1f}")
    print(f"健康分类：{category}")


if __name__ == "__main__":
    main()
#（注：内容由AI生成）
