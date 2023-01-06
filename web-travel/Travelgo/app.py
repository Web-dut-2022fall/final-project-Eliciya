from flask import Flask, render_template, request
from flask import escape
import weather
from log_sys import log_request
app = Flask(__name__)
import road
# 下面的注释是为了让进入路径成功不变灰
# noinspection PyUnresolvedReferences
import xingzuo

# 登录页面
@app.route('/login',methods=['GET'])
def login() -> 'html':
    return render_template('login.html')

# 注册页面
@app.route('/setup',methods=['GET'])
def setup() -> 'html':
    return render_template('setup.html')

# 步行导航
@app.route('/walk', methods=['POST'])
# 传输数据
def road_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    begin = request.form['begin']
    end = request.form['end']
    title = '这里是帮你占卜到的路线：'
    begincode = road.geocode(key1, begin)
    endcode = road.geocode(key1, end)
    results = str(road.walking(key1, begincode, endcode))
    log_request(request, results)

    return render_template('roadresult.html',
                           the_title=title,
                           the_begin=begin,
                           the_end=end,
                           the_road=results,
                           the_results=results)

# 驾车导航
@app.route('/car', methods=['POST'])
# 传输数据
def car_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    begin = request.form['begin']
    end = request.form['end']
    title = '这里是帮你占卜到的路线：'
    # 先使用地理编码api将用户的地址转化为地理编码
    begincode = road.geocode(key1 ,begin)
    endcode = road.geocode(key1 ,end)
    # 进行驾车api调用
    results = str(road.car(key1, begincode, endcode))
    log_request(request,results)

    return render_template('roadresult.html',
                           the_title=title,
                           the_begin=begin,
                           the_end=end,
                           the_road=results,
                           the_results=results)

# 骑行导航
@app.route('/bike', methods=['POST'])
# 传输数据
def bike_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    begin = request.form['begin']
    end = request.form['end']
    title = '这里是帮你占卜到的路线：'
    begincode = road.geocode(key1, begin)
    endcode = road.geocode(key1, end)
    results = str(road.bike(key1, begincode, endcode))
    log_request(request, results)

    return render_template('roadresult.html',
                           the_title=title,
                           the_begin=begin,
                           the_end=end,
                           the_road=results,
                           the_results=results)

# 天气查询
@app.route('/weathersearch', methods=['POST'])
# 传输数据
def do_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    city = request.form['city']
    title = '这里是占卜的结果：'
    results = str(weather.weather1(key1, city))
    log_request(request,results)

    return render_template('results.html',
                           the_title=title,
                           the_city=city,
                           the_weather=results,
                           the_results=results)

# 温度查询
@app.route('/temperature', methods=['POST'])
# 传输数据
def wendu_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    city = request.form['city']
    title = '这里是占卜的结果：'
    results = str(weather.temperature(key1, city))
    log_request(request,results)

    return render_template('results.html',
                           the_title=title,
                           the_city=city,
                           the_weather=results,
                           the_results=results)

# 风向查询
@app.route('/winddirection', methods=['POST'])
# 传输数据
def winddirection_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    city = request.form['city']
    title = '这里是占卜的结果：'
    results = str(weather.winddirection(key1, city))
    log_request(request,results)
    return render_template('results.html',
                           the_title=title,
                           the_city=city,
                           the_weather=results,
                           the_results=results)

# 风力查询
@app.route('/windpower', methods=['POST'])
# 传输数据
def fengli_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    city = request.form['city']
    title = '这里是占卜的结果：'
    results = str(weather.windpower(key1, city))
    log_request(request,results)
    return render_template('results.html',
                           the_title=title,
                           the_city=city,
                           the_weather=results,
                           the_results=results,)

# 湿度查询
@app.route('/humidity', methods=['POST'])
# 传输数据
def shidu_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    city = request.form['city']
    title = '这里是占卜的结果：'
    results = str(weather.humidity(key1, city))
    log_request(request,results)

    return render_template('results.html',
                           the_title=title,
                           the_city=city,
                           the_weather=results,
                           the_results=results)

# 天气整体查询
@app.route('/quanbu', methods=['POST'])
# 传输数据
def quanbu_search() -> 'html':
    key1 = "5ae4d72387a97e8529903ac948ab9eff"
    city = request.form['city']
    title = '这里是占卜的结果：'
    results = str(weather.quanbu(key1, city))
    log_request(request,results)

    return render_template('all.html',
                           the_title=title,
                           the_city=city,
                           the_weather=results,
                           the_results=results,)

# 日志系统
@app.route('/viewlog')
def view_the_log() -> 'html':
    """将用户输入和返回的数据装进表格"""
    contents = []
    with open('weather.log','r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    len(contents)
    titles = ('用户提交','远程地址','访问代理','用户结果')
    return render_template('viewlog.html',
                           the_title='日志系统后台',
                           the_row_title=titles,
                           the_data=contents)

# 首页
@app.route('/')
@app.route('/entry')
def guanwang():
    title = '欢迎来到Travelgo!'
    return render_template("guanwang.html",
                           the_title = title)

# 进入主功能页
@app.route('/home',methods=['GET','POST'])
def shouye():
    title = '欢迎来到Travelgo!'
    topic = '来一起完善您的旅游计划吧(oﾟvﾟ)ノ'
    name1 = request.form.get('name1')
    astroid = request.form.get('xingzuo')
    results = str(xingzuo.yunshi(astroid))
    return render_template("yibiaopan.html",
                           the_title = title,
                           the_topic = topic,
                           the_name1 = name1,
                           the_xingzuo = results)

# 进入侧边栏的主功能页
@app.route('/homepage',methods=['GET','POST'])
def homepage():
    title = '欢迎来到Travelgo!'
    topic = '来一起完善您的旅游计划吧(oﾟvﾟ)ノ'
    return render_template("zhuye-wuxingzuo.html",
                           the_title = title,
                           the_topic = topic,)

# 天气栏的开屏
@app.route('/kaiping',methods=['GET','POST'])
def home():
    title = '欢迎来到天气占卜屋~'
    return render_template("home.html",
                           the_title=title,)

# 天气查询的首页
@app.route('/tianqizhanbu')
def tianqizhanbu() -> 'html':
    title = '欢迎来到天气占卜屋~'
    return render_template('weather-search.html',
                           the_title=title)

# 路径查询的首页
@app.route('/road')
def roadfind_page() -> 'html':
    title = '欢迎来到路径占卜屋~'
    return render_template('road.html',
                           the_title=title)

# 路径查询的开屏页
@app.route('/roadhome',methods=['GET','POST'])
def roadhome_page() -> 'html':
    title = '欢迎来到路径占卜屋~'
    return render_template('roadhome.html',
                           the_title=title)

if __name__ == '__main__':
    app.run()
