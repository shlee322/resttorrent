from resttorrent.decorators import command
from resttorrent.modules.torrent import get_session_raw, get_session, get_torrent_info
from resttorrent.exceptions import APIException


@command('1', '/sessions/<session_id>/torrents')
def get_torrent_list(session_id):

    if not get_session(session_id):
        raise APIException('session.notfound')

    session = get_session_raw(session_id)

    torrents = []
    for torrent in session.get_torrents():
        torrents.append(get_torrent_info(torrent))

    return {
        'torrents': torrents
    }
