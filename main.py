# -*- coding: gbk -*-
from flask import Flask,render_template,redirect


app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():

    paths=[
        '../static/images/logo2.jpg',
        '../static/images/logo3.jpg',
        '../static/images/logo4.png',
        '../static/images/logo6.jpg',
        '../static/images/logo7.jpg',
        '../static/images/logo8.jpg',
        '../static/images/logo9.jpg',
        '../static/images/logo10.jpg',
    ]
    names=[
        '华师科教',
        '广东专插本考试网',
        '广东专插本招考网',
        '广州大学',
        '岭南师范学院',
        '广东金融学院',
        '广东财经大学',
        '广东理工学院',
    ]
    path_and_name = {}
    for name,path in zip(names,paths):
        path_and_name[name]=path


    return render_template('index.html',path_and_name=path_and_name)

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
    app.run(debug=True,host='0.0.0.0')
    #app.run(debug=True)