import pymysql
import json

def get_phq_result(phone,cursor,num=4):
    sql = f"select * from `PHQ-9` where right(id,{num}) = '"+phone+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return "未查询到该用户PHQ-9数据"

def get_gad_result(phone,cursor,num=4):
    sql = f"select * from `GAD-7` where right(id,{num}) = '"+phone+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return "未查询到该用户GAD-7数据"

def get_dialoge_result(phone,cursor,num=4):
    sql = f"select dialogue from `instant_info` where right(id,{num}) = '"+phone+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        result = result[0][0]
        result = json.loads(result)
        # 对对话进行过滤
        filtered_dialogue = [{item['role']: item['content']} for item in result]
        return filtered_dialogue
    else:
        return "未查询到该用户对话数据"

def check_num_q(phone,cursor,num=4):
    sql = f"select count(*) from `student_info` where right(id,{num}) = '"+phone+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]
