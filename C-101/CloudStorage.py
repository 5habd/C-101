import dropbox
class transferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadfiles(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        f = open (filefrom,"rb")
        dbx.files_upload(f.read(),fileto)
def main():
    access_token="sl.Aibo5HljdO-1l1P0xZTXk1BJMUZTzoVsglZxGQElHpe_roa4EJX8xVMvAVKAYrhN2e4yFrKJo43DIHpDkX9HFZWSKgZLXQVa0ZwENZXgrYMNunXbVKNDuNXLZNRVH98qZDJ-qGU"
    transferdata=transferData(access_token)
    filefrom = input("enter the file path to transfer: ")
    fileto = input("enter the file to upload into dropbox: ")
    transferdata.uploadfiles(filefrom,fileto)
    print("file has been moved")
main()    
