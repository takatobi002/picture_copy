import os
import shutil

#コピー元フォルダ内のファイルをリストfiles_file に格納する
files = os.listdir("/hoge/hoge")
files_file = [f for f in files if os.path.isfile(os.path.join(path,f))]
#リストをソートする
files_file.sort()

#コピー先のフォルダ
copy_folder = "/hoge/copy"

#関数copy_picを作成。コピーするファイルとコピー先のディレクトリを指定してコピーする。
def copy_pic(co_file,copy_folder):
    shutil.copy(co_file,copy_folder)

#files_fileを順番に叩いていく。
for i in files_file:
    #800枚に1枚の間隔でコピーをおこなう。
    if int(files_file.index(i)) % 800 == 0:
        #現在扱っているfileを格納する変数co_fileを呼び出し
        co_file = os.path.abspath((files_file[(files_file.index(i))]))
        copy_pic(co_file,copy_folder)
        #関数が動いているかどうか、コピーしたファイル名を絶対パスでコンソールに表示。
        print(co_file)
    #iに1を足して次のファイルの判定をする。iはファイル名が格納されているので、indexでリスト番号を取る。
    i = int(files_file.index(i)) + 1