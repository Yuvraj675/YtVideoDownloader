from flask import Flask,  render_template, request, send_file, redirect
from pytube import YouTube
app = Flask(__name__)
import os


@app.route("/", methods = ['GET', 'POST'])
def best_quality():
    
    b = os.listdir()

    for file in b:
        if file.endswith(".mp4"):
            os.remove(file)

    if request.method == "POST" :
        if 'link' in request.form:
            link = request.form['link']
            quality = request.form["quality"]
            yt = YouTube(link)
            global a
            if quality == "hq":
                a = yt.streams.get_highest_resolution()
            elif quality == "720p":
                a = yt.streams.get_by_resolution("720p")
            elif quality == "360p":
                a = yt.streams.get_by_resolution("360p")
            elif quality == "480p":
                a = yt.streams.get_by_resolution("480p")
    
            if a == None:
                # a = yt.streams.get_highest_resolution()
                return redirect("/error")
            else:
                return redirect('/downloading')
        

    return render_template("index.html")

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500
  

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/downloading",  methods = ['GET', 'POST'])
def downloading():
    
    if request.method == "POST" :
         return redirect("/download")
    else:
    # return send_file(a.download(), as_attachment=True)
        return render_template("downloading.html")

@app.route("/download",  methods = ['GET', 'POST'])
def download():
    
    return send_file(a.download(), as_attachment=True)



app.run(host = "0.0.0.0", port=8080  ,debug = False)


# 