from flask import Flask,render_template,redirect

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    paths=[
        '../static/images/logo1.png',
        '../static/images/logo2.jpg',
        '../static/images/logo3.jpg',
        '../static/images/logo4.png',
    ]
    return render_template('index.html',paths=paths)

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

@app.route('/news-formats')
def news_formats():
    return render_template('news-formats.html')

if __name__=='__main__':
    app.run(debug=True)