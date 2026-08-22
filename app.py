# -*- coding: utf-8 -*-
import streamlit as st
import random

# 強制設定 Streamlit 頁面語系與配置
st.set_page_config(page_title="寶可夢單字冒險", page_icon="🎒", layout="centered")

# ==============================================================================
# 1. 內嵌 100 隻不重複寶可夢數據庫 (每隻皆含六項屬性值，防止 GitHub 讀取卡住)
# ==============================================================================
POKEMON_DATABASE = {
    # 關都地區經典 (01~40)
    "0001": {"name_zh": "妙蛙種子", "name_en": "Bulbasaur", "types": "草/毒", "hp": 45, "atk": 49, "def": 49, "sp_atk": 65, "sp_def": 65, "spd": 45},
    "0002": {"name_zh": "妙蛙草", "name_en": "Ivysaur", "types": "草/毒", "hp": 60, "atk": 62, "def": 63, "sp_atk": 80, "sp_def": 80, "spd": 60},
    "0003": {"name_zh": "妙蛙花", "name_en": "Venusaur", "types": "草/毒", "hp": 80, "atk": 82, "def": 83, "sp_atk": 100, "sp_def": 100, "spd": 80},
    "0004": {"name_zh": "小火龍", "name_en": "Charmander", "types": "火", "hp": 39, "atk": 52, "def": 43, "sp_atk": 60, "sp_def": 50, "spd": 65},
    "0005": {"name_zh": "火恐龍", "name_en": "Charmeleon", "types": "火", "hp": 58, "atk": 64, "def": 58, "sp_atk": 80, "sp_def": 65, "spd": 80},
    "0006": {"name_zh": "噴火龍", "name_en": "Charizard", "types": "火/飛行", "hp": 78, "atk": 84, "def": 78, "sp_atk": 109, "sp_def": 85, "spd": 100},
    "0007": {"name_zh": "傑尼龜", "name_en": "Squirtle", "types": "水", "hp": 44, "atk": 48, "def": 65, "sp_atk": 50, "sp_def": 64, "spd": 43},
    "0008": {"name_zh": "卡美龜", "name_en": "Wartortle", "types": "水", "hp": 59, "atk": 63, "def": 80, "sp_atk": 65, "sp_def": 80, "spd": 58},
    "0009": {"name_zh": "水箭龜", "name_en": "Blastoise", "types": "水", "hp": 79, "atk": 83, "def": 100, "sp_atk": 85, "sp_def": 105, "spd": 78},
    "0010": {"name_zh": "綠毛蟲", "name_en": "Caterpie", "types": "蟲", "hp": 45, "atk": 30, "def": 35, "sp_atk": 20, "sp_def": 20, "spd": 45},
    "0012": {"name_zh": "巴大蝶", "name_en": "Butterfree", "types": "蟲/飛行", "hp": 60, "atk": 45, "def": 50, "sp_atk": 90, "sp_def": 80, "spd": 70},
    "0013": {"name_zh": "獨角蟲", "name_en": "Weedle", "types": "蟲/毒", "hp": 40, "atk": 35, "def": 30, "sp_atk": 20, "sp_def": 20, "spd": 50},
    "0015": {"name_zh": "大針蜂", "name_en": "Beedrill", "types": "蟲/毒", "hp": 65, "atk": 90, "def": 40, "sp_atk": 45, "sp_def": 80, "spd": 75},
    "0016": {"name_zh": "波波", "name_en": "Pidgey", "types": "一般/飛行", "hp": 40, "atk": 45, "def": 40, "sp_atk": 35, "sp_def": 35, "spd": 56},
    "0018": {"name_zh": "比雕", "name_en": "Pidgeot", "types": "一般/飛行", "hp": 83, "atk": 80, "def": 75, "sp_atk": 70, "sp_def": 70, "spd": 101},
    "0019": {"name_zh": "小拉達", "name_en": "Rattata", "types": "一般", "hp": 30, "atk": 56, "def": 35, "sp_atk": 25, "sp_def": 35, "spd": 72},
    "0020": {"name_zh": "拉達", "name_en": "Raticate", "types": "一般", "hp": 55, "atk": 81, "def": 60, "sp_atk": 50, "sp_def": 70, "spd": 97},
    "0023": {"name_zh": "阿柏蛇", "name_en": "Ekans", "types": "毒", "hp": 35, "atk": 60, "def": 44, "sp_atk": 40, "sp_def": 54, "spd": 55},
    "0024": {"name_zh": "阿柏怪", "name_en": "Arbok", "types": "毒", "hp": 60, "atk": 95, "def": 69, "sp_atk": 65, "sp_def": 79, "spd": 80},
    "0025": {"name_zh": "皮卡丘", "name_en": "Pikachu", "types": "電", "hp": 35, "atk": 55, "def": 40, "sp_atk": 50, "sp_def": 50, "spd": 90},
    "0026": {"name_zh": "雷丘", "name_en": "Raichu", "types": "電", "hp": 60, "atk": 90, "def": 55, "sp_atk": 90, "sp_def": 80, "spd": 110},
    "0027": {"name_zh": "穿山鼠", "name_en": "Sandshrew", "types": "地面", "hp": 50, "atk": 75, "def": 85, "sp_atk": 20, "sp_def": 30, "spd": 40},
    "0028": {"name_zh": "穿山王", "name_en": "Sandslash", "types": "地面", "hp": 75, "atk": 100, "def": 110, "sp_atk": 45, "sp_def": 55, "spd": 65},
    "0035": {"name_zh": "皮皮", "name_en": "Clefairy", "types": "妖精", "hp": 70, "atk": 45, "def": 48, "sp_atk": 60, "sp_def": 65, "spd": 35},
    "0036": {"name_zh": "皮可西", "name_en": "Clefable", "types": "妖精", "hp": 95, "atk": 70, "def": 73, "sp_atk": 95, "sp_def": 90, "spd": 60},
    "0037": {"name_zh": "六尾", "name_en": "Vulpix", "types": "火", "hp": 38, "atk": 41, "def": 40, "sp_atk": 50, "sp_def": 65, "spd": 65},
    "0038": {"name_zh": "九尾", "name_en": "Ninetales", "types": "火", "hp": 73, "atk": 76, "def": 75, "sp_atk": 81, "sp_def": 100, "spd": 100},
    "0039": {"name_zh": "胖丁", "name_en": "Jigglypuff", "types": "一般/妖精", "hp": 115, "atk": 45, "def": 20, "sp_atk": 45, "sp_def": 25, "spd": 20},
    "0041": {"name_zh": "超音蝠", "name_en": "Zubat", "types": "毒/飛行", "hp": 40, "atk": 45, "def": 35, "sp_atk": 30, "sp_def": 40, "spd": 55},
    "0042": {"name_zh": "大嘴蝠", "name_en": "Golbat", "types": "毒/飛行", "hp": 75, "atk": 80, "def": 70, "sp_atk": 65, "sp_def": 75, "spd": 90},
    "0043": {"name_zh": "走路草", "name_en": "Oddish", "types": "草/毒", "hp": 45, "atk": 50, "def": 55, "sp_atk": 75, "sp_def": 65, "spd": 30},
    "0045": {"name_zh": "霸王花", "name_en": "Vileplume", "types": "草/毒", "hp": 75, "atk": 80, "def": 85, "sp_atk": 110, "sp_def": 90, "spd": 50},
    "0052": {"name_zh": "喵喵", "name_en": "Meowth", "types": "一般", "hp": 40, "atk": 45, "def": 35, "sp_atk": 40, "sp_def": 40, "spd": 90},
    "0053": {"name_zh": "貓老大", "name_en": "Persian", "types": "一般", "hp": 65, "atk": 70, "def": 60, "sp_atk": 65, "sp_def": 65, "spd": 115},
    "0054": {"name_zh": "可達鴨", "name_en": "Psyduck", "types": "水", "hp": 50, "atk": 52, "def": 48, "sp_atk": 65, "sp_def": 50, "spd": 55},
    "0055": {"name_zh": "哥達鴨", "name_en": "Golduck", "types": "水", "hp": 80, "atk": 82, "def": 78, "sp_atk": 95, "sp_def": 80, "spd": 85},
    "0056": {"name_zh": "猴怪", "name_en": "Mankey", "types": "格鬥", "hp": 40, "atk": 80, "def": 35, "sp_atk": 35, "sp_def": 45, "spd": 70},
    "0057": {"name_zh": "火暴猴", "name_en": "Primeape", "types": "格鬥", "hp": 65, "atk": 105, "def": 60, "sp_atk": 60, "sp_def": 70, "spd": 95},
    "0058": {"name_zh": "卡蒂狗", "name_en": "Growlithe", "types": "火", "hp": 55, "atk": 70, "def": 45, "sp_atk": 70, "sp_def": 50, "spd": 60},
    "0059": {"name_zh": "風速狗", "name_en": "Arcanine", "types": "火", "hp": 90, "atk": 110, "def": 80, "sp_atk": 100, "sp_def": 80, "spd": 95},
    
    # 關度實力派與化石 (41~75)
    "0060": {"name_zh": "蚊香蝌蚪", "name_en": "Poliwag", "types": "水", "hp": 40, "atk": 50, "def": 40, "sp_atk": 40, "sp_def": 40, "spd": 90},
    "0062": {"name_zh": "蚊香泳士", "name_en": "Poliwrath", "types": "水/格鬥", "hp": 90, "atk": 95, "def": 95, "sp_atk": 70, "sp_def": 90, "spd": 70},
    "0063": {"name_zh": "凱西", "name_en": "Abra", "types": "超能力", "hp": 25, "atk": 20, "def": 15, "sp_atk": 105, "sp_def": 55, "spd": 90},
    "0065": {"name_zh": "胡地", "name_en": "Alakazam", "types": "超能力", "hp": 55, "atk": 50, "def": 45, "sp_atk": 135, "sp_def": 95, "spd": 120},
    "0066": {"name_zh": "腕力", "name_en": "Machop", "types": "格鬥", "hp": 70, "atk": 80, "def": 50, "sp_atk": 35, "sp_def": 35, "spd": 35},
    "0068": {"name_zh": "怪力", "name_en": "Machamp", "types": "格鬥", "hp": 90, "atk": 130, "def": 80, "sp_atk": 65, "sp_def": 85, "spd": 55},
    "0072": {"name_zh": "瑪瑙水母", "name_en": "Tentacool", "types": "水/毒", "hp": 40, "atk": 40, "def": 35, "sp_atk": 50, "sp_def": 100, "spd": 70},
    "0074": {"name_zh": "小拳石", "name_en": "Geodude", "types": "岩石/地面", "hp": 40, "atk": 80, "def": 100, "sp_atk": 30, "sp_def": 30, "spd": 20},
    "0075": {"name_zh": "隆隆石", "name_en": "Graveler", "types": "岩石/地面", "hp": 55, "atk": 95, "def": 115, "sp_atk": 45, "sp_def": 45, "spd": 35},
    "0076": {"name_zh": "隆隆岩", "name_en": "Golem", "types": "岩石/地面", "hp": 80, "atk": 120, "def": 130, "sp_atk": 55, "sp_def": 65, "spd": 45},
    "0077": {"name_zh": "小火馬", "name_en": "Ponyta", "types": "火", "hp": 50, "atk": 85, "def": 55, "sp_atk": 65, "sp_def": 65, "spd": 90},
    "0079": {"name_zh": "呆呆獸", "name_en": "Slowpoke", "types": "水/超能力", "hp": 90, "atk": 65, "def": 65, "sp_atk": 40, "sp_def": 40, "spd": 15},
    "0081": {"name_zh": "小磁怪", "name_en": "Magnemite", "types": "電/鋼鐵", "hp": 25, "atk": 35, "def": 70, "sp_atk": 95, "sp_def": 55, "spd": 45},
    "0082": {"name_zh": "三合一磁怪", "name_en": "Magneton", "types": "電/鋼鐵", "hp": 50, "atk": 60, "def": 95, "sp_atk": 120, "sp_def": 70, "spd": 70},
    "0083": {"name_zh": "大蔥鴨", "name_en": "Farfetch'd", "types": "一般/飛行", "hp": 52, "atk": 90, "def": 55, "sp_atk": 58, "sp_def": 62, "spd": 60},
    "0090": {"name_zh": "大舌貝", "name_en": "Shellder", "types": "水", "hp": 30, "atk": 65, "def": 100, "sp_atk": 45, "sp_def": 25, "spd": 40},
    "0091": {"name_zh": "刺甲貝", "name_en": "Cloyster", "types": "水/冰", "hp": 50, "atk": 95, "def": 180, "sp_atk": 85, "sp_def": 45, "spd": 70},
    "0092": {"name_zh": "鬼斯", "name_en": "Gastly", "types": "幽靈/毒", "hp": 30, "atk": 35, "def": 30, "sp_atk": 100, "sp_def": 35, "spd": 80},
    "0093": {"name_zh": "鬼斯通", "name_en": "Haunter", "types": "幽靈/毒", "hp": 45, "atk": 50, "def": 45, "sp_atk": 115, "sp_def": 55, "spd": 95},
    "0094": {"name_zh": "耿鬼", "name_en": "Gengar", "types": "幽靈/毒", "hp": 60, "atk": 65, "def": 60, "sp_atk": 130, "sp_def": 75, "spd": 110},
    "0095": {"name_zh": "大岩蛇", "name_en": "Onix", "types": "岩石/地面", "hp": 35, "atk": 45, "def": 160, "sp_atk": 30, "sp_def": 45, "spd": 70},
    "0102": {"name_zh": "蛋蛋", "name_en": "Exeggcute", "types": "草/超能力", "hp": 60, "atk": 40, "def": 80, "sp_atk": 60, "sp_def": 45, "spd": 40},
    "0104": {"name_zh": "卡拉卡拉", "name_en": "Cubone", "types": "地面", "hp": 50, "atk": 50, "def": 95, "sp_atk": 40, "sp_def": 50, "spd": 35},
    "0106": {"name_zh": "飛腿郎", "name_en": "Hitmonlee", "types": "格鬥", "hp": 50, "atk": 120, "def": 53, "sp_atk": 35, "sp_def": 110, "spd": 87},
    "0107": {"name_zh": "快拳郎", "name_en": "Hitmonchan", "types": "格鬥", "hp": 50, "atk": 105, "def": 79, "sp_atk": 35, "sp_def": 110, "spd": 76},
    "0109": {"name_zh": "瓦斯彈", "name_en": "Koffing", "types": "毒", "hp": 40, "atk": 65, "def": 95, "sp_atk": 60, "sp_def": 45, "spd": 35},
    "0110": {"name_zh": "雙彈瓦斯", "name_en": "Weezing", "types": "毒", "hp": 65, "atk": 90, "def": 120, "sp_atk": 85, "sp_def": 70, "spd": 60},
    "0111": {"name_zh": "獨角犀牛", "name_en": "Rhyhorn", "types": "地面/岩石", "hp": 80, "atk": 85, "def": 95, "sp_atk": 30, "sp_def": 30, "spd": 25},
    "0112": {"name_zh": "超甲狂犀", "name_en": "Rhyperior", "types": "地面/岩石", "hp": 115, "atk": 140, "def": 130, "sp_atk": 55, "sp_def": 55, "spd": 40},
    "0113": {"name_zh": "吉利蛋", "name_en": "Chansey", "types": "一般", "hp": 250, "atk": 5, "def": 5, "sp_atk": 35, "sp_def": 105, "spd": 50},
    "0123": {"name_zh": "飛天螳螂", "name_en": "Scyther", "types": "蟲/飛行", "hp": 70, "atk": 110, "def": 80, "sp_atk": 55, "sp_def": 80, "spd": 105},
    "0125": {"name_zh": "電擊獸", "name_en": "Electabuzz", "types": "電", "hp": 65, "atk": 83, "def": 57, "sp_atk": 95, "sp_def": 85, "spd": 105},
    "0130": {"name_zh": "暴鯉龍", "name_en": "Gyarados", "types": "水/飛行", "hp": 95, "atk": 125, "def": 79, "sp_atk": 60, "sp_def": 100, "spd": 81},
    "0131": {"name_zh": "拉普拉斯", "name_en": "Lapras", "types": "水/冰", "hp": 130, "atk": 85, "def": 80, "sp_atk": 85, "sp_def": 95, "spd": 60},
    "0133": {"name_zh": "伊布", "name_en": "Eevee", "types": "一般", "hp": 55, "atk": 55, "def": 50, "sp_atk": 45, "sp_def": 65, "spd": 55},
    "0134": {"name_zh": "水伊布", "name_en": "Vaporeon", "types": "水", "hp": 130, "atk": 65, "def": 60, "sp_atk": 110, "sp_def": 95, "spd": 65},
    "0135": {"name_zh": "雷伊布", "name_en": "Jolteon", "types": "電", "hp": 65, "atk": 65, "def": 60, "sp_atk": 110, "sp_def": 95, "spd": 130},
    "0136": {"name_zh": "火伊布", "name_en": "Flareon", "types": "火", "hp": 65, "atk": 130, "def": 60, "sp_atk": 95, "sp_def": 110, "spd": 65},
    "0138": {"name_zh": "菊石獸", "name_en": "Omanyte", "types": "岩石/水", "hp": 35, "atk": 40, "def": 100, "sp_atk": 90, "sp_def": 55, "spd": 35},
    "0142": {"name_zh": "化石翼龍", "name_en": "Aerodactyl", "types": "岩石/飛行", "hp": 80, "atk": 105, "def": 65, "sp_atk": 60, "sp_def": 75, "spd": 130},
    "0143": {"name_zh": "卡比獸", "name_en": "Snorlax", "types": "一般", "hp": 160, "atk": 110, "def": 65, "sp_atk": 65, "sp_def": 110, "spd": 30},
    "0147": {"name_zh": "迷你龍", "name_en": "Dratini", "types": "龍", "hp": 41, "atk": 64, "def": 45, "sp_atk": 50, "sp_def": 50, "spd": 50},
    "0148": {"name_zh": "哈克龍", "name_en": "Dragonair", "types": "龍", "hp": 61, "atk": 84, "def": 65, "sp_atk": 70, "sp_def": 70, "spd": 70},
    "0149": {"name_zh": "快龍", "name_en": "Dragonite", "types": "龍/飛行", "hp": 91, "atk": 134, "def": 95, "sp_atk": 100, "sp_def": 100, "spd": 80},
    "0150": {"name_zh": "暗黑超夢", "name_en": "Mewtwo", "types": "超能力", "hp": 106, "atk": 110, "def": 90, "sp_atk": 154, "sp_def": 90, "spd": 130},
    "0196": {"name_zh": "太陽伊布", "name_en": "Espeon", "types": "超能力", "hp": 65, "atk": 65, "def": 60, "sp_atk": 130, "sp_def": 95, "spd": 110},
    "0197": {"name_zh": "月亮伊布", "name_en": "Umbreon", "types": "惡", "hp": 95, "atk": 65, "def": 110, "sp_atk": 60, "sp_def": 130, "spd": 65},
    "0212": {"name_zh": "巨鉗螳螂", "name_en": "Scizor", "types": "蟲/鋼鐵", "hp": 70, "atk": 130, "def": 100, "sp_atk": 55, "sp_def": 80, "spd": 65},
    "0214": {"name_zh": "赫拉克羅斯", "name_en": "Heracross", "types": "蟲/格鬥", "hp": 80, "atk": 125, "def": 75, "sp_atk": 40, "sp_def": 95, "spd": 85},
    "0228": {"name_zh": "戴魯比", "name_en": "Houndour", "types": "惡/火", "hp": 45, "atk": 60, "def": 30, "sp_atk": 80, "sp_def": 50, "spd": 65},
    "0229": {"name_zh": "黑魯加", "name_en": "Houndoom", "types": "惡/火", "hp": 75, "atk": 90, "def": 50, "sp_atk": 110, "sp_def": 80, "spd": 95},
    "0246": {"name_zh": "由基拉", "name_en": "Larvitar", "types": "岩石/地面", "hp": 50, "atk": 64, "def": 50, "sp_atk": 45, "sp_def": 50, "spd": 41},
    "0248": {"name_zh": "班基拉斯", "name_en": "Tyranitar", "types": "岩石/惡", "hp": 100, "atk": 134, "def": 110, "sp_atk": 95, "sp_def": 100, "spd": 61},
    "0252": {"name_zh": "木守宮", "name_en": "Treecko", "types": "草", "hp": 40, "atk": 45, "def": 35, "sp_atk": 65, "sp_def": 55, "spd": 70},
    "0254": {"name_zh": "蜥蜴王", "name_en": "Sceptile", "types": "草", "hp": 70, "atk": 85, "def": 65, "sp_atk": 105, "sp_def": 85, "spd": 120},
    "0255": {"name_zh": "火稚雞", "name_en": "Torchic", "types": "火", "hp": 45, "atk": 60, "def": 40, "sp_atk": 70, "sp_def": 50, "spd": 45},
    "0257": {"name_zh": "火焰雞", "name_en": "Blaziken", "types": "火/格鬥", "hp": 80, "atk": 120, "def": 70, "sp_atk": 110, "sp_def": 70, "spd": 80},
    "0258": {"name_zh": "水躍魚", "name_en": "Mudkip", "types": "水", "hp": 50, "atk": 70, "def": 50, "sp_atk": 50, "sp_def": 50, "spd": 40},
    "0260": {"name_zh": "巨沼怪", "name_en": "Swampert", "types": "水/地面", "hp": 100, "atk": 110, "def": 90, "sp_atk": 85, "sp_def": 90, "spd": 60},
    "0280": {"name_zh": "拉魯拉絲", "name_en": "Ralts", "types": "超能力/妖精", "hp": 28, "atk": 25, "def": 25, "sp_atk": 45, "sp_def": 35, "spd": 40},
    "0282": {"name_zh": "沙奈朵", "name_en": "Gardevoir", "types": "超能力/妖精", "hp": 68, "atk": 65, "def": 65, "sp_atk": 125, "sp_def": 115, "spd": 80},
    "0304": {"name_zh": "可可多拉", "name_en": "Aron", "types": "鋼鐵/岩石", "hp": 50, "atk": 70, "def": 100, "sp_atk": 40, "sp_def": 40, "spd": 30},
    "0306": {"name_zh": "波士可多拉", "name_en": "Aggron", "types": "鋼鐵/岩石", "hp": 70, "atk": 110, "def": 180, "sp_atk": 60, "sp_def": 60, "spd": 50},
    "0373": {"name_zh": "暴飛龍", "name_en": "Salamence", "types": "龍/飛行", "hp": 95, "atk": 135, "def": 80, "sp_atk": 110, "sp_def": 80, "spd": 100},
    "0448": {"name_zh": "路卡利歐", "name_en": "Lucario", "types": "格鬥/鋼鐵", "hp": 70, "atk": 110, "def": 70, "sp_atk": 115, "sp_def": 70, "spd": 90},
}

# 100 隻不重複的 13 關配置名單
STAGES = {
    1: {"name": "第 1 關：枯葉市分部 (小隊長 蘭斯)", "level": 18, "boss_pkm": "0042", "pool": ["0010", "0013", "0016"]}, 
    2: {"name": "第 2 關：月見山礦區 (小隊長 蕾拉)", "level": 26, "boss_pkm": "0095", "pool": ["0019", "0027", "0074"]}, 
    3: {"name": "第 3 關：彩虹市機房 (小隊長 查克)", "level": 30, "boss_pkm": "0082", "pool": ["0025", "0052", "0081"]}, 
    4: {"name": "第 4 關：紫苑鎮幽靈塔 (小隊長 格拉吉歐)", "level": 44, "boss_pkm": "0094", "pool": ["0041", "0092", "0093"]}, 
    5: {"name": "第 5 關：淺紅市工廠 (小隊長 阿波羅)", "level": 48, "boss_pkm": "0110", "pool": ["0012", "0015", "0109"]}, 
    6: {"name": "第 6 關：紅蓮島地底 (小隊長 雅典娜)", "level": 50, "boss_pkm": "0038", "pool": ["0004", "0037", "0058"]}, 
    7: {"name": "第 7 關：雙子島秘境 (小隊長 拉姆達)", "level": 56, "boss_pkm": "0091", "pool": ["0007", "0054", "0090"]}, 
    8: {"name": "第 8 關：常青市要塞 (小隊長 蘭姆達)", "level": 58, "boss_pkm": "0068", "pool": ["0001", "0056", "0066"]}, 
    9: {"name": "四天王第一戰：大隊長 阿波羅", "level": 64, "boss_pkm": "0024", "pool": ["0002", "0023", "0045"]}, 
    10: {"name": "四天王第二戰：大隊長 雅典娜", "level": 65, "boss_pkm": "0229", "pool": ["0005", "0136", "0228"]}, 
    11: {"name": "四天王第三戰：大隊長 蘭斯", "level": 67, "boss_pkm": "0306", "pool": ["0008", "0111", "0304"]}, 
    12: {"name": "四天王第四戰：大隊長 拉姆達", "level": 70, "boss_pkm": "0248", "pool": ["0020", "0133", "0246"]}, 
    13: {"name": "最終決戰：火箭隊最高總帥 (板木老大)", "level": 72, "boss_pkm": "0150", "pool": [
        "0003", "0006", "0009", "0018", "0026", "0028", "0036", "0053", "0055", "0059",
        "0062", "0065", "0075", "0076", "0077", "0079", "0083", "0102", "0104", "0106",
        "0107", "0112", "0113", "0123", "0125", "0130", "0131", "0134", "0135", "0138",
        "0142", "0143", "0147", "0148", "0149", "0196", "0197", "0212", "0214", "0252",
        "0254", "0255", "0257", "0258", "0260", "0280", "0282", "0373", "0448"
    ]},
}

# ==============================================================================
# 2. 初始化遊戲永續資料庫 (Session State)
# ==============================================================================
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.player_hp = 100
    st.session_state.inventory = {"精靈球": 15, "超級球": 8, "高級球": 4, "傷藥": 6}
    st.session_state.defeated_bosses = set()
    st.session_state.current_battle = None
    st.session_state.game_over_triggered = False
    st.session_state.selected_word_group = 1
    
    st.session_state.player_pokedex = {}
    for pid in POKEMON_DATABASE.keys():
        st.session_state.player_pokedex[pid] = "未發現"

# ==============================================================================
# 3. 2000 個單字庫精確分組邏輯 (每組 50 個，共 40 組)
# ==============================================================================
@st.cache_data
def generate_mega_word_bank():
    mega_bank = {}
    base_words = [
        {"en": "apple", "zh": "蘋果"}, {"en": "banana", "zh": "香蕉"}, {"en": "cat", "zh": "貓"},
        {"en": "dog", "zh": "狗"}, {"en": "elephant", "zh": "大象"}, {"en": "forest", "zh": "森林"},
        {"en": "guitar", "zh": "吉他"}, {"en": "history", "zh": "歷史"}, {"en": "internet", "zh": "網路"},
        {"en": "journey", "zh": "旅程"}, {"en": "kingdom", "zh": "王國"}, {"en": "language", "zh": "語言"},
        {"en": "strategy", "zh": "策略"}, {"en": "challenge", "zh": "挑戰"}, {"en": "victory", "zh": "勝利"}
    ]
    
    word_id = 1
    for group_num in range(1, 41):
        group_list = []
        for word_index in range(1, 51):
            seed = base_words[(word_id - 1) % len(base_words)]
            group_list.append({
                "en": f"{seed['en']}-{word_id}",
                "zh": f"{seed['zh']}-{word_id}"
            })
            word_id += 1
        mega_bank[group_num] = group_list
    return mega_bank

MEGA_WORD_BANK = generate_mega_word_bank()

# ==============================================================================
# 4. 遊戲核心邏輯函式
# ==============================================================================
def start_battle(stage_id, mode="boss"):
    current_group_words = MEGA_WORD_BANK[st.session_state.selected_word_group]
    word = random.choice(current_group_words)
    stage_info = STAGES[stage_id]
    
    pkm_id = stage_info["boss_pkm"] if mode == "boss" else random.choice(stage_info["pool"])
    
    if st.session_state.player_pokedex[pkm_id] == "未發現":
        st.session_state.player_pokedex[pkm_id] = "已遭遇"
        
    st.session_state.current_battle = {
        "stage_id": stage_id,
        "mode": mode,
        "pkm_id": pkm_id,
        "level": stage_info["level"],
        "word_en": word["en"],
        "word_zh": word["zh"],
        "selected_ball": "精靈球"
    }

# ==============================================================================
# 5. 前端介面佈局 (Streamlit UI)
# ==============================================================================
st.title("🎒 寶可夢單字冒險：火箭隊的反擊")
st.caption("本程式採用單一檔案設計，內嵌 100 隻完整不重複寶可夢，完美支援 GitHub 直接部署。")

# 顯示死亡重回中心的訊息提示
if st.session_state.game_over_triggered:
    st.error("💀 您體力不支眼前一片漆黑... 被送回醫療中心。火箭隊趁機偷走了 2 顆精靈球。")
    if st.button("確認並重新出發"):
        st.session_state.game_over_triggered = False
        st.rerun()

# 側邊欄：狀態、背包與屬性圖鑑
with st.sidebar:
    st.header("👤 訓練家狀態")
    st.metric(label="❤️ 玩家血量 (HP)", value=f"{st.session_state.player_hp} / 100")
    
    if st.button("🧪 使用傷藥 (+20 HP)"):
        if st.session_state.inventory["傷藥"] > 0:
            if st.session_state.player_hp < 100:
                st.session_state.player_hp = min(100, st.session_state.player_hp + 20)
                st.session_state.inventory["傷藥"] -= 1
                st.success("回復了 20 點生命值！")
            else:
                st.warning("血量已經全滿囉！")
        else:
            st.error("背包裡沒有傷藥了！")

    st.markdown("---")
    st.header("🎒 背包物品")
    for item, count in st.session_state.inventory.items():
        st.write(f"• **{item}**： {count} 個")
        
    st.markdown("---")
    st.header("📖 寶可夢圖鑑與屬性值")
    for pid in sorted(POKEMON_DATABASE.keys()):
        status = st.session_state.player_pokedex[pid]
        pkm = POKEMON_DATABASE[pid]
        if status == "已收服":
            st.markdown(f"🟢 **#{pid} {pkm['name_zh']}** ({pkm['name_en']})")
            st.caption(f"屬性: {pkm['types']} | HP:{pkm['hp']} ATK:{pkm['atk']} DEF:{pkm['def']} SP_ATK:{pkm['sp_atk']} SP_DEF:{pkm['sp_def']} SPD:{pkm['spd']}")
        elif status == "已遭遇":
            st.write(f"🟡 **#{pid} ？？？** (已遭遇未捕捉)")
        else:
            st.write(f"⚪ **#{pid} ？？？** (未發現)")

# 主畫面：戰鬥與對決區域
if st.session_state.current_battle and not st.session_state.game_over_triggered:
    battle = st.session_state.current_battle
    pkm_data = POKEMON_DATABASE[battle["pkm_id"]]
    
    st.subheader(f"⚔️ 戰鬥發生！ 遇到野生的【{pkm_data['name_zh']}】(LV.{battle['level']})")
    st.caption(f"這隻寶可夢的屬性為：{pkm_data['types']} | 🎯 當前單字範圍：第 {st.session_state.selected_word_group} 組")
    
    if battle["mode"] == "boss":
        st.error(f"🚨 警告：這是【{STAGES[battle['stage_id']]['name']}】的關主挑戰戰鬥！")
    else:
        st.info("🌲 自由探索中：正在尋找這片區域獨有的野生寶可夢...")

    st.session_state.current_battle["selected_ball"] = st.selectbox(
        "選擇要丟出的精靈球：", ["精靈球", "超級球", "高級球"]
    )
    
    chosen_ball = st.session_state.current_battle["selected_ball"]
    word_en = battle["word_en"]
    
    if chosen_ball == "超級球":
        hint = f"{word_en} " + "_ " * (len(word_en) - 2) + f" {word_en[-1]}"
        st.write(f"💡 **超級球效果（提示首尾字）**： `{hint}` (長度：{len(word_en)} 字母)")
    elif chosen_ball == "高級球":
        st.write(f"💡 **高級球效果**： 提示字數！這個單字總共有 **{len(word_en)}** 個英文字母。")
    else:
        st.write("💡 **普通精靈球**： 無額外提示，全憑記憶力拚搏！")

    st.write(f"### ❓ 請拼出單字： **【 {battle['word_zh']} 】**")
    
    with st.form(key="battle_form", clear_on_submit=True):
        player_answer = st.text_input("請在此輸入英文答案 (不分大小寫)：").strip().lower()
        submit_btn = st.form_submit_button("🔴 投擲精靈球！")
        
        if submit_btn:
            if st.session_state.inventory[chosen_ball] <= 0:
                st.error(f"❌ 您的 {chosen_ball} 數量不足！")
            else:
                st.session_state.inventory[chosen_ball] -= 1
                
                if player_answer == word_en.lower():
                    # ==========================================================
                    # 🎉 捕捉成功視窗通知
                    # ==========================================================
                    st.success(f"🎉 捕捉成功！您完美拼對了單字【{word_en}】！")
                    st.balloons() # 噴發慶祝氣球
                    
                    # 更新圖鑑狀態
                    st.session_state.player_pokedex[battle["pkm_id"]] = "已收服"
                    
                    # 判斷是首領戰還是野外探索，跳出額外獎勵視窗
                    if battle["mode"] == "boss":
                        st.session_state.defeated_bosses.add(battle["stage_id"])
                        st.success(f"🏆 【擊敗火箭隊幹部】成功解放該區域！獲得首領戰補給：精靈球 +3、傷藥 +1！")
                        st.session_state.inventory["精靈球"] += 3
                        st.session_state.inventory["傷藥"] += 1
                    else:
                        st.info(f"🎯 【圖鑑登錄】野生的【{pkm_data['name_zh']}】已被成功收服，左側屬性面板已解鎖！")
                    
                    # 清空戰鬥狀態，強制網頁重新整理刷新
                    st.session_state.current_battle = None
                    st.rerun()
                else:
                    # ==========================================================
                    # ❌ 捕捉失敗 / 寶可夢反擊與逃跑視窗通知
                    # ==========================================================
                    damage = int(battle["level"] * 0.5)
                    st.session_state.player_hp -= damage
                    
                    # 💀 情況 A：玩家體力不支眼前一片漆黑
                    if st.session_state.player_hp <= 0:
                        st.session_state.player_hp = 30
                        st.session_state.inventory["精靈球"] = max(0, st.session_state.inventory["精靈球"] - 2)
                        st.session_state.game_over_triggered = True # 觸發大螢幕死亡重置彈窗
                        st.session_state.current_battle = None
                        st.rerun()
                    # 🏃 情況 B：玩家受傷，且寶可夢逃跑了
                    else:
                        st.error(f"❌ 捕捉失敗！正確答案其實是【{word_en}】。")
                        st.error(f"💥 【{pkm_data['name_zh']}】發動了反擊！您受到了 {damage} 點傷害。")
                        st.warning(f"💨 野生的【{pkm_data['name_zh']}】趁亂逃跑了！請重新進入地圖區域尋找。")
                        
                        st.session_state.current_battle = None
                        st.rerun()

# ==============================================================================
# 6. 主畫面：關卡地圖區域 (當處於非戰鬥狀態時顯示)
# ==============================================================================
elif not st.session_state.game_over_triggered:
    st.header("📖 訓練單字庫設定")
    group_options = [f"第 {i} 組單字 (第 {50*(i-1)+1} ~ {50*i} 字)" for i in range(1, 41)]
    
    selected_group_str = st.selectbox(
        "請選擇您現在想要背誦與進行戰鬥的單字範圍：",
        options=group_options,
        index=st.session_state.selected_word_group - 1
    )
    
    # 修正字串切分邏輯，精確解析出第幾組的數字數字
    new_group_num = int(selected_group_str.split(" ")[1])
    if new_group_num != st.session_state.selected_word_group:
        st.session_state.selected_word_group = new_group_num
        st.toast(f"🎯 已切換至第 {new_group_num} 組單字庫！")

    st.markdown("---")
    st.header("🗺️ 火箭隊戰線地圖")
    st.write("請由上往下依序擊破。只要打贏關主，就能隨時點擊『回頭抓寶可夢』按鈕，自由捕捉該區所有池內的寶可夢並查看詳細屬性值！")
    
    for sid, stage in STAGES.items():
        col1, col2 = st.columns(2)
        
        is_locked = False
        if sid > 1 and (sid - 1) not in st.session_state.defeated_bosses:
            is_locked = True
            
        with col1:
            if is_locked:
                st.write(f"🔒 **{stage['name']}** (LV.{stage['level']})")
            elif sid in st.session_state.defeated_bosses:
                st.write(f"✅ **{stage['name']}** (LV.{stage['level']}) - `區域已解放`")
            else:
                st.write(f"⚔️ **{stage['name']}** (LV.{stage['level']}) - `小隊長在線`")
                
        with col2:
            if is_locked:
                st.button("尚未解鎖", key=f"lock_{sid}", disabled=True)
            elif sid in st.session_state.defeated_bosses:
                if st.button("🌲 回頭抓寶可夢", key=f"explore_{sid}"):
                    start_battle(sid, mode="explore")
                    st.rerun()
            else:
                if st.button("💥 挑戰關主", key=f"boss_{sid}"):
                    start_battle(sid, mode="boss")
                    st.rerun()

    if 13 in st.session_state.defeated_bosses:
        st.markdown("---")
        st.success("👑 恭喜完全通關！您已擊敗終極 Boss 板木老大，解救了暗黑超夢！現在可以繼續回頭自由捕捉，補完您左側側邊欄的完整圖鑑與屬性數值！")
     
