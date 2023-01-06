# 实现日志系统的函数
def log_request(req: 'flask_request',res: str) -> None:
    """返回用户输入的数据以及查询结果加入表格"""
    with open('weather.log', 'a') as log:
        print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')