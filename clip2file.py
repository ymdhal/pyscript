import os
import shutil as su
import argparse as ap
from PIL import ImageGrab as ig
from PIL import Image as im
import datetime as dt

__doc__=\
  """
  クリップボードの画像を取得し、txtファイルとして出力する.
  引数に出力ファイル名を与えられない場合は、'tmp_日付'のファイル名とする.
  出力ファイル形式:png
  """

# CONST
VERSION = "1.0.0"

def main():
    #---------------------------------------------------
    # 引数チェック
    #---------------------------------------------------
    parser = ap.ArgumentParser(description=__doc__,
                               formatter_class=ap.RawDescriptionHelpFormatter)

    # required args

    # optional args
    parser.add_argument("-f","--filename", type=str,default=None,help="outputfile name/No extension required")
    parser.add_argument("-v", "--version", action="version", version=VERSION)
    args = parser.parse_args()

    #---------------------------------------------------
    # MAIN処理
    #---------------------------------------------------
    # binaryで読み出し,txtで出力
    img = ig.grabclipboard()
    if isinstance(img,im.Image) :
        if args.filename:
            img.save(args.filename,"PNG")
        else:
            now = dt.datetime.now()
            img.save("tmp_"+now.strftime("%Y%m%d_%H%M%S") + ".png","PNG")
            print("saved")
    else:
        print("No Image in ClipBoard!")

if __name__ == "__main__":
    main()
