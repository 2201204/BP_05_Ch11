1.
filename = input("파일 이름을 입력하세요: ").strip()  # 공백 없이사용자 입력
infile = open(filename, "r") #입력한 이름(문자열)로 파일 읽기 또는 쓰기
count = 0

for line in infile:   #파일 안 글 만큼 반복
    for ch in line:
        count += 1\

print("파일 안에는 총 ", count , "개의 글자가 있습니다.") #출력
infile.close() # 파일을 닫는다.
2.
infilename = input("파일 이름을 입력하시오: ").strip() #공백 없이 입력 받아서 저장
infile = open(infilename, "r") #읽기 모드로 파일 열기
file_s = infile.read() #읽기
removed_s = input("삭제할 문자열을 입력하시오: ").strip() #공백 없이 삭제할 문자열 입력 받아서 저장
modified_s = file_s.replace(removed_s, "") # 삭제할 문자열을 ""로 대체

infile.close()
outfile = open(infilename, "w") # 쓰기 형식으로 파일열기

print(modified_s, file = outfile, end = "") #쓰기 파일 // 공백 없음
print("변경된 파일이 저장되었습니다.")
outfile.close() #파일 닫음
3.
filename=str(input('입력 파일 이름: '))

infile=open(filename,"r",encoding='utf-8')

char_list={}

for line in infile : #문장 수 만큼 반복
    for word in line:
        for letter in word:
            if not letter in char_list:
                char_list[letter]=0
            char_list[letter]+=1

infile.close()

print(char_list)
4.
import pickle  #피클 라이브러리 불러옴
#pickle모듈을 사용해 저장
outfile = open("test.dat", "wb") #저장장소 설정 dump로 저장하기위해 wb모드
pickle.dump(12, outfile) # 출력 파일에 12 정수형 객체값 저장
pickle.dump(3.14, outfile)   # 출력 파일에 3.14 실수형 객체값 저장
pickle.dump([1, 2, 3, 4, 5], outfile) # 출력 파일에 1~5 배열 객체값 저장
outfile.close()

#pickle모듈을 사용해 읽기
infile = open("test.dat", "rb")
print(pickle.load(infile))
print(pickle.load(infile))
print(pickle.load(infile))
#파일 읽기하여 출력
infile.close() #파일 닫기
5. 
inFileName = input("입력 파일 이름: ")  #입력 파일 경로 입력
outFileName = input("출력 파일 이름: ")  #작성할 파일 경로 입력

infile = open(inFileName, "r")   # 읽기 모드로 파일 열기
outfile = open(outFileName, "w") # 쓰기 모드로 파일 열기

total = 0.0
count = 0

line = infile.readline()
while line != "" :
 value = float(line)
 total = total + value
 count = count + 1
 line = infile.readline()
  
outfile.write("합계="+ str(total)+"\n")

avg = total / count
outfile.write("평균="+ str(avg)+"\n")

infile.close() #파일 닫기
outfile.close() #파일 닫기
6.
import pickle  #피클 라이브러리 불러옴
from tkinter import *  # tkinter 라이브러리 모든 기능 불러옴
 
phone_book = { } # 딕셔너리 생성
current = 0  # 변수 0으로 초기화 및 생성
name = ""    # 공백 으로 초기화
phone = ""   # 공백 으로 초기화

window = Tk()

frame1 = Frame(window)
frame1.pack()
Label(frame1, text = "이름 ").grid(row = 1, column = 1, sticky = W)
nameEntry = Entry(frame1, textvariable = name, width = 30)
nameEntry.grid(row = 1, column = 2)

frame2 = Frame(window)
frame2.pack()
Label(frame2, text = "전화번호").grid(row = 1, column = 1, sticky = W)
phoneEntry = Entry(frame2, textvariable = phone, width = 30)
phoneEntry.grid(row = 1, column = 2)

frame3 = Frame(window)
frame3.pack()

def save(): #저장 함수 생성
 outfile = open("phonebook.dat", "wb") # 바이너리 쓰기 모드로 파일 읽기
 pickle.dump(phone_book, outfile)  # 출력 파일에 전화번호 객체값 저장
 print("주소들이 파일에 저장되었습니다") #저장 문구 출력
 outfile.close() # 파일 닫기
     
def load(): #읽기 함수 생성
 infile = open("phonebook.dat", "rb") # 바이너리 읽기 모드로 파일 읽기
 phone_book = pickle.load(infile) # 연락처에 파일 읽어서 저장
 infile.close()  #파일 닫기
 print("파일에서 주소를 읽었습니다.") #문구 출력
 go_first()  # go_first() 함수 실행

def add():  #추가 함수 생성
 phone_book[nameEntry.get()] = phoneEntry.get() # 연락처에서 파일 가져와서 저장
 print(phone_book) #연락처 출력
 save() #저장 함수 실행

def go_first():  #go_first 함수 생성
 global current  #전역 변수
 current = 0    # 0으로 초기화 및 변수 생성
 ks = list(phone_book)   # 리스트 형식으로 주소록 저장
 print(phone_book)   #연락처 출력
 nameEntry.delete(0, END)
 nameEntry.insert(0, ks[current])
 phoneEntry.delete(0, END)
 phoneEntry.insert(0, phone_book[ks[current]])
 #기입창 0으로 초기화 및 삭제
    
def go_next(): #go_next 함수 생성
 global current  #전역 변수
 current += 1  # 함수 실행 시 +1
 ks = list(phone_book) #리스트 형식으로 주소록 저장
 nameEntry.delete(0, END)
 nameEntry.insert(0, ks[current])
 phoneEntry.delete(0, END)
 phoneEntry.insert(0, phone_book[ks[current]])
# 기입창 0으로 초기화 및 삭제
def go_previous(): # 이전 함수 생성
 print("구현되지 않았음")

def go_last():
 print("구현되지 않았음")

b1 = Button(frame3, text = "추가", command = add).grid(row = 1, column = 1)
b2 = Button(frame3, text = "처음", command = go_first).grid(row = 1, column = 2)
b3 = Button(frame3, text = "다음", command = go_next).grid(row = 1, column = 3)
b4 = Button(frame3, text = "이전", command =go_previous).grid(row = 1, column = 4)
b5 = Button(frame3, text = "마지막", command = go_last).grid(row = 1, column = 5)
b6 = Button(frame3, text = "파일 읽기", command = load).grid(row = 1, column = 6)

window.mainloop()
