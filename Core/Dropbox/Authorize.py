import dropbox
from Core.Dropbox.exceptions import DropboxAuthorizeException


class Authorize:
    def __init__(self, access_token: str):
        if access_token is None:
            raise DropboxAuthorizeException("access_token must exist")
        self.access_token = access_token

    def authorize(self) -> dropbox.Dropbox:
        dbx = dropbox.Dropbox(self.access_token)
        if dbx.users_get_current_account():
            return dbx
        raise DropboxAuthorizeException("Authorize Failed")