import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
# name = input('알고 싶은 지역 이름 입력해주세요 : ')

spec_region = []
name = '부흥동'
# 엑셀에서 쉼표(,) 꼭 지우기 -> 서식지우기 하면됨!!
# 제주특별자치도는 여러항목이 있으니 break 를 써서 오류나지 않도록 한다

for row in data:
    if name in row[0]:

        region = row[0].split(' ')
        # 동일 이름인 지역이 있기 때문에 이름을 구체적으로 표현하여 그래프로 표시 (예를 들어 부흥동은 안양,목포 2군데)
        spcific = region[-1] + region[-2]
        spec_region.append(spcific)
        if name in row[0]:
            for i in range(101):
                m.append(-int(row[i+3]))
                f.append(int(row[-(i+1)]))
            break

print(len(m), len(f))

names = ''.join(spec_region)

f.reverse()
plt.rc('font', family='Malgun Gothic')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.rcParams['axes.unicode_minus'] = False
plt.legend()
plt.style.use('ggplot')

plt.title(names + '_지역의 2019년 12월 남녀 인구구조', fontsize=13)

# plot 해당 하나 넣으면됨!
# plt.plot(result)
# bar는 x값에 범위, y값에 해당 수치 입력

# plt.savefig('{}.png'.format(names+ '_지역의인구비율'), dpi=300)
plt.show()




