# BTC/USDT Parser & Analysis
Jupyter Notebook для сбора и анализа данных о курсе BTC/USDT с Binance API с целью прогнозирования цен. На данный момент реализован только парсинг данных со странички Binance. В дальнейшем планируется:
1. Первичная обработка данных
2. Аналитика полученных данных
3. Дополнительный сбор данных
4. Построение прогноза

## Цель проекта
Прогнозирование котировок BTC/USDT на недельном горизонте на основе исторических данных.

## Основные функции
- Получение данных через Binance Public API
- Очистка и структурирование данных
- Анализ динамики цен (1h, 24h, 7d, 30d)
- Визуализация рыночных показателей

## Технологии
- Языки: Python (Pandas, Requests). 

## Пример данных
Анализируемые показатели:
['percent_change_1h', 'percent_change_24h', 'percent_change_7d',
 'percent_change_30d', 'price', 'volume_24h', 'market_cap',
 'total_supply', 'circulating_supply', 'timestamp']

## Стурктура проекта
Parse_Of_Bitcoin/BTC_parser.ipynb - основной аналитический ноутбук.
Parse_Of_Bitcoin/README.md - этот файл.
