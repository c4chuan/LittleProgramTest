import pymysql
from config import config
from tools import get_phq_result,get_gad_result,get_dialoge_result,check_num_q

# 使用config中的配置连接数据库
db_config = config['database']
conn = pymysql.connect(host=db_config['host'],user=db_config['user'],password=db_config['password'],database=db_config['database'])
cursor = conn.cursor()

if __name__ == '__main__':
    while True:

        phone = input("请输入手机号后四位：")
        # 检查是否有重复数据，若有则判断多少位数合适
        num_q = check_num_q(phone,cursor)
        print(num_q)
        print('该用户的对话数据为：'+str(get_dialoge_result(phone,cursor)))
        print('该用户的PHQ-9数据为：'+str(get_phq_result(phone,cursor)))
        print('该用户的GAD-7数据为：'+str(get_gad_result(phone,cursor)))
