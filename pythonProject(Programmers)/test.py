def solution(record):
    answer = []
    ID_NAME = {}

    for i in record:
        temp = i.split()
        if temp[0] in ['Change', 'Enter']:
            ID_NAME[temp[1]] = temp[2]

    for i in record:
        if i.split()[0] == 'Enter': answer.append(f"{ID_NAME[i.split()[1]]}님이 들어왔습니다.")
        if i.split()[0] == 'Leave': answer.append(f"{ID_NAME[i.split()[1]]}님이 나갔습니다.")

    print(answer)
    return answer

if __name__ == '__main__':
    solution(["Enter 123 A",
              "Leave 123",
              "Enter uid1234 B",
              "Enter uid12345 C",
              "Leave uid1234",
              "Leave uid12345",
              "Enter uid123 AB",
              "Enter ABC 광우",
              "Change ABC 현주",
              "Leave ABC"])