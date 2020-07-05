from flask import Flask, render_template, flash, redirect, request, url_for


from flask_hcaptcha import hCaptcha
import requests

app = Flask(__name__)

hcaptcha = hCaptcha()
hcaptcha.init_app(app)
# RECAPTCHA_ENABLED=True
RECAPTCHA_SITE_KEY = "aedd98f2-fb87-4a94-a1d2-b82133b99216"
RECAPTCHA_SECRET_KEY = "0x9529f006371c495190B40DEAfD1B805608794e7e"
VERIFY_URL = "https://hcaptcha.com/siteverify"

# hcaptcha.init_app(app, RECAPTCHA_SITE_KEY, RECAPTCHA_SECRET_KEY)

# hcaptcha.init(app, RECAPTCHA_SITE_KEY, RECAPTCHA_SECRET_KEY, is_enabled=True)
# app.config.update({
#     "debug": False,
#     "HCAPTCHA_SITE_KEY": RECAPTCHA_SITE_KEY,
#     "HCAPTCHA_SITE_SECRET": RECAPTCHA_SECRET_KEY,
#     "HCAPTCHA_ENABLED": True
# })

hcaptcha = hCaptcha(site_key=RECAPTCHA_SITE_KEY,
                    secret_key=RECAPTCHA_SECRET_KEY, is_enabled=True)


@app.route("/confirm")
def index():
    captcha_html = hcaptcha.get_code()
    print("Captch" + captcha_html)
    return render_template("captcha.html", captcha_html=captcha_html)


@app.route("/submit", methods=["POST"])
def submit():

    token = request.form.get('h-captcha-response')
    print("request.form: " + repr(request.form))
    print(token)

    if not hcaptcha.verify():
        return render_template("error.html")

    # else:
    
        # flash('Captcha Was incorrect please try again!')
        # print(f"-->|{token}|<--")
    return render_template("index.html")


# if __name__ == '__main__':
app.run(host='0.0.0.0', debug=True, port=3333)
# app.run(host="0.0.0.0", debug=True, port=8080)
