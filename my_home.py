'''我的主页'''
import streamlit as st 
import time
import base64
from PIL import Image
def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('天象奇景.jpg')
page_bg('天象奇景.jpg')
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','梗百科'])
def jiazai():
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
def jump():
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')
def page1():
    jiazai()
    '''兴趣推荐'''
    with open('王者.txt', 'r', encoding='utf-8') as f:
        msg1 = f.read().split('\n') 
    for i in range(len(msg1)):
        st.write(f':orange[{msg1[i]}]')
    ex = st.toggle('显示我的战绩')
    if ex:
        st.image("战绩图片.jpg")
    with open("音乐.mp3",'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    jump()
    
def page2():
    jiazai()
    '''图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name 
        file_type = uploaded_file.type 
        file_size = uploaded_file.size 
        img = Image.open(uploaded_file)
        st.image(img) 
        st.image(img_change(img,0,2,1))
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img_change(img,0,1,2)) 
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3: 
            st.image(img_change(img,1,2,0)) 
        with tab4: 
            st.image(img_change(img,1,0,2))
    jump()

def page3():
    jiazai()
    '''智慧词典'''
    st.write("智慧词典") 
    # 从本地文件中将词典信息读取出来，并储存在列表中 
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n') 
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释” 
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {} 
    for i in words_list: 
        words_dict[i[1]] = [int(i[0]),i[2]] 
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n') 
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {} 
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框 
    word = st.text_input('请输入要查询的单词') 
    # 显示查询内容 
    if word in words_dict:
        st.write(words_dict[word]) 
        n = words_dict[word][0] 
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1 
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = '' 
            for k,v in times_dict.items():
                message+=str(k)+'#'+str(v)+'\n'
            message = message[:-1] 
            f.write(message) 
        st.write('查询次数：',times_dict[n])
        if word == 'python':
            st.balloons() 
            st.write('原来你也学python')
        elif word == 'tww':
            st.snow() 
            st.write('努力跟随她的步伐')
    jump()
            

def page4():
    jiazai()
    '''留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list: 
        if i[1]=='时雨':
            with st.chat_message('🍕'):
                st.write(i[1],':',i[2]) 
        elif i[1] == '丁毅民':
            with st.chat_message('🍔'):
                st.write(i[1],':',i[2])

    name = st.selectbox('我是......',['时雨','丁毅民'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = '' 
            for i in messages_list:
                message += i[0] + '#' +i[1]+'#'+i[2]+'\n'
            message = message[:-1] 
            f.write(message)
    jump()
def choice(a,b):
    ex = st.toggle(a)
    if ex:
        st.image(b)
def page5():
    jiazai()
    st.write('梗百科')
    choice('鸡你太美','1.jpg')
    choice('因为他善','2.jpg')
    choice('牢大','3.jpg')
    choice('肘击','4.gif')
    choice('呐喊','呐喊.jpg')
    choice('老八','老八.jpg')
    choice('秀才','秀才.gif')
    jump()
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load() 
    for x in range(width):
        for y in range(height):
            # 获取RGB值 

            r = img_array[x,y][rc] 
            g = img_array[x,y][gc] 
            b = img_array[x,y][bc]

            img_array[x,y] = (r,g,b)

    return img
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2() 
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区': 
    page4()
elif page == '梗百科':
    page5()