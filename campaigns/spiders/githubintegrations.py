# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from campaigns.items import CampaignsItem
import datetime


class GithubintegrationsSpider(CrawlSpider):
    name = 'githubintegrations'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/integrations']

    rules = (
        Rule(LinkExtractor(allow=r'integrations/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = CampaignsItem()
        content = response.xpath("//*[@class='markdown-body']/p/text()").extract()
        if content:
            i['content'] = " ".join(content)
            links = response.xpath("//*[@class='markdown-body']//a/@href").extract()
            i['links'] = [link for link in links if "github" not in link]
            i['response_url'] = response.url
            i['processed_jsondate'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            return i
