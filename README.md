# My-Python-Learning-Journey

## 一、项目简介

本仓库用于记录我在 Python 课程学习过程中编写的练习程序，目前包含两个基础小工具：一个 BMI 身体质量指数计算器，一个学生成绩统计小工具。项目主要解决两类日常计算问题：根据身高体重判断体重是否处于健康范围，以及对一组课程成绩进行统计与排序。所有程序均使用 Python 3 编写，功能明确、代码完整，可直接运行。

## 二、文件说明

| 文件名 | 用途 |
| --- | --- |
| `bmi_calculator.py` | 输入身高（米）和体重（千克），计算 BMI 指数，并按中国成人标准给出健康分类。 |
| `grade_manager.py` | 录入若干门课程成绩，计算平均分、最高分、最低分，并按从高到低排序输出。 |

## 三、代码说明

### 1. `bmi_calculator.py`

- `calc_bmi(height, weight)`：根据身高和体重计算 BMI，公式为体重除以身高的平方。

```python
def calc_bmi(height, weight):
    return weight / (height * height)
```

- `bmi_category(bmi)`：按中国成人标准对 BMI 进行分类，依次判断偏瘦（小于 18.5）、正常（18.5～23.9）、超重（24.0～27.9）和肥胖（不低于 28.0）。

```python
def bmi_category(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24.0:
        return "正常"
    elif bmi < 28.0:
        return "超重"
    else:
        return "肥胖"
```

- `main()`：组织输入数据、调用计算与分类函数，并格式化输出结果。

### 2. `grade_manager.py`

- `analyze_grades(grades)`：接收成绩列表，返回平均分、最高分、最低分以及降序排列后的成绩列表，分别使用 `sum`、`max`、`min` 和 `sorted` 实现。

```python
def analyze_grades(grades):
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    sorted_desc = sorted(grades, reverse=True)
    return average, highest, lowest, sorted_desc
```

- `main()`：提供示例成绩，调用统计函数后逐项输出课程成绩与各项统计结果。

## 四、运行环境

- 编程语言：Python 3
- 运行方式：在终端中进入仓库目录，执行对应命令即可，例如：

```bash
python bmi_calculator.py
python grade_manager.py
```

## 五、学习心得与规划

在浏览 GitHub 上其他 Python 项目并完成本次 README 编写的过程中，我对个人项目管理和技能展示有了几点启发。首先，一个清晰的 README 是项目的门面：别人进入仓库后，最先看到的就是项目简介、文件结构和运行方式，说明写得规范，项目才容易被理解和复用。其次，规范的目录与命名、分阶段的提交记录，能体现有条理的开发习惯，也方便自己日后回溯代码的演变过程。再次，把解题思路和关键代码注释清楚，不仅是写给别人看，也是对自己学习过程的梳理。

这让我意识到，GitHub 不只是存放代码的网盘，更是展示个人编程能力和学习轨迹的窗口。未来我计划把这个仓库作为 Python 学习的长期记录：每完成一个课堂练习或小项目，就及时上传对应的源代码和简要说明；按阶段补充学习笔记、错题与改进记录；定期整理 README，更新已掌握的知识点和待办内容。遇到有价值的练习，再补充测试用例和注释，逐步积累成一份完整、可展示的个人学习作品集。
