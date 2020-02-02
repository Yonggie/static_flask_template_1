# -*- coding: gbk -*-
from flask import Flask,render_template,redirect


app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    image_base='../static/images/'

    #合作伙伴信息
    class cop_info:
        def __init__(self,name,path):
            self.name=name
            self.path=path
    cop_infos=[]
    cop_names = [
        '华师科教',
        '广东专插本考试网',
        '广东专插本招考网',
        '广州大学',
        '岭南师范学院',
        '广东金融学院',
        '广东财经大学',
        '广东理工学院',
    ]
    for i in range(8):
        cop_infos.append(cop_info(
            name=cop_names[i],
            path=image_base+'logo{}.jpg'.format(i+1)))

    #创业团队信息
    class team_info:
        def __init__(self,name,path,content,link):
            self.name = name
            self.path=path
            self.content = content
            self.link=link
    team_names=['朱一旦','大祥哥','欣小萌','星悦','李永乐','黄晓明','杨幂','黄渤',]
    team_content=[
        '朱一旦原名朱亘，把自己的名字亘分成了一旦，这才有了“朱一旦的枯燥生活”。朱老板的名下实际有11家公司',
        '特殊时期更新频率暂时改为每周五晚六点更新！您的点赞投币是对我最好的鼓励~爱你们么么大！',
        '从夏天到秋天，这支舞终于圆满了。大家久等了。这次的舞是浪人琵琶，第一次看嘉儿跳就种草了，真的好美呀，',
        '在旧金山跟爸爸呆了一天~ 我想带你们认识一下他！',
        '前一段时间我洗澡的时候 腿上突然喷血不止，搞的家里面跟凶杀现场一样。我觉得，我这个静脉曲张是不能不治了。',
        '黄晓明，1977年11月13日生于山东省青岛市市南区，中国内地男演员、歌手、商人，毕业于北京电影学院表演系。',
        '杨幂，1986年9月12日出生于北京市，中国内地影视女演员、流行乐歌手、影视制片人。2005年，杨幂进入北京电影学院表演系本科班就读。',
        '黄渤，1974年8月26日出生于山东青岛，祖籍甘肃临洮，中国内地男演员、导演、歌手，中国电影家协会副主席。',
    ]
    team_links=[
        'https://www.bilibili.com/video/av59028923',
        'https://www.bilibili.com/video/av83601490',
        'https://www.bilibili.com/video/av33962846',
        'https://www.bilibili.com/video/av57196621',
        'https://www.bilibili.com/video/av57715127',
        'https://baike.baidu.com/item/%E9%BB%84%E6%99%93%E6%98%8E/6597',
        'https://www.bilibili.com/video/av77503400',
        'https://www.bilibili.com/video/av3009493'
    ]

    team_infos=[]
    for i in range(8):
        team_infos.append(team_info(
            name=team_names[i],
            path=image_base+'cover-{}.jpg'.format(i+1),
            content=team_content[i],
            link=team_links[i]
        ))

    #学生成就信息
    class stu_goal_info:
        def __init__(self,name,content):
            self.content=content
            self.name=name
    stu_goal_infos=[]
    stu_goal_name=['章泽天','章子怡','张笑天']
    stu_goal_content=[
        '2018年4月28日，正值清华大学107周年校庆，京东集团董事局主席兼首席执行官刘强东与夫人章泽天宣布向清华大学捐赠2亿元人民币，用于支持清华大学苏世民书院、清华大学学生全球胜任力发展指导中心及清华大学量子计算、AI研究、供应链和物流等项目的建设和发展',
        '1996年，出演个人首部电影《星星点灯》，从而正式进入演艺圈 [1]  。1998年，在剧情电影《我的父亲母亲》中饰演女主角招娣 [2]  ，并凭借该片获得第23届大众电影百花奖最佳女主角奖 [3]  。花奖最佳女主角奖主角奖主角奖主角奖主角奖主角奖',
        '张笑天（1939年11月13日—2016年2月23日），笔名纪延华、纪华、严东华，出生于黑龙江省哈尔滨市延寿县黑龙宫镇，中国内地作家、编剧，毕业于东北师范大学历史系。作家、编剧，毕业于东北师范大学历史系作家、编剧，毕业于东北师范大学历史系',
    ]
    for i in range(len(stu_goal_name)):
        stu_goal_infos.append(stu_goal_info(
            name=stu_goal_name[i],
            content=stu_goal_content[i],
        ))

    #图片和文字模块信息
    class TAP:
        def __init__(self,src,name,href,content):
            self.src=src
            self.name=name
            self.href=href
            self.content=content
    fake_content='随便写些东西，待开发'
    srcs=[]
    for i in range(6):
        srcs.append(image_base+'blog-{}.jpg'.format(i+1))
    taps=[TAP(srcs[0],'待开发','#',fake_content)]*6
    return render_template('index.html',
                           cop_infos=cop_infos,
                           team_infos=team_infos,
                           stu_goal_infos=stu_goal_infos,
                           text_pic_infos=taps
                           )

#http://127.0.0.1:5000/contact-us/contact-us problem

@app.route('/404/')
def for404():
    return render_template('404.html')
@app.route('/about-us/')
def about_us():
    return render_template('about-us.html')

@app.route('/contact-us/')
def contact_us():
    return render_template('contact-us.html')

@app.route('/courses-detail/')
def courses_detail():
    return render_template('courses-detail.html')

@app.route('/single-course/')
def single_course():
    return render_template('single-course.html')

@app.route('/single-post')
def single_post():
    return render_template('single-post.html')

@app.route('/former-years/')
def former_years():
    return render_template('former-years.html')

@app.route('/mini-program/')
def mini_program():
    return render_template('mini-program.html')

if __name__=='__main__':
    #app.run(debug=True,host='0.0.0.0')
    app.run(debug=True)