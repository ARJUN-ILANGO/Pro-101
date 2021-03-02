import dropbox

class transfer:
    def __init__(self,dropbox_path,accessToken):
        self.dropbox_path = dropbox_path

    def uploadFiles(self,file_from,file_to):
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        
        with open(local_path,'rd')as f:
            dbx.file_upload(f, read(), dropbox_path, mode = WriteMode('overwrite'))
        
def main():
    accessToken = 'sl.Ar0sJPAijXojXS3GF2JyR3o8wFy55AUlmquF-hoZLthohnVclOLQ6abZbtEQJ4ABDZ75diR88mVGDwNZuRIwT26tOKxjr2g_iefatYFhqsNln05QR9XXsiCX8-9pR2yPVa_G5Nc'
    tranferData = transfer(accessToken)
    file_from = input('Enter The File Path To Trasfer : ')
    file_to = input('Enter The Full Path To Upload To DropBox ')
    tranferData.uploadFiles(file_from,file_to)
    print('File Has Been Moved')

main()