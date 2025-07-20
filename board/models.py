from django.db import models

# Create your models here.
from django.utils import timezone

# 게시판에 들어갈 내용들
class Board(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    regdate = models.DateField(auto_now=timezone.now)  # 현재 시간으로 자동 설정
    readcount = models.IntegerField(default=0)


    def __str__(self):
        return  '%s. %s(%d)' % (self.title, self.writer, self.readcount)
    
    # 이런 멤버 메서드를 이용하면 편하게 구현할 수 있다.
    # 도메인주도개발 = DDD(Domain Driven Development)에서
    # 도메인 모델에 해당하는 객체의 행동을 정의하는 것.
    # 이 경우에는 게시판 글의 조회수를 증가시키는 행동을 정의한다.
    # 이 메서드를 호출하면 readcount가 1 증가한다.
    # 이 메서드는 Board 객체의 인스턴스에서 호출할 수 있다.
    def incrementReadCount(self) :
        self.readcount += 1
        self.save()