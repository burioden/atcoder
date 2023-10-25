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
c.execute('CREATE TABLE IF NOT EXISTS contest_info (name TEXT PRIMARY KEY, next_start_date DATE)')
c.execute('CREATE TABLE IF NOT EXISTS past_problems (contest_name TEXT, date DATE, problem_id TEXT)')

problem_json = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()


# 一覧生成
for text_name in ("abc_day", "argc_day", "abc_night", "argc_night"):
    with open("tweet_list_"+text_name+".txt", 'w', encoding="utf-8") as f:
        pass

# 通知個別ツイート生成
with open('tweet.txt', 'w', encoding="utf-8") as f:
    pass


def create_virtual_contest(day: datetime.date, day_or_night: int, contest_type: str):
    # バチャコンを立てる
    print(f"{day.month}月{day.day}日{day_of_week[day.weekday()]}{'よ' if day_or_night else 'ひ'}る A{contest_type.upper()}Cなにか を立てるよ")
    contest_info = config.get_contest_info(contest_type, day_or_night)
    problem_info = contest_info['problem_info']
    contest_type = f"a{contest_type}c"
    date = day.isoformat()  # YYYY-MM-DDの形式になる

    c.execute("SELECT name FROM contest_info WHERE name=?", (f"{contest_type}_{day_or_night}_{date}",))
    if c.fetchone():
        print("同じ日、同じ時間帯、同じ内容のコンテストがすでにあったよ")
        return

    # 問題を絞り込み、その中からそれぞれ選ぶ
    if contest_type == 'abc': # 126〜300まで
        contest_range = set(range(126, 301))
        problem_type = ['a', 'b', 'c', 'd']
    elif contest_type == 'arc': # 104〜158まで
        contest_range = set(range(104, 159))
        problem_type = ['a', 'b', 'c']
    else:
        contest_range = set(range(10, 48)) | set(range(49, 61)) 
        problem_type = ['a', 'b']

    problems = []
    candidate_problem_ids = {n: [] for n in problem_type}
    difficulty_range = problem_info['difficulty_range']
    include_experimental = problem_info['include_experimental']
    for problem_id in problem_json.keys():
        if not contest_type in problem_id:
            continue
        if not 'difficulty' in problem_json[problem_id]:
            continue
        if int(problem_id[3:].split("_")[0]) not in contest_range:
            continue
        if problem_id.split("_")[1] not in problem_type:
            continue
        difficulty = max(0, problem_json[problem_id]['difficulty'])
        if difficulty < difficulty_range[0] or difficulty > difficulty_range[1]:
            # 問題が難しすぎる/易しすぎる
            continue
        is_experimental = problem_json[problem_id]['is_experimental']
        if not include_experimental and is_experimental:
            continue
        c.execute(
            'SELECT * FROM past_problems WHERE contest_name = ? AND date >= date(?, ?) AND problem_id = ?',
            (contest_info['name'], date, '-%d days' % problem_info['duplicate_remove_days'], problem_id)
        )
        if c.fetchone():
            # 過去60日以内にバチャに出した問題は出さない
            continue
        candidate_problem_ids[problem_id.split("_")[1]].append(problem_id)

    for d in problem_type:
        if len(candidate_problem_ids[d]) == 0:
            print(f'{d}の候補問題がないなあ')
            exit(1)
        problems.append({
            'id': random.choice(candidate_problem_ids[d]),
            'point': 1, # 配点
            'order': 0 # なんだこれは
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
    icon = ""
    text_name = ""

    if contest_type == 'abc':
        icon = '🍰'
        text_name = 'tweet_list_abc_'
    elif contest_type == 'arc':
        icon = '🍘'
        text_name = 'tweet_list_argc_'
    elif contest_type == 'agc':
        icon = '🌶'
        text_name = 'tweet_list_argc_'

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
        f.write(str(day)[8:10] + day_of_week[day.weekday()] + '\n')
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

    for problem in problems:
        c.execute('INSERT INTO past_problems VALUES (?, ?, ?)', (contest_info['name'], date, problem['id']))
    c.execute("INSERT INTO contest_info VALUES (?, ?)", (f"{contest_type}_{day_or_night}_{date}", date))


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
