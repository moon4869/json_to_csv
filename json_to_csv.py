import json
# 原账号文件，json格式，'utf-8'编码
with open('user.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    temp = []
    for i in data:
        temp.append(i['type'])
        temp.append('T0')
        temp.append(i['title'])
        temp.append(i['account'])
        temp.append('密码_@X@_' + i['password'])
        # 备注可能为空，为空时新账号文件内该字段不填
        if i['note']:
            temp.append('备注_@X@_' + i['note'])
        w_str = ','.join(temp)
        # 新账号文件注意编码为'GB2312'
        with open('user.csv', 'a', encoding='GB2312') as res:
            res.write(w_str + '\n')
            temp = []
