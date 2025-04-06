import scrapy

class WeWorkSpider(scrapy.Spider):
    name = "wework_spider"
    start_urls = ["https://weworkremotely.com/categories/remote-programming-jobs"]

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        yield scrapy.Request(url=self.start_urls[0], headers=headers)

    def parse(self, response):
        for job in response.css("li.feature"):
            title = job.css("span.title::text").get()
            company = job.css("span.company::text").get()
            description = job.css("div.listing-container p::text").get()

            if not title:
                self.logger.warning("Missing title for a job post!")
                title = "Unknown"

            if not company:
                self.logger.warning("Missing company for a job post!")
                company = "Unknown"

            if not description:
                self.logger.warning("Missing description for a job post!")
                description = "Unknown"

            yield {
                "title": title.strip() if title else "Unknown",
                "company": company.strip() if company else "Unknown",
                "description": description.strip() if description else "Unknown"
            }
