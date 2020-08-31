#coding=utf-8

print("test")

#3-2
#出力
print(1+2)
print(3+4)
print(4+5)

#3-4
#文字列の出力
print("abe")
#バックスラッシュの出力時のバグの解決
print("\\10,000")
#raw String バグのもう１つの解決方法
print(r"\10,000")

#3-5
#文字列の連結
print("abc"+"cde")
print("abc"+"cde"+"def"+"hig")
#繰り返し
print("abc"*3)
#文字列と数列の連結
print("abc"+123)
#(↑解決策として)数値の文字列への変換
print("abc"+"123")
#計算結果との連結
print("abc"+"123*234")
#str関数と関数の呼び出し(call)
print("abc"+str(123*234)) 


#3-6
#日本語の表示
print("こんにちは")


#3-7
#長い文字列の表示
#エスケープシーケンス \n
print("こんにちは。今日の晩ご飯は何でしたか？\nおいしかったですか？\n何カロリーでしたか？")
#三重クォート
print("""こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？""")
#長い分のそのままの出力
print("こんにちは。今日の晩ご飯は何でしたか？おいしかったですか？何カロリーでしたか？")
print("こんにちは。今日の晩ご飯は何でしたか？"　+
"おいしかったですか？"　+
"何カロリーでしたか？")
print("こんにちは。今日の晩ご飯は何でしたか？\
おいしかったですか？\
何カロリーでしたか？")
#printで開業したく無い時 , end=""
print("こんにちは。今日の晩ご飯は何でしたか？", end="")
print("おいしかったですか？", end="")
print("何カロリーでしたか？")


#3-8
#空白
print("abc"+"cde")
print( "abc" + "cde" )
print(   "abc"   +   "cde"  )
print("abc       def")

print(" こんにちは。今日の晩ご飯は何でしたか？ ")
print(" おいしかったですか？ ")
print(" 何カロリーでしたか？ ")
#改行
print("こんにちは。今日の晩ご飯は何でしたか？")

print("おいしかったですか？")

print("何カロリーでしたか？")
#行間の空白は例外
　　　print(" こんにちは ")


#4-2
#変数 インタラクティブモードとプログラムファイルから変更可能
a = 1
b = 2
print(a + b)
#4-3
#繰り返し実行 for文 
print(1)
print(2)
print(3)
print(4)
print(5)
for a in [1,2,3,4,5]:
    print(a)
for a in [1,2,3,4,5]:
    print(i)　   #出力はインデントを入れて繰り返しの範囲の判別を楽に
#複数の分を入力する場合のインデントの違い
for a in [1,2,3,4,5]:
    print(a)
    print("こんにちは")
#インデントの範囲による繰り返しの範囲の違い
for a in [1,2,3,4,5]:
    print[a]
print("こんにちは")
#range関数   range(開始する値,終了する値)
for a in range(1,100 + 1):
    print(a)
    print("こんにちは")
for a in range(0, 100)
    print(a+1)
    print("こんにちは")
for a in range(100)
    print(a + 1)
    print("こんにちは")
for a in "Hello":
    print(a)

#4-4 条件が成り立っている時のみ実行したい
#while分で繰り返す
total =  0
a = 1
while total <= 50:
    total = total + a
    a = a + 1
print(total)
#for公文と同じ処理をwhileで記述する
for a in range(1, 5 + 1):
    print(a)
a = 1
while a <= 5:
    print(a)
    a = a + 1
#永遠に繰り返したい時
while True:

#4-5条件分岐する　if構文
for a in range(1, 10+1):
    if a <= 5:
        print("小さいです")
    else:
        print("大きいです")
#条件を組み合わせる
if (a >= 1) and (a <= 5):
    print("aは3かもしれません")
if 1 <= a <= 5:
    print("aは3かもしれません")
#演習
for a in (1, 10 + 1 ):
    print(a)
    if a % 2 == 0:
        print("◯")
    if a % 3 == 0:
        print("×")
    if ( a % 2 == 0) and ( a % 3 == 0):
        print("△")　#プログラムとして表現できる、同じ意味での考え方の置き換え
#elseを使って『出ない時の条件』を並べる
for a in (1, 12 + 1 ):
    print(a)
    if (a % 12 == 0):
        print("○")
else:
    if (a % 4 == 0):
        print ("△")
    else:
        if (a % 2 == 0):
            print("×")
        else:
            print("☆")
#elifを使う
for a in (1, 12 + 1 ):
    print(a)
    if (a % 12 == 0):
        print("o")
    elif (a % 4 == 0):
        print("△")
    elif if (a % 2 == 0):
        print("x")
    else:
        print("☆")
#条件が成り立ったときに繰り返しをやめる
total = 0
a = 1
while total <= 50:
    total = total + a
    a = a + 1
print(total)
#上記のプログラムをbreakを用いて
total = 0
a = 1
while True:
    total = total + a = a + 1
    if total > 50:
        break
print(total)

#4-6 関数
#関数の定義
def tashizan(a, b + 1):
    total = 0
    for i in range(a, b + 1):
        total = total + 1
    return total    #return構文



