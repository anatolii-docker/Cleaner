#!/bin/python

import os
import time

DAYS = 5  # Максимальный возраст файлов, файлы старше будут удалены
FOLDERS = ["D:\Python\Folders", "D:\Python\Folders-1"]  #Папки, где будет происходить поиск

TOTAL_DELETED_SIZE = 0      # Общий размер удаленных файлов, Mb
TOTAL_DELETED_FILES = 0     # Количество удаленных файлов
TOTAL_DELETED_DIRS = 0      # Количество удаленных директорий

nowTime = time.time()       # Текущее время в сек.
ageTime = nowTime - 60*60*24*DAYS  # Определяем возраст файлов

def del_old_files(folder):
    global TOTAL_DELETED_FILES
    global TOTAL_DELETED_SIZE
    for path, dir, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)   #Полный путь к файлу
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile     # Общий размер удаленных файлов
                TOTAL_DELETED_FILES +=1            # Количество удаленных файлов
                print("Удаленный файл: " + str(fileName))
                os.remove(fileName)               # Удаляем файл

def del_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders = 0
    for path, dirs, files in os.walk(folder):
        if(not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders += 1
            print("Удаленная пустая папка: " + str(path))
            os.rmdir(path)
        if empty_folders > 0:
            del_old_files(folder)

starttime = time.asctime()   # Время начала работы функции

for folder in FOLDERS:
    del_old_files(folder)    # Удаление старых файлов
    del_empty_dir(folder)    # Удаление пустых папок

finishtime = time.asctime()  # Время окончания

print("Время начала: " + str(starttime))
print("Размер удаленных файлов: " + str(TOTAL_DELETED_SIZE) + "Mb")
print("Количество удаленных файлов: " + str(TOTAL_DELETED_FILES))
print("Количество удаленных папок: " + str(TOTAL_DELETED_DIRS))
print(finishtime)








