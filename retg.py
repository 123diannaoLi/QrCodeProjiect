# -*- coding:utf8 -*-

import os


class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''

    def __init__(self):
        self.path = 'C:/Users/lenovo/Desktop/label5/3'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), '02' + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print
                    'converting %s to %s ...' % (src, dst)
                    group = 0
                except:
                    continue
            if item.endswith('.xml'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), '02' + str(i) + '.xml')
                try:
                    os.rename(src, dst)
                    print
                    'converting %s to %s ...' % (src, dst)
                    group = 1

                except:
                    continue
            if group:
                i = i + 1
        print
        'total %d to rename & converted %d jpgs' % (total_num, i)


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()