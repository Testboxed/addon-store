from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder = "app")

def Header(title: str, listelem: list):
    strx = ""

    for x in listelem:
        # icon - dfc-team/models-sandbox.png
        strx = strx + f"""
        <div class="addon-card" onclick="window.open('view-addon.html', '_blank', 'popup=true height=600 width=800')">
            <img src="/img/gamemode/{x['icon']}">
            <h3>{x['title']}</h3>
            <p>{x['author']}</p>
        </div>"""

    return f"""
    <h1>{title}</h1>
    <div class="addon-group">
        {strx}
    </div>
    """

xzxz = []
for x in range(1, 10):
    xzxz.append({"icon": "xz/xz.png", "title": x, "author": "DFC Team"})

@app.get("/")
def index():
    return render_template(
        "index.html",
        gamemodes = Header(
            "Gamemodes",
            xzxz
        )
    )

@app.route("/style.css")
def style():
    return send_from_directory("app", "style.css")

@app.route("/img/<path:path>")
def img_path(path):
    return send_from_directory("app/img", path)


app.run(
    port = 7000,
    debug = True
)