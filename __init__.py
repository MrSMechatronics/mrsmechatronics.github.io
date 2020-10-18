from packages import *

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/videos")
@app.route("/Videos")
@app.route("/videos/")
@app.route("/Videos/")
def videos():
    if request.method == "GET":
        app.config['MYSQL_DB'] = "youtube"
        conn = mysql.connection.cursor()
        vids = conn.execute('SELECT * FROM `videos`')
        if vids:
            vidList = conn.fetchall()
            return render_template("videos.html", videos=vidList, l = url_for("watch"))
    else:
        pass        #return render_template("signup.html",form=signupForm())

@app.route("/watch")
@app.route("/Watch")
@app.route("/watch/<token>")
@app.route("/Watch/<token>")
def watch(token):
    app.config['MYSQL_DB'] = "youtube"
    conn = mysql.connection.cursor()
    vidExist = conn.execute('SELECT * FROM `videos` WHERE `token` = "' + token + '"')
    if vidExist:
        vidData = conn.fetchall()
        url = "https://www.youtube.com/embed/" + token
        return render_template("watch.html", data=vidData, vidUrl=url)
    else:
        return 'Invalid Video Token! Click <a href="' + url_for("videos") + '">Here</a> To See The List Of Available Videos'

@app.route("/account/recover", methods=["POST","GET"])
def recover():
    if request.method == "POST":
        return "hi"
    else:
        return render_template("recover.html");

@app.route("/account/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        form = signupForm()
        if form.validate_on_submit():
            conn = mysql.connection.cursor()
            #data = [request.form]
            mail = form.Email.data
            passw = form.Password.data
            usr_List = conn.execute('SELECT `password` FROM `users` WHERE Email = "' + mail + '"')
            if usr_List:
                list = conn.fetchall()
                data = list[0]
                hash = data[0]
                if check(passw, hash):#"logged in"
                    return "true"
                    session["UData"] = list
                    session["loggedIn"] = True
                    flash("Logged In Successfully!", "message")
                else:
                    return "false"
            else:            
                flash("Email Not Registered! Create A New Account.", "warning")
                return redirect(url_for("createUser"))
        else:
            return "ERROR"
#    elif "email" in session:
#        mail = session["email"]
#        passw = session["pass"]
#        usr_List = ""
#        if usr_List:
#            return "logged in"
#        else:
#            pass
    else:
        return render_template("login.html", form=loginForm())


@app.route("/account/new", methods=["POST","GET"])
def createUser():
    if request.method == "POST":
        form = signupForm()
        if form.validate_on_submit():
            conn = mysql.connection.cursor()
            data = request.form
            mail = form.Email.data
            passw = crypt(form.Password.data)
            nickn = form.Nickname.data
            user_count = conn.execute('SELECT 1 FROM `users` WHERE Email = "' + mail + '"')
            if user_count:
                flash("User Already Exists! Please Login.", "warning")
                return redirect(url_for("login"))
            else:
                flash("User Created Successfully! Please Login.","info")
                out = conn.execute("INSERT INTO `users`(`Nickname`, `Email`, `Password`) VALUES (%s,%s,%s)",(nickn,mail,passw))
                mysql.connection.commit()
                return redirect(url_for("login"))
        else:
            return("An Error Occured")
    else:
        return render_template("signup.html",form=signupForm())

def crypt(inp):

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(inp.encode('utf-8'),salt)
    #hashlib.sha512().update(inp)
    #return hashlib.sha512().hexdigest()

def check(inp, hash):

    return bcrypt.checkpw(inp.encode('utf-8'), bytes(hash.encode('utf-8')))

if __name__ == "__main__":
    app.run(debug=True)
