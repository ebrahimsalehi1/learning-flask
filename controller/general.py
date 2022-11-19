from init import app

@app.route('/')
def index():
    return "Learning Flask !!!"