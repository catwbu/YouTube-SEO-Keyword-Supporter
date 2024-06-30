# First things, first. Import the wxPython package.
import wx

import random


def main():
    app = wx.App()

    frame = wx.Frame(
        parent=None,
        id=wx.ID_ANY,
        title='Hello',
        size=wx.Size(800, 720)
    )
    frame.Show()

    # 產生字型設定
    font = wx.Font(wx.FontInfo(18).FaceName('Consolas'))

    poX = 10
    poY = 13

    # 建立文字元件
    label = wx.StaticText(
        parent=frame,
        label='主題',
        pos=wx.Point(poX, poY),
        size=wx.Size(50, 20)
    )
    # 套用字型
    label.SetFont(font)

    # 產生按鈕元件
    button = wx.Button(
        parent=frame,
        id=wx.ID_ANY,
        label='Say',
        pos=wx.Point(poX+650, poY),
        size=wx.Size(100, 22)
    )
    # 套用字型
    button.SetFont(font)
    # 綁定按鈕點擊事件


    # 產生輸入元件
    inputA = wx.TextCtrl(
        parent=frame,
        id=wx.ID_ANY,
        #value='Hello666',
        pos=wx.Point(100, poY),
        size=wx.Size(500, 40)
    )
    # 套用字型
    inputA.SetFont(font)


    inputB = wx.TextCtrl(
        parent=frame,
        id=wx.ID_ANY,
        #value='',
        pos=wx.Point(100, poY+50),
        size=wx.Size(500, 40)
    )
        # 套用字型
    inputB.SetFont(font)


    inputC = wx.TextCtrl (
            parent=frame,
            id=wx.ID_ANY,
            #value='',
            pos=wx.Point(100, poY+100),
            size=wx.Size(500, 40)
    )
            # 套用字型
    inputC.SetFont(font)









    def OnClickTop(event):

        listA=[]
        listB=[]
        listC=[]
        listA = (inputA.GetValue().split(','))
        listB = (inputB.GetValue().split(','))
        listC = (inputC.GetValue().split(','))
        print(len(listA))
        print(len(listB))
        print(len(listC))

        for text1 in listA:
            if text1 == '':
                break

            for text2 in listB:
                if text2 == '':
                    output = str(text1)
                    output_(output)
                    break

                for text3 in listC:
                    if text3 == '':

                        output = str(text1)+str(text2)
                        output_(output)
                        break
                    output = str(text1)+str(text2)+str(text3)
                    output_(output)

    def output_(context):
        textarea.AppendText(str(context)+',\n')
        return




    button.Bind(wx.EVT_BUTTON, OnClickTop)





    # 產生輸出用元件
    textarea = wx.TextCtrl(
        parent=frame,
        id=wx.ID_ANY,
        style=wx.TE_MULTILINE,
        pos=wx.Point(100, 350),
        size=wx.Size(500, 300)
    )
    # 套用字型
    textarea.SetFont(font)
    # 設為唯讀
    textarea.SetEditable(False)

    app.MainLoop()

if __name__ == '__main__':
    main()
