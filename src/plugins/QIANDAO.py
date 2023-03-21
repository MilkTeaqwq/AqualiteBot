import os
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import datetime as datetime
from nonebot.typing import T_State
import random

sign = on_keyword({'签到', 'sign', '/sign'})

@sign.handle()
async def sign_handle(bot: Bot, event: Event, state: T_State):
    today = datetime.date.today()
    id = event.get_user_id()
    getncm = random.randint(1,10)
    user_qq = int(event.get_user_id())
    qd_ok1 = f"[CQ:at,qq={id}]"
    qd_ok2 = f'\n{today}\n签到成功！\n获得了{getncm}瓶奶茶！\n查看已拥有的奶茶请发送：我的奶茶 或 !mm'
    qd_ok = qd_ok1 + qd_ok2
    qd_no1 = f"[CQ:at,qq={id}]"
    qd_no2 = f'\n{today}\n今天已经签到过了哦！\n查看已拥有的奶茶请发送：我的奶茶 或 !mm'
    qd_no = qd_no1 + qd_no2
    file_path = 'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\签到记录'
    nc_path = f'C:\\Users\\Administrator\\Desktop\\MilkTea237\\MilkTea237\\data\\Aqualite\\奶茶总数'
    nc_paths = f'{nc_path}\\{user_qq}.txt'
    file_paths = f'{file_path}\\{user_qq}{today}.txt'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        print(f'当前无匹配路径，已自动创建目录{file_path}')
    elif not os.path.exists(nc_path):
        os.makedirs(nc_path)
        print(f'当前无匹配路径，已自动创建目录{nc_path}')
    elif not os.path.exists(nc_paths):
        with open(nc_paths, 'w') as n:
            n.write(f'{getncm}')
            n.close()
        with open(file_paths,'w') as a:
            a.write('114514')
            a.close()
            await sign.finish(Message(f'{qd_ok}'))
    else:
        if os.path.isfile(file_paths):
            await sign.finish(Message(f'{qd_no}'))
        else:
            ncs = open(nc_paths,'r',encoding='utf-8').read()
            with open(nc_paths, 'w') as n:
                ncms = int(ncs) + getncm
                n.write(str(ncms))
                n.close()
            with open(file_paths,'w') as a:
                a.write('114514')
                a.close()
                await sign.finish(Message(f'{qd_ok}'))

