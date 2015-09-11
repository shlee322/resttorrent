import binascii
import libtorrent
from resttorrent.exceptions import APIException

_sessions = {}


def create_session(port_range, memory_only):
    session = libtorrent.session()
    session.listen_on(*set(port_range))

    session_id = binascii.hexlify(session.id().to_bytes())

    _sessions[session_id] = session

    return session_id


def get_session_list():
    sessions = []
    for session_id in _sessions.keys():
        sessions.append(get_session(session_id))
    return sessions


def get_session(session_id):
    session = _sessions.get(session_id)
    if not session:
        return None

    return {
        'id': session_id,
        'port': session.listen_port()
    }


def delete_session(session_id):
    session = _sessions.get(session_id)
    if not session:
        raise APIException('')

    del session
    del _sessions[session_id]


def get_session_raw(session_id):
    session = _sessions.get(session_id)
    if not session:
        return None
    return session


def get_torrent_info(torrent):
    if not torrent:
        return None

    state = torrent.status()

    return {
        'info_hash': binascii.hexlify(torrent.info_hash().to_bytes()),
        'state': str(state.state),
        'progress': state.progress,
        'download_rate': state.download_rate,
        'upload_rate': state.upload_rate,
        'num_peers': state.num_peers
    }
