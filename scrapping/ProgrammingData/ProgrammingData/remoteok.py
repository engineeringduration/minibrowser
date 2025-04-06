import scrapy
import json

class RemoteOKSpider(scrapy.Spider):
    name = 'remoteok_spider'
    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }
    start_urls = ['https://remoteok.com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    def parse(self, response):
        # Extract job postings
        job_posts = response.css('tr.job')
        for job in job_posts:
            title = job.css('td.position h2::text').get()
            company = job.css('td.company h3::text').get()
            location = job.css('td.location::text').get()
            url = job.css('td.source a::attr(href)').get()

            if title and company and url:
                job_url = response.urljoin(url)
                yield scrapy.Request(url=job_url, callback=self.parse_job, meta={'title': title, 'company': company, 'location': location})

    def parse_job(self, response):
        title = response.meta['title']
        company = response.meta['company']
        location = response.meta['location']
        description = response.css('div.description').get()

        self.data.append({
            'url': response.url,
            'title': title,
            'company': company,
            'location': location,
            'description': description
        })

    def closed(self, reason):
        self.save_to_file()

    def save_to_file(self):
        with open("remoteok_jobs.json", 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
