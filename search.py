from data import BayStars, Dragons, Eagles, Hawks, Carp, Tigers, Marines, Buffaloes, Swallows, Giants, Lions, Fighters

# Set alias of each team's name
Buffaloes_name=["オリックス","おりっくす","バファローズ","ばふぁろーず","オリックスバファローズ","おりっくすばふぁろーず"]
Swallows_name=["ヤクルト","やくると","スワローズ","すわろーず","ヤクルトスワローズ","やくるとすわろーず","東京ヤクルトスワローズ","とうきょうやくるとすわろーず"]
Tigers_name=["阪神","はんしん","タイガース","たいがーす","阪神タイガース","はんしんたいがーす"]
Marines_name=["ロッテ","ろって","マリーンズ","まりーんず","千葉ロッテマリーンズ","ちばろってまりーんず"]
Giants_name=["巨人","きょじん","ジャイアンツ","じゃいあんつ","読売ジャイアンツ","よみうりじゃいあんつ"]
Eagles_name=["楽天","らくてん","イーグルス","いーぐるす","東北楽天ゴールデンイーグルス","とうほくらくてんごーるでんいーぐるす"]
Carp_name=["広島","ひろしま","カープ","かーぷ","広島カープ","ひろしまかーぷ","広島東洋カープ","ひろしまとうようかーぷ"]
Hawks_name=["ソフトバンク","そふとばんく","ホークス","ほーくす","福岡ソフトバンクホークス","ふくおかそふとばんくほーくす"]
Dragons_name=["中日","ちゅうにち","ドラゴンズ","どらごんず","中日ドラゴンズ","ちゅうにちどらごんず"]
Fighters_name=["日ハム","にちはむ","ファイターズ","ふぁいたーず","北海道日本ハムファイターズ","ほっかいどうにっぽんはむふぁいたーず"]
BayStars_name=["横浜","よこはま","バファローズ","べいすたーず","横浜DeNAベイスターズ","よこはまでぃーえぬえーべいすたーず"]
Lions_name=["西武","せいぶ","ライオンズ","らいおんず","埼玉西武ライオンズ","さいたませいぶらいおんず"]

# team data list
team_list={
    "BayStars":[BayStars.data,BayStars_name],
    "Dragons":[Dragons.data,Dragons_name],
    "Eagles":[Eagles.data,Eagles_name],
    "Hawks":[Hawks.data,Hawks_name],
    "Carp":[Carp.data,Carp_name],
    "Tigers":[Tigers.data,Tigers_name],
    "Marines":[Marines.data,Marines_name],
    "Buffaloes":[Buffaloes.data,Buffaloes_name],
    "Swallows":[Swallows.data,Swallows_name],
    "Giants":[Giants.data,Giants_name],
    "Lions":[Lions.data,Lions_name],
    "Fighters":[Fighters.data,Fighters_name]
}

# find and return team member
def team_member(team_name):
    team_member_list=team_name+"の応援歌登録済み選手一覧です。\n"
    for team_member in team_list[team_name][0].keys():
        team_member_list+="\n"+team_member
    return team_member_list

# find and return player's lylic
def search_player_to_lylic(player_name):
    lylic=""
    for team_name in team_list.keys():
        for player in team_list[team_name][0].keys():
            if player_name in player:
                if len(lylic)>0:
                    lylic+="\n\n\n"
                lylic+=team_name+":"+player+"\n"+team_list[team_name][0][player]
    if len(lylic)==0:
        lylic="選手が見つかりませんでした。\nチーム名を入れると、応援歌登録済み選手一覧を表示します。"
    return lylic