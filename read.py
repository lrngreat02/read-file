# 读取档案
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		print(len(data)
			print(len(data)  # print很费时间
print('档案读取完了，总共有', len(data), '笔资料'）
print(data[0])
print('----------------')
print(data[1])

# 留言总长度
sum_len = 0  # 橙色
for d in data:
	sum_len += len(d)
print('留言的平均长度为'， sum_len/len(data)

# 筛选：留言长度小于100的
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有'， len(new), '笔留言长度小于100')
print(new[0])

# 筛选：留言中有'good' 
# good = [d for d in data if 'good' in d]
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(good[0])

# 筛选：判断每一条留言中是否有‘bad'
bad = ['bad' in d for d in data]
print(bad)