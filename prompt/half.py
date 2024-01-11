with open('scripts/TextClassification/newsgroups6/manual_verbalizer.txt', 'r') as file:
    lines = file.readlines()
with open('scripts/TextClassification/newsgroups6/manual_verbalizer.txt', 'w') as file:
    for line in lines:
        # 去除行末的换行符
        line = line.strip()

        # 将每行的单词按逗号分隔
        words = line.split(',')

        # 计算需要保留的单词数量（前一半）
        half_length = len(words) // 2

        # 获取前一半的单词
        first_half_words = words[:half_length]

        # 将前一半的单词重新组合成一行并打印出来
        result_line = ','.join(first_half_words)
        file.write(result_line + '\n')
