# time module

import time, math

# time.time() method : Convert a string or number to a floating point number, if possible.

start = time.time()
math.factorial(10000)
end = time.time()

print(f"{end - start:.5f} sec")
print(time.time().__doc__)

# datetime module -> 00:00:00 형태로 출력하고 싶다면 사용
# 시:분:초. 마이크로초 -> microsec 보기 싫으므로 split(".") 사용하여 리스트 변환 후 [0] 출력
import datetime

start = time.time()
math.factorial(2322)
end = time.time()

sec = end - start
result_list = str(datetime.timedelta(seconds = sec)).split(".")
print(result_list[0])

