## Тестовое задание от компании 'Тэнзор' на автотестирование

ссылка
на задание: https://mail.google.com/mail/u/0?ui=2&ik=dd231a7fec&attid=0.1&permmsgid=msg-f:1804108718783301683&th=19097b5237438833&view=att&disp=inline

![Page 1](task/1.png)
![Page 2](task/2.png)
![Page 3](task/3.png)
![Page 4](task/4.png)


### Запустить тесты: 
1. создать виртуальное окружение 
2. активировать виртуальное окружение
3. установить зависимости
4. запускаем тесты из корня директории командой 'pytest', 
'pytest -s -v' - для подробной информации


P. S. Регион, в котором производится тестирование (сейчас - Ярославская обл.)
      указан статично (в модуле sbis_contacts.py: self.my_region_ru: str = 'Ярославская обл.', self.my_region_en: str = '76-yaroslavskaya-oblast')


      В директории utils я реализовал определение геолокации тестируемого оборудования автоматически, создал словарь соответсвий регионов, 
      но в API геолокации есть расхождения имен регионов с именами на тестируемом сайте, что затруднило доделать автоподстановку в класс.