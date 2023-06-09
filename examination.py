import random as rnd
import json

import matplotlib as mpl
import matplotlib.pyplot as plt
import streamlit as st

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
mpl.rcParams["ytick.direction"] = "in"

add_selectbox = st.sidebar.radio("选择做题数目", \
    ("10题", "20题", "40题", "60题", "100题"))
if add_selectbox == "10题":
    num = 10
elif add_selectbox == "20题":
    num = 20
elif add_selectbox == "40题":
    num = 40
elif add_selectbox == "60题":
    num = 60
elif add_selectbox == "100题":
    num = 100

#rnd.seed(225)

st.header("中药材知识考试")
st.subheader("点击左上角的→可选择题目数量")

st.markdown("本软件代码由陈一翰[@Chen-YiHan](https://github.com/Chen-YiHan)制作，方利国老师指导")

name = st.text_input("请输入您的姓名", "张三")
sel_no = st.number_input(
    "选择一个试卷序列号", value=3, min_value=0, max_value=65535, step=1, format="%i"
)
rnd.seed(sel_no)

with open("./questions.json", "r", encoding='utf-8') as f:
    dic = json.load(f)

q_set = set()
while len(q_set) < num:
    q_set.add(rnd.randint(0, len(dic) - 1))
rnd_l = list(q_set)

al = ["A", "B", "C", "D", "E"]
n = 0
with st.form("my_form"):
    for i in range(num):
        str_k = "第" + str(i + 1) + "题"
        st.subheader(str_k)
        # k=test_num[i]
        select = st.radio(
            dic[str(rnd_l[i])]["title"],
            (f'{i + 1}A.{dic[str(rnd_l[i])]["chioces"]["A"].replace("<br>", "")}', 
             f'{i + 1}B.{dic[str(rnd_l[i])]["chioces"]["B"].replace("<br>", "")}', 
             f'{i + 1}C.{dic[str(rnd_l[i])]["chioces"]["C"].replace("<br>", "")}', 
             f'{i + 1}D.{dic[str(rnd_l[i])]["chioces"]["D"].replace("<br>", "")}',
             f'{i + 1}E.{dic[str(rnd_l[i])]["chioces"]["E"].replace("<br>", "")}'),
            horizontal=True,
        )  # 前面题目，后面4个选项
        if dic[str(rnd_l[i])]["zhizhu"] != None:
            st.image(f"./120image/zhizhu/{dic[str(rnd_l[i])]['zhizhu']}.jpg")
            st.image(f"./120image/chengyao/{dic[str(rnd_l[i])]['chengyao']}.jpg")
        
        ans = dic[str(rnd_l[i])]["chioces"][al[dic[str(rnd_l[i])]["answer"]]]
        ans = f"{i + 1}{al[dic[str(rnd_l[i])]['answer']]}.{ans.replace('<br>', '')}"
        #print(f"ans:{ans}, select:{select}")
        if select == ans:  # 这里填正确答案
            n = n + 1
    submitted = st.form_submit_button("点击提交")
    if submitted:
        # con_num=1
        str_finsh = "欢迎您" + name + ",已完成考试,试卷序号为" + str(sel_no) + ",选择题目数为" + str(num)
        st.subheader(str_finsh)
        # for i in range(num):
        # k=test_num[i]
        # if select ==str_test[k][answer[k-100]] :  #这里填正确答案,目前题目从100 199
        # n=n+1
        if n / num > 0.9:
            str_n = str(n)
            sstr = (
                "恭喜您答对"
                + str_n
                + "题,答对率为"
                + str(int(100. * 100 * n / num + 0.5) / 100)
                + "%，是个中药材大行家"
            )
            st.subheader(sstr)
            # st.experimental_rerun()
        elif n / num > 0.6:
            str_n = str(n)
            sstr = (
                "恭喜您答对"
                + str_n
                + "题,答对率为"
                + str(int(100. * 100 * n / num + 0.5) / 100)
                + "%，本次成绩不错，还有提升空间"
            )
            st.subheader(sstr)
            # st.experimental_rerun()
        elif n / num <= 0.6:
            str_n = str(n)
            sstr = (
                "本次只答对"
                + str_n
                + "题,答对率为"
                + str(int(100 * 100 * n / num + 0.5) / 100)
                + "%，成绩不理想，请多多学习"
            )
            st.subheader(sstr)
        fig = plt.figure(num="Correct Answer Chart", figsize=(8, 8))
        labels = ["Correct", "Mistake"]
        C_M_data = [n / num, 1 - n / num]  # 正确与错误数据
        colors = ["lightblue", "red"]  # 颜色
        explode = (0.1, 0.1)  # 间隔距离，半径的比例
        plt.pie(
            C_M_data,
            explode=explode,
            labels=labels,
            startangle=45,
            shadow=True,
            colors=colors,
            autopct="%3.1f%%",
        )
        # st.subheader("*******答题对错率图******")
        plt.title("Question Answering Correct and Mistake Rate Chart")

        st.pyplot(fig)
        str_finsh1 = str_finsh + "请截屏成绩发给指定人员或地址"
        sstr = (
            "本次只答对"
            + str(n)
            + "题,答对率为"
            + str(int(100 * 100 * n / num + 0.5) / 100)
            + "%"
        )
        sstr = sstr + str_finsh1
        add_selectbox = st.sidebar.subheader(sstr)
        add_selectbox = st.sidebar.subheader("##若要继续考试可重新选择左边的答题数目或改变右上方试卷序号##")

'''
*本软件仅供学习交流。*
本软件参考了香港理工大学中药资料库、维基百科、百度图片、优酷视频等网络资料.
如有侵权，请联系本人删除'''
"本软件遵循Apache协议"
'''Copyright 2023 Yihan Chen

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''