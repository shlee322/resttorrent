from resttorrent.decorators import command


@command('1', '/sessions/<session_id>')
def get_session(session_id):
    from resttorrent.modules.torrent import get_session as get_info
    return get_info(session_id)
