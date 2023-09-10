import json 

score_data_raw = {"code":200,"msg":"","requestUri":"","traceIdentifier":"","data":{"lkid":576,"kaoHao":"554610221503","xingMing":"陈乐祺","xueXiao":"三亚市第一中学","banJi":"15","type":0,"moreRateOfMineClass":80,"isCheckSmallQuestion":1,"isCheckStandScore":1,"isCheckHistoryScore":1,"historyScoreRangeID":16,"isCheckAssignScore":0,"scoreSortList":[{"subjectName":"总分","fenShu":401.00,"jiMing":5753,"xiaoMing":462,"banMing":10,"examinationFlag":1},{"subjectName":"语文","fenShu":83.00,"jiMing":14810,"xiaoMing":734,"banMing":40,"examinationFlag":1},{"subjectName":"数学","fenShu":38.00,"jiMing":22798,"xiaoMing":870,"banMing":34,"examinationFlag":1},{"subjectName":"外语","fenShu":110.00,"jiMing":3014,"xiaoMing":185,"banMing":2,"examinationFlag":1},{"subjectName":"政治","fenShu":0.00,"jiMing":20517,"xiaoMing":335,"banMing":1,"examinationFlag":0},{"subjectName":"历史","fenShu":0.00,"jiMing":17258,"xiaoMing":351,"banMing":32,"examinationFlag":0},{"subjectName":"地理","fenShu":76.00,"jiMing":50,"xiaoMing":9,"banMing":2,"examinationFlag":1},{"subjectName":"物理","fenShu":57.00,"jiMing":3761,"xiaoMing":194,"banMing":3,"examinationFlag":1},{"subjectName":"化学","fenShu":37.00,"jiMing":10227,"xiaoMing":528,"banMing":17,"examinationFlag":1},{"subjectName":"生物","fenShu":0.00,"jiMing":29348,"xiaoMing":554,"banMing":2,"examinationFlag":0}],"historyScoreSortList":[{"subjectName":"总分","scoreList":[{"projectId":544,"projectName":"22-23海南高一一联","projectStudentCount":36882,"score":{"subjectName":"总分","fenShu":508.00,"jiMing":3999,"xiaoMing":412,"banMing":4,"examinationFlag":1},"createOn":"2023-02-20T23:23:13.263"},{"projectId":576,"projectName":"22-23海南高一下期末","projectStudentCount":49598,"score":{"subjectName":"总分","fenShu":401.00,"jiMing":5753,"xiaoMing":462,"banMing":10,"examinationFlag":1},"createOn":"2023-07-15T12:23:11.667"}]},{"subjectName":"语文","scoreList":[{"projectId":544,"projectName":"22-23海南高一一联","projectStudentCount":36080,"score":{"subjectName":"语文","fenShu":92.00,"jiMing":1547,"xiaoMing":142,"banMing":2,"examinationFlag":1},"createOn":"2023-02-20T23:23:13.263"},{"projectId":576,"projectName":"22-23海南高一下期末","projectStudentCount":48818,"score":{"subjectName":"语文","fenShu":83.00,"jiMing":14810,"xiaoMing":734,"banMing":40,"examinationFlag":1},"createOn":"2023-07-15T12:23:11.667"}]},{"subjectName":"数学","scoreList":[{"projectId":544,"projectName":"22-23海南高一一联","projectStudentCount":35922,"score":{"subjectName":"数学","fenShu":43.00,"jiMing":10075,"xiaoMing":698,"banMing":20,"examinationFlag":1},"createOn":"2023-02-20T23:23:13.263"},{"projectId":576,"projectName":"22-23海南高一下期末","projectStudentCount":47121,"score":{"subjectName":"数学","fenShu":38.00,"jiMing":22798,"xiaoMing":870,"banMing":34,"examinationFlag":1},"createOn":"2023-07-15T12:23:11.667"}]},{"subjectName":"外语","scoreList":[{"projectId":544,"projectName":"22-23海南高一一联","projectStudentCount":36024,"score":{"subjectName":"外语","fenShu":64.00,"jiMing":8622,"xiaoMing":704,"banMing":22,"examinationFlag":1},"createOn":"2023-02-20T23:23:13.263"},{"projectId":576,"projectName":"22-23 海南高一下期末","projectStudentCount":48591,"score":{"subjectName":"外语","fenShu":110.00,"jiMing":3014,"xiaoMing":185,"banMing":2,"examinationFlag":1},"createOn":"2023-07-15T12:23:11.667"}]},{"subjectName":"地理","scoreList":[{"projectId":544,"projectName":"22-23海南高一一联","projectStudentCount":34684,"score":{"subjectName":"地理","fenShu":47.00,"jiMing":10736,"xiaoMing":527,"banMing":19,"examinationFlag":0},"createOn":"2023-02-20T23:23:13.263"},{"projectId":576,"projectName":"22-23海南高一下期末","projectStudentCount":27397,"score":{"subjectName":"地理","fenShu":76.00,"jiMing":50,"xiaoMing":9,"banMing":2,"examinationFlag":1},"createOn":"2023-07-15T12:23:11.667"}]},{"subjectName":"物理","scoreList":[{"projectId":544,"projectName":"22-23海南高一一联","projectStudentCount":33333,"score":{"subjectName":"物理","fenShu":28.00,"jiMing":9328,"xiaoMing":636,"banMing":19,"examinationFlag":0},"createOn":"2023-02-20T23:23:13.263"},{"projectId":576,"projectName":"22-23海南高一下期末","projectStudentCount":23930,"score":{"subjectName":"物理","fenShu":57.00,"jiMing":3761,"xiaoMing":194,"banMing":3,"examinationFlag":1},"createOn":"2023-07-15T12:23:11.667"}]},{"subjectName":"化学","scoreList":[{"projectId":544,"projectName":"22-23海南高一一 联","projectStudentCount":33432,"score":{"subjectName":"化学","fenShu":52.00,"jiMing":3110,"xiaoMing":279,"banMing":6,"examinationFlag":0},"createOn":"2023-02-20T23:23:13.263"},{"projectId":576,"projectName":"22-23海南高一下期末","projectStudentCount":21436,"score":{"subjectName":"化学","fenShu":37.00,"jiMing":10227,"xiaoMing":528,"banMing":17,"examinationFlag":1},"createOn":"2023-07-15T12:23:11.667"}]}],"subjectScoreList":["总分","语文","数学","外语","地理","物理","化学"],"scoreRangeList":[{"range":"0_100","count":986},{"range":"100_200","count":8721},{"range":"200_300","count":21146},{"range":"300_400","count":12825},{"range":"400_500","count":4895},{"range":"500_600","count":965},{"range":"600_700","count":60},{"range":"700_满分","count":0}],"projectAvgInfo":[{"subjectName":"总分","mineScore":401.00,"max":651.0,"avg":282.7},{"subjectName":"语文","mineScore":83.00,"max":126.0,"avg":73.51},{"subjectName":"数学","mineScore":38.00,"max":147.0,"avg":42.28},{"subjectName":"外语","mineScore":110.00,"max":144.0,"avg":57.65},{"subjectName":"政治","mineScore":0.00,"max":89.0,"avg":37.73},{"subjectName":"历史","mineScore":0.00,"max":89.0,"avg":46.33},{"subjectName":"地理","mineScore":76.00,"max":86.0,"avg":45.37},{"subjectName":"物理","mineScore":57.00,"max":100.0,"avg":37.36},{"subjectName":"化学","mineScore":37.00,"max":99.0,"avg":39.19},{"subjectName":"生物","mineScore":0.00,"max":97.0,"avg":31.08}],"schoolAvgInfo":[{"subjectName":"总分","mineScore":401.00,"max":640.0,"avg":391.57},{"subjectName":"语文","mineScore":83.00,"max":122.0,"avg":88.93},{"subjectName":"数学","mineScore":38.00,"max":135.0,"avg":63.27},{"subjectName":"外语","mineScore":110.00,"max":136.0,"avg":87.26},{"subjectName":"政治","mineScore":0.00,"max":89.0,"avg":47.83},{"subjectName":"历史","mineScore":0.00,"max":82.0,"avg":58.14},{"subjectName":"地理","mineScore":76.00,"max":81.0,"avg":56.82},{"subjectName":"物理","mineScore":57.00,"max":100.0,"avg":49.22},{"subjectName":"化学","mineScore":37.00,"max":94.0,"avg":54.05},{"subjectName":"生物","mineScore":0.00,"max":83.0,"avg":39.77}],"classAvgInfo":[{"subjectName":"总分","mineScore":401.00,"max":505.0,"avg":359.0},{"subjectName":"语文","mineScore":83.00,"max":107.0,"avg":87.42},{"subjectName":"数学","mineScore":38.00,"max":101.0,"avg":47.5},{"subjectName":"外语","mineScore":110.00,"max":111.0,"avg":78.48},{"subjectName":"政治","mineScore":0.00,"max":0.0,"avg":0.0},{"subjectName":"历史","mineScore":0.00,"max":73.0,"avg":57.52},{"subjectName":"地理","mineScore":76.00,"max":81.0,"avg":57.52},{"subjectName":"物理","mineScore":57.00,"max":84.0,"avg":34.94},{"subjectName":"化学","mineScore":37.00,"max":75.0,"avg":48.4},{"subjectName":"生物","mineScore":0.00,"max":12.0,"avg":12.0}],"scoreLineInfo":[]}}



def decoding_score(data):
    score_data = data["data"]
    subjects = score_data["scoreSortList"]
    student_score = {
        "学校":score_data["xueXiao"],
        "考生姓名":score_data["xingMing"],
        "班级":score_data["banJi"],
        "准考证号":score_data["kaoHao"],
        "考试成绩":[],
        "班级考试情况":[],
        "学校考试情况":[],
        "联考考试情况":[],
        "分数分布情况":[],
    }
    for subject in subjects:
        student_score["考试成绩"].append({
            "科目":subject["subjectName"],
            "分数":subject["fenShu"],
            "班级排名":subject["banMing"],
            "学校排名":subject["xiaoMing"],
            "联考排名":subject["jiMing"],
            "已选科目":subject["examinationFlag"]
        })
    
    for subject in score_data["classAvgInfo"]:
        student_score["班级考试情况"].append({
            "科目":subject["subjectName"],
            "平均分":subject["avg"],
            "最高分":subject["max"],

        })

    for subject in score_data["schoolAvgInfo"]:
        student_score["学校考试情况"].append({
            "科目":subject["subjectName"],
            "平均分":subject["avg"],
            "最高分":subject["max"],

        })
    
    for subject in score_data["projectAvgInfo"]:
        student_score["联考考试情况"].append({
            "科目":subject["subjectName"],
            "平均分":subject["avg"],
            "最高分":subject["max"],

        })
    
    for number in score_data["scoreRangeList"]:
        student_score["分数分布情况"].append({
            "区间":number["range"],
            "人数":number["count"]
        })
    
    return student_score

 
data = decoding_score(score_data_raw)
print(data)