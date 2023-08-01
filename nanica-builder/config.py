'''
name:コンテスト名
title:コンテスト名
memo:説明文
everyday_start_time:開始時間
duration_second:開催時間（何分間のバチャかということ）
penalty_second:ペナ
problem_infos:
 difficulty_range:diffの範囲
 include_experimental:？
 duplicate_remove_days:おそらく、今日以前この期間のものは省くという意味な気がする
'''


# データベースのファイル名
dbname = 'problems.sqlite3'

# コンテストセット一覧
# abc
contest_sets_abc = [
    {
        'name': '☀️🍰ABCなにか(Dまで)!',
        'title': '☀️🍰ABCなにか(Dまで)!',
        'memo': 'だれでも参加してください！早解き練習にどうぞ / A〜D問題を35分間走るバチャ / ABC126〜最新-10までのなにかがランダムで出現 / 通知bot https://twitter.com/abc_nanica',
        'everyday_start_time': '14:00',
        'duration_second': 2100,
        'penalty_second': 300,
        'problem_infos': [
            {
                'difficulty_range': (0, 1500),
                'include_experimental': True,
                'duplicate_remove_days': 60,
            }
        ]
    },
    {
        'name': '🌙🍰ABCなにか(Dまで)!',
        'title': '🌙🍰ABCなにか(Dまで)!',
        'memo': 'だれでも参加してください！早解き練習にどうぞ / A〜D問題を35分間走るバチャ / ABC126〜最新-10までのなにかがランダムで出現 / 通知bot https://twitter.com/abc_nanica',
        'everyday_start_time': '21:00',
        'duration_second': 2100,
        'penalty_second': 300,
        'problem_infos': [
            {
                'difficulty_range': (0, 1500),
                'include_experimental': True,
                'duplicate_remove_days': 60
            }
        ]
    }
]



#arc
contest_sets_arc = [
    {
        'name': '☀️🍘ARCなにか(Cまで)!',
        'title': '☀️🍘ARCなにか(Cまで)!',
        'memo': 'だれでも参加してください！早解き練習にどうぞ / A〜C問題を55分間走るバチャ / ARC104〜最新-2までのなにかがランダムで出現 / 通知bot https://twitter.com/abc_nanica',
        'everyday_start_time': '15:00',
        'duration_second': 3300,
        'penalty_second': 300,
        'problem_infos': [
            {
                'difficulty_range': (0, 4000),
                'include_experimental': True,
                'duplicate_remove_days': 60,
            }
        ]
    },
    {
        'name': '🌙🍘ARCなにか(Cまで)!',
        'title': '🌙🍘ARCなにか(Cまで)!',
        'memo': 'だれでも参加してください！早解き練習にどうぞ / A〜C問題を55分間走るバチャ / ARC104〜最新-2までのなにかがランダムで出現 / 通知bot https://twitter.com/abc_nanica',
        'everyday_start_time': '22:00',
        'duration_second': 3300,
        'penalty_second': 300,
        'problem_infos': [
            {
                'difficulty_range': (0, 4000),
                'include_experimental': True,
                'duplicate_remove_days': 60
            }
        ]
    }
]



#agc
contest_sets_agc = [
    {
        'name': '☀️🌶AGCなにか(Bまで)!',
        'title': '☀️🌶AGCなにか(Bまで)!',
        'memo': 'だれでも参加してください！早解き練習にどうぞ / A〜B問題を55分間走るバチャ / AGC001〜最新-2までのなにかがランダムで出現 / 通知bot https://twitter.com/abc_nanica',
        'everyday_start_time': '15:00',
        'duration_second': 3300,
        'penalty_second': 300,
        'problem_infos': [
            {
                'difficulty_range': (0, 10000),
                'include_experimental': True,
                'duplicate_remove_days': 60,
            }
        ]
    },
    {
        'name': '🌙🌶AGCなにか(Bまで)!',
        'title': '🌙🌶AGCなにか(Bまで)!',
        'memo': 'だれでも参加してください！早解き練習にどうぞ / A〜B問題を55分間走るバチャ / AGC001〜最新-2までのなにかがランダムで出現 / 通知bot https://twitter.com/abc_nanica',
        'everyday_start_time': '22:00',
        'duration_second': 3300,
        'penalty_second': 300,
        'problem_infos': [
            {
                'difficulty_range': (0, 10000),
                'include_experimental': True,
                'duplicate_remove_days': 60
            }
        ]
    }
]
