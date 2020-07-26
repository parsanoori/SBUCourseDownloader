import os
import sys
import bs4
import _thread
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
from urllib3 import PoolManager
from pyunpack import Archive

className = 'Ahmad_Ali_DS'
html_part = """
            <ol><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_0 تاریخ برگزاری :  ( 1398/12/13 15:27:50) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/94/?1223864&amp;url=pwu2kokmer4h">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_1 تاریخ برگزاری :  ( 1398/12/20 15:22:36) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/94/?33110971&amp;url=pge6xv18dcpk">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_2 تاریخ برگزاری :  ( 1398/12/25 15:09:41) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/94/?109116615&amp;url=p83r4js48vwl">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_3 تاریخ برگزاری :  ( 1398/12/27 15:13:01) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/94/?110443696&amp;url=pf4knv1q4wua">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_4 تاریخ برگزاری :  ( 1399/01/17 15:28:59) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/94/?121277291&amp;url=p5ajkg4dybkt">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_5 تاریخ برگزاری :  ( 1399/01/19 15:15:35) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/94/?123386809&amp;url=p8x4mdfs3brr">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_0 تاریخ برگزاری :  ( 1399/01/24 15:16:22) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?375970&amp;url=p78gkma723xg">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_1 تاریخ برگزاری :  ( 1399/01/26 15:04:54) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?771884&amp;url=ptp6j6i5x2et">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_2 تاریخ برگزاری :  ( 1399/01/31 15:04:23) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?1402011&amp;url=p8cgh1uhxfkx">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_3 تاریخ برگزاری :  ( 1399/02/02 15:03:45) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?1785021&amp;url=pp8p36hxjamm">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_4 تاریخ برگزاری :  ( 1399/02/07 15:05:40) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?2247203&amp;url=piz78nbdmjsv">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_5 تاریخ برگزاری :  ( 1399/02/09 15:11:36) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?2678106&amp;url=p9kqacd4m4hc">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_6 تاریخ برگزاری :  ( 1399/02/14 14:58:11) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?3092106&amp;url=p2lgt7g8u0oy">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_7 تاریخ برگزاری :  ( 1399/02/16 14:52:58) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?3506735&amp;url=pmbpulawb9ew">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_8 تاریخ برگزاری :  ( 1399/02/21 15:02:46) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?3919636&amp;url=poyxzcp1xlnl">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_9 تاریخ برگزاری :  ( 1399/02/23 15:08:49) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?4314841&amp;url=p4bbedamoozi">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_10 تاریخ برگزاری :  ( 1399/02/28 15:07:24) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?4722871&amp;url=pdowwpb60heo">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_11 تاریخ برگزاری :  ( 1399/02/30 14:32:03) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?5098637&amp;url=psfbe390fs5w">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_12 تاریخ برگزاری :  ( 1399/03/11 15:13:52) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?6018726&amp;url=pmzxw94tdvak">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_13 تاریخ برگزاری :  ( 1399/03/13 15:25:41) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?6371783&amp;url=pj0kzoic66vw">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_14 تاریخ برگزاری :  ( 1399/03/18 14:48:45) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?6757351&amp;url=p2alw3bf9v0o">باز نمودن لینک 
            </a></li><li style="padding: 10px;">ساختمان داده ها - آبين احمدعلي - (4301010-01)_15 تاریخ برگزاری :  ( 1399/04/10 12:03:25) <a class="btn btn-info" style="width:10em;" target="_blank" href="http://194.225.24.83/records/95/?8661224&amp;url=prabamasstwp">باز نمودن لینک 
            </a></li></ol>
            """


def login(link, response):
    soup = BeautifulSoup(response, features="html.parser")
    goto = soup.find('input', {'type': 'hidden'}).get('value')
    parsed = urllib.parse.urlparse(link)
    path = parsed.path.split('/')
    path.pop()
    path.append('login.php')
    parsed = parsed._replace(path='/'.join(path))
    loginURL = urllib.parse.urlunparse(parsed)
    result = requests.post(loginURL, verify=False,
                           data={'goto': goto, 'username': '0440913942', 'password': '0440913942'})
    return result.text


def extract_mp4_rar_url(response):
    soup = BeautifulSoup(response, features="html.parser")
    for aTag in soup.findAll('a'):
        aTag: bs4.element.Tag
        stringToCheck = '  دانلود فایل آفلاین کلاس  (MP4) '
        if aTag.text == stringToCheck:
            print(aTag.get('href'))
            return aTag.get('href')


def download_file(url, filename, filesize, foldername):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        downloaded = 0
        with open(foldername + '/' + filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += 8192
                percent = downloaded * 100 / filesize
                downloadedInMB = (downloaded / 1024) / 1024
                strin_to_write_to_stdout = f'Downloaded {downloadedInMB:.2f}MBs ({percent:.1f}%)'
                sys.stdout.write("\r" + strin_to_write_to_stdout)
                sys.stdout.flush()
    print()
    return filename


def check_file_size(url) -> float:
    pool = PoolManager()
    response = pool.request("GET", url, preload_content=False)
    content_bytes = response.headers.get("Content-Length")
    return int(content_bytes)


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def unrar_and_delete_file(filename, foldername):
    temp_foler_name = f'{foldername}/{filename}_temp_foler'
    create_folder(temp_foler_name)
    Archive(foldername + '/' + filename + '.rar').extractall(temp_foler_name)
    for file in os.listdir(temp_foler_name):
        if file.endswith('.mp4'):
            os.rename(f'{temp_foler_name}/{file}', f'{foldername}/{filename}.mp4')
    if os.path.exists(foldername + '/' + filename + '.rar'):
        os.remove(foldername + '/' + filename + '.rar')
    if os.path.exists(temp_foler_name):
        os.rmdir(temp_foler_name)
    global current_folders_bytes_count
    current_folders_bytes_count += os.path.getsize(f'{foldername}/{filename}.mp4')


soup = BeautifulSoup(html_part, features="html.parser")

sessions_count = 1
maximum_number_of_each_part = 1.9 * 1024 * 1024 * 1024
current_folder_files_count = 0
current_folders_count = 1
current_folder_name = className + '_part_' + str(current_folders_count)
create_folder(current_folder_name)
current_folders_bytes_count = 0

for aTag in soup.findAll('a'):
    link = aTag.get('href')
    response: str = requests.get(link, verify=False).text
    mp4_rar_url: str
    if 'ورود' in response:
        mp4_rar_url = extract_mp4_rar_url(login(link, response))
    else:
        mp4_rar_url = extract_mp4_rar_url(response)
    if mp4_rar_url is not None:
        size = check_file_size(mp4_rar_url)
        print(current_folders_bytes_count / maximum_number_of_each_part)
        print(f'Downloading session {sessions_count}')
        if current_folders_bytes_count > maximum_number_of_each_part:
            current_folder_files_count = 0
            current_folders_count += 1
            current_folder_name = className + '_part_' + str(current_folders_count)
            create_folder(current_folder_name)
            current_folders_bytes_count = 0
        print(f"{(size / 1024) / 1024} MB")
        rar_file_name = f'{className} Session {sessions_count}.rar'
        download_file(mp4_rar_url, rar_file_name, size, current_folder_name)
        filename = rar_file_name.split('.')[0]
        _thread.start_new_thread(unrar_and_delete_file, (filename, current_folder_name))
        print('Unraring the file')
        current_folder_files_count += 1
    else:
        print(f'Jumped: {link}, Session: {sessions_count}', file=sys.stderr)
    sessions_count += 1
