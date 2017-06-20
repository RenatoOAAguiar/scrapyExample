__author__ = 'tixie'

SearchEngines = {
    'google': 'https://www.google.com.br/search?q={0}&start={1}',
    'bing': 'http://www.bing.com/search?q={0}&first={1}'
}


SearchEngineResultSelectors= {
    'google': '//h3/a/@href',
    'bing':'//h2/a/@href',
}