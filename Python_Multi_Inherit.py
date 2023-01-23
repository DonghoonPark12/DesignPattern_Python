"""
https://dojang.io/mod/page/view.php?id=2388
"""

# 1) 다중 상속
class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')
 
class Undergraduate(Person, University):
    def study(self):
       print('공부하기')

james = Undergraduate() # james 객체는 Person, University 두 부모 클래스 기능을 모두 상속 받음
james.greeting()
james.manage_credit()
james.study()

"""
안녕하세요.
학점 관리
공부하기
"""

# 2) 다이아몬드 상속
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
 
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
 
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
 
class D(B, C):
    pass
 
x = D()
x.greeting()    # 안녕하세요. B입니다.

"""
안녕하세요. B입니다.
(D는 어떤 클래스의 메서드를 호출해야 할까요? 조금 애매합니다.)
(그래서 다이아몬드 상속은 문제가 많다고 해서 죽음의 다이아몬드라고도 부릅니다)
"""

"""
파이썬에서는 메서드 탐색 순서(Method Resolution Order, MRO)를 따릅니다
"""

D.mro()
"""
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
파이썬은 다중 상속을 한다면, 클래스 목록 중 왼쪽에서 오른쪽 순서로 메서드를 찾습니다
"""

"""
파이썬 3에서 모든 클래스는 object 클래스를 상속받으므로 기본적으로 object를 생략합니다.
다음과 같이 클래스를 정의한다면

class X:
    pass

괄호 안에 object를 넣은 것과 같습니다.

class X(object):
    pass
"""






