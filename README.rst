RestTorrent
===========

  RestTorrent is BitTorrent Restful API and Socket.IO Server based Libtorrent.

License
-------
  RestTorrent is released under the MIT-license.


Requirements
------------
  - Install libtorrent

    * Ubuntu

      .. code-block::

         apt-get install python-libtorrent

    * ArchLinux

      .. code-block::

         yaourt -S python-libtorrent-rasterbar


    * Mac

      .. code-block::

         brew install libtorrent-rasterbar --with-python


  - Install Python Requirements

      .. code-block::

         pip install -r requirements.txt


Usage
-----

  - WSGI Application

    .. code-block::

       resttorrent.wsgi:application

  - Run Debug Mode

    .. code-block::

       python debug.py

  - HTTP Restful API

    .. code-block::

       POST /v1/sessions

    JSONP parameter name : callback
    
    CORS(Access-Control-Allow-Origin) Header : *

  - Socket.IO

    .. code-block:: javascript

       socket.emit('v1', { t_id:'1', command:'create_session', ports:[6881] });


API
---

  - **GET** /v1/sessions

    * Request

      +----------------+------------+-----------------------+
      | Name           | Require    | Description           |
      +================+============+=======================+
      | t_id           | socket.io  | Transaction ID        |
      |                | only       |                       |
      +----------------+------------+-----------------------+
      | command        | socket.io  | **get_session_list**  |
      |                | only       |                       |
      +----------------+------------+-----------------------+

    * Response

      .. code-block:: json

         {
           "status": "success",
           "sessions": [
             {
               "id": "2d4c54303130302d655f38397933685052467163",
               "port": 6881
             }
           ]
         }

  - **POST** /v1/sessions

    * Request

      +----------------+------------+-----------------------+
      | Name           | Require    | Description           |
      +================+============+=======================+
      | port_range     | option     | Listen Range          |
      |                |            | (default: 6881,6891)  |
      +----------------+------------+-----------------------+
      | memory_only    | option     | default:1             |
      +----------------+------------+-----------------------+
      | t_id           | socket.io  | Transaction ID        |
      |                | only       |                       |
      +----------------+------------+-----------------------+
      | command        | socket.io  | **create_session**    |
      |                | only       |                       |
      +----------------+------------+-----------------------+

    * Response

      .. code-block:: json

         {
           "status": "success",
           "session": {
             "id": "2d4c54303130302d655f38397933685052467163",
             "port": 6881
           }
         }

      .. code-block:: json

         {
           "status": "fail",
           "message": "bind failed address already in use"
         }

  - **GET** /v1/sessions/<session_id>

    * Response

      .. code-block:: json

         {
           "status": "success",
           "id": "2d4c54303130302d655f38397933685052467163",
           "port": 6881
         }

  - **DELETE** /v1/sessions/<session_id>

    * Response

      .. code-block:: json

         {
           "status": "success"
         }

  - **POST** /v1/sessions/<session_id>/torrents

    * Request

      +----------------+------------+-----------------------+
      | Name           | Require    | Description           |
      +================+============+=======================+
      | file           | select one | Torrent Metainfo File |
      +----------------+            +-----------------------+
      | magnet         |            | Torrent Magnet URL    |
      +----------------+            +-----------------------+
      | url            |            | download torrent url  |
      +----------------+------------+-----------------------+
      | save_path      | require    | Save Target Path      |
      +----------------+------------+-----------------------+
      | autostart      | option     | autostart (default:1) |
      +----------------+------------+-----------------------+
      | storage_mode   | option     | default: sparse       |
      +----------------+------------+-----------------------+
      | memory_only    | option     | default:session value |
      +----------------+------------+-----------------------+

    * Response

      .. code-block:: json

         {
             "status": "success",
             "info_hash": "6f8cd699135b491513e65d967a052a7087750d9c",
             "download_rate": 0,
             "num_peers": 0,
             "progress": 0,
             "state": "checking_resume_data",
             "upload_rate": 0
         }


  - **GET** /v1/sessions/<session_id>/torrents

    * Response

      .. code-block:: json

         {
             "status": "success",
             "torrents": [
                 {
                     "info_hash": "6f8cd699135b491513e65d967a052a7087750d9c",
                     "download_rate": 0,
                     "num_peers": 5,
                     "progress": 0.0037299999967217445,
                     "state": "downloading",
                     "upload_rate": 116
                 }
             ]
         }
