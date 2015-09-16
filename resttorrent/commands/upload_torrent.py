import os
import libtorrent
from resttorrent.decorators import command
from resttorrent.modules.torrent import get_session_raw, get_session, get_torrent_info
from resttorrent.exceptions import APIException

ROOT_DIR = os.path.normpath(os.environ.get('RESTTORRENT_ROOT_DIR', '/') + '/')

@command('1', '/sessions/<session_id>/torrents', method='POST')
def upload_torrent(session_id, save_path,
                   file=None, magnet=None, url=None,
                   autostart='1', storage_mode='sparse', memory_only=None):

    if not get_session(session_id):
        raise APIException('session.notfound')

    if [file, magnet, url].count(None) != 2:
        raise APIException('upload.target.selectone')

    session = get_session_raw(session_id)

    if file:
        e = libtorrent.bdecode(file.read())
        info = libtorrent.torrent_info(e)
    elif magnet:
        info = libtorrent.torrent_info(magnet)
    else:
        raise APIException('upload.notsupported')

    save_path = os.path.normpath(os.path.join(ROOT_DIR, save_path))
    if not save_path.startswith(ROOT_DIR):
        raise APIException('access denied')

    params = {
        'save_path': save_path,
        'storage_mode': libtorrent.storage_mode_t.storage_mode_sparse,
        'ti': info
    }

    torrent_handle = session.add_torrent(params)
    return get_torrent_info(torrent_handle)
