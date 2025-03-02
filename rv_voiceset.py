import rv_voicevox

file_name="rv_voice_dic.txt"
voice_settings={}#ユーザーIDをキーに声を呼び出す

voice_dic={}

"""テキストファイルとして保存しておいたボイス設定を読み込む"""
#ここをenvに保存出来たらいいかも
def load_voice():
  with open(file_name,"r")as file:
    for line in file:
      words = line.strip().split()
      voice_settings[words[0]]=words[1]

"""指定したユーザーidのデータがディクショナリ内にあるか探索"""
def seach_id(usr_id):
  if usr_id in voice_settings:
    return True
  else:
    return False

"""声設定をディクショナリに保存し、テキストファイルに書き込む"""
def set_voice(usr_id,voice):
  global voice_settings
  voice_settings[usr_id]=voice
  if seach_id(usr_id):
    with open(file_name,"w",encoding="utf-8") as file:
      for key,value in voice_settings.items():
        file.write(f"{key} {value}\n")
  else:
    with open(file_name,"a",encoding="utf-8") as file:
        file.write(f"{usr_id} {voice}\n")

def mk_dic():#声を変更するコマンドの選択肢を与えるための関数
  data=rv_voicevox.all_voice()
  for name, feature, id in data:
    if len(voice_dic) >= 25:
      break
    if not(name in voice_dic) and (feature=="ノーマル"):
      if name!="剣崎雌雄" and name!="玄野武宏" and name!="麒ヶ島宗麟":
        voice_dic[name]=id
  return voice_dic