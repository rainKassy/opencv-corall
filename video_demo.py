import cv2

# Загружаем видео с камеры (0 — первая веб-камера) или файл
cap = cv2.VideoCapture(0)              # Можно заменить на 'py/video.mp4' для файла

# Проверяем, открылось ли видео
if not cap.isOpened():
    print("Ошибка: не удалось открыть видео.")
    exit()

while True:
    ret, frame = cap.read()            # Считываем один кадр. ret=True, если успешно
    if not ret:
        print("Кадры закончились или ошибка.")
        break

    # Переводим кадр в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Применяем размытие для снижения шумов
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    # Находим контуры (границы) объектов
    edges = cv2.Canny(blur, 50, 150)

    # Показываем текущий кадр с эффектом
    cv2.imshow('Video Edges', edges)

    # Ждём 1 мс и проверяем — нажата ли клавиша 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Очищаем ресурсы
cap.release()
cv2.destroyAllWindows()
