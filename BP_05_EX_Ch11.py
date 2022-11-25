1.
filename = input("파일 이름을 입력하세요: ").strip()
infile = open(filename, "r")
count = 0

for line in infile:
    for ch in line:
        count += 1\

print("파일 안에는 총 ", count , "개의 글자가 있습니다.")
infile.close() # 파일을 닫는다.
2.
infilename = input("파일 이름을 입력하시오: ").strip()
infile = open(infilename, "r")
file_s = infile.read()
removed_s = input("삭제할 문자열을 입력하시오: ").strip()
modified_s = file_s.replace(removed_s, "")

infile.close()
outfile = open(infilename, "w")

print(modified_s, file = outfile, end = "")
print("변경된 파일이 저장되었습니다.")
outfile.close() 
3.
filename=str(input('입력 파일 이름: '))

infile=open(filename,"r",encoding='utf-8')

char_list={}

for line in infile :
    for word in line:
        for letter in word:
            if not letter in char_list:
                char_list[letter]=0
            char_list[letter]+=1

infile.close()

print(char_list)
4.
import pickle
outfile = open("test.dat", "wb")
pickle.dump(12, outfile)
pickle.dump(3.14, outfile)
pickle.dump([1, 2, 3, 4, 5], outfile)
outfile.close()

infile = open("test.dat", "rb")
print(pickle.load(infile))
print(pickle.load(infile))
print(pickle.load(infile))
infile.close()
5.
inFileName = input("입력 파일 이름: ")
outFileName = input("출력 파일 이름: ")

infile = open(inFileName, "r")
outfile = open(outFileName, "w")

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

infile.close()
outfile.close()
6.
from tkinter import *

total=0


def add():
    global total
    total=total+int(entry.get())
    SumNum.config(text=str(total))

def minus():
    global total
    total=total-int(entry.get())
    SumNum.config(text=str(total))

def reset():
    global total
    total=0
    SumNum.config(text=str(total))

window=Tk()


total=0

NowSum=Label(window,text="현재 합계: ")
SumNum=Label(window,text=total)
NowSum.grid(row=0,column=0)
SumNum.grid(row=0,column=1)

entry=Entry(window)
entry.grid(row=1, column=0, columnspan=3)

addbutt=Button(window,text='더하기(+)', command=add)
minusbutt=Button(window,text='빼기(-)', command=minus)
resetbutt=Button(window,text='reset', command=reset)
addbutt.grid(row=2,column=0)
minusbutt.grid(row=2,column=1)
resetbutt.grid(row=2,column=2)

window.mainloop()
