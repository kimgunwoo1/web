from django.db import models

class Myboard(models.Model):    #myboard table 이 될 것입니다.
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()

# myboard table
# 컬럼명 : myname, mytitle, mycontent, mydate
# MyBoard의 object(row)를 출력할 때 메모리 출력대신에 정의된 것이 출력
# 메모리에 들어가 있는 오브젝트를 대표할 이름을 지정
# 프린트 할 때 확인이 용이하여 필수적인 것은 아니지만 사용한다.
    def __str__(self) :
        return str({'mytitle':self.mytitle, 'mydate':self.mydate})

class MyMember(models.Model):
    myname = models.CharField(max_length=100)
    mypassword = models.CharField(max_length=100)
    myemail = models.CharField(max_length=100)

    def __str__(self):
        return str({'myname':self.myname, 'myemail':self.myemail})