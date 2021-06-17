from flask import Flask, redirect, url_for, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/test", methods=["POST", "GET"])
def test():
	if request.method == "POST":
		mystring = request.form["string_to_cut"]
		return_string = ""
		for x in range(2, len(mystring), 3):
			return_string += mystring[x]
		return jsonify({"return_string": return_string})
	else:
		return render_template("test.html")

if __name__ == "__main__":
	app.run(debug=True)