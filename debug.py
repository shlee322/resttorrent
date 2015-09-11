from resttorrent.load_modules import load_modules
from resttorrent.app import app

if __name__ == '__main__':
    load_modules()
    app.run(debug=True)
