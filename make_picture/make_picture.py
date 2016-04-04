#! /usr/bin/env python3
# coding:UTF-8
"""
プログラム名: make_picture.py
説明:　文字データをコマンドラインから受け取り，画像に変換するプログラム
"""

from PIL import Image, ImageDraw, ImageFont

def make_picture():

    HEIGHT_PIC = 32 #ディスプレイの高さpixel単位

    FONT_FILE = r"fonts/nihongo/FontopoNIHONGO.otf" #表示に使用するフォントの保存場所
    TEXT_FILE = r"tweet.txt"                #ツイッターからのメッセージの保存場所
    IMG_FILE = r"text_image"                          #画像の保存場所（拡張子は後で付加）
    BK_COLOR = "black"                              #背景色の設定
    FONT_COLOR = "green"                            #文字色の設定
    TEXT_PASTE_POINT = (0, -4)                      #フォントによる貼り付け位置のズレを修正

    with open(TEXT_FILE, "r") as f:
        TEXT = f.read()
    print(TEXT)

    #用意する画像の幅を表示する文字によって設定する例:"こんにちは世界        "
    TEXT = TEXT.rstrip('\n')                #改行文字を取り除く
    WIDTH_PIC = (len(TEXT) + 1)*HEIGHT_PIC  #空白を作るために + 1

    FONT = ImageFont.truetype(FONT_FILE, HEIGHT_PIC, encoding="unic")
    IMAGE = Image.new("RGB", (WIDTH_PIC, HEIGHT_PIC), color=BK_COLOR)
    DRAW = ImageDraw.Draw(IMAGE)
    DRAW.text(TEXT_PASTE_POINT, TEXT, font=FONT, fill=FONT_COLOR)

    IMAGE.save(IMG_FILE + ".pbm", "PPM", quality=300, optimize=True)
    IMAGE.save(IMG_FILE + ".bmp", "BMP", quality=300, optimize=True)
    print("made a picture, " + IMG_FILE + ".pbm")

def make_strint_list(text, line_limit = 8):
    #半角と全角での文字の大きさを判定し、文字を詰める関数
    text_iter = iter(text)
    text_lists = ['']
    count = 0

    while True:
        try:
            character = next(text_iter)

            if count >= line_limit:
                count = 0
                text_lists.append('')

            if ord(character) <= 127:#文字が半角の時
                count += 1

            else:#文字が全角の時
                count += 2

            if count > line_limit:
                count = 0
                text_lists.append('')

            text_lists[-1] += character

        except StopIteration:
            break

    return text_lists
def make_picture_scroll_y():

        font_file = r"fonts/misaki_ttf_2015-04-10/misaki_gothic.ttf" #表示に使用するフォントの保存場所
        text_file = r"tweet.txt"                #ツイッターからのメッセージの保存場所
        img_file = r"text_image"                          #画像の保存場所（拡張子は後で付加）
        bk_color = "black"                              #背景色の設定
        font_color = "green"                            #文字色の設定
        font_size = 8 #フォントの大きさ

        with open(text_file, "r") as f:
            text = f.read().replace('\n', '')#改行文字を取り除く

        text = make_strint_list(text)
        print(text)
        WIDTH_PIC = 32 #ディスプレイの高さpixel単位
        HEIGHT_PIC = len(text)*font_size

        font = ImageFont.truetype(font_file, font_size, encoding="unic")
        img = Image.new("RGB", (WIDTH_PIC, HEIGHT_PIC+32), color=bk_color)
        draw = ImageDraw.Draw(img)

        for n in range(len(text)):
            draw.text((0, n*font_size), text[n], font=font, fill=font_color)

        img.save(img_file + ".bmp", "BMP", quality=300, optimize=True)
        img.save(img_file + ".pbm", "PPM", quality=300, optimize=True)

if __name__ == "__main__":
    make_picture_scroll_y()
