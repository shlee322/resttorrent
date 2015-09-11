
MODULES = [
    'resttorrent.app',
    'resttorrent.modules.socketio',
    'resttorrent.commands.get_session_list',
    'resttorrent.commands.create_session',
    'resttorrent.commands.get_session',
    'resttorrent.commands.delete_session',
    'resttorrent.commands.upload_torrent',
    'resttorrent.commands.get_torrent_list',
]


def load_modules():
    for module in MODULES:
        __import__(module, globals(), locals(), [])
