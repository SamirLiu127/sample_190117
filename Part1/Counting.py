# -*- coding: utf-8 -*-
from collections import Counter


def file_count(url_list):
    file_list = [u.split('/').pop() for u in url_list]
    return file_list


def main():
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]
    f_list = file_count(urls)
    count_dict = Counter(f_list)
    for k, v in count_dict.items():
        print(str(k) + ': ' + str(v))
    return count_dict


if __name__ == '__main__':
    main()
