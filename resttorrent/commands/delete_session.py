from resttorrent.decorators import command


@command('1', '/sessions/<session_id>', method='DELETE')
def delete_session(session_id):
    from resttorrent.modules.torrent import delete_session as delete
    delete(session_id)

    return {
    }
