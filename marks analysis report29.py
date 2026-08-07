#marks  analysis report

n=int(input("enter number of students"))
marks=[]

for i in range(1,n+1):
    mark=int(input(f"enter the student {i} value"))
    marks.append(mark)
for i in marks:
    print(i)
print(marks)
print(".........marks analysis report.........")
print("total no of students",n)
print("heighest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average marks",sum(marks)/n)
