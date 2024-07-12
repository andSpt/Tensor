import requests

region_names = {
            'Moscow': 'Москва',
            'St. Petersburg': 'Санкт-Петербург',
            'Republic of Adygeya': 'Республика Адыгея',
            'Republic of Bashkortostan': 'Республика Башкортостан',
            'Republic of Buryatia': 'Республика Бурятия',
            'Republic of Altai': 'Республика Алтай',
            'Republic of Daghestan': 'Республика Дагестан',
            'Republic of Ingushetia': 'Республика Ингушетия',
            'Kabardino-Balkarian Republic': 'Респ. Кабардино-Балкария',
            'Republic of Kalmykia': 'Республика Калмыкия',
            'Karachayevo-Circassian Republic': 'Респ. Карачаево-Черкессия',
            'Republic of Karelia': 'Республика Карелия',
            'Komi Republic': 'Республика Коми',
            'Republic of Mari El': 'Республика Марий Эл',
            'Republic of Mordovia': 'Республика Мордовия',
            'Republic of Sakha (Yakutia)': 'Республика Саха (Якутия)',
            'Republic of North Ossetia – Alania': 'Северная Осетия - Алания',
            'Republic of Tatarstan': 'Республика Татарстан',
            'Republic of Tuva': 'Республика Тыва',
            'Udmurtian Republic': 'Удмуртская Республика',
            'Republic of Khakassia': 'Республика Хакасия',
            'Chechen Republic': 'Республика Чечня',
            'Chuvash Republic': 'Республика Чувашия',
            'Altai Territory': 'Алтайский край',
            'Krasnodar Territory': 'Краснодарский край',
            'Krasnoyarsk Territory': 'Красноярский край',
            'Primorye Territory': 'Приморский край',
            'Stavropol Territory': 'Ставропольский край',
            'Khabarovsk Territory': 'Хабаровский край',
            'Amur Region': 'Амурская обл.',
            'Arkhangelsk Region': 'Архангельская обл.',
            'Astrakhan Region': 'Астраханская обл.',
            'Belgorod Region': 'Белгородская обл.',
            'Bryansk Region': 'Брянская обл.',
            'Vladimir Region': 'Владимирская обл.',
            'Volgograd Region': 'Волгоградская обл.',
            'Vologda Region': 'Вологодская обл.',
            'Voronezh Region': 'Воронежская обл.',
            'Ivanovo Region': 'Ивановская обл.',
            'Irkutsk Region': 'Иркутская обл.',
            'Kaliningrad Region': 'Калининградская обл.',
            'Kaluga Region': 'Калужская обл.',
            'Kamchatka Territory': 'Камчатский край',
            'Kemerovo Region': 'Кемеровская обл.',
            'Kirov Region': 'Кировская обл.',
            'Kostroma Region': 'Костромская обл.',
            'Kurgan Region': 'Курганская обл.',
            'Kursk Region': 'Курская обл.',
            'Leningrad Region': 'Ленинградская обл.',
            'Lipetsk Region': 'Липецкая обл.',
            'Magadan Region': 'Магаданская обл.',
            'Moscow Region': 'Московская обл.',
            'Murmansk Region': 'Мурманская обл.',
            'Nizhny Novgorod Region': 'Нижегородская обл.',
            'Novgorod Region': 'Новгородская обл.',
            'Novosibirsk Region': 'Новосибирская обл.',
            'Omsk Region': 'Омская обл.',
            'Orenburg Region': 'Оренбургская обл.',
            'Orel Region': 'Орловская обл.',
            'Penza Region': 'Пензенская обл.',
            'Perm Territory': 'Пермский край',
            'Pskov Region': 'Псковская обл.',
            'Rostov Region': 'Ростовская обл.',
            'Ryazan Region': 'Рязанская обл.',
            'Samara Region': 'Самарская обл.',
            'Tolyatti': 'Тольятти',
            'Saratov Reg': 'Саратовская обл.',
            'Sakhalin Region': 'Сахалинская обл.',
            'Sverdlovsk Region': 'Свердловская обл.',
            'Smolensk Region': 'Смоленская обл.',
            'Tambov Region': 'Тамбовская обл.',
            'Tver Region': 'Тверская обл.',
            'Tomsk Region': 'Томская обл.',
            'Tula Region': 'Тульская обл.',
            'Tyumen Region': 'Тюменская обл.',
            'Ulyanovsk Region': 'Ульяновская обл.',
            'Chelyabinsk Region': 'Челябинская обл.',
            'Trans-Baikal Territory': 'Забайкальский край',
            'Yaroslavl Region': 'Ярославская обл.',
            'Jewish Autonomous Region': 'Еврейская АО',
            'Nenets Autonomous Area': 'Ненецкий АО',
            'Khanty-Mansi Autonomous Area – Yugra': 'Ханты-Мансийский АО',
            'Chukotka Autonomous Area': 'Чукотский АО',
            'Yamal-Nenets Autonomous Area': 'Ямало-Ненецкий АО'
        }

def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        region = data['regionName']
        region_ru = region_names[region] if region in region_names else region
        region_en = region

        return f"Регион (RU): {region_ru}, Регион (EN): {region_en}"
    else:
        return "Невозможно определить местоположение"


# Получаем IP-адрес пользователя
ip = requests.get('https://api64.ipify.org').text

# Получаем информацию о местоположении по IP-адресу
location = get_location(ip)
print(location)
