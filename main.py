from endpoints import AVQuery

if __name__ == "__main__":

    avq = AVQuery()

    #daily = avq.daily_data(symbol='IBM', function='TIME_SERIES_DAILY', outputsize='full')
    #daily2 = avq.daily_data(symbol='XOM', function='TIME_SERIES_DAILY', outputsize='full')

    avq.find_ticker(ticker_to_search='bmw')


