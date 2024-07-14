import requests

region_names = {
            '77-moskva': 'Москва',
            '78-sankt-peterburg': 'г. Санкт-Петербург',
            '01-respublika-adygeya': 'Республика Адыгея',
            '02-respublika-bashkortostan': 'Республика Башкортостан',
            '03-respublika-buryatiya': 'Республика Бурятия',
            '04-respublika-altaj': 'Республика Алтай',
            '05-respublika-dagestan': 'Республика Дагестан',
            '06-respublika-ingushetiya': 'Республика Ингушетия',
            '07-respublika-kabardino-balkariya': 'Респ. Кабардино-Балкария',
            '08-respublika-kalmykiya': 'Республика Калмыкия',
            '09-respublika-karachaevo-cherkessiya': 'Респ. Карачаево-Черкессия',
            '10-respublika-kareliya': 'Республика Карелия',
            '11-respublika-komi': 'Республика Коми',
            '12-respublika-marij-el': 'Республика Марий Эл',
            '13-respublika-mordoviya': 'Республика Мордовия',
            '14-respublika-saha-yakutiya': 'Республика Саха (Якутия)',
            '15-severnaya-osetiya---alaniya': 'Северная Осетия - Алания',
            '16-respublika-tatarstan': 'Республика Татарстан',
            '17-respublika-tyva': 'Республика Тыва',
            '18-udmurtskaya-respublika': 'Удмуртская Республика',
            '19-respublika-hakasiya': 'Республика Хакасия',
            '20-respublika-chechnya': 'Республика Чечня',
            '21-respublika-chuvashiya': 'Республика Чувашия',
            '22-altajskij-kraj': 'Алтайский край',
            '23-krasnodarskij-kraj': 'Краснодарский край',
            '24-krasnoyarskij-kraj': 'Красноярский край',
            '25-primorskij-kraj': 'Приморский край',
            '26-stavropolskij-kraj': 'Ставропольский край',
            '27-habarovskij-kraj': 'Хабаровский край',
            '28-amurskaya-oblast': 'Амурская обл.',
            '29-arhangelskaya-oblast': 'Архангельская обл.',
            '30-astrahanskaya-oblast': 'Астраханская обл.',
            '31-belgorodskaya-oblast': 'Белгородская обл.',
            '32-bryanskaya-oblast': 'Брянская обл.',
            '33-vladimirskaya-oblast': 'Владимирская обл.',
            '34-volgogradskaya-oblast': 'Волгоградская обл.',
            '35-vologodskaya-oblast': 'Вологодская обл.',
            '36-voronezhskaya-oblast': 'Воронежская обл.',
            '37-ivanovskaya-oblast': 'Ивановская обл.',
            '38-irkutskaya-oblast': 'Иркутская обл.',
            '39-kaliningradskaya-oblast': 'Калининградская обл.',
            '40-kaluzhskaya-oblast': 'Калужская обл.',
            '41-kamchatskij-kraj': 'Камчатский край',
            '42-kemerovskaya-oblast': 'Кемеровская обл.',
            '43-kirovskaya-oblast': 'Кировская обл.',
            '44-kostromskaya-oblast': 'Костромская обл.',
            '45-kurganskaya-oblast': 'Курганская обл.',
            '46-kurskaya-oblast': 'Курская обл.',
            '47-leningradskaya-oblast': 'Ленинградская обл.',
            '48-lipeczkaya-oblast': 'Липецкая обл.',
            '49-magadanskaya-oblast': 'Магаданская обл.',
            '50-moskovskaya-oblast': 'Московская обл.',
            '51-murmanskaya-oblast': 'Мурманская обл.',
            '52-nizhegorodskaya-oblast': 'Нижегородская обл.',
            '53-novgorodskaya-oblast': 'Новгородская обл.',
            '54-novosibirskaya-oblast': 'Новосибирская обл.',
            '55-omskaya-oblast': 'Омская обл.',
            '56-orenburgskaya-oblast': 'Оренбургская обл.',
            '57-orlovskaya-oblast': 'Орловская обл.',
            '58-penzenskaya-oblast': 'Пензенская обл.',
            '59-permskij-kraj': 'Пермский край',
            '60-pskovskaya-oblast': 'Псковская обл.',
            '61-rostovskaya-oblast': 'Ростовская обл.',
            '62-ryazanskaya-oblast': 'Рязанская обл.',
            '63-samarskaya-oblast': 'Самарская обл.',
            '63t-tolyatti': 'Тольятти',
            '64-saratovskaya-oblast': 'Саратовская обл.',
            '65-sahalinskaya-oblast': 'Сахалинская обл.',
            '66-sverdlovskaya-oblast': 'Свердловская обл.',
            '67-smolenskaya-oblast': 'Смоленская обл.',
            '68-tambovskaya-oblast': 'Тамбовская обл.',
            '69-tverskaya-oblast': 'Тверская обл.',
            '70-tomskaya-oblast': 'Томская обл.',
            '71-tulskaya-oblast': 'Тульская обл.',
            '72-tyumenskaya-oblast': 'Тюменская обл.',
            '73-ulyanovskaya-oblast': 'Ульяновская обл.',
            '74-chelyabinskaya-oblast': 'Челябинская обл.',
            '75-zabajkalskij-kraj': 'Забайкальский край',
            '76-yaroslavskaya-oblast': 'Ярославская обл.',
            '79-evrejskaya-ao': 'Еврейская АО',
            '83-neneczkij-ao': 'Ненецкий АО',
            '86-hanty-mansijskij-ao': 'Ханты-Мансийский АО',
            '87-chukotskij-ao': 'Чукотский АО',
            '89-yamalo-neneczkij-ao': 'Ямало-Ненецкий АО',
            '90-zaporozhskaya-oblast': 'Запорожская обл.',
            '91-respublika-krym': 'Республика Крым',
            '92-sevastopol': 'г. Севастополь',
            '93-doneczkaya-nar.-resp.': 'Донецкая народная республика',
            '95-hersonskaya-oblast': 'Херсонская обл.',
        }


def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        region = data['regionName']
        region_short = region.lower().replace('republic of ', '').replace('territory of ', '').replace('region ', '').replace(' region', '')
        print(region_short)
        # region_en = region.lower() if region.lower() in processed_region_names


# Получаем IP-адрес пользователя
ip = requests.get('https://api64.ipify.org').text

# Получаем информацию о местоположении по IP-адресу
location = get_location(ip)
print(location)
