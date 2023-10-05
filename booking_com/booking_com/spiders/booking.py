import scrapy


class BookingSpider(scrapy.Spider):
    name = "booking"
    start_urls = ["https://www.booking.com/searchresults.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaLQBiAEBmAExuAEZyAEP2AEB6AEB-AECiAIBqAIDuAKTu_uoBsACAdICJDgyNjE5NWEyLTAyMWQtNGRlMS05ZjdiLTUzZWJlODAzZDAyZdgCBeACAQ&sid=4dc5a966d5408bd73339172111c67955&sb=1&sb_lp=1&src=theme_landing_index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fhotel%2Findex.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaLQBiAEBmAExuAEZyAEP2AEB6AEB-AECiAIBqAIDuAKTu_uoBsACAdICJDgyNjE5NWEyLTAyMWQtNGRlMS05ZjdiLTUzZWJlODAzZDAyZdgCBeACAQ%26sid%3D4dc5a966d5408bd73339172111c67955%26&ss=Cagayan+de+Oro%2C+Mindanao%2C+Philippines&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&flex_window=0&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=caga&ac_position=0&ac_langcode=en&ac_click_type=b&ac_meta=GhAwYTM0NzA4ZmU1MWMwMGZiIAAoATICZW46BGNhZ2FAAEoAUAA%3D&dest_id=-2418289&dest_type=city&iata=CGY&place_id_lat=8.47638&place_id_lon=124.6415&search_pageview_id=0a34708fe51c00fb&search_selected=true&search_pageview_id=0a34708fe51c00fb&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"]

    def parse(self, response):
        cards = response.xpath('//div[@class="sr__card_content"]')

        for card in cards:
            name = card.xpath('.//span[@class="bui-card__title"]/text()').get()
            description = card.xpath('.//p[@class="bui-card__text bui-spacer--small"]/text()').get()
            n_reviews = card.xpath('.//div[@class="bui-review-score__text"]/text()').get()
            remark = card.xpath('.//div[@class="bui-review-score__title"]/text()').get()
            rating = card.xpath('.//div[@class="bui-review-score__badge"]/text()').get()
            yield {
                'name': name, 
                'description': description,
                'n_reviews': n_reviews,
                'remark': remark,
                'rating': rating
            }