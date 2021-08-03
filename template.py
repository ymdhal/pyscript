import os
import shutil as su
import argparse as ap

__doc__=\
  """
  処理内容
  指定したファイルをbinaryで読み込みtxtとして出力する
  """

# CONST
VERSION = "0.0.1"
OUTPUT_DIR = "./result"
OUTPUT_FILE = "template.dat"

def main():
    #---------------------------------------------------
    # 引数チェック
    #---------------------------------------------------
    parser = ap.ArgumentParser(description=__doc__,
                               formatter_class=ap.RawDescriptionHelpFormatter)

    # must args
    parser.add_argument("filename", help="target file")

    # option args
    parser.add_argument("-v", "--version", action="version", version=VERSION)
    parser.add_argument("-s", "--start", type=int, default=1,help="開始位置[int]")
    parser.add_argument("-e", "--end"  , type=int, default=0,help="終了位置[int]")
    args = parser.parse_args()

    #---------------------------------------------------
    # 書き出し先
    #---------------------------------------------------
    # 既存であれば削除し新規作成
    if os.path.isdir(OUTPUT_DIR):
        su.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    #---------------------------------------------------
    # MAIN処理
    #---------------------------------------------------
    # binaryで読み出し,txtで出力
    print("start={},end={}".format(args.start,args.end))
    with open(args.filename, "rb") as rf:
        data = rf.read()
        wpath = os.path.join(OUTPUT_DIR,OUTPUT_FILE)
        with open(wpath, "w") as wf:
            wf.write(str(data))

if __name__ == "__main__":
    main()
