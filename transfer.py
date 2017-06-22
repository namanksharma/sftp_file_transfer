import paramiko

def transfer_files():
    ssh = None
    ftp = None
    try:
        host = "[Your_host_name]"
        port = "[Your_port_no]"
        username = "[Your_sftp_username]"
        password = "[Your_sftp_password]"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password, port=port)
        ftp = ssh.open_sftp()
        LocalPath = "[File_path_and_name_which_you_want_to_upload] # "/home/user/abc.extension"
        ServerPath = '[File_path_in_server/filename.extension]'    # "/home/Downloads/xyz.extension"
        ftp.put(LocalPath, ServerPath)
        ftp.close()
    except Exception, e:
        print e
    finally:
        if ftp is not None:
            ftp.close()
        if ssh is not None:
            ssh.close()
