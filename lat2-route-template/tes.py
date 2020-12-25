from flask import Flask, render_template, redirect, url_for
from forms import mahasiswa_P


app=Flask(__name__)
app.config['SECRET_KEY']="iboibo"

data_mahasiswa=[
    {'nama':'chaerul',
    'info':'ilkom',
    'alamat':'bogor'},

    {'nama':'sella',
    'info':'nurse',
    'alamat':'bandung'},

    {'nama':'rachel',
    'info':'nurse',
    'alamat':'bandung'}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data_mahasiswa", methods=['GET', 'POST'])
def data_m():
    form=mahasiswa_P()
    if form.validate_on_submit():
        return redirect(url_for('data_m'))
    return render_template("data_mahasiswa.html", data_mahasiswa=data_mahasiswa, form=form)

@app.route("/article/<info>")
def article_info(info):
    return "halaman article" + info

    


if __name__=="__main__":
    app.run(debug=True)

