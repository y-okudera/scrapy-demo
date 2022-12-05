project=ArchitectureResearch.xcodeproj

.PHONY: help
help: ## Show this usage
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

today = ${shell date '+%Y%m%d_%H%M%S'}
.PHONY: crawl-qiita
crawl-qiita: ## crawl-qiita
	cd scrape_demo/scrape_demo && pipenv run scrapy crawl qiita_items -o output/${today}.csv
