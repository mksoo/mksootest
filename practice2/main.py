"""
사업자 등록 번호 체크
- 10자리 구조이다. 구성 요소의 의미는 아래와 같다.
  - 세자리: 국세청, 세무사별 코드
  - 두자리 개인 범인 구분 코드
  - 과세/면세/법인 사업자 등록/지정일자 일련번호
  - 마지막 한자리: 검증번호

조건
-
- 사업자번호 뒤에서 2번째자리와 인증키 마지막 값을 곱하고 10으로 나눈 후 위의 합과 추가로 더해줍니다.( 소수점은 제거)
- 합계를 10으로 나머지 연산을 합니다.
- 10에서 나머지 연산의 값을 빼줍니다.
- 사업자번호 마지막자리와 마지막 처리한값이 같으면 사업자번호

추가
- 예외 처리 하기.
"""


def check_num(registration_num):
    key = [1, 3, 7, 1, 3, 7, 1, 3, 5]

    list_of_regit_num = [int(i) for i in registration_num if i != "-"]

    # 1번: 마지막 자리 1을 제외한 사업자번호 앞 9자리 인증키 9자리의 각 자리수를 각각 곱하여 전부 더해준다.(인증키값 = 1 3 7 1 3 7 1 3 5)
    temp = 0
    for i in range(len(key)):
        temp += list_of_regit_num[i] * key[i]

    # 2번
    temp += (list_of_regit_num[-2] * key[-1]) // 10

    # 3번
    temp %= 10

    # 4번
    temp = 10 - temp

    # 5번
    if list_of_regit_num[-1] != temp:
        raise Exception(f"유효하지 않은 사업자 등록 번호. {list_of_regit_num[-1]} != {temp}")
    else:
        print(True)


check_num("110-81-41272")
