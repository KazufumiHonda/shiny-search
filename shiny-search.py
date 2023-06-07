import pyautogui as pgui
import time
import numpy as np
import cv2

class ShinySearch:
    BUTTON_KEY_A = 'k'
    BUTTON_KEY_B = 'j'
    BUTTON_KEY_START = 'm'
    BUTTON_KEY_SELECT = 'n'
    BUTTON_KEY_LEFT = 'a'
    BUTTON_KEY_RIGHT = 'd'
    BUTTON_KEY_UP = 'w'
    BUTTON_KEY_DOWN = 's'
    BUTTON_KEY_R = 'p'
    BUTTON_KEY_L = 'q'

    WAIT_TIME = 0.2

    SWEET_POKE_POS = 2
    SWEET_MOVE_POS = 3
    NORMAL_VALUE = 153.08891558441 # 通常ドーブル
    #SIHIY_VALUE = 153.3019805194805 # 色違いドーブル

    def search(self):
        # 1. mgba画面を最前面にする
        # ただし、プレイヤーの現在地は草むらとする
        self.foregroundMGBA()
        # 2. メニュー起動->甘い香り発動
        self.sweetScent(self.SWEET_POKE_POS, self.SWEET_MOVE_POS)
        # 3. 甘い香りで遭遇したかを判定
        # 遭遇していれば4. 色違いの判定へ、そうでなければ2をもう一度行う
        # 4. 色違いの判定
        # 画像処理でポケモンの部分だけトリミングし、通常値と比較して判定する
        # 通常値はあらかじめ採取しておく
        if self.shinyCheck():
            # 色違いであった場合は処理を停止し、プログラムを終了する(今後通知できるようにする)
            print('case true')
            return True
        else:
            # 色違いでなかった場合は、逃げる.その後、2から処理をやり直す
            print('case false')
            self.run()
            time.sleep(1.0)
            return False

        return False

    def foregroundMGBA(self):
        pgui.click(100, 100)
        print('foregroundMGBA')
        time.sleep(1.0)

    def sweetScent(self, poke_pos, move_pos=3):
        print('poke_pos: ', poke_pos, ' , move_pos: ', move_pos)
        # メニュー起動
        self.pressButtonStart()
        # ポケモン一覧選択
        # 前回のカーソル位置を記憶する仕様があるため、要検討
        # 今回は簡単のため、既にポケモン欄が選択されているとする
        self.pressButtonA()
        time.sleep(1.0)
        # 甘い香りを使うポケモンの選択
        # pos-1回だけAを押す
        for i in range(poke_pos-1):
            self.pressButtonDown()
        time.sleep(0.2)
        # ポケモンを選択し、甘い香りを発動
        self.pressButtonA()
        for i in range(move_pos):
            self.pressButtonDown()
        self.pressButtonA()
        time.sleep(12.0)

    def run(self):
        # A button(最初の遭遇画面)
        self.pressButtonA()
        # 少し待つ(自分のポケモン投げるモーション)
        time.sleep(3.5)
        # 右->下->A button(逃げるの選択)
        self.pressButtonRight()
        self.pressButtonDown()
        self.pressButtonA()
        # A button(メッセージを読む)
        self.pressButtonA()

    def shinyCheck(self):
        # ゲーム画面の画像を取る(範囲キャプチャ)
        screen_shot = pgui.screenshot(region=(1250, 100, 700, 660))
        img = np.array(screen_shot, dtype=np.uint8)
        # 画像から平均値を求める
        mean_val = img.mean()
        # その値をNORMAL_VALUEと比較
        # 一致していたら通常個体->False
        # 不一致の場合、非通常個体=色違い->True
        if mean_val == self.NORMAL_VALUE:
            return False
        else:
            print('shiny mean: ', mean_val)
            screen_shot.save('shiny.png')
            return True

    def testKey(self):
        pgui.click(100, 100)
        #pgui.typewrite('Hello, pyautogui key!')
        pgui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

    def pressButtonA(self):
        pgui.keyDown(self.BUTTON_KEY_A)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_A)
        time.sleep(0.1)

    def pressButtonB(self):
        pgui.keyDown(self.BUTTON_KEY_B)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_B)
        time.sleep(0.1)

    def pressButtonStart(self):
        pgui.keyDown(self.BUTTON_KEY_START)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_START)
        time.sleep(0.1)

    def pressButtonSelect(self):
        pgui.keyDown(self.BUTTON_KEY_SELECT)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_SELECT)
        time.sleep(0.1)

    def pressButtonLeft(self):
        pgui.keyDown(self.BUTTON_KEY_LEFT)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_LEFT)
        time.sleep(0.1)

    def pressButtonRight(self):
        pgui.keyDown(self.BUTTON_KEY_RIGHT)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_RIGHT)
        time.sleep(0.1)

    def pressButtonUp(self):
        pgui.keyDown(self.BUTTON_KEY_UP)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_UP)
        time.sleep(0.1)

    def pressButtonDown(self):
        pgui.keyDown(self.BUTTON_KEY_DOWN)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_DOWN)
        time.sleep(0.1)

    def pressButtonR(self):
        pgui.keyDown(self.BUTTON_KEY_R)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_R)
        time.sleep(0.1)

    def pressButtonL(self):
        pgui.keyDown(self.BUTTON_KEY_L)
        time.sleep(0.1)
        pgui.keyUp(self.BUTTON_KEY_L)
        time.sleep(0.1)

def main():
    ss = ShinySearch()
    #ss.search()

    count = 0
    # main codes
    while(True):
        flag = ss.search()
        count += 1
        print('count: ', count)
        if flag:
            break

    # test code
    #ss.foregroundMGBA()
    #screen_shot = pgui.screenshot(region=(1250, 100, 700, 660))
    #screen_shot.save('sample.png')
    #img = np.array(screen_shot, dtype=np.uint8)
    #print('mean: ', img.mean())

if __name__ == "__main__":
    main()
