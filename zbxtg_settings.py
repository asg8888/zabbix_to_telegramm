# -*- coding: utf-8 -*-

tg_key = "541387739:AAHZZfFDmt8MmOOdQYzqacNATO8u0LXjv4Y"  # telegram bot api key

zbx_tg_prefix = "zbxtg"  # variable for separating text from script info
zbx_tg_tmp_dir = "/home/zabbix1/" + zbx_tg_prefix  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = False

zbx_tg_update_messages = True
zbx_tg_matches = {
    "problem": "PROBLEM: ",
    "ok": "OK: "
}

zbx_server = "http://zabbix.krasmed.ru/zabbix/"  # zabbix server full url
zbx_api_user = "api"
zbx_api_pass = "api"
zbx_api_verify = False  # True - do not ignore self signed certificates, False - ignore

zbx_basic_auth = False
zbx_basic_auth_user = "zabbix"
zbx_basic_auth_pass = "zabbix"

proxy_to_zbx = None
proxy_to_tg = "socks5://tg-id308297004:TpXEueol@en.socksy.seriyps.ru:1080"

#proxy_to_zbx = "proxy.local:3128"
#proxy_to_tg = "proxy.local:3128"

google_maps_api_key = None  # get your key, see https://developers.google.com/maps/documentation/geocoding/intro

zbx_tg_daemon_enabled = True
zbx_tg_daemon_wl_ids = [145816059,202210293]
zbx_tg_daemon_wl_u = ["orangekrs","EvgeniyKRSK"]

zbx_db_host = "localhost"
zbx_db_database = "zabbix"
zbx_db_user = "zabbix"
zbx_db_password = "Vjquehe7"


emoji_map = {
    "OK": "✅",
    "PROBLEM": "❗",
    "info": "ℹ️",
    "WARNING": "⚠️",
    "DISASTER": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}
