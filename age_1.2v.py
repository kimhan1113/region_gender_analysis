import csv
import matplotlib.pyplot as plt

# 동일 이름인 지역이 있을 수 있기 때문에 2개 이상인 곳은 둘다 그래프 띄우기!!!
f = open('gender.csv')
data = csv.reader(f)

# name = input('알고 싶은 지역 이름 입력해주세요 : ')

name = '부흥동'
# 엑셀에서 쉼표(,) 꼭 지우기 -> 서식지우기 하면됨!!

for row in data:
    if name in row[0]:

        region = []
        region.append(row[0])

        for r in region:
            m = []
            f = []
            for i in range(101):
                m.append(-int(row[i + 3]))
                f.append(int(row[-(i + 1)]))

            f.reverse()
            plt.rc('font', family='Malgun Gothic')
            plt.barh(range(101), m, label='남성')
            plt.barh(range(101), f, label='여성')
            plt.rcParams['axes.unicode_minus'] = False
            plt.legend()
            plt.style.use('ggplot')

            # plt.title(r + '_지역의 2019년 12월 남녀 인구구조', fontsize=10)
            plt.title(r + '지역의 2019년 12월 남녀 인구구조')

            # plt.savefig('{}.png'.format(r + '_지역의인구비율'), dpi=300)
            plt.show()




