import sqlite3
import os


USERNAME = 'SOBER'
lnk_path = 'D:\\Users\\SOBER\\Desktop\\便笺.lnk'


if __name__ == '__main__':
    db_path = 'C:\\Users\\' + USERNAME + '\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe' \
                                         '\\LocalState\\plum.sqlite'
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM Note")
    num = int(cursor.fetchall()[0][0])
    if num:
        os.system(lnk_path)