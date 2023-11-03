'''
やりたいこと：

ABC
・どのばちゃを立てる？ -> abc
・def abc()を実行
・開始日は？ -> 08-07（次の週の月曜日を入れる。ここは頑張る）
・そこから5日分のひる・よるをfor文で回し、1つずつインターバル挟んでAPIを発信する

ARC / AGC
・どのばちゃを立てる？ -> argc
・def argc()を実行
・開始日は？ -> 08-07（次の週の月曜日を入れる。ここは頑張る）
・そこから5日分のひる・よるをfor文で回し、1つずつインターバル挟んでAPIを発信する
・weekdayが0(月), 2(水), 4(金)の場合はarcを、1(火), 3(木)の場合はagcをセット

って、これは一つにしても良いのですが…

'''


import datetime
import sqlite3
import random
import requests
import time
import config


day_of_week = {0: '(月)', 1: '(火)', 2: '(水)', 3: '(木)', 4: '(金)'}
# tokenの設定
token = 'xxxxxxxxxxxxxxxx'

headers = {
    'Content-Type': 'application/json',
    'Cookie': 'token=' + token
}


# データベースの準備
dbname = config.DB_NAME

conn = sqlite3.connect(dbname)
c = conn.cursor()

# 次の月曜を探す
monday = datetime.date.today() + datetime.timedelta(days=1)
while monday.weekday():
    monday += datetime.timedelta(days=1)

print(f'来週分({monday.month}月{monday.day}日～)のバチャをすべて自動でたてるよ')
print('休みにしたい曜日があったらその数字を空白区切りで入力してね(例 月曜と水曜を休みにしたいとき：`0 2`)')
yasumi = input()

kaisaibi = set(range(5))

for i in yasumi.split():
    if i.isdigit() and 0 <= int(i) <= 4:
        kaisaibi.discard(int(i))
    else:
        print('打ち間違いだよ。0～4の数字を空白区切りでで入力してね')
        exit(1)

if not kaisaibi:
    print("1日も開催しないみたいだよ")
    exit(1)

# データベースに今まで立てたなにかバチャの情報を記録できるようにする
c.execute('CREATE TABLE IF NOT EXISTS contest_info2 (date DATE, day_or_night INT, contest_type TEXT, contest_id INT)')

# PROBLEM_JSON = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()


# 一覧生成 (初期化)
for text_name in ("abc_day", "argc_day", "abc_night", "argc_night"):
    with open("tweet_list_"+text_name+".txt", 'w', encoding="utf-8") as f:
        pass

# 通知個別ツイート生成 (初期化)
with open('tweet.txt', 'w', encoding="utf-8") as f:
    pass


def create_virtual_contest(day: datetime.date, day_or_night: int, contest_type: str):
    # バチャコンを立てる
    print(f"{day.month}月{day.day}日{day_of_week[day.weekday()]}{'よ' if day_or_night else 'ひ'}る A{contest_type.upper()}Cなにか を立てるよ")
    contest_info = config.get_contest_info(contest_type, day_or_night)
    contest_type = f"a{contest_type}c"
    date = day.isoformat()  # YYYY-MM-DDの形式になる

    c.execute(
        "SELECT * FROM contest_info2 WHERE date=? AND day_or_night=? AND contest_type=?",
        (date, day_or_night, contest_type)
    )
    if c.fetchone():
        print("同じ日、同じ時間帯、同じ内容のコンテストがすでにあったよ")
        return

    # 問題を絞り込み、その中からそれぞれ選ぶ
    if contest_type == 'abc': # 126〜300まで
        contest_range = list(range(126, 301))
        problem_type = ['a', 'b', 'c', 'd']
    elif contest_type == 'arc': # 104〜158まで
        contest_range = list(range(104, 159))
        problem_type = ['a', 'b', 'c']
    else:
        contest_range = list(range(10, 48)) + list(range(49, 61)) 
        problem_type = ['a', 'b']

    contest_number = random.choice(contest_range)
    contest_range.remove(contest_number)
    while contest_range:
        # 過去60日間にバチャで出した番号かどうかを判定
        c.execute(
            'SELECT * FROM contest_info2 WHERE contest_type = ? AND date >= date(?, ?) AND contest_id = ?',
            (contest_type, date, '-%d days' % contest_info['problem_info']['duplicate_remove_days'], contest_number)
        )
        if not c.fetchone():
            # 出題なしならループ脱出
            break
        contest_number = random.choice(contest_range)
        contest_range.remove(contest_number)
    if not contest_range:
        print("過去%d日間の間に出せる範囲すべての問題を出し切ったよ" % contest_info['problem_info']['duplicate_remove_days'])
        exit(1)

    problems = []
    for d in problem_type:
        problems.append({
            'id': f"{contest_type}{contest_number}_{d}",
            'point': 1, # 配点
            'order': 0 # 問題の順番
        })

    # 開始日時
    start_dt = datetime.datetime.combine(day, contest_info["start_time"])

    # コンテスト生成
    r = requests.post('https://kenkoooo.com/atcoder/internal-api/contest/create', headers=headers, json={
        'title': contest_info['title'],
        'memo': contest_info['memo'],
        'start_epoch_second': int(start_dt.timestamp()),
        'duration_second': contest_info['duration_second'],
        'mode': None,
        'is_public': True,
        'penalty_second': contest_info['penalty_second'],
    })
    if r.status_code != 200:
        print('コンテストの作成に失敗した…')
        exit(1)
    contest_id = r.json()['contest_id']
    print('作成したよ！: https://kenkoooo.com/atcoder/#/contest/show/' + contest_id)


    # 通知ツイート生成
    # ABCひる / よる ・ ARGCひる / よる で、ファイルを分けている

    # アイコンと、生成先のテキストの名前
    icon = config.CONTEST_EMOJI[contest_type[1]]
    text_name = "tweet_list_a{}c_"

    if contest_type == 'abc':
        text_name = text_name.format("b")
    else:
        text_name = text_name.format("rg")

    if day_or_night == 0:
        contest_time = 'おひる'
        text_name += 'day.txt'
    else:
        contest_time = 'よる'
        text_name += 'night.txt'

    # 一覧生成
    with open(text_name, 'a', encoding="utf-8") as f:
        f.write(str(day)[8:10] + day_of_week[day.weekday()] + '\n')
        f.write('https://kenkoooo.com/atcoder/#/contest/show/' + contest_id + '\n\n')

    # 通知個別ツイート生成
    with open('tweet.txt', 'a', encoding="utf-8") as f:
        f.write(f"{contest_number}\n{str(day)[8:10]}{day_of_week[day.weekday()]}\n")
        f.write(f'{icon}今日の{contest_time}のぶん！' + '\n')
        f.write('https://kenkoooo.com/atcoder/#/contest/show/' + contest_id + '\n\n')

    # コンテストの問題情報をアップロード
    r = requests.post('https://kenkoooo.com/atcoder/internal-api/contest/item/update', headers=headers, json={
        'contest_id': contest_id,
        'problems': problems
    })
    if r.status_code != 200:
        print('コンテストの問題を設定できんかった')
        exit(1)
    print('コンテストの問題を設定したよ')

    # 今回の問題情報をデータベースに保存する
    c.execute(
        "INSERT INTO contest_info2 VALUES (?, ?, ?, ?)",
        (date, day_or_night, contest_type, contest_number)
    )
    conn.commit()


print(f"バチャコンを30秒ごとに1個立てるので、{len(kaisaibi)*2}分ほど待っててね")

for delta in sorted(list(kaisaibi)):
    day = monday + datetime.timedelta(days=delta)
    for day_or_night in range(2):  # 昼か夜
        for contest_type in ["b", "rg"]:  # コンテストの種類
            # arc/agcの場合は曜日から自動でrかgかを判定
            contest_type = contest_type[day.weekday() % len(contest_type)]
            create_virtual_contest(day, day_or_night, contest_type)
            time.sleep(30)


print('完了したよ！おつかれさま、いつもありがとう！')
conn.commit()
conn.close()
