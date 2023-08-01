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
import re
import requests
import config

dbname = config.dbname

conn = sqlite3.connect(dbname)
c = conn.cursor()

print('どのバチャをたてる？')
contest_type = input()

if contest_type == 'abc': # configのabc設定から
    contest_sets = config.contest_sets_abc
elif contest_type == 'arc': # configのarc設定から
    contest_sets = config.contest_sets_arc
elif contest_type == 'agc': # configのagc設定から
    contest_sets = config.contest_sets_agc
else:
    print('打ち間違いだよ')
    exit(1)

# configに指定されてるname（ABCなにかDまで！の部分）
contest_names = [contest_set['name'] for contest_set in contest_sets]

# contestのセットが空か
if len(contest_names) == 0:
    print('contest_setsが空だな')
    exit(1)

# contest_setの最初を入れておく（選んだコンテストの昼が入る）
contest = contest_sets[0]

# 昼か夜かを選ばせる
if len(contest_names) > 1:
    print('バチャを作成したい時間帯を選んでね(おひる: 0, よる: 1)')
    for i, contest_name in enumerate(contest_names):
        print(f'{i}: {contest_name}')
    contest_index = int(input('番号を入力してね: '))
    while contest_index < 0 or contest_index >= len(contest_names):
        print('番号が不正だよ')
        contest_index = int(input('番号を入力してね: '))
    contest = contest_sets[contest_index]

# これなんだ？
c.execute('CREATE TABLE IF NOT EXISTS contest_info (name TEXT PRIMARY KEY, next_start_date DATE)')
c.execute('CREATE TABLE IF NOT EXISTS past_problems (contest_name TEXT, date DATE, problem_id TEXT)')

c.execute('SELECT * FROM contest_info WHERE name = ?', (contest['name'],))
contest_info = c.fetchone()
if contest_info is None:
    date = '2023-' + input('開催日を入力してね（MM-DD）: ')
    while re.match(r'\d{4}-\d{2}-\d{2}', date) is None:
        print('日付フォーマットが不正だよ')
        date = '2023-' + input('開催日を入力してね（MM-DD）: ')
    c.execute('INSERT INTO contest_info VALUES (?, date(?, \'+1 day\'))', (contest['name'], date))
else:
    date = contest_info[1]
    print('次回のコンテストは%sに設定されてるよ' % date)
    if input('変更する？（y/n）: ').lower() == 'y':
        date = '2023-' + input('開催日を入力してね（MM-DD）: ')
        while re.match(r'\d{4}-\d{2}-\d{2}', date) is None:
            print('日付フォーマットが不正だよ')
            date = '2023-' + input('開催日を入力してね（MM-DD）: ')
    c.execute('UPDATE contest_info SET next_start_date = date(?, \'+1 day\') WHERE name = ?', (date, contest['name']))

problem_infos = contest['problem_infos']
problem_json = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()

# 問題セットを絞り込んでいる？？
problems = []
for i, problem_info in enumerate(problem_infos):
    candidate_problem_ids = []
    difficulty_range = problem_info['difficulty_range']
    include_experimental = problem_info['include_experimental']
    for problem_id in problem_json:
        if not contest_type in problem_id:
            continue
        if not 'difficulty' in problem_json[problem_id]:
            continue
        difficulty = max(0, problem_json[problem_id]['difficulty'])
        if difficulty < difficulty_range[0] or difficulty > difficulty_range[1]:
            continue
        is_experimental = problem_json[problem_id]['is_experimental']
        if not include_experimental and is_experimental:
            continue
        c.execute('SELECT * FROM past_problems WHERE contest_name = ? AND date >= date(?, ?) AND problem_id = ?', (contest['name'], date, '-%d days' % problem_info['duplicate_remove_days'], problem_id))
        if c.fetchone() is not None:
            continue
        candidate_problem_ids.append(problem_id)
    if len(candidate_problem_ids) == 0:
        print('候補問題がないなあ')
        exit(1)
    
    
    # 問題の数などを設定
    if contest_type == 'abc': # 126〜300まで
        problem_id = f'abc{str(random.randint(126, 300))}_'
        problem_type = ['a', 'b', 'c', 'd']
    elif contest_type == 'arc': # 104〜158まで
        problem_id = f'arc{str(random.randint(104, 158))}_'
        problem_type = ['a', 'b', 'c']
    else:
        x = random.randint(10, 60) # 10〜60まで
        if x >= 48: # 048は欠番なので、それ以降は+1 つまり本当は61まで
            x += 1
        problem_id = f'agc0{str(x)}_' 
        problem_type = ['a', 'b']
    
    for d in problem_type:
        problems.append({
            'id': problem_id + d,
            'point': 1, # 配点
            'order': i # なんだこれは
        })

# 開始日時
start_dt = datetime.datetime.strptime(date + ' ' + contest['everyday_start_time'], '%Y-%m-%d %H:%M')

# tokenの設定
token = 'xxxxxxxxxxxxxxxx'

headers = {
    'Content-Type': 'application/json',
    'Cookie': 'token=' + token
}

# コンテスト生成
r = requests.post('https://kenkoooo.com/atcoder/internal-api/contest/create', headers=headers, json={
    'title': start_dt.strftime(contest['title']),
    'memo': contest['memo'],
    'start_epoch_second': int(start_dt.timestamp()),
    'duration_second': contest['duration_second'],
    'mode': None,
    'is_public': True,
    'penalty_second': contest['penalty_second'],
})
if r.status_code != 200:
    print('コンテストの作成に失敗した…')
    exit(1)
contest_id = r.json()['contest_id']
print('コンテストを作成したよ！: https://kenkoooo.com/atcoder/#/contest/show/' + contest_id)


# 通知ツート生成
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

if contest_index == 0:
    contest_time = 'おひる'
    text_name += 'day.txt'
else:
    contest_time = 'よる'
    text_name += 'night.txt'

# 日付と、曜日
day = start_dt.weekday()
day_of_week = {0: '(月)', 1: '(火)', 2: '(水)', 3: '(木)', 4: '(金)'}

# 一覧生成
f = open(text_name, 'a', encoding="utf-8")
f.write(str(start_dt)[8:10] + day_of_week[day] + '\n')
f.write('https://kenkoooo.com/atcoder/#/contest/show/' + contest_id + '\n\n')
f.close()


# 通知個別ツイート生成
f = open('tweet.txt', 'a', encoding="utf-8")
f.write(problem_id + '\n' + str(start_dt)[8:10] + day_of_week[day] + '\n')
f.write(f'{icon}今日の{contest_time}のぶん！' + '\n')
f.write('https://kenkoooo.com/atcoder/#/contest/show/' + contest_id + '\n\n')
f.close()

# ここでリクエストを飛ばしているの？154行めはなんだ？？
r = requests.post('https://kenkoooo.com/atcoder/internal-api/contest/item/update', headers=headers, json={
    'contest_id': contest_id,
    'problems': problems
})
if r.status_code != 200:
    print('コンテストの問題を設定できんかった')
    exit(1)
print('コンテストの問題を設定したよ')

for problem in problems:
    c.execute('INSERT INTO past_problems VALUES (?, ?, ?)', (contest['name'], date, problem['id']))

print('完了したよ！おつかれさま、いつもありがとう！')
conn.commit()
conn.close()