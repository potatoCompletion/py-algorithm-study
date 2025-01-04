# 출석하지 않은 한명의 학생의 이름 반환
# if - in 구절을 이용해서 풀어야 할 것 같다. 왜냐하면 if - in 구절은 파이썬에서 hash의 형태로 값을 저장하기 때문에 O(1)의 시간복잡도로 빠르게 검색할 수 있다.

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}
    for student in all_array:
        dict[student] = True

    for student in present_array:
        del dict[student]

    for key in dict.keys():
        return key


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))