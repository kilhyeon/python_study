import datetime

# 현재 날짜
now = datetime.datetime.now()

# 출력
print(now.year, '년')

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

if now.hour >=12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

if 12 <= now.month <= 2:
    print("이번 달은 {}월로 봄입니다.".format(now.month))


number = input("정수 입력> ")

last_character = number[-1]

last_number = int(last_character)

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다")


