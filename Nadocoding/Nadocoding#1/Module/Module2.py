# import Module  # 일반 모듈 호출
# Module.price(3)
# Module.price_morning(4)
# Module.price_soldier(5)
#
# import Module as mv  # Module 을 mv 로 호출 가능
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)
#
# from Module import *  # 모듈에 있는 모든거 사용할꺼야
# price(3)
# price_morning(3)
# price_soldier(3)
#
# from Module import price, price_morning  # 필요한것만 추출가능
# price(5)
# price_morning(6)
# price_solder(5)

from Module import price_soldier as price   #  필요한것에 별칭으로도 사용 가능
price(5)
