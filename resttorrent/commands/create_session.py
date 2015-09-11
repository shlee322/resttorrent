from resttorrent.decorators import command


@command('1', '/sessions', method='POST')
def create_session(port_range='6881,6891', memory_only='1'):
    # ports (default: 6881,6891)
    port_range = port_range.split(',')
    port_range = [int(port) for port in port_range]

    # memory_only (default:1)
    memory_only = memory_only != '0'

    from resttorrent.modules.torrent import create_session, get_session

    session_id = create_session(
        port_range=port_range,
        memory_only=memory_only
    )

    return {
        'session': get_session(session_id)
    }
