"""
1. 角色: 姓名 性别 职业
2. 功能:
需求: 王者荣耀角色管理系统
       1 添加角色
       2 删除角色
       3 修改角色
       4 查询角色
       5 显示所有角色
       6 退出系统
"""
import time

character = []  # 存放角色的列表
while True:
    print('*' * 80 + '王者荣耀角色管理' + '*' * 80)
    choice = input('请选择功能:\n1-添加角色\n2-删除角色\n3-修改角色\n4-查询角色\n5-显示所有角色\n6-退出系统\n')
    print('*' * 80 + '王者荣耀角色管理' + '*' * 80)
    if choice == '1':
        print('-' * 80 + '添加角色' + '-' * 80)
        name = input('输入角色名:')
        sex = input('输入角色性别:')
        job = input('输入角色职业:')
        role = [name, sex, job]
        character.append(role)
        print(f'成功添加{name}角色')
        print('-' * 80 + '添加角色' + '-' * 80)
    elif choice == '2':
        print('-' * 80 + '删除角色' + '-' * 80)
        del_name = input("输入要删除的角色名:")
        for j in character:  # 每次遍历的都是一个子列表
            if del_name in j:
                character.remove(j)
                print(f'成功删除{del_name}')
                break
        else:
            print('本系统不存在此角色, 请重新输入角色名称')
        print('-' * 80 + '删除角色' + '-' * 80)
    elif choice == '3':
        print('-' * 80 + '修改角色' + '-' * 80)
        change_name = input('输入要修改的角色的名字:\n')
        for a in character:
            if change_name in a:
                print('存在该角色, 请输入修改的内容')
                answer = input('1-修改名字   2-修改性别    3-修改职业\n')
                if answer == '1':
                    newname = input('输入该角色的新名字')
                    a[0] = newname
                    print(f'角色名字修改成功, 角色名变为{newname}')
                elif answer == '2':
                    new_sex = input('输入该角色的新性别')
                    a[1] = new_sex
                    print(f'该角色性别修改成功, 性别变为{new_sex}')
                elif answer == '3':
                    new_job = input('输入该角色的新职业')
                    a[2] = new_job
                    print(f'该角色性别修改成功, 性别变为{new_job}')
                else:
                    print('选项错误, 请重新选择')
        print('-' * 80 + '修改角色' + '-' * 80)
    elif choice == '4':
        print('-' * 80 + '查询角色' + '-' * 80)
        find_name = input("输入要查询的角色名:")
        for k in character:  # 每次遍历的都是一个子列表
            if find_name in k:
                print('存在此角色, 角色信息如下')
                print('姓名' + '\t' * 10 + '性别' + "\t" * 10 + '职业')
                print(k[0], end="\t" * 10)
                print(k[1], end="\t" * 10)
                print(k[2], end="\t" * 10)
                break
        else:
            print('本系统不存在此角色, 请重新输入角色名称')
        print('-' * 80 + '删除角色' + '-' * 80)
    elif choice == '5':
        print('-' * 80 + '角色列表' + '-' * 80)
        print('姓名' + '\t'*10 + '性别' + "\t"*10 + '职业')
        for i in character:
            print(i[0], end="\t" * 10)
            print(i[1], end="\t" * 10)
            print(i[2], end="\t" * 10)
            print()
        print('-' * 80 + '角色列表' + '-' * 80)
    elif choice == '6':
        print('正在退出~')
        time.sleep(2)  # 休眠两秒
        print('退出成功')
        break
    else:
        print('选择错误, 请重新选择')











































