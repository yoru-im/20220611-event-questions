# -*- coding: utf-8 -*-


def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    
    ##未完成です##
    left = []
    right = []
    pivots = []
    
    # pivotとの比較で要素を分割
    for i in array:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            pivots.append(i)
        else:
            right.append(i)
    
    print(left + pivots + right)

    return array


    # ここまで記述

if __name__ == '__main__':
    main()