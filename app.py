import streamlit as st
import random

# ==============================================================================
# 1. 內嵌完整寶可夢數據庫 (完全不依賴外部 JSON 檔案，防止 GitHub 讀取卡住)
# ==============================================================================
POKEMON_DATABASE = {
    "0001": {"name_zh": "妙蛙種子", "name_en": "Bulbasaur", "types": "草/毒", "hp": 45, "atk": 49, "def": 49, "sp_atk": 65, "sp_def": 65, "spd": 45},
    "0002": {"name_zh": "妙蛙草", "name_en": "Ivysaur", "types": "草/毒", "hp": 60, "atk": 62, "def": 63, "sp_atk": 80, "sp_def": 80, "spd": 60},
    "0003": {"name_zh": "妙蛙花", "name_en": "Venusaur", "types": "草/毒", "hp": 80, "atk": 82, "def": 83, "sp_atk": 100, "sp_def": 100, "spd": 80},
    "0004": {"name_zh": "小火龍", "name_en": "Charmander", "types": "火", "hp": 39, "atk": 52, "def": 43, "sp_atk": 60, "sp_def": 50, "spd": 65},
    "0005": {"name_zh": "火恐龍", "name_en": "Charmeleon", "types": "火", "hp": 58, "atk": 64, "def": 58, "sp_atk": 80, "sp_def": 65, "spd": 80},
    "0006": {"name_zh": "噴火龍", "name_en": "Charizard", "types": "火/飛行", "hp": 78, "atk": 84, "def": 78, "sp_atk": 109, "sp_def": 85, "spd": 100},
    "0007": {"name_zh": "傑尼龜", "name_en": "Squirtle", "types": "水", "hp": 44, "atk": 48, "def": 65, "sp_atk": 50, "sp_def": 64, "spd": 43},
    "0008": {"name_zh": "卡美龜", "name_en": "Wartortle", "types": "水", "hp": 59, "atk": 63, "def": 80, "sp_atk": 65, "sp_def": 80, "spd": 58},
    "0009": {"name_zh": "水箭龜", "name_en": "Blastoise", "types": "水", "hp": 79, "atk": 83, "def": 100, "sp_atk": 85, "sp_def": 105, "spd": 78},
    "0025": {"name_zh": "皮卡丘", "name_en": "Pikachu", "types": "電", "hp": 35, "atk": 55, "def": 40, "sp_atk": 50, "sp_def": 50, "spd": 90},
    "0026": {"name_zh": "雷丘", "name_en": "Raichu", "types": "電", "hp": 60, "atk": 90, "def": 55, "sp_atk": 90, "sp_def": 80, "spd": 110},
    "0094": {"name_zh": "耿鬼", "name_en": "Gengar", "types": "幽靈/毒", "hp": 60, "atk": 65, "def": 60, "sp_atk": 130, "sp_def": 75, "spd": 110},
    "0112": {"name_zh": "超甲狂犀", "name_en": "Rhyperior", "types": "地面/岩石", "hp": 115, "atk": 140, "def": 130, "sp_atk": 55, "sp_def": 55, "spd": 40},
    "0143": {"name_zh": "卡比獸", "name_en": "Snorlax", "types": "一般", "hp": 160, "atk": 110, "def": 65, "sp_atk": 65, "sp_def": 110, "spd": 30},
    "0149": {"name_zh": "快龍", "name_en": "Dragonite", "types": "龍/飛行", "hp": 91, "atk": 134, "def": 95, "sp_atk": 100, "sp_def": 100, "spd": 80},
    "0150": {"name_zh": "暗黑超夢", "name_en": "Mewtwo", "types": "超能力", "hp": 106, "atk": 110, "def": 90, "sp_atk": 154, "sp_def": 90, "spd": 130},
}

# 關卡設定
STAGES = {
    1: {"name": "第 1 關：枯葉市分部 (小隊長 蘭斯)", "level": 18, "boss_pkm": "0001", "pool": ["0001", "0004", "0007"]},
    2: {"name": "第 2 關：月見山礦區 (小隊長 蕾拉)", "level": 26, "boss_pkm": "0004", "pool": ["0002", "0004", "0025"]},
    3: {"name": "第 3 關：彩虹市機房 (小隊長 查克)", "level": 30, "boss_pkm": "0007", "pool": ["0005", "0007", "0008"]},
    4: {"name": "第 4 關：紫苑鎮幽靈塔 (小隊長 格拉吉歐)", "level": 44, "boss_pkm": "0025", "pool": ["0025", "0094", "0001"]},
    5: {"name": "第 5 關：淺紅市工廠 (小隊長 阿波羅)", "level": 48, "boss_pkm": "0002", "pool": ["0002", "0005", "0008"]},
    6: {"name": "第 6 關：紅蓮島地底 (小隊長 雅典娜)", "level": 50, "boss_pkm": "0005", "pool": ["0003", "0005", "0006"]},
    7: {"name": "第 7 關：雙子島秘境 (小隊長 拉姆達)", "level": 56, "boss_pkm": "0008", "pool": ["0006", "0008", "0009"]},
    8: {"name": "第 8 關：常青市要塞 (小隊長 蘭姆達)", "level": 58, "boss_pkm": "0026", "pool": ["0026", "0094", "0143"]},
    9: {"name": "四天王第一戰：大隊長 阿波羅", "level": 64, "boss_pkm": "0003", "pool": ["0003", "0006", "0009"]},
    10: {"name": "四天王第二戰：大隊長 雅典娜", "level": 65, "boss_pkm": "0006", "pool": ["0006", "0094", "0143"]},
    11: {"name": "四天王第三戰：大隊長 蘭斯", "level": 67, "boss_pkm": "0009", "pool": ["0009", "0112", "0149"]},
    12: {"name": "四天王第四戰：大隊長 拉姆達", "level": 70, "boss_pkm": "0143", "pool": ["0143", "0112", "0149"]},
    13: {"name": "最終決戰：火箭隊最高總帥 (板木老大)", "level": 72, "boss_pkm": "0150", "pool": ["0150"]},
}

# 單字庫
WORD_BANK = [
    {"en": "apple", "zh": "蘋果"}, {"en": "banana", "zh": "香蕉"}, {"en": "cat", "zh": "貓"},
    {"en": "dog", "zh": "狗"}, {"en": "elephant", "zh": "大象"}, {"en": "forest", "zh": "森林"},
    {"en": "guitar", "zh": "吉他"}, {"en": "history", "zh": "歷史"}, {"en": "internet", "zh": "網路"},
    {"en": "journey", "zh": "旅程"}, {"en": "kingdom", "zh": "王國"}, {"en": "language", "zh": "語言"},
    {"en": "strategy", "zh": "策略"}, {"en": "challenge", "zh": "挑戰"}, {"en": "victory", "zh": "勝利"}
]

# ==============================================================================
# 2. 初始化遊戲永續資料庫 (Session State)
# ==============================================================================
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.player_hp = 100
    st.session_state.inventory = {"精靈球": 10, "超級球": 5, "高級球": 2, "傷藥": 5}
    st.session_state.defeated_bosses = set()
    st.session_state.current_battle = None
    st.session_state.game_over_triggered = False  # 新增：控制死亡通知的狀態
    
    # 動態建立玩家個人的圖鑑狀態紀錄
    st.session_state.player_pokedex = {}
    for pid in POKEMON_DATABASE.keys():
        st.session_state.player_pokedex[pid] = "未發現"

# ==============================================================================
# 3. 遊戲核心邏輯函式
# ==============================================================================
def start_battle(stage_id, mode="boss"):
    word = random.choice(WORD_BANK)
    stage_info = STAGES[stage_id]
    
    # 決定寶可夢編號 (關主戰固定王牌，自由探索從該關卡池隨機抽)
    pkm_id = stage_info["boss_pkm"] if mode == "boss" else random.choice(stage_info["pool"])
    
    # 更新圖鑑狀態為「已遭遇」
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
# 4. 前端介面佈局 (Streamlit UI)
# ==============================================================================
st.title("🎒 寶可夢單字冒險：火箭隊的反擊")
st.caption("本程式採用單一檔案設計，內嵌所有數據庫，完美支援 GitHub 零設定直接部署。")

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
    for pid, status in st.session_state.player_pokedex.items():
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
    st.caption(f"這隻寶可夢的屬性為：{pkm_data['types']}")
    
    if battle["mode"] == "boss":
        st.error(f"🚨 警告：這是【{STAGES[battle['stage_id']]['name']}】的關主挑戰戰鬥！")

    # 精靈球與提示功能
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
        submit_btn = st.form_submit_button("🔴 投擲精靈球！") # ✅ 正確的語法（拿掉 with）

        
        if submit_btn:
            if st.session_state.inventory[chosen_ball] <= 0:
                st.error(f"❌ 您的 {chosen_ball} 數量不足！")
            else:
                st.session_state.inventory[chosen_ball] -= 1
                
                if player_answer == word_en.lower():
                    st.success(f"🎉 答對了！順利捕捉到【{pkm_data['name_zh']}】! ")
                    st.balloons()
                    st.session_state.player_pokedex[battle["pkm_id"]] = "已收服"
                    
                    if battle["mode"] == "boss":
                        st.session_state.defeated_bosses.add(battle["stage_id"])
                        st.success("🏆 成功擊敗關主！該區域自由探索功能已解除鎖定！")
                        st.session_state.inventory["精靈球"] += 3
                        st.session_state.inventory["傷藥"] += 1
                    
                    st.session_state.current_battle = None
                    st.rerun()
                else:
                    # 💡 答錯單字扣血機制
                    damage = int(battle["level"] * 0.5)
                    st.session_state.player_hp -= damage
                    
                    # 💀 血量歸零：玩家體力不支眼前一片漆黑觸發點
                    if st.session_state.player_hp <= 0:
                        st.session_state.player_hp = 30
                        st.session_state.inventory["精靈球"] = max(0, st.session_state.inventory["精靈球"] - 2)
                        st.session_state.game_over_triggered = True  # 觸發大螢幕死亡彈窗
                        st.session_state.current_battle = None
                        st.rerun()
                    else:
                        st.error(f"❌ 答錯了！正確答案是 **{word_en}**。遭受反擊，扣除生命值 {damage} 點！")
                        st.session_state.current_battle = None
                        st.rerun()

# ==============================================================================
# 5. 主畫面：關卡地圖選單區域 (當沒有處於戰鬥與死亡狀態時顯示)
# ==============================================================================
elif not st.session_state.game_over_triggered:
    st.header("🗺️ 火箭隊戰線地圖")
    st.write("請由上往下依序擊破。只要打贏關主，就能隨時點擊『回頭抓寶可夢』按鈕，自由捕捉該區所有池內的寶可夢並查看詳細屬性值！")
    
    for sid, stage in STAGES.items():
        col1, col2 = st.columns(2)  # ✅ 修改後的程式碼（明確指定分成 2 欄）


        # 檢查前置關卡是否已解鎖
        is_locked = False
        if sid > 1 and (sid - 1) not in st.session_state.defeated_bosses:
            is_locked = True
            
        with col1:
            if is_locked:
                st.write(f"🔒 **{stage['name']}** (LV.{stage['level']})")
            elif sid in st.session_state.defeated_bosses:
                st.write(f"✅ **{stage['name']}** (LV.{stage['level']}) - `區域已解放`")
            else:
                st.write(f"⚔️ **{stage['name']}** (LV.{stage['level']}) - `首領在線`")
                
        with col2:
            if is_locked:
                st.button("尚未解鎖", key=f"lock_{sid}", disabled=True)
            elif sid in st.session_state.defeated_bosses:
                # 已通關關卡：開啟回溯自由捕捉功能
                if st.button("🌲 回頭抓寶可夢", key=f"explore_{sid}"):
                    start_battle(sid, mode="explore")
                    st.rerun()
            else:
                # 尚未通關關卡：挑戰當前關主
                if st.button("💥 挑戰關主", key=f"boss_{sid}"):
                    start_battle(sid, mode="boss")
                    st.rerun()

    # 👑 最終完全通關大彩蛋
    if 13 in st.session_state.defeated_bosses:
        st.markdown("---")
        st.success("👑 恭喜完全通關！您已擊敗終極 Boss 板木老大，解救了暗黑超夢！現在可以繼續回頭自由捕捉，補完您左側側邊欄的完整圖鑑與屬性數值！")
