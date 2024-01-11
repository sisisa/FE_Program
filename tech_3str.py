def find_longest_string(s1, s2, s3):
    # 各文字列の長さを取得
    len_s1 = len(s1)
    len_s2 = len(s2)
    len_s3 = len(s3)

    # 最も長い文字列を見つける
    if len_s1 > len_s2 and len_s1 > len_s3:
        return s1
    elif len_s2 > len_s1 and len_s2 > len_s3:
        return s2
    else:
        return s3

# 3つの文字列を入力として受け取る
s1 = input()
s2 = input()
s3 = input()

# 最も長い文字列を出力
result = find_longest_string(s1, s2, s3)
print(result)
