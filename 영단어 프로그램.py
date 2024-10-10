# 2019142010 도재우
# Python 3.9.9 기준
# coding ='utf-8'

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import csv, random, os, webbrowser, tkinter.font

# def register(id,pw):

# 메인 메뉴, 설정 화면, 시험지 화면이 따로 출력되도록 함
# 프레임을 한 점에 겹치게 하고 그 화면을 그때 그때 위로 올리도록 설정 

def open_frame(frame):
    frame.tkraise()

# 알림창 설정

## 종료

def exit():
    window.destroy()
    window.quit()
    exit()

## 파일이 선택되지 않았을 때 프로그램 종료

def info_openfile_false():
    tkinter.messagebox.showwarning("경고", ".csv 형식이나 .txt 형식의 파일을 선택해주세요!")
    window.destroy()
    window.quit()
    exit()

## 회원가입 알림

def info_register_comp():
    tkinter.messagebox.showinfo ("알림", "회원가입이 완료되었습니다!")

def info_ID_overlap_check_warning():
    tkinter.messagebox.showwarning("경고", "아이디 중복체크를 해주세요.")
    
def info_ID_overlap_warning():
    tkinter.messagebox.showwarning ("경고", "아이디가 중복됩니다.")

def info_ID_overlap_confirm():
    tkinter.messagebox.showinfo("알림", "사용가능한 아이디입니다!") 

def info_PW_check_warning():
    tkinter.messagebox.showwarning ("경고", "비밀번호가 일치하지 않습니다!")

def info_inv_ID_warning():
    tkinter.messagebox.showwarning("경고", "사용할 수 없는 아이디입니다!")

## 로그인 알림

def info_empty_ID_warning():
    tkinter.messagebox.showwarning ("경고", "아이디를 입력하세요")

def info_empty_PW_warning():
    tkinter.messagebox.showwarning ("경고", "비밀번호를 입력하세요")

def info_empty_ID_PW_warning():
    tkinter.messagebox.showwarning ("경고", "로그인 정보를 입력하세요")

def info_ID_warning():
    tkinter.messagebox.showwarning ("경고", "아이디를 확인해주십시오.")

def info_PW_warning():
    tkinter.messagebox.showwarning ("경고", "비밀번호를 확인해주십시오.")

def info_login_comp():
    tkinter.messagebox.showinfo("알림", "성공적으로 로그인 했습니다!")

## 로그아웃 알림

def logout():
    if testING==1:
        tkinter.messagebox.showwarning("경고", "시험 중에는 로그아웃이 불가합니다!")

    elif testING==0:    

        global myTopGrade
        global myId
        global myInfo

        myTopGrade=0
        myId=''
        myInfo={}

        tkinter.messagebox.showinfo("알림","성공적으로 로그아웃하였습니다!")
        open_frame(homeFrame)
        

## 설정 프레임 알림

def empty_setting_warning():
    tkinter.messagebox.showwarning("경고", "모든 설정을 체크하십시오!")

# 로그인

## 로그인 버튼 실행 함수

def login():
    global user_infos
    global myId                                            ### 로그인 시에 출력될 아이디
    global testING

    myId =''
    if h_entryId.get() == '' and h_entryPw.get() != '':     ### 공백 ID
        info_empty_ID_warning()
    elif h_entryId.get() != '' and h_entryPw.get() == '':   ### 공백 PW
        info_empty_PW_warning()
    elif h_entryId.get() == '' and h_entryPw.get() == '':   ### 공백 ID,PW
        info_empty_ID_PW_warning()        
    else:         
        if h_entryId.get() in user_ids:                     ### ID,PW를 입력받았다면 실행
            index=user_ids.index(h_entryId.get())           ### 아이디 리스트에서 입력받은 아이디의 index를 반환
            if user_pws[index]==h_entryPw.get():            ### 비밀번호 리스트에서 index의 원소가 입력받은 비밀번호와 같다면 실행
                info_login_comp()
                myId=h_entryId.get()
                open_frame(mainFrame)

            else:
                info_PW_warning()
        else:
            info_ID_warning()    

    h_entryId.delete(0,'end')                                ### 로그인 성공, 실패시 아이디와 비밀번호 entry 초기화
    h_entryPw.delete(0,'end')

## 회원가입

def register():
    global user_ids  
    global user_pws 
    global user_infos
    global temp
    
    print(user_ids)
    print(r_entryId.get())
    if r_entryId.get() == '' and r_entryPw.get() != '': ### 공백 ID
        info_empty_ID_warning()

    elif r_entryId.get() != '' and r_entryPw.get() == '': ### 공백 PW
        info_empty_PW_warning()

    elif r_entryId.get() == '' and r_entryPw.get() == '': ### 공백 ID,PW
        info_empty_ID_PW_warning()  

    elif r_entryId.get() in user_ids:
        info_ID_overlap_check_warning()

    else:
        if temp!=r_entryId.get() and temp=='':
            info_ID_overlap_check_warning()  

        else:             
            user_info['ID'] = r_entryId.get()
            user_info['PW'] = r_entryPw.get()
            user_ids.append(r_entryId.get())
            user_pws.append(r_entryPw.get())
            user_infos.append(user_info)
            info_register_comp()
            open_frame(homeFrame)

    r_entryId.delete(0,'end')
    r_entryPw.delete(0,'end')
    temp=''

### 아이디 중복체크

def overlapCheck():
    global temp
    if r_entryId.get() in user_ids:
        info_ID_overlap_warning
        r_entryId.delete(0,'end')
    else:
        if r_entryId.get() =='':
            info_inv_ID_warning()
        else:    
            temp=r_entryId.get()
            info_ID_overlap_confirm() 

# 시험지 함수

## 시험지 프레임띄우기 함수

def test(mode, type):
    global wordQindex
    global randumWord
    global testQLabel
    global testING
    global Qcount

    Qcount=0
    wordQindex=0

    if wordNum.get()!='' and type_var.get() !=0 and mode_var!=0:

        testING=1
        randnum=int(wordNum.get())
        randumWord=random.sample(range(len(english)),randnum) ### spindbox 수만큼 랜덤 단어 생성

    ### 한영 모드

        input_ans=StringVar()

        if mode==1:  
            label2=Label(testFrame,text='한->영 시험',font=titleFont)
            label2.grid(row=0,column=0,columnspan=2)

            ### Quiz 형식 

            if type==1:

                testQTitleLabel=Label(testFrame, text='제시된 한글에 일치하는 영어를 적으시오.',font=buttonFont)
                testQTitleLabel.grid(row=1,column=0,columnspan=2)

                testQLabel=Label(testFrame,text=f'{wordQindex+1}) {korean[randumWord[wordQindex]]}',font=buttonFont) 
                testQLabel.grid(row=2,column=1,columnspan=1)

                entryQAns=Entry(testFrame,textvariable=input_ans,insertofftime=0)
                entryQAns.grid(row=2,column=2,columnspan=2)

                checkQButton=Button(testFrame, text='제출',command=lambda:[get_eng_Q_ans(input_ans,randumWord[wordQindex])])
                checkQButton.grid(row=3,column=3)
                open_frame(testFrame)  

        ### 영한 모드

        elif mode==2:    

            label2=Label(testFrame,text='영->한 시험',font=titleFont)
            label2.grid(row=0,column=0,columnspan=2)

            ### Quiz 형식  
            
            if type==1:

                testQTitleLabel=Label(testFrame, text='제시된 영어에 일치하는 한글을 적으시오.',font=buttonFont)
                testQTitleLabel.grid(row=1,column=0,columnspan=2)

                testQLabel=Label(testFrame,text=f'{english[randumWord[wordQindex]]}',font=buttonFont) 
                testQLabel.grid(row=2,column=1,columnspan=1)
                
                entryQAns=Entry(testFrame,textvariable=input_ans,insertofftime=0)
                entryQAns.grid(row=2,column=2,columnspan=2)

                checkQButton=Button(testFrame, text='제출', command=lambda:[get_kor_Q_ans(input_ans,randumWord[wordQindex])])
                checkQButton.grid(row=3,column=3)

                open_frame(testFrame)

    else:
        empty_setting_warning()
        

## 시험지 초기 설정 함수

## Quiz

## 영어 답을 확인하는 함수

def get_eng_Q_ans(input_ans,num):       ### 키와 값을 확인하여 맞았는지 틀렸는지 출력하는 함수
    global randumWord
    global testQLabel
    global wordQindex
    global Qcount
    global eng_kor_dict
    global entryQAns

    if input_ans.get() == eng_kor_dict.get(korean[num]): 

        checkQAns=Label(testFrame,text="맞았습니다.",font=buttonFont)
        checkQAns.grid(row=3,column=4)
        Qcount+=1

    else: 

        checkQAns=Label(testFrame,text="틀렸습니다.",font=buttonFont)
        checkQAns.grid(row=3,column=4)

    if wordQindex<len(randumWord)-1:
        wordQindex+=1

        testQLabel.configure(text=f'{wordQindex+1}) {korean[randumWord[wordQindex]]}')
        testQLabel.grid(row=2,column=1,columnspan=1)

        entryQAns=Entry(testFrame,textvariable=input_ans,insertofftime=0)
        entryQAns.grid(row=2,column=2,columnspan=2)

        checkQButton=Button(testFrame, text='제출',command=lambda:[get_eng_Q_ans(input_ans,randumWord[wordQindex])])
        checkQButton.grid(row=3,column=3)   

    else:
        testING=0
        Qresult()

    entryQAns.delete(0,'end')

## 한글 답을 확인하는 함수

def get_kor_Q_ans(input_ans,num):       ### 키와 값을 확인하여 맞았는지 틀렸는지 출력하는 함수
    global randumWord
    global testQLabel
    global wordQindex
    global Qcount
    global resultQFrame
    
    if input_ans.get() == word[english[num]]: 

        checkQAns=Label(testFrame,text="맞았습니다.",font=buttonFont)
        checkQAns.grid(row=3,column=4)
        Qcount+=1

    else: 

        checkQAns=Label(testFrame,text="틀렸습니다.",font=buttonFont)
        checkQAns.grid(row=3,column=4)
    
    if wordQindex<len(randumWord)-1:
        wordQindex+=1
        testQLabel.configure(text=f'{wordQindex+1}) {english[randumWord[wordQindex]]}') 
        testQLabel.grid(row=2,column=1,columnspan=1)

        entryQAns=Entry(testFrame,textvariable=input_ans,insertofftime=0)
        entryQAns.grid(row=2,column=2,columnspan=2)

        checkQButton=Button(testFrame, text='제출',command=lambda:[get_eng_Q_ans(input_ans,randumWord[wordQindex])])
        checkQButton.grid(row=3,column=3)

    else:
        Qresult()    

    entryQAns.delete(0,'end')

## 퀴즈 결과 프레임 함수

def Qresult():
    global Qcount
    global users_info
    global myInfo
    global testING

    resultQFrame=tkinter.Frame(window,padx=320,pady=300) ## 퀴즈 형식 시험지 결과 객체 생성
    resultQFrame.grid(row=0,column=0)

    resultQlabel1=Label(resultQFrame,text='내 퀴즈 결과',font=titleFont)
    resultQlabel1.grid(row=0,column=0)

    resultQlabel2=Label(resultQFrame,text=f'내가 맞은 수 : {Qcount}개 / {wordNum.get()}개',font=buttonFont)
    resultQlabel2.grid(row=1,column=0)

    resultQlabel3=Label(resultQFrame,text=f'점수 {float(((Qcount*100)//int(wordNum.get())))}점',font=buttonFont)
    resultQlabel3.grid(row=2,column=0)

    resultQlabel4=Button(resultQFrame,text='홈으로 복귀',font=buttonFont,command=lambda:[return_mainFrame()])
    resultQlabel4.grid(row=3,column=1)

    printQresult=Button(resultQFrame,text='내 성적 보기',font=buttonFont,command=lambda:[print_my_grade()])
    printQresult.grid(row=4,column=1)

    users_info.append(myInfo)
    testING=0

# csv 쓰기 함수

def print_my_grade():

    write_my_grade()

    global myInfo
    global myId
    global myTopGrade
    global items
    if '' in myInfo:
        del myInfo['']
    else:
        pass

    item=[f'아이디 : {myId}',f'최고 성적 : {myTopGrade}',f'기록 : {myInfo[myId]}']
    items.append(item)

    with open ('out.csv', 'w', newline='') as f:
        writer=csv.writer(f)
        writer.writerow(item)

    item=[]

def write_my_grade():
    global Qcount
    global myTopGrade
    global myInfo
    global users_info
    global testFrame
    global resultQFrame
    global myId
    
    if myInfo not in users_info:

        myInfo[myId]=[]

    elif myInfo in users_info:

        pass

    if Qcount>=myTopGrade:
        myTopGrade=Qcount

    else:
        pass
    
    myInfo[myId]=users_info
    myInfo[myId]+=f'{Qcount}'
    myInfo[myId][0]=myTopGrade 
    
    testFrame.forget()
    resultQFrame.forget()

    open_frame(mainFrame)

## 홈으로 복귀 함수
def return_mainFrame():
    write_my_grade()
    open_frame(mainFrame)
    

# 메뉴 창 설정

def show_dev_info():      ## 개발자 사이트로 이동
    url1 = 'https://kevin-diary.tistory.com/'
    webbrowser.open(url1)    

def donate_dev():        ## 토스 사이트로 이동
    url2 = 'https://toss.im/'
    webbrowser.open(url2)

def show_info():

    global myId
    global myTopGrade

    newWindow = Toplevel(window)
    newWindow.geometry('400x400')
    labelInfo = Label(newWindow, text = "사용자 정보",font=titleFont)
    labelInfo2 = Label(newWindow, text = f"내 아이디 : {myId}",font=buttonFont)
    labelInfo3 = Label(newWindow, text = f"내 최고성적 : {myTopGrade}",font=buttonFont)

    labelInfo.grid(row=0,column=0)
    labelInfo2.grid(row=1,column=0)
    labelInfo3.grid(row=2,column=0)


# 윈도우 객체 생성 및 설정

window=Tk()
window.title('영단어 프로그램')
window.geometry('1000x1000')
window.resizable(False,False)
window.configure(bg='#49A')

# 메뉴 객체 생성 및 설정

menu=Menu(window)

## 상단바 메뉴 설정

filemenu1 = Menu(menu,tearoff=0)

filemenu1.add_command(label="로그아웃",command=logout)
filemenu1.add_command(label="종료", command=exit)
menu.add_cascade(label="파일", menu=filemenu1)

filemenu2 = Menu(menu,tearoff=0)

filemenu2.add_command(label="정보", command = show_info)
filemenu2.add_command(label="개발자 사이트", command = show_dev_info)
filemenu2.add_command(label="개발자에게 후원하기", command = donate_dev)
menu.add_cascade(label="도움말", menu=filemenu2)

window.config(menu=menu)

## 프레임 설정

homeFrame=tkinter.Frame(window) ## 홈 화면 객체 생성 
registerFrame=tkinter.Frame(window) ## 가입 화면 객체 생성 
mainFrame=tkinter.Frame(window) ## 메인 화면 객체 생성 
settingFrame=tkinter.Frame(window) ## 설정 화면 객체 생성 
testFrame=tkinter.Frame(window) ## 시험지 화면 객체 생성
resultQFrame=tkinter.Frame(window) ## 퀴즈 형식 시험지 결과 객체 생성
resultTFrame=tkinter.Frame(window) ## 시험 형식 시험지 결과 객체 생성

homeFrame.grid(row=0,column=0,sticky='nsew')
registerFrame.grid(row=0,column=0,sticky='nsew')
mainFrame.grid(row=0,column=0,sticky='nsew')
settingFrame.grid(row=0,column=0,sticky='nsew')
testFrame.grid(row=0,column=0,sticky='nsew')
resultTFrame.grid(row=0,column=0,sticky='nsew')

## 출력 폰트 설정

titleFont=tkinter.font.Font(family='Consolas', size=30, weight='bold')
buttonFont=tkinter.font.Font(family='나눔고딕', size=17)

## entry에서 입력받을 형식 설정

input_ans=StringVar()   ### 답을 입력을 받을 형식 결정
checkMode=IntVar()      ### 설정에서 모드를 받을 형식 결정
wordNum_var = IntVar()  ### 설정에서 단어 갯수를 받을 형식 결정
mode_var = IntVar()  ### 설정에서 한영,영한 방식을 받을 형식 결정
type_var = IntVar()  ### 설정에서 시험 형식을 받을 형식 결정
login_id=StringVar()    ### 홈화면에서 아이디를 입력 받을 형식 결정
login_pw=StringVar()    ### 홈화면에서 패스워드를 입력 받을 형식 결정
register_id=StringVar() ### 메인화면에서 아이디를 입력 받을 형식 결정
register_pw=StringVar() ### 메인화면에서 패스워드를 입력 받을 형식 결정

## 라디오 버튼 해당하는 그룹 항목 설정, value를 int형으로 저장

mode_var=IntVar()
type_var=IntVar()

## 여러 변수 초기화

word={}                   ### English : Korean 딕셔너리 생성
eng_kor_dict={}           ### Korean : English 딕셔너리 생성
user_info={}
users_info=[]
user_infos=[]   
user_ids=[]
user_pws=[]
items=[5,10,15,20]    ### 설정에서 받을 단어 갯수 지정
Qcount=0
myTopGrade=0
myId=''
myInfo={}
myInfo[myId]=[]
temp=''
testING=0

## readPath = '선택한 파일의 경로'
## initialdir = '파일 위치 경로', title = '이름' 
readPath = askopenfilename(initialdir="/", title="단어장 선택",filetypes=(("텍스트 파일 (.txt)", "*.txt"),("CSV 파일 (.csv)", "*.csv")))
root, extension=os.path.splitext(readPath)

## 확장자명이 .csv면 

if extension=='.csv':           
    f=open(readPath,'r')
    for line in f:
        (key,value)=line.rstrip().split(',')    ### 한 줄씩 받아서 오른쪽 공백을 제거하고, ','를 기준으로 영어와 한글로 나눔
        word[key]=value

## 확장자명이 .txt면 

elif extension=='.txt':          
    f=open(readPath,'r',encoding='UTF-8')
    for line in f:
        (key,value)=line.rstrip().split()       ### 한 줄씩 받아서 오른쪽 공백을 제거하고, 띄어쓰기를 기준으로 영어와 한글로 나눔
        word[key]=value 

else:
    info_openfile_false()

eng_kor_dict={v:k for k,v in word.items()} ### 한영사전
english = list(word.keys()) ### a의 key 값들을 리스트로 정렬
korean =list(word.values()) ### a의 value 값들을 리스트로 정렬

# homeFrame 구성

h_label1=Label(homeFrame, text="영단어 프로그램에 오신 것을 환영합니다",relief='ridge',fg='black',font=titleFont)
h_label1.grid(row=0,column=3,columnspan=4)
h_labelId=Label(homeFrame, text="ID",fg='black',font=buttonFont)
h_labelId.grid(row=1,column=3)
h_labelPw=Label(homeFrame, text="PW",fg='black',font=buttonFont)
h_labelPw.grid(row=2,column=3)

## 아이디와 비밀번호 입력 받는 입력창

h_entryId=Entry(homeFrame, textvariable=login_id,insertofftime=0)
h_entryId.grid(row=1,column=4)
h_entryPw=Entry(homeFrame, textvariable=login_pw, show='*',insertofftime=0)
h_entryPw.grid(row=2,column=4)

## 로그인 버튼 및 회원가입 버튼

h_loginButton=Button(homeFrame, text='Login',fg='black',font=buttonFont,command=lambda:[login()])
h_loginButton.grid(row=6,column=4,sticky='nsew')
h_registerButton=Button(homeFrame, text='회원가입',fg='black',font=buttonFont,command=lambda:[open_frame(registerFrame)])
h_registerButton.grid(row=7,column=4,sticky='nsew')

# mainFrame 구성

## 제목 구성

m_label1=Label(mainFrame, text="영단어 프로그램에 오신 것을 환영합니다",fg='black',font=titleFont)
m_label1.grid(row=3,column=3)

## 시험 시작 버튼

m_button1=Button(mainFrame, text='시험 시작',fg='black',font=buttonFont,command=lambda:[open_frame(settingFrame)])
m_button1.grid(row=4,column=2)

# registerFrame 구성

r_titleLabel=Label(registerFrame, text='회원 등록')
r_titleLabel.grid(row=1,column=1,columnspan =1)

r_registerId=Label(registerFrame, text='아이디')
r_registerId.grid(row=2,column=1,columnspan =1)

r_registerPw=Label(registerFrame, text='비밀번호')
r_registerPw.grid(row=3,column=1,columnspan =1)

r_entryId=Entry(registerFrame, textvariable=register_id,insertofftime=0)
r_entryId.grid(row=2,column=2,columnspan =2)
r_entryPw=Entry(registerFrame, textvariable=register_pw,show='*',insertofftime=0)
r_entryPw.grid(row=3,column=2,columnspan =2)

r_overlapButton=Button(registerFrame,text='ID 중복체크',fg='black',font=buttonFont,command=lambda:[overlapCheck()])
r_overlapButton.grid(row=2,column=4,rowspan=2)
r_regButton=Button(registerFrame, text='등록',fg='black',font=buttonFont,command=lambda:[register()])
r_regButton.grid(row=4,column=2)
h_regCancelButton=Button(registerFrame, text='취소',fg='black',font=buttonFont,command=lambda:[open_frame(homeFrame)])
h_regCancelButton.grid(row=4,column=3)

# settingFrame 구성

label1=Label(settingFrame, text="설정",fg='black',font=titleFont)
label1.grid(row=3,column=3)

## 설정부

modeLabel=Label(settingFrame, text='문제 형식',fg='black',font=buttonFont)
modeLabel.grid(row=4,column=2,ipadx=50,ipady=50)
testModeKor=Radiobutton(settingFrame, text='한글 문제',fg='black',font=buttonFont, value=1,variable=mode_var)
testModeKor.grid(row=5,column=2)

testModeEng=Radiobutton(settingFrame, text='영어 문제',fg='black',font=buttonFont, value=2,variable=mode_var)
testModeEng.grid(row=6,column=2)

typeLabel=Label(settingFrame, text='문제 풀이 형식',fg='black',font=buttonFont)
typeLabel.grid(row=4,column=3,ipadx=50,ipady=50)

testTypeQ=Radiobutton(settingFrame, text='퀴즈 형식',fg='black',font=buttonFont, value=1,variable=type_var)
testTypeQ.grid(row=5,column=3)

wordNumLabel=Label(settingFrame, text='문제 갯수',fg='black',font=buttonFont)
wordNumLabel.grid(row=4,column=6,ipadx=50,ipady=50)

wordNum = ttk.Combobox(settingFrame,values=items)
wordNum.grid(row=5,column=6)

testStartButton=Button(settingFrame, text='시험 시작',fg='black',font=buttonFont,command=lambda:[test(mode_var.get(),type_var.get())])
testStartButton.grid(row=7,column=4)

## resultQFrame 구성

# resultFrame 구성

open_frame(homeFrame)
window.mainloop()
            
