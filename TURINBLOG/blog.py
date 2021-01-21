from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt


#kullanici kayit formu
class RegisterForm(Form):
    name = StringField("ISIM SOYISMI",validators=[validators.Length(min = 4,max = 25)])
    username = StringField("KULLANICI ADI",validators=[validators.Length(min = 5,max = 35)])
    email = StringField("Email Adresi",validators=[validators.Email(message = "LUTFEN GECERLI Bir Email Adresi Girin...")])
    password = PasswordField("PAROLA:",validators=[
        validators.DataRequired(message = "LUTFEN bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="parolaniz UYUSMUYOR...")
    ])
    confirm = PasswordField("Parola dogrula")

app = Flask(__name__)


app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "turinblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    #articles = [
    #   {"id":1 , "title":"deneme1", "content":"deneme1 icerik"},
    #    {"id":2 , "title":"deneme2", "content":"deneme2 icerik"},
    #    {"id":3 , "title":"deneme3", "content":"deneme3 icerik"}
    #]
    #return render_template("index.html",articles = articles)
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
#@app.route("/article/<string:id>")
#def detail(id):
#    return "Article ID: " + id
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate(): # POST 
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data) #password sha256
 
        cursor = mysql.connection.cursor()
 
        sorgu = "Insert into users (NAME,USERNAME,EMAIL,PASSWORD) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,username,email,password)) 
        cursor.close() 
        return redirect(url_for("index")) 
    else: 
        return render_template("register.html",form = form)
if __name__ == "__main__":
    app.run(debug=True)
     
