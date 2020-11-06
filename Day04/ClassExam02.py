class Person:
    # 초기자(생성자, initializer)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def viewPerson(self):
        print("{}({}세)".format(self.name, self.age))

    def nextAge(self):
        print("{}씨 내년 나이는 {}세입니다.".format(self.name, self.age+1))

    def __str__(self):  # 자바의 toString()메소드 기능
        return "{}({}세)".format(self.name,self.age)


person = Person('한사람', 33)
person.viewPerson()
print(person)   # 객체를 출력하면 __str__ 호출
print(person.__str__())   # 객체를 출력하면 __str__ 호출
person.nextAge()
print(person.name)  # 멤버가 공개된다.
print(person.age)

person2 = Person('두사람', 18)
print(person2)
person2.nextAge()
print(person2.name)
print(person2.age)