from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({"Vadhiraj_Activity": "text/csv"})
file1.SetContentFile("Vadhiraj_Activity")
file1.Upload()

file2 = drive.CreateFile({"Sarthak_Activity": "text/csv"})
file2.SetContentFile("Sarthak_Activity")
file2.Upload()

file3 = drive.CreateFile({"Mridul_Activity": "text/csv"})
file3.SetContentFile("Mridul_Activity.csv")
file3.Upload()

file4 = drive.CreateFile({"Soham_Activity": "text/csv"})
file4.SetContentFile("Soham_Activity.csv")
file4.Upload()

file5 = drive.CreateFile({"Attendance_Stats": "text/csv"})
file5.SetContentFile("Attendance_Stats.csv")
file5.Upload()
