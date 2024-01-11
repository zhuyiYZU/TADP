import pandas as pd

# 读取DAT文件（假设DAT文件使用制表符分隔字段，如果使用其他分隔符，请相应地设置sep参数）
dat_file_path = '/home/ubuntu/user_lzl/simplernn_0_combined_swap_10_500.dat'
df = pd.read_csv(dat_file_path, sep='\t',error_bad_lines=False,encoding='iso-8859-1')

# 保存为CSV文件
csv_file_path = '/home/ubuntu/user_lzl/file.csv'
df.to_csv(csv_file_path, index=False)
