"""
需求:
.............................................................................
昨天晚会遇到一个漂亮的小姐姐, 要不要表白
.............................................................................
输入用户名: 小白
反复回复:
    1. 回复的内容不能为空
    2. 里面不能存在敏感词汇
    3. 最多评论20个字,
    4. 回复的内容前后不能有空格
"""


message = input("发表一句话: ")

print('以下为回复内容: ')
print('*' * 50)

while True:
    username = input('请输入你的用户名: ')
    while True:
        comment = input("评论: ")
        comment = comment.strip(' ')
        if len(comment) != 0:
            if len(comment) <= 20:
                comment = comment.replace('丑陋', '**')
                print(f'{username}发表的评论是{comment}')
                break
            else:
                print('评论字数不能超过20字, 请重新输入')
        else:
            print("评论内容不能为空, 请重新输入")


















