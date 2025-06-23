file_size = int(input('Укажите развер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения: '))
downloaded = 0
seconds = 0

while downloaded < file_size:
    seconds += 1

    new_downloaded = min(downloaded + speed, file_size)
    percentage = (new_downloaded / file_size) * 100
    print(f"Прошло {seconds} сек. Скачано {new_downloaded:.0f} из {file_size:.0f} Мб ({percentage:.0f}%)")
    downloaded = new_downloaded

print(f"Скачивание заняло {seconds} секунд.")