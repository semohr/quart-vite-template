from quart import Quart, render_template, send_from_directory, websocket

app = Quart(__name__)

# Register frontend folder
# basically a reverse proxy for the frontend
@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def reverse_proxy(path):
    # not include assets
    if (
        "assets" not in path
        and "logo.png" not in path
        and not path.startswith("favicon.ico")
    ):
        path = "index.html"

    # Remove everything infront of assets
    if "assets" in path:
        path = path[path.index("assets") :]
    if "logo.png" in path:
        path = path[path.index("logo.png") :]

    r = send_from_directory("../../frontend/dist/", path)
    return r

@app.route("/api")
async def json():
    return {"hello": "world"}

@app.websocket("/ws")
async def ws():
    while True:
        await websocket.send("hello")
        await websocket.send_json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
