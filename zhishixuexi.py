import json
from pathlib import Path
import random

import streamlit as st

import get


def dis(page):
        name, zhongzhi, paozhi, yaoxing, zhizhu = get.get_page(page)
        st.header(name)
        st.subheader("种植")
        f"{zhongzhi.replace('<br>', '')}"
        st.subheader("炮制")
        f"{paozhi.replace('<br>', '')}"
        st.subheader("药性")
        f"{yaoxing.replace('<br>', '')}"
        st.subheader("植株")
        f"{zhizhu.replace('<br>', '')}"
        if Path(f"./120image/zhizhu/{name}.jpg").exists():
            zhizhu_img = st.image(f"./120image/zhizhu/{name}.jpg")
        if Path(f"./120image/chengyao/{name}.jpg").exists():
            chengyao_img = st.image(f"./120image/chengyao/{name}.jpg")
        
def disn(name):
        zhongzhi, paozhi, yaoxing, zhizhu = get.get_value(name).values()
        st.header(name)
        st.subheader("种植")
        f"{zhongzhi.replace('<br>', '')}"
        st.subheader("炮制")
        f"{paozhi.replace('<br>', '')}"
        st.subheader("药性")
        f"{yaoxing.replace('<br>', '')}"
        st.subheader("植株")
        f"{zhizhu.replace('<br>', '')}"
        if Path(f"./120image/zhizhu/{name}.jpg").exists():
            zhizhu_img = st.image(f"./120image/zhizhu/{name}.jpg")
        if Path(f"./120image/chengyao/{name}.jpg").exists():
            chengyao_img = st.image(f"./120image/chengyao/{name}.jpg")



st.header("中药材知识学习")
"*包罗8000余种中药材的知识宝库，附图数百张倾力之作*"
st.markdown("本软件代码由陈一翰[@Chen-YiHan](https://github.com/Chen-YiHan)制作，方利国老师指导")

#if 'page' not in st.session_state:
#	st.session_state.page = 0
#	#dis(st.session_state.page)
##dis(st.session_state.page)
#if st.button(f"上一页"):
#    st.session_state.page -= 1
#    #dis(st.session_state.page)
#if st.button(f"下一页"):
#    #print(1)
#    st.session_state.page += 1
#    #dis(st.session_state.page)
#dis(st.session_state.page)

choice = st.sidebar.selectbox("快速进入中药材", get.get_name_list())
disn(choice)

#st.write('Count = ', st.session_state.page)
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