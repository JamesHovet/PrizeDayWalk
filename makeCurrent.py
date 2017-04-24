from appMain.models import Student as S

f = open("currentNumbers.csv", mode="r")

numbers = [int(line.strip()) for line in f]

all = S.objects.all()

for i in all:
	if i.StudentID not in numbers:
		print(i)

for n in numbers:
	try:
		S.objects.get(StudentID=n)
	except:
		print(n)



