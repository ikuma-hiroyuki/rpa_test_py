from time import sleep

import pyautogui

# 画面の中にこのパスの画像があるか検索する。
button = './btn.png'


def find_image_locate(image_path, time_out=10, confidence=0.9):
    """
    プライマリスクリーンから任意の画像の座標を検索する。
    :param image_path: 画面から見つけたい画像のパス。
    :param time_out: 画像検索待ち時間(秒)。
    :param confidence: 信頼感。数値が高いほど信頼できるが、見つからない確率も上がる。(0~1?)
    :return: 画像の座標。
    """

    for _ in range(time_out):
        locate = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if locate is not None:
            return locate
        else:
            sleep(1)


if __name__ == '__main__':
    try:
        button_locate = find_image_locate(image_path=button)
        x, y = pyautogui.center(button_locate)
    except TypeError:
        print('Image not found.')
    else:
        pyautogui.moveTo(x, y)
