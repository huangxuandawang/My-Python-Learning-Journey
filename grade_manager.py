# -*- coding: utf-8 -*-
"""
程序 2：学生成绩统计小工具
功能：录入若干门课程成绩，计算平均分、最高分、最低分，并按从高到低排序输出。
作者：Python 课程练习
"""


def analyze_grades(grades):
    """返回平均分、最高分、最低分及降序排列的成绩列表。"""
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    sorted_desc = sorted(grades, reverse=True)
    return average, highest, lowest, sorted_desc


def main():
    # 示例成绩：也可改为循环从键盘录入
    grades = [88, 76, 95, 62, 81, 90]
    courses = ["语文", "数学", "英语", "物理", "化学", "生物"]

    average, highest, lowest, sorted_desc = analyze_grades(grades)

    print("===== 学生成绩统计 =====")
    print("课程与成绩：")
    for course, score in zip(courses, grades):
        print(f"  {course}：{score} 分")

    print(f"\n成绩门数：{len(grades)}")
    print(f"平均分：{average:.1f} 分")
    print(f"最高分：{highest} 分")
    print(f"最低分：{lowest} 分")
    print(f"从高到低排序：{sorted_desc}")


if __name__ == "__main__":
    main()
