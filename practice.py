import json

path = "fangji.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)


def search_by_name(name,data):
    for item in data:
        if name == item["name"]:
            print(f"找到{name}")
            print(f"组成:{','.join(item["herbs"])}")
            print(f"功效：{item["effect"]}")
            print(f"主治：{item["indications"]}")
            found = True
            break
    else :
            print("没找到")
found = False


def search_by_herb(herb,data):
     for item in data:
          if herb in item["herbs"]:
               print(f"方剂:{item["name"]}")
               found = True
               
if not found:
            print("没找到")

while True:
      print("1:按方名搜")
      print("2:按药材搜")
      print("3:退出")
      choice = input("选啥？")
      if choice == "1":
            name = input("方名：")
            search_by_name(name,data)
      elif choice == "2":
            herb = input("药材：")
            search_by_herb(herb,data)
      elif choice == "3":
            break
      else:
            print("输错了，请重试！！！")

