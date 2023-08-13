'''
name:コンテスト名
title:コンテスト名
memo:説明文
start_time:開始時間
duration_second:開催時間（何秒間のバチャかということ）
penalty_second:ペナ
problem_info:
 difficulty_range:diffの範囲
 include_experimental:？
 duplicate_remove_days:(指定した期間)過去に同じ問題が出ていたら除くという設定
'''
from datetime import time


DAYNIGHT_EMOJI = ["☀️", "🌙"]
CONTEST_EMOJI = {"b": "🍰", "r": "🍘", "g": "🌶"}
PROBLEM_MAX = {"b": "D", "r": "C", "g": "B"}
START_TIME = {"b": [time(hour=14), time(hour=21)], "r": [time(hour=15), time(hour=22)], "g": [time(hour=15), time(hour=22)]}
DURATION_SECOND = {"b": 2100, "r": 3300, "g": 3300}
START_NUM = {"b": "126", "r": "104", "g": "001"}
LATEST_NUM = {"b": "10", "r": "2", "g": "2"}
MAX_DIFFICULTY = {"b": 1500, "r": 4000, "g": 10000}

def get_contest_info(contest_type, day_or_night):
    # コンテスト情報を生成する
    name = f"{DAYNIGHT_EMOJI[day_or_night]}{CONTEST_EMOJI[contest_type]}A{contest_type.upper()}Cなにか({PROBLEM_MAX[contest_type]}まで)!"
    return {
        "name": name,
        "title": name,
        "memo": f"だれでも参加してください！早解き練習にどうぞ / A〜{PROBLEM_MAX[contest_type]}問題を{DURATION_SECOND[contest_type]//60}分間走るバチャ / A{contest_type.upper()}C{START_NUM[contest_type]}〜最新-{LATEST_NUM[contest_type]}までのなにかがランダムで出現 / 通知bot https://twitter.com/abc_nanica",
        'start_time': START_TIME[contest_type][day_or_night],
        "duration_second": DURATION_SECOND[contest_type],
        "penalty_second": 300,
        "problem_info": {
            "difficulty_range": (0, MAX_DIFFICULTY[contest_type]),
            "include_experimental": True,
            "duplicate_remove_days": 60
        }
    }
