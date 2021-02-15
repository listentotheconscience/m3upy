import dropbox
import requests
from dropbox.exceptions import DropboxException
from requests.exceptions import HTTPError

from Core.Helpers import Logger


class GetFile:
    def __init__(self, filename, dbx: dropbox.Dropbox):
        self.filename = filename
        self.dbx = dbx

    @property
    def data(self) -> str:
        try:
            url = self.dbx.files_get_temporary_link(self.filename)
            url = url.link()
            r = requests.get(url)
            return r.text
        except (DropboxException, HTTPError) as e:
            Logger.error(f'{e}')
