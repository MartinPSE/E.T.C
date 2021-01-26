# import travel.thailand  # 모듈, 패키지만 가능하다 // class 나 함수는 import 바로 못한다.
# # mport travel.thailand.ThailandPackage()  # 모듈, 패키지만 가능하다 // class 나 함수는 import 바로 못한다.
#
# # trip_to = travel.thailand.ThailandPackage()
# # trip_to.detail()
#
# from travel.thailand import ThailandPackage  # from / import 구문에서는 module, package, 함수, class 모두 가능
#
# trip_to = ThailandPackage()
# trip_to.detail()
#
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
#
from travel import *  # 왜 지? -> * 을 쓰는건 travel 패키지꺼 다 쓰겠다는거야
#   # 공개범위를 설정해줘야해! -> __init__.py 가서!
# # trip_to = vietnam.VietnamPackage()
# # trip_to.detail()
#
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 모듈의 위치 확인
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile((thailand)))
