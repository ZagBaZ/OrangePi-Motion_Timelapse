# OrangePi-Motion_Timelapse
## Timelapse на OrangePi + Google_disk + Telegram

### Установка и запуск motion
```
apt-get install motion
```
Создаем каталог и файл для логов motion:
```
mkdir /var/log/motion
```
```
touch /var/log/motion/motion.log
```
Редактируем владельца для лог-файла:
```
chown motion:motion /var/log/motion/motion.log
```
Открываем файл:
```
vi /etc/default/motion
```
В нем либо не должно быть параметра start_motion_daemon, либо он должен иметь значение:

> start_motion_daemon=yes

Разрешаем автоматический запуск демона и перезапускаем сервис:
```
systemctl enable motion
```
```
systemctl restart motion
```
Можно проверить, что сервис работает корректно:
```
systemctl status motion
```


### Параметры для конфигурационных файлов можно найти по адресу:

> https://motion-project.github.io/4.2.2/motion_config.html
