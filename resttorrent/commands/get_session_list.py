from resttorrent.decorators import command


@command('1', '/sessions')
def get_session_list():
    from resttorrent.modules.torrent import get_session_list as get_list

    return {
        'sessions': get_list()
    }
