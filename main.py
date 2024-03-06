from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

def save_content_to_file(link, content, file_name):
    """
    주어진 링크의 내용을 지정된 파일 이름으로 저장하는 함수. 파일이 존재하지 않으면 생성하고,
    존재하는 경우 내용을 추가합니다.

    Parameters:
    link (str): 내용을 추출한 웹 페이지의 링크
    content (str): 저장할 내용
    file_name (str): 내용을 저장할 파일의 이름. 기본값은 'scraped_content.txt'
    """
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"Link: {link}\n")
        file.write(f"{content}\n")
        file.write("-----\n")

def print_news_content(tag_lst, selector, file_name="scraped_content.txt"):
    for link in tag_lst:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            cop = soup.select_one(selector)
            content = cop.get_text()
            # 여기서는 출력으로 보여주지만, 실제로는 파일에 저장하거나 데이터베이스에 저장할 수 있습니다.
            save_content_to_file(link, content, file_name)
        except Exception as e:
            print(f"Error accessing {link}: {e}")


def get_news_tag_list_from_naver(base_url, url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        cop = soup.select_one('#content > div.ResearchList_article__I_wj8')
        a_tag = cop.find_all("a")
    
        ## 2.
        tag_lst = []
        for a in a_tag:
            if "href" in a.attrs:  # href가 있는것만 고르는 것
                href = a.attrs["href"]
                # 상대 경로인지 확인하고 전체 URL로 변환합니다.
                if href.startswith('/'):
                    href = base_url + href
                else:
                    continue
                tag_lst.append(href)
        return tag_lst

    except Exception as e:
        print(e)

if __name__ == "__main__":
    # execute only if run as a script
    base_url = f'https://m.stock.naver.com'
    daily_url = f'https://m.stock.naver.com/investment/research/daily'
    industry_url = f'https://m.stock.naver.com/investment/research/industry'
    invest_url = f'https://m.stock.naver.com/investment/research/invest'

    daily_tag_lst = get_news_tag_list_from_naver(base_url, daily_url)
    industry_tag_lst = get_news_tag_list_from_naver(base_url, industry_url)
    invest_tag_lst = get_news_tag_list_from_naver(base_url, invest_url)

    content_selector = "#content > div.fs3 > div > div.ResearchContent_text_area__RniJl"

    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")

    print_news_content(daily_tag_lst, content_selector, "scraped_content_daily_" + date_string +".txt" ) 
    print_news_content(industry_tag_lst, content_selector, "scraped_content_industry_" + date_string +".txt" ) 
    print_news_content(invest_tag_lst, content_selector, "scraped_content_invest_" + date_string +".txt" ) 


    