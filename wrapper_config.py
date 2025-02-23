#coding: utf-8

# proxy types: http|https|socks4|socks5


DEBUG = True # False - without logs
#DEBUG = False # False - without logs

URLS_FILE = '1.txt'
SQLi_SAVE_FILE = 'goodsqli.txt'
BRUTE_SAVE_FILE = 'goodbrute.txt'

LOG_FILE = 'wrapper_session.log'

# Режим дампов
DUMP = True
STRUCT = False
DUMP_ALL = False
Check_SQLi = False

# Кол-во строк для дампа
start = 1
stop = 100000000

# Поиск файла robots
Robots = False
ROBOTS_SAVE = 'goodrobots.txt'

# Проверка ссылок на популярные домен
Check_List = True

# Брут CMS - не используется
BRUTE_CMS = False
THREADS_BRUTE = 100
# Пробив эксплоитами
EXPLOITS_CMS = False

# Поиск админки и бэкапов
ADMIN_FIND = False
FILES_FIND = False
FILES_SAVE = 'filesave.txt'
FILES_PAGE = 'files.txt'

# Файлы для сохранения найденных страниц
ADMIN_PAGE = 'adminpage.txt'
ADMIN_SAVE = 'adminsave.txt'
PASSW_FILE = 'passw.txt'

# Папка для сохранения найденных админок
ADMIN_FOLDER = 'admdump'

# Взлом админки с помощью SQLi
ADMIN_HACK_SAVE = 'adminhacksave.txt'

# Колонки для дампов
COLUMN_DUMP = 'user,email,mail,account,login,pass,password,passwd,pwd,hash,salt,wachtwoord,senha,clave,motdepasse,phone,mobile,tel,cell,pw,country'

# Паук
SPIDER = True
SPIDER_LINKS = '10'

# Сохранение дампов
SQLMAP_DUMPS = 'dumps'
WRAPPER_TXT_DUMPS = 'txt_dumps'
DUMP_FORMAT='CSV'

# Время подключения и время ответа СУБД
time_sec = 30
TIMEOUT = 240 # sec

# Сохранять сайты с алексой выше
ALEXA_CHECK = False
ALEXA = 1000000

# Тамперы по умолчанию
TAMPER = 'space2comment,equaltolike,randomcase'

PROXY = False # False if work without it
DUMP_COLUMN_LIMIT = 20
PROXY_TYPE = 'socks5'
PROXY_URL = '' # first
PROXY_FILE = '' # second if not first
PROXY_USERNAME = ''
PROXY_PASSWORD = ''
URLS_LIMIT = 10000000
DUMP_FOLDER = 'dumps_folder'
DUMP_COLUMN_LIMIT = 20 # 91 - 100 ...
THREADS = 300

# Удаление пустых папок
DELETE=False

RISK = 3
LEVEL = 5
RETRIES = '5'
