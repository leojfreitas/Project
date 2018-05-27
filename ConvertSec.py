sec_str = input("insert total of sec, please: ")
total_sec = int(sec_str)


hour = total_sec // 3600
day = hour // 24
sec_rest = total_sec % 3600
minut = sec_rest // 60
sec_rest_final = sec_rest % 60

print("total of sec is",day, "days" ,hour, "hours, ",minut, "minuts and ", sec_rest_final, "seconds.")
