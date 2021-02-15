import dropbox
from dropbox.files import WriteMode
from Core.Dropbox.exceptions import DropboxUploadException


class Upload:
    def __init__(self, dbx: dropbox.Dropbox):
        self.dbx = dbx

    def upload(self, file, path, mode=WriteMode.overwrite):
        try:
            self.dbx.files_upload(file, path, mode=mode)
        except Exception as e:
            raise DropboxUploadException(f'Upload/overwrite failed: {e}')
