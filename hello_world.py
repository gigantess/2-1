import datetime

output_filename = "print_result.md"

# 파일에서 기존 실행 횟수를 읽어옵니다.
try:
    with open(output_filename, 'r', encoding='utf-8') as f:
        execution_count = len(f.readlines())
except FileNotFoundError:
    execution_count = 0

# 현재 실행 번호를 계산합니다.
current_execution_number = execution_count + 1

# 현재 시간을 가져옵니다.
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 파일에 기록할 메시지를 생성하고 추가합니다.
output_message = f"{current_time} hello world {current_execution_number}\n"
with open(output_filename, 'a', encoding='utf-8') as f:
    f.write(output_message)

print(f"'{output_filename}'에 실행 결과가 기록되었습니다: {output_message.strip()}")