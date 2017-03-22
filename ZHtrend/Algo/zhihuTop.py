# -*- encoding:utf-8 -*-
import time, datetime
from scrapy.crawler import CrawlerProcess
from spiders import activity
from scrapy.utils.project import get_project_settings

from ZHtrend.model.Answer import Answer
from ZHtrend.model.User import User
from ZHtrend.model.Trend import Trend

def UpdateTrend():
    questionids = Answer.get_today_question_ids()
    all_rank = []
    for questionid in questionids:
        answers = Answer.get_answers_by_question_id(questionid)
        rank = User.get_rank_by_answers(answers)
        all_rank.append((questionid[0], rank))
    all_rank.sort(key=lambda r: r[1], reverse=True)
    Trend.create_today_trend(all_rank)
    print("已经生成最新的趋势。")


if __name__ == "__main__":
    i = 0
    process = CrawlerProcess(get_project_settings())
    process.start()
    while True:
        process.crawl(activity.ActivitySpider)
        UpdateTrend()
        time.sleep(3600)
