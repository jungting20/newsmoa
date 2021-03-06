from django.shortcuts import render
import feedparser
from newsproject.user.models import NewsCustom
from newsproject.news_component.models import NewsContent
from html.parser import HTMLParser
# Create your views here.


def home(request):
    news_contents = []
    if request.user.is_authenticated:
        news_customs = NewsCustom.objects.filter(user_info__user=request.user).order_by('priority')
        news_customs_count = news_customs.count()
        for news_custom in news_customs:
            i = 1
            feed = feedparser.parse(news_custom.news_content.xml_address)
            for item in feed.entries:
                from datetime import datetime
                from time import mktime
                if hasattr(item, 'published_parsed'):
                    item['published_datetime'] = datetime.fromtimestamp(mktime(item['published_parsed']))
                elif hasattr(item, 'updated_parsed'):
                    item['published_datetime'] = datetime.fromtimestamp(mktime(item['updated_parsed']))
                item['news_company'] = news_custom.news_content.get_company_name
                item['news_section'] = news_custom.news_content.get_section_name
                item['news_image'] = 'newsproject/image/news_company' + str(news_custom.news_content.news_company) + '.png'
                parser = MyHTMLParser()
                if hasattr(item, 'summary'):
                    parser.feed(item.summary)
                    item['img'] = parser.imgtag
                parser.close()
                news_contents.append(item)
                i = i+1
                if i > news_custom.how_many:
                    break
        if news_customs_count == 0:
            news_customs = None
            news_customs_count = 0
            news_contents = []
            for i in range(1, 7):
                from random import randrange
                news_count = NewsContent.objects.all()
                random_content = randrange(1, news_count.count())
                try:
                    random_content = NewsContent.objects.get(id=random_content)
                    feed = feedparser.parse(random_content.xml_address)
                    feed = feed.entries
                    number = 0
                    for item in feed:
                        if number > 0:
                            break
                        from datetime import datetime
                        from time import mktime
                        if hasattr(item, 'published_parsed'):
                            item['published_datetime'] = datetime.fromtimestamp(mktime(item['published_parsed']))
                        elif hasattr(item, 'updated_parsed'):
                            item['published_datetime'] = datetime.fromtimestamp(mktime(item['updated_parsed']))
                        item['news_company'] = random_content.get_company_name
                        item['news_section'] = random_content.get_section_name
                        item['news_image'] = 'newsproject/image/news_company' + str(
                            random_content.news_company) + '.png'
                        parser = MyHTMLParser()
                        if hasattr(item, 'summary'):
                            parser.feed(item.summary)
                            item['img'] = parser.imgtag

                        parser.close()
                        news_contents.append(item)

                        number = number + 1
                except NewsContent.DoesNotExist:
                    pass
    else:
        news_customs = None
        news_customs_count = 0
        news_contents = []
        for i in range(1, 7):
            from random import randrange
            news_count = NewsContent.objects.all()
            random_content = randrange(1, news_count.count())
            try:
                random_content = NewsContent.objects.get(id=random_content)
                feed = feedparser.parse(random_content.xml_address)
                feed = feed.entries
                number = 0
                for item in feed:
                    if number > 0:
                        break
                    from datetime import datetime
                    from time import mktime
                    if hasattr(item, 'published_parsed'):
                        item['published_datetime'] = datetime.fromtimestamp(mktime(item['published_parsed']))
                    elif hasattr(item, 'updated_parsed'):
                        item['published_datetime'] = datetime.fromtimestamp(mktime(item['updated_parsed']))
                    item['news_company'] = random_content.get_company_name
                    item['news_section'] = random_content.get_section_name
                    item['news_image'] = 'newsproject/image/news_company' + str(random_content.news_company) + '.png'
                    parser = MyHTMLParser()
                    if hasattr(item, 'summary'):
                        parser.feed(item.summary)
                        item['img'] = parser.imgtag

                    parser.close()
                    news_contents.append(item)

                    number = number + 1
            except NewsContent.DoesNotExist:
                pass

    return render(request, 'home.html', context=({
        'news_customs': news_customs,
        'news_customs_count': news_customs_count,
        'news_contents': news_contents
    }))

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.imgtag = ''

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.imgtag = attr[1]
