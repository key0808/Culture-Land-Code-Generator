import random

def generate_random_number():
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(14)])
    return f"4180 08{random_numbers[:2]} {random_numbers[2:6]} {random_numbers[6:10]} {random_numbers[10:]}"

def save_to_file(number):
    with open('output.txt', 'a') as file:
        file.write(number + '\n')

try:
    while True:
        random_number = generate_random_number()
        print(random_number)  # 생성된 숫자를 출력
        save_to_file(random_number)
except KeyboardInterrupt:
    print("사용자에 의해 종료되었습니다.")
