def label(func):
    def wrapper(name):
        print(name, end = ' : ')
        func(name)
    return wrapper

def label2(func):
    def wrapper(name):
        
        func(name)
        print('자기소개끝')
    return wrapper

@label
@label2
def prof(name):
    # name : 반갑네 {name} 교수라네
    print(f'반갑네 {name} 교수라네.')
    print('과제 했나?')

def student(name):
    # name : 안녕하세요! {name} 입니다.
    print(f'안녕하세요! {name} 입니다.')

prof_name = 'vik'
# print(label(prof)(prof_name)) #wrapper
print(prof(prof_name))
# prof(prof_name)

student_name = '이소정'
# label(student_name, student)
print(student(student_name))
# prof(student_name)