from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts1.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    villagename=db.Column(db.String(100),nullable=False)
    yeild=db.Column(db.Text,nullable=True)
    mobnum=db.Column(db.String(12),nullable=False)
    formername=db.Column(db.String(20),nullable=False,default='unknown')
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post '+str(self.id)
@app.route('/home')
def index():
    return render_template('index.html')

@app.route("/post",methods=['GET','POST'])
def post():

    if request.method=='POST':
        post_title=request.form['villagename']
        post_content=request.form['yeild']
        post_mobnum=request.form['mobnum']
        post_author=request.form['formername']
        new_post=BlogPost(villagename=post_title,yeild=post_content,mobnum=post_mobnum,formername=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/post')
    else:
        all_poste=BlogPost.query.all()
        return render_template('post.html',posts=all_poste)
@app.route("/post/delete/<int:id>")
def delete(id):
    post =BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/post')
@app.route('/post/update/<int:id>',methods=['GET','POST'])
def update(id):
    post=BlogPost.query.get_or_404(id)
    if request.method=='POST':
        post.title=request.form['villagename']
        post.content=request.form['yeild']
        post.mobnum=request.form['mobnum']
        post.author=request.form['formername']
        db.session.commit()
        return redirect('/post')
    else:
        return render_template('edit.html',post=post) 
@app.route('/post/new',methods=['GET','POST'])
def newpost():
    if request.method=='POST':
        post.title=request.form['villagename']
        post.content=request.form['yeild']
        post.mobnum=request.form['mobnum']
        post.author=request.form['formername']
        new_post=BlogPost(villagename=post.title,yeild=post.content,mobnum=post.mobnum,formername=post.author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/post')
    else:
        return render_template('newpost.html')
    return 
@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)