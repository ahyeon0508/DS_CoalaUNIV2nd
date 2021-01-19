birth = input("생년월일을 6자리로 입력해주세요.(yymmdd): ")
print("---------------------------------------------------")

year = birth[0:2] + "년"
month = birth[2:4] + "월"
day = birth[4:] + "일"

print("당신의 생일은", year, month, day, "입니다.")
print("당신의 생일은 {}{}{}입니다.".format(year, month, day))