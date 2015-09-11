RestTorrent
===========

RestTorrent is BitTorrent Restful API and Socket.IO Server based Libtorrent.

# License

RestTorrent is released under the MIT-license.


# Requirements

## Install libtorrent
### Ubuntu
  .. code-block::

     apt-get install python-libtorrent

### ArchLinux
  .. code-block::

     yaourt -S python-libtorrent-rasterbar


### Mac
  .. code-block::

     brew install libtorrent-rasterbar --with-python

## Install Python Requirements
  .. code-block::

     pip install -r requirements.txt


# Usage

## WSGI Application
  .. code-block::

     resttorrent.wsgi:application

## Run Debug Mode
  .. code-block::

     python debug.py

## HTTP Restful API
  .. code-block::
     POST /v1/sessions

## Socket.IO
  .. code-block:: javascript
     socket.emit('v1', { t_id:'1', command:'create_session', ports:[6881] });


# API

## **GET** /v1/sessions
### Request
+----------------+------------+-----------------------+
| Name           | Require    | Description           |
+================+============+=======================+
| t_id           | socket.io  | Transaction ID        |
|                | only       |                       |
+----------------+------------+-----------------------+
| command        | socket.io  | **get_session_list**  |
|                | only       |                       |
+----------------+------------+-----------------------+
### Response
  .. code-block:: json

     {
       "sessions": [
         {
           "id": "1",
           "ports": [6881, 6891]
         }
       ]
     }

## **POST** /v1/sessions
### Request
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

### Response
  .. code-block:: json

     {
       "status": "success",
       "session": {
        "id": "849c5f68b6ef41b8ab3e4218edaf5dae",
        "port": 6881
       }
     }

  .. code-block:: json

     {
       "status": "fail",
       "message": "bind failed address already in use"
     }

## **GET** /v1/sessions/<session_id>
### Response
  .. code-block:: json

     {
       "id": "849c5f68b6ef41b8ab3e4218edaf5dae",
       "port": 6881
     }

## **DELETE** /v1/sessions/<session_id>
### Response
  .. code-block:: json

     {
       "status": "success"
     }

## **POST** /v1/sessions/<session_id>/torrents
### Request
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

### Response
  .. code-block:: json

     {
       "status": "success"
     }


## **GET** /v1/sessions/<session_id>/torrents?fields=infohash
### Response
  .. code-block:: json

     {
       "torrents": [
         {
           "infohash": "",
         }
       ]
     }


## **GET** /v1/sessions/<session_id>/torrents/<infohash>



## **PUT** /v1/sessions/<session_id>/torrents/<infohash>
### Request
+----------------+------------+-----------------------+
| Name           | Require    | Description           |
+================+============+=======================+
| pause          | option     | 1: pause 0:resume     |
+----------------+------------+-----------------------+


## **GET** /v1/sessions/<session_id>/torrents/<infohash>/peers
