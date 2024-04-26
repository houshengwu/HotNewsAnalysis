import jieba
import wordcloud
from imageio import imread
# 排除词库
excludes = {
    '两个', '一个', '只见', '如何', '那里', '说道', '这里', '出来', '这个', '今日', '便是', '问道',
    '起来', '甚么', '因此', '却是', '我们', '正是', '三个', '如此', '且说', '不知', '不是', '只是',
    '次日', '不曾', '不得', '一面', '看时', '不敢', '如今', '来到', '当下', '原来', '喝道', '只得',
    '里面', '大喜', '一齐', '商议', '那个', '公人', '将来', '前面', '那厮', '城中', '下山', '不见',
    '怎地', '上山', '随即', '不要'
}
# 读入水浒传，分词，并以空格连接
txt = open("水浒传.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
txt0 = ''
for i in words:
    if len(i) > 1:
        txt0 += ' '
        txt0 += i
txt0.replace('宋江道', '宋江')  # 纠正错误分词
# mk = imread('皮卡丘.jpg')  # 设置蒙版为皮卡丘
w = wordcloud.WordCloud(
    width=1920,
    height=1080,  # 设置图片长宽为1080p
    background_color='white',  # 设置背景颜色为白色
    font_path='C://Windows//Fonts/msyh.ttc',  # 设置字体为微软雅黑
    max_words=300,  # 设置词汇最大数量为300
    stopwords=excludes,  # 设置排除词库
    # mask=mk,  # 设置蒙版
    colormap='magma'  # 设置配色集为magma
)
w.generate(txt0)
w.to_file('img.png')
