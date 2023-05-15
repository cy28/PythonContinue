"""
hashlib模块是Python标准库中的一个模块，提供了多种加密哈希算法的实现。它用于计算数据的哈希值，常用于密码学、数据完整性校验、数字签名等领域。
以下是hashlib模块的一些常见功能和用法：

哈希算法：
md5(): 创建一个MD5哈希对象。
sha1(): 创建一个SHA-1哈希对象。
sha256(): 创建一个SHA-256哈希对象。
sha512(): 创建一个SHA-512哈希对象。

更新哈希对象：
update(data): 更新哈希对象的输入数据。可以多次调用此方法以追加数据。

获取哈希值：
hexdigest(): 返回哈希对象的十六进制表示的哈希值。
digest(): 返回哈希对象的原始字节表示的哈希值。
"""

import hashlib

msg = '今天中午一起吃饭'

md5 = hashlib.md5(msg.encode('utf-8'))  # 这是不可逆的

print(md5.hexdigest())  # 5a72b2a219d514ba7625be19a5edd211






































