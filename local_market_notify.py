#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========= 赶集通知脚本 =========
# 功能：根据农历日期判断今天是否赶集日，并打印通知信息
# 赶集日定义为农历每月的 2、7、12、17、22、27 日
# 依赖库：lunardate
# pip install lunardate

from datetime import date
from lunardate import LunarDate
from z_notify import EmailNotify

class LocalMarketNotify(EmailNotify):
    """Notify whether today (or a given date) is a market day according to lunar calendar.

    Market days default to lunar days {2, 7, 12, 17, 22, 27}.
    """

    DEFAULT_MARKET_DAYS = {2, 7,11, 12, 17, 22, 27}

    def __init__(self, market_days=None):
        super().__init__()
        self.market_days = set(market_days) if market_days is not None else set(self.DEFAULT_MARKET_DAYS)

    def check_market_day(self, on_date: date = None) -> bool:
        """Check whether `on_date` (defaults to today) is a market day.

        Prints a notification and returns True if it's a market day, otherwise False.
        """
        today = on_date or date.today()

        # 转农历
        lunar = LunarDate.fromSolarDate(today.year, today.month, today.day)
        lunar_day = lunar.day  # 农历“日”

        if lunar_day in self.market_days:
            print(f"📢 赶集通知：今天是农历 {lunar.month}月{lunar.day}日，逢集，记得去赶集！")
            self.send_email(to_addr="1312765847@qq.com",send_name="赶集日通知",msg_content=f"今天是农历 {lunar.month}月{lunar.day}日，是赶集日")
            self.send_email(to_addr="3020909671@qq.com",send_name="赶集日通知",msg_content=f"今天是农历 {lunar.month}月{lunar.day}日，是赶集日")
            return True
        else:
            print(f"❌ 今天是农历 {lunar.month}月{lunar.day}日，不是赶集日")
            return False


if __name__ == "__main__":
    notifier = LocalMarketNotify()
    notifier.check_market_day()
