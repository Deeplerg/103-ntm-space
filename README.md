## Сборка с NTM: Space для Minecraft 1.7.10

Сборка основана на модпаке *Space Tech: Integrated*: моды плотно взаимодействуют с основным модом **HBM's NTM: Space** (плотная интеграция в духе GTNH)

### Что можно в модпаке
- Отправиться в космос; планеты в стиле Kerbal Space Program
- Строить мегазаводы в стиле Factorio / Dyson Sphere Program
- Пройти путь от первобытного постукивания камнями до термоядерных реакторов, сфер Дайсона и терраформирования
- Писать программы с OpenComputers
- Строить ж/д сети с RailCraft

### 1.7.10? Не совсем
Максимально модернизировали старый клиент:
- Angelica: бекпорт Sodium + Iris, поддержка последних шейдеров
- Distant Horizons (+ DH на сервере)
- Java 21+
- Современный ад 1.16+, современное плавание, элитры и новые блоки
- Красивый ландшафт с Realistic Terrain Generation

### Что еще есть?
- **КОТ НА АРБУЗЕ 🐈🍉 🐈🍉 🐈🍉**
- **МОРЖ 🦭 🦭 🦭**
- Система квестов для помощи с прогрессией (из Space Tech: Integrated) + полный перевод на русский

[Полный список модов](MODS.md) 


## Как скачать сборку?

### ***Рекомендованный способ***

Есть собранные готовые лаунчеры:
- [Windows](https://github.com/Deeplerg/103-ntm-space/releases/latest/download/103-ntm-space-Windows.zip)
- [Linux](https://github.com/Deeplerg/103-ntm-space/releases/latest/download/103-ntm-space-Linux.tar.gz)
- [MacOS](https://github.com/Deeplerg/103-ntm-space/releases/latest/download/103-ntm-space-macOS.zip)

Лаунчеры собираются автоматически на основе 
[PrismLauncher-Cracked](https://github.com/Diegiwg/PrismLauncher-Cracked) 
и Java 21.

Лаунчер нужно просто распаковать и запустить исполняемый файл. 

**ВАЖНО:** первый запуск игры довольно долгий, потому что инстанс сам скачивает нужные ему файлы. 
При скачивании самой сборки может показаться, что ничего не происходит, 
но прогресс можно отследить в логах.

У готовых лаунчеров есть автообновление сборки при каждом запуске.

#### Про безопасность.
Этот репозиторий - набор инструкций, 
как сгенерировать сборку, и сам по себе .jar файлы не хранит.
При релизе автоматически генерируется аттестация, 
[см. один из последних actions](https://github.com/Deeplerg/103-ntm-space/actions).
Получившиеся SHA256 хэши можно сравнить с теми, что в релизе, 
чтобы удостовериться, что ничего не было подменено. 
Все исходники для генерации сборки в репе в открытом доступе.


### ***Собрать самому (не поддерживается!)***

Если все же хочется использовать со своим лаунчером:
- [Сборка в формате Modrinth .mrpack](https://github.com/Deeplerg/103-ntm-space/releases/latest/download/103-ntm-space-modrinth.mrpack)
- [Клиентская сборка (моды + конфиги)](https://github.com/Deeplerg/103-ntm-space/releases/latest/download/103-ntm-space-client.zip)
- [Серверная сборка (моды + конфиги)](https://github.com/Deeplerg/103-ntm-space/releases/latest/download/103-ntm-space-server.zip)

Нужно учитывать, что в сборке используется [lwjgl3](https://github.com/GTNewHorizons/lwjgl3ify).
Так что если не работает со своим лаунчером: см. готовые лаунчеры.


## Локальная разработка

Для сборки сборки используется [packwiz](https://github.com/packwiz/packwiz).

Установка:
1. Установить Go: https://golang.org/dl/
2. `go install github.com/packwiz/packwiz@latest`
3. Копируем `index.toml.template` и `pack.toml.template` в обычные .toml 
и делаем `packwiz refresh`  
4. (Опционально) Даем packwiz токен гитхаба, чтобы избежать rate limit:
   1. Копируем `global-config.toml.example` в `global-config.toml`
   2. [Здесь](https://github.com/settings/tokens) генерируем классический токен, разрешения ставить не обязательно 

После любого изменения делаем `packwiz refresh` 

Добавить мод: см. `packwiz help`

Чтобы не прописывать `packwiz mr export` и не удалять сборки в Prism каждый раз, можно сделать следующий сетап:
1. В Prism или MultiMC добавляем новый инстанс 1.7.10 с Forge
2. Заходим в папку `minecraft` инстанса и кидаем туда 
[packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar)
3. Редактировать инстанс -> настройки -> кастомные команды -> команда перед запуском: 
```
"$INST_JAVA" -jar packwiz-installer-bootstrap.jar --no-gui --side client "[ЛОКАЛЬНЫЙ ПУТЬ К РЕПОЗИТОРИЮ]\pack.toml"
```
4. Не забыть заменить \[ЛОКАЛЬНЫЙ ПУТЬ К РЕПОЗИТОРИЮ] на путь к папке, куда склонировали репу
5. Теперь каждый раз при запуске инстанса сборка будет автоматически экспортироваться 
(на всякий случай можно прописывать `packwiz refresh` перед запуском)


## Credits

Основано на сборке [Space Tech: Integrated](https://www.curseforge.com/minecraft/modpacks/space-tech-integrated).

[NTM: Space](https://github.com/JameH2/Hbm-s-Nuclear-Tech-GIT) ❤️

[HBM: NTM](https://github.com/hbmmods/hbm-s-nuclear-tech-git) 🔥
