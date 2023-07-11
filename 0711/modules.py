import sys
import mymath
sys.path.append("./") #현재 디렉토리에서 모듈이나 패키지를 검색하도록 설정
print(mymath.MYPI)
mymath.func("모듈 사용")

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,7))
plt.boxplot(([100,87,29,76,88], [20,30,20,1000,20]))
plt.grid()
plt.show()
fig.savefig("graph.png")