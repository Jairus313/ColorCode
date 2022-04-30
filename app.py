from flask import Flask, render_template, request, send_from_directory
from color_extractor import ColorCodes


# name of the flask name
app = Flask(__name__)


# allowed file types for prediction
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# error handlings.
@app.errorhandler(500)
def error_page(e):
    return render_template("error.html")

@app.errorhandler(405)
def error_page(e):
    return render_template("error.html")

# home page.
@app.route("/")
def index():
    return render_template("index.html")

# profile picture for demo page.
@app.route("/profile_pic")
def profile_pic():
    try:
        return send_from_directory("templates","profile_pic.jpg")
    except Exception as err:
        #return jsonify(success=False, response=str(err))
        return render_template("error.html")

# upload page for prediction.
@app.route("/uploaded_image")
def uploaded_image():
    try:
        return send_from_directory("./","image.jpg")
    except Exception as err:
        #return jsonify(success=False, response=str(err))
        return render_template("error.html")

# demo/tutorial page.
@app.route("/demo")
def demo():
    try:
        return render_template("demo.html")
    except Exception as err:
        #return jsonify(success=False, response=str(err))
        return render_template("error.html")

# uploading image page.
@app.route("/upload", methods=["GET"])
def upload_image():
    try:
        return render_template("upload_image.html")
    except Exception as err:
        #return jsonify(success=False, response=str(err))
        return render_template("error.html")

# about author page.
@app.route("/about_me")
def about_me():
    try:
        return render_template("about_me.html")
    except Exception as err:
        #return jsonify(success=False, response=str(err))
        return render_template("error.html")

# prediction page.
@app.route("/result", methods=["POST", "GET"])
def result():
    try:
        file = request.files['file']
        num_of_color = request.form['btnradio']

        if file and allowed_file(file.filename):
            filename = "image.jpg"
            file.save(filename)

            color_codes = ColorCodes(filename, int(num_of_color))
            color_hex_codes = color_codes.extract_colors_code()

            if color_hex_codes:
                return render_template("result.html", color_codes=color_hex_codes)
            else:
                return render_template("error.html")

        else:
            #return jsonify(success=False, response="Uploaded the file is not valid, Please upload images only.")
            return render_template("error.html")

    except Exception as err:
        print(err)
        return render_template("error.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)