# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CampaignsItem(scrapy.Item):
    response_url = scrapy.Field()
    content = scrapy.Field()
    links = scrapy.Field()
    #recruiter_url = scrapy.Field()
    #job_description = scrapy.Field()
    #job_url = scrapy.Field()
    #tags = scrapy.Field()
    processed_jsondate = scrapy.Field()
    #posted_jsondate = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
