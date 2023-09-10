import requests
import json
import tkinter as tk
from tkinter import ttk
import pandas as pd
import time


def decoding_score(data):
    score_data = data["data"]
    subjects = score_data["scoreSortList"]
    student_score = {
        "学校": score_data["xueXiao"],
        "考生姓名": score_data["xingMing"],
        "班级": score_data["banJi"],
        "准考证号": score_data["kaoHao"],
        "考试成绩": [],
        "班级考试情况": [],
        "学校考试情况": [],
        "联考考试情况": [],
        "分数分布情况": [],
    }
    for subject in subjects:
        student_score["考试成绩"].append({
            "科目": subject["subjectName"],
            "分数": subject["fenShu"],
            "班级排名": subject["banMing"],
            "学校排名": subject["xiaoMing"],
            "联考排名": subject["jiMing"],
            "已选科目": subject["examinationFlag"]
        })

    for subject in score_data["classAvgInfo"]:
        student_score["班级考试情况"].append({
            "科目": subject["subjectName"],
            "平均分": subject["avg"],
            "最高分": subject["max"],

        })

    for subject in score_data["schoolAvgInfo"]:
        student_score["学校考试情况"].append({
            "科目": subject["subjectName"],
            "平均分": subject["avg"],
            "最高分": subject["max"],

        })

    for subject in score_data["projectAvgInfo"]:
        student_score["联考考试情况"].append({
            "科目": subject["subjectName"],
            "平均分": subject["avg"],
            "最高分": subject["max"],

        })

    for number in score_data["scoreRangeList"]:
        student_score["分数分布情况"].append({
            "区间": number["range"],
            "人数": number["count"]
        })

    return student_score


def dicttrans(data):
    result = {}
    for dict_item in data:
        for key, value in dict_item.items():
            if key in result:
                result[key].append(value)
            else:
                result[key] = [value]
    return result


def score_single(datasets):
    results = []

    for data in datasets:
        score = data["考试成绩"]
        result = {
            "学校": data["学校"],
            "考生姓名": data["考生姓名"],
            "班级": data["班级"],
            "准考证号": data["准考证号"],

            "总分": score[0]["分数"],
            "总分-班级排名": score[0]["班级排名"],
            "总分-全校排名": score[0]["学校排名"],
            "总分-联考排名": score[0]["联考排名"],
            "总分-全班平均分": data["班级考试情况"][0]["平均分"],
            "总分-全校平均分": data["学校考试情况"][0]["平均分"],
            "总分-联考平均分": data["联考考试情况"][0]["平均分"],
            "总分-全班最高分": data["班级考试情况"][0]["最高分"],
            "总分-全校最高分": data["学校考试情况"][0]["最高分"],
            "总分-联考最高分": data["联考考试情况"][0]["最高分"],

            "语文": score[1]["分数"],
            "语文-班级排名": score[1]["班级排名"],
            "语文-全校排名": score[1]["学校排名"],
            "语文-联考排名": score[1]["联考排名"],
            "语文-全班平均分": data["班级考试情况"][1]["平均分"],
            "语文-全校平均分": data["学校考试情况"][1]["平均分"],
            "语文-联考平均分": data["联考考试情况"][1]["平均分"],
            "语文-全班最高分": data["班级考试情况"][1]["最高分"],
            "语文-全校最高分": data["学校考试情况"][1]["最高分"],
            "语文-联考最高分": data["联考考试情况"][1]["最高分"],

            "数学": score[2]["分数"],
            "数学-班级排名": score[2]["班级排名"],
            "数学-全校排名": score[2]["学校排名"],
            "数学-联考排名": score[2]["联考排名"],
            "数学-全班平均分": data["班级考试情况"][2]["平均分"],
            "数学-全校平均分": data["学校考试情况"][2]["平均分"],
            "数学-联考平均分": data["联考考试情况"][2]["平均分"],
            "数学-全班最高分": data["班级考试情况"][2]["最高分"],
            "数学-全校最高分": data["学校考试情况"][2]["最高分"],
            "数学-联考最高分": data["联考考试情况"][2]["最高分"],

            "外语": score[3]["分数"],
            "外语-班级排名": score[3]["班级排名"],
            "外语-全校排名": score[3]["学校排名"],
            "外语-联考排名": score[3]["联考排名"],
            "外语-全班平均分": data["班级考试情况"][3]["平均分"],
            "外语-全校平均分": data["学校考试情况"][3]["平均分"],
            "外语-联考平均分": data["联考考试情况"][3]["平均分"],
            "外语-全班最高分": data["班级考试情况"][3]["最高分"],
            "外语-全校最高分": data["学校考试情况"][3]["最高分"],
            "外语-联考最高分": data["联考考试情况"][3]["最高分"],

            "政治": score[4]["分数"],
            "政治-班级排名": score[4]["班级排名"],
            "政治-全校排名": score[4]["学校排名"],
            "政治-联考排名": score[4]["联考排名"],
            "政治-全班平均分": data["班级考试情况"][4]["平均分"],
            "政治-全校平均分": data["学校考试情况"][4]["平均分"],
            "政治-联考平均分": data["联考考试情况"][4]["平均分"],
            "政治-全班最高分": data["班级考试情况"][4]["最高分"],
            "政治-全校最高分": data["学校考试情况"][4]["最高分"],
            "政治-联考最高分": data["联考考试情况"][4]["最高分"],

            "历史": score[5]["分数"],
            "历史-班级排名": score[5]["班级排名"],
            "历史-全校排名": score[5]["学校排名"],
            "历史-联考排名": score[5]["联考排名"],
            "历史-全班平均分": data["班级考试情况"][5]["平均分"],
            "历史-全校平均分": data["学校考试情况"][5]["平均分"],
            "历史-联考平均分": data["联考考试情况"][5]["平均分"],
            "历史-全班最高分": data["班级考试情况"][5]["最高分"],
            "历史-全校最高分": data["学校考试情况"][5]["最高分"],
            "历史-联考最高分": data["联考考试情况"][5]["最高分"],

            "地理": score[6]["分数"],
            "地理-班级排名": score[6]["班级排名"],
            "地理-全校排名": score[6]["学校排名"],
            "地理-联考排名": score[6]["联考排名"],
            "地理-全班平均分": data["班级考试情况"][6]["平均分"],
            "地理-全校平均分": data["学校考试情况"][6]["平均分"],
            "地理-联考平均分": data["联考考试情况"][6]["平均分"],
            "地理-全班最高分": data["班级考试情况"][6]["最高分"],
            "地理-全校最高分": data["学校考试情况"][6]["最高分"],
            "地理-联考最高分": data["联考考试情况"][6]["最高分"],

            "物理": score[7]["分数"],
            "物理-班级排名": score[7]["班级排名"],
            "物理-全校排名": score[7]["学校排名"],
            "物理-联考排名": score[7]["联考排名"],
            "物理-全班平均分": data["班级考试情况"][7]["平均分"],
            "物理-全校平均分": data["学校考试情况"][7]["平均分"],
            "物理-联考平均分": data["联考考试情况"][7]["平均分"],
            "物理-全班最高分": data["班级考试情况"][7]["最高分"],
            "物理-全校最高分": data["学校考试情况"][7]["最高分"],
            "物理-联考最高分": data["联考考试情况"][7]["最高分"],

            "化学": score[8]["分数"],
            "化学-班级排名": score[8]["班级排名"],
            "化学-全校排名": score[8]["学校排名"],
            "化学-联考排名": score[8]["联考排名"],
            "化学-全班平均分": data["班级考试情况"][8]["平均分"],
            "化学-全校平均分": data["学校考试情况"][8]["平均分"],
            "化学-联考平均分": data["联考考试情况"][8]["平均分"],
            "化学-全班最高分": data["班级考试情况"][8]["最高分"],
            "化学-全校最高分": data["学校考试情况"][8]["最高分"],
            "化学-联考最高分": data["联考考试情况"][8]["最高分"],

            "生物": score[9]["分数"],
            "生物-班级排名": score[9]["班级排名"],
            "生物-全校排名": score[9]["学校排名"],
            "生物-联考排名": score[9]["联考排名"],
            "生物-全班平均分": data["班级考试情况"][9]["平均分"],
            "生物-全校平均分": data["学校考试情况"][9]["平均分"],
            "生物-联考平均分": data["联考考试情况"][9]["平均分"],
            "生物-全班最高分": data["班级考试情况"][9]["最高分"],
            "生物-全校最高分": data["学校考试情况"][9]["最高分"],
            "生物-联考最高分": data["联考考试情况"][9]["最高分"],




        }
        results.append(result)

    return results


# 创建一个持久化会话
session = requests.Session()

# 设置 cookie
cookies = {'uid': '4148359661949870080'}
session.cookies.update(cookies)

# 设置UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
session.headers.update(headers)

# 获取各个联考及其productid
# 发送请求
product_json = session.post(
    'http://score.tydlk.com/scorequery/goldentouch/api/Project/ListForQueryScore').json()["data"]

# 设定空列表存放
products = []
# 解析json
for product in product_json:
    products.append(
        {"id": product["id"],
         "name": product["projectName"],
         "creat_time": product["createdOn"]
         }
    )


# 设定配置文件变量
spider_config = {}


# 用户界面
root = tk.Tk()
root.title("天一大联考成绩查询-批量")


# 创建选项
options = products
# 设定变量
productid_selected = tk.StringVar()
productname_selected = tk.StringVar()

# 定义回调函数


def on_option_selected(event):
    global product_id_selected
    selected_item = options[combobox.current()]  # 获取当前选择的选项
    productid_selected.set(selected_item['id'])
    # 将选项的ID存储到productid_selected变量中
    productname_selected.set(selected_item['name'])
    product_id_selected = productid_selected.get()


def submit():
    try:
        global spider_config
        start_range = int(start_range_entry.get())
        end_range = int(end_range_entry.get())
        # school_code = int(school_code_entry.get())
        # class_number = int(classnumber_entry.get())

        # 更新spider_config
        spider_config = {
            "start": start_range,
            "end": end_range,
            # "schoolcode": school_code,
            # "classnumber": class_number
        }
        print(spider_config)

    except:
        tk.messagebox.showerror("错误", "发生了一个错误！")


def start():
    global spider_config

    number = []
    for i in range(spider_config["start"], spider_config["end"], 1):
        print("当前考生：",i)
        get_score_post_data = {
            "projectId": product_id_selected,
            "candidateNumber": i,
            "historyRangeId": 16,
            "type": 0,
            "className": "",
            "needInfoFalg": 1
        }
        try:
            score_response = session.post(
                url="http://score.tydlk.com/scorequery/goldentouch/api/QueryScoreOnlie/ScoreQuery", json=get_score_post_data)
            data = score_response.json()
            print(data)
            number.append(decoding_score(data))
        except:
            print("AUTO SKIP")
    progress_bar['value'] = (i + 1) * 10
    root.update()

    results = score_single(number)
    result = dicttrans(results)
    c = pd.DataFrame(result)
    c.to_excel("data.xlsx", index=0)


# 定义选择框
combobox_label = tk.Label(text="选择考试")
combobox_label.pack()
combobox = ttk.Combobox(root, textvariable=productname_selected, values=[
                        item['name'] for item in options])
combobox['state'] = 'readonly'  # 设置为只读模式不允许手动输入
combobox.bind("<<ComboboxSelected>>", on_option_selected)  # 绑定选择变化的回调函数
combobox.pack()

# 起始范围输入框
start_range_label = tk.Label(text="开始范围")
start_range_label.pack()
start_range_entry = tk.Entry()
start_range_entry.pack()


# 终止范围输入框
end_range_label = tk.Label(text="结束范围")
end_range_label.pack()
end_range_entry = tk.Entry()
end_range_entry.pack()

# # 班级人数输入框
# school_code_label = tk.Label(text="学校代号")
# school_code_label.pack()
# school_code_entry = tk.Entry()
# school_code_entry.pack()

# # 班级人数输入框
# classnumber_label = tk.Label(text="班级人数")
# classnumber_label.pack()
# classnumber_entry = tk.Entry()
# classnumber_entry.pack()

# 提交按钮
submit_button = tk.Button(text="提交", command=submit)
submit_button.pack()

# 进度条
progress_bar = ttk.Progressbar(root, mode='determinate', length=200)  # 创建进度条
progress_bar.pack()

# 开始按钮
start_button = tk.Button(text="开始处理", command=start)
start_button.pack()

# 创建一个文本框
text_box = tk.Label(root, height=1,text="天一大联考成绩查询系统 chenleqi767")
text_box.pack()


# 显示主界面
root.mainloop()
