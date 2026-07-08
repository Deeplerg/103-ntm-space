## Как скачать сборку?
**TODO ссылки на releases/latest**


## Локальная разработка

Для сборки сборки используется [packwiz](https://github.com/packwiz/packwiz).

Установка:
1. Установить Go: https://golang.org/dl/
2. `go install github.com/packwiz/packwiz@latest`
3. (Опционально) Даем packwiz токен гитхаба, чтобы избежать rate limit:
   1. Копируем `global-config.toml.example` в `global-config.toml`
   2. [Здесь](https://github.com/settings/tokens) генерируем классический токен, разрешения ставить не обязательно 

После любого изменения делаем `packwiz refresh` 

Добавить мод: см. `packwiz help`

Чтобы не прописывать `packwiz mr export` и не удалять сборки в Prism каждый раз, можно сделать следующий сетап:
1. В Prism добавляем новый инстанс 1.7.10 с forge
2. Заходим в папку `minecraft` инстанса и кидаем туда 
[packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar)
3. Редактировать инстанс -> настройки -> кастомные команды -> команда перед запуском: 
```
"$INST_JAVA" -jar packwiz-installer-bootstrap.jar --no-gui --side client "[ПУТЬ К РЕПОЗИТОРИЮ]\pack.toml"
```
4. Не забыть заменить \[ПУТЬ К РЕПОЗИТОРИЮ]
5. Теперь каждый раз при запуске инстанса сборка будет автоматически экспортироваться
