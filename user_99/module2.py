# 模块调用其他模块
# 在同一个包中, 也要写完整的导入
from user_99.module import User
from article_99.module import Article

user = User('admin', 123456)

article = Article('个人总结', '嘉伟')

user.publish_article(article)


# 也可以使用 .表示当前目录

from .module import User








