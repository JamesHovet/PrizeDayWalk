from appMain.models import Student as S

f = open('exported.csv', mode='r')

def parse(line):
	
	li = line.split(',')

	n = li[6] + ' ' + li[5]
	ln = li[5]
	f = int(li[2])
	g = 1 if li[4] == "M" else 2
	id = int(li[1])

	return S(Name=n,LName=ln,Form=f,Gender=g,StudentID=id)

for line in f:
	newStudent = parse(line)
	newStudent.save()


