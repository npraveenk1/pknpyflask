from flask import Flask, render_template, request, flash, redirect, url_for



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title='PKN Digital', nav='home')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", title='Projects')

@app.route("/projects/project_aws")
def project_aws():
	return render_template('project_aws.html', title='Project_AWS')


@app.route("/projects/project_mobile")
def project_mobile(): 
	return render_template('project_mobile.html', title='Project_Mobile')


@app.route("/projects/project_jenkins")
def project_jenkins():
	return render_template('project_jenkins.html', title='Project_Jenkins')


@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Not Found'), 404




if __name__ == "__main__":
    app.run(debug=True)