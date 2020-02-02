# -*- coding: gbk -*-
from flask import Flask,render_template,redirect


app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    image_base='../static/images/'

    #���������Ϣ
    class cop_info:
        def __init__(self,name,path):
            self.name=name
            self.path=path
    cop_infos=[]
    cop_names = [
        '��ʦ�ƽ�',
        '�㶫ר�屾������',
        '�㶫ר�屾�п���',
        '���ݴ�ѧ',
        '����ʦ��ѧԺ',
        '�㶫����ѧԺ',
        '�㶫�ƾ���ѧ',
        '�㶫��ѧԺ',
    ]
    for i in range(8):
        cop_infos.append(cop_info(
            name=cop_names[i],
            path=image_base+'logo{}.jpg'.format(i+1)))

    #��ҵ�Ŷ���Ϣ
    class team_info:
        def __init__(self,name,path,content,link):
            self.name = name
            self.path=path
            self.content = content
            self.link=link
    team_names=['��һ��','�����','��С��','����','������','������','����','�Ʋ�',]
    team_content=[
        '��һ��ԭ����ب�����Լ�������ب�ֳ���һ����������ˡ���һ���Ŀ�����������ϰ������ʵ����11�ҹ�˾',
        '����ʱ�ڸ���Ƶ����ʱ��Ϊÿ������������£����ĵ���Ͷ���Ƕ�����õĹ���~������ôô��',
        '�����쵽���죬��֧������Բ���ˡ���Ҿõ��ˡ���ε������������ã���һ�ο��ζ������ֲ��ˣ���ĺ���ѽ��',
        '�ھɽ�ɽ���ְִ���һ��~ �����������ʶһ������',
        'ǰһ��ʱ����ϴ���ʱ�� ����ͻȻ��Ѫ��ֹ����ļ��������ɱ�ֳ�һ�����Ҿ��ã���������������ǲ��ܲ����ˡ�',
        '��������1977��11��13������ɽ��ʡ�ൺ�����������й��ڵ�����Ա�����֡����ˣ���ҵ�ڱ�����ӰѧԺ����ϵ��',
        '���ݣ�1986��9��12�ճ����ڱ����У��й��ڵ�Ӱ��Ů��Ա�������ָ��֡�Ӱ����Ƭ�ˡ�2005�꣬���ݽ��뱱����ӰѧԺ����ϵ���ư�Ͷ���',
        '�Ʋ���1974��8��26�ճ�����ɽ���ൺ���漮������䬣��й��ڵ�����Ա�����ݡ����֣��й���Ӱ��Э�ḱ��ϯ��',
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

    #ѧ���ɾ���Ϣ
    class stu_goal_info:
        def __init__(self,name,content):
            self.content=content
            self.name=name
    stu_goal_infos=[]
    stu_goal_name=['������','������','��Ц��']
    stu_goal_content=[
        '2018��4��28�գ���ֵ�廪��ѧ107����У�죬�������Ŷ��¾���ϯ����ϯִ�й���ǿ��������������������廪��ѧ����2��Ԫ����ң�����֧���廪��ѧ��������Ժ���廪��ѧѧ��ȫ��ʤ������չָ�����ļ��廪��ѧ���Ӽ��㡢AI�о�����Ӧ������������Ŀ�Ľ���ͷ�չ',
        '1996�꣬���ݸ����ײ���Ӱ�����ǵ�ơ����Ӷ���ʽ��������Ȧ [1]  ��1998�꣬�ھ����Ӱ���ҵĸ���ĸ�ס�������Ů������� [2]  ����ƾ���Ƭ��õ�23����ڵ�Ӱ�ٻ������Ů���ǽ� [3]  ���������Ů���ǽ����ǽ����ǽ����ǽ����ǽ����ǽ�',
        '��Ц�죨1939��11��13�ա�2016��2��23�գ����������ӻ����ͻ����϶����������ں�����ʡ�������������غ��������й��ڵ����ҡ���磬��ҵ�ڶ���ʦ����ѧ��ʷϵ�����ҡ���磬��ҵ�ڶ���ʦ����ѧ��ʷϵ���ҡ���磬��ҵ�ڶ���ʦ����ѧ��ʷϵ',
    ]
    for i in range(len(stu_goal_name)):
        stu_goal_infos.append(stu_goal_info(
            name=stu_goal_name[i],
            content=stu_goal_content[i],
        ))

    #ͼƬ������ģ����Ϣ
    class TAP:
        def __init__(self,src,name,href,content):
            self.src=src
            self.name=name
            self.href=href
            self.content=content
    fake_content='���дЩ������������'
    srcs=[]
    for i in range(6):
        srcs.append(image_base+'blog-{}.jpg'.format(i+1))
    taps=[TAP(srcs[0],'������','#',fake_content)]*6
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