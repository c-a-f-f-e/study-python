# coding:utf-8
old = 18
print("年齢は" + str(old) + "です。")

if old < 20:
    print("20歳未満の方はご利用できません。")
    print("またのご利用をお待ちしております。")

print("ありがとうございました。")

old = 24
print("年齢は" + str(old) + "です。")

if old < 20:
    print("20歳未満の方はご利用できません。")
    print("またのご利用をお待ちしております。")

print("ありがとうございました。")





if old < 20:
    print("20歳未満の方はご利用できません。")
    print("またのご利用をお待ちしております。")
else:
    print("ご利用ありがとうございます。開始ボタンをクリックして下さい。")

print("\n")

if old < 20:
    print("20歳未満の方はご利用出来ません。")
    print("またのご利用をお待ちしています。")
else:
    print("ご利用ありがとうございます。開始ボタンをクリックして下さい。")




postcode = "125-0062"
print("郵便番号は " + postcode + "です。")

if postcode == "140-0015":
    adress = "東京都品川区大井"
elif postcode == "102-0072":
    adress = "東京都千代田区飯田橋"
elif postcode == "125-0062":
    adress = "東京都葛飾区青戸"
else:
    adress = "不明"

print("住所は" + adress + "です。")

print("\n")

postcode = "102-0072"
print("郵便番号は" + postcode + "です。")

if postcode == "140-0015":
    adress = "東京都品川区大井"
elif postcode == "102-0072":
    adress = "東京都千代田区飯田橋"
elif postcode == "102-0062":
    adress = "東京都葛飾区青戸"
else:
    adress = "不明"

print("住所は" + adress + "です。")