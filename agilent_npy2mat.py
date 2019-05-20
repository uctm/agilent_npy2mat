import os, tkinter, tkinter.filedialog, tkinter.messagebox
import glob
import scipy.io
import numpy as np
import scipy.io
def agilent_npy2mat(dirname):
    '''
    Agilent製のオシロスコープを使用するプログラム
    Get_waveform_data_elegant_VISA_Python
    で保存されたnpyファイルをMatlabで読み取れるようなデータ形式に変換する
    プログラム
    1つのデータには時間データとセンサデータが含まれているがデータ容量削減のため
    センサデータのみを変換する
    ディレクトリ名を受け取ってそのディレクトリ名に_matを追加した
    ディレクトリを作成し，そこに.matファイルを保存するプログラム
    
    Parameters
    ----------
    dirname : データが保存されているディレクトリ名

    Returns
    -------
    無し
    '''
    save_dir = dirname + r'_mat/' # matファイルを保存するディレクトリパス
    os.mkdir(save_dir)
    fnames = glob.glob(dirname + r'/*.npy')
    
    T = np.load(fnames[0])[:, 0]
    scipy.io.savemat(save_dir + 'time.mat', {'time': T})

    for f in fnames:
        x = np.load(f)[:, 1]
        # 絶対パスから拡張子なしのファイル名に変換
        fname_no_extension = f.split('\\')[-1].split('.')[0]
        scipy.io.savemat(save_dir+fname_no_extension + '.mat', {'pvdf':x})

if __name__ == '__main__':
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    root.withdraw()
    # 実行ファイルが存在しているディレクトリパス
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('npy2mat.py','処理データが存在するフォルダを選択してください')
    dirname = tkinter.filedialog.askdirectory(initialdir = iDir)
    agilent_npy2mat(dirname) # matファイルに変換
    tkinter.messagebox.showinfo('npy2mat.py', '変換しました')