# DOOM-ASCII

![LOGO](screenshots/ubuntu.png)

**Текстовый думм у вас в терминале!!**
**Но пока без звука, я работаю на этим**

### Ubuntu
Creates ```doom_ascii/doom_ascii```
```
cd src
make
```

## Controls

Дефолтные настройки, можно править в ```.default.cfg```

|Action         |Default Keybind|
|---------------|---------------|
|UP             |ARROW UP		|
|DOWN			|ARROW DOWN		|
|LEFT			|ARROW LEFT		|
|RIGHT			|ARROW RIGHT	|
|STRAFE LEFT	|,				|
|STRAFE RIGHT	|.				|
|FIRE			|SPACE			|
|USE			|E				|
|SPEED			|]				|
|WEAPON SELECT  |1-7            |

### Display

Есть проблемы с разрешением экрана, можно настроить в ```-scaling n``` и твоего значения

|Terminal      |No Strobing|Some Strobing|
|--------------|-----------|-------------|
|Alacritty     |3          |2            |
|Yakuake       |4          |2            |
|Konsole       |4          |3            |
|Xfce4-terminal|5          |3            |
|Windows CMD   |-          |4 (severe)   |

Дефолт 4
