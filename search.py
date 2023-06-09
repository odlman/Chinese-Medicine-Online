import streamlit as st
import difflib
from pathlib import Path

import get

st.header("欢迎使用中药材搜索系统")
"*本系统由陈一翰[@Chen-YiHan](https://github.com/Chen-YiHan)制作，方利国老师指导*"

key_word = st.text_input("搜索:请输入关键词，按回车确认", "")
n_list = get.get_name_list()
result = difflib.get_close_matches(key_word, n_list, 16, cutoff=0.1)
for r in result:
    if st.button(r):
        value = get.get_value(r)
        st.header("种植")
        st.write(value["种植"].replace("<br>","\n"))
        st.header("炮制")
        st.write(value["炮制"].replace("<br>","\n"))
        st.header("药性")
        st.write(value["药性"].replace("<br>","\n"))
        st.header("主治")
        st.write(value["主治"].replace("<br>","\n"))
        if Path(f"./120image/zhizhu/{r}.jpg").exists():
            zhizhu_img = st.image(f"./120image/zhizhu/{r}.jpg")
        if Path(f"./120image/chengyao/{r}.jpg").exists():
            chengyao_img = st.image(f"./120image/chengyao/{r}.jpg")

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