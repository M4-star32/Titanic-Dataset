# # range 相当于计数器记录循环次数
# for i in range(1,5): #range包前不包后 range里只有一个参数则从0开始
#     print(i)
#
# s = 0
# for i in range(1,101):
#     s +=i
# print('计算结果是:',s)


# break 和 continue
# i = 1
# while i <= 5:
#     print(f'今天是周{i}')
#     if i == 4:
#         print('今天是周四')
#         break
#     i += 1


for i in range(1,8):
    print(f'今天写作业了')
    if i == 5:
        print(f'今天不写作业')
        i +=1
        continue  #continue前要修改计数器，否则嵌套if会一直循环


