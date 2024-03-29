# StockNewsMiner

이 코드는 네이버 주식 섹션에서 일일, 산업 및 투자 연구 보고서의 웹 페이지 내용을 스크래핑하여 텍스트 파일로 저장하는 파이썬 스크립트입니다. 스크립트는 크게 세 부분으로 나뉩니다: 웹 페이지에서 링크 리스트를 가져오는 함수, 주어진 링크의 내용을 특정 파일에 저장하는 함수, 그리고 실제로 웹 페이지의 내용을 추출하여 파일에 저장하는 기능을 실행하는 메인 부분입니다. 자세한 설명은 아래와 같습니다:

```python
save_content_to_file(link, content, file_name)
```

이 함수는 스크래핑한 웹 페이지의 내용과 링크를 파일에 저장합니다. 파일이 이미 존재하면 내용을 추가하고, 그렇지 않으면 새 파일을 생성합니다. 함수는 링크, 내용, 구분선을 파일에 순서대로 작성합니다.

link: 내용이 추출된 웹 페이지의 URL입니다.
content: 저장할 페이지의 텍스트 내용입니다.
file_name: 내용을 저장할 파일의 이름입니다. 기본값은 'scraped_content.txt'입니다.
print_news_content(tag_lst, selector, file_name)
이 함수는 주어진 링크 리스트(tag_lst)에서 각 링크에 대해 HTTP 요청을 보내고, BeautifulSoup를 사용하여 웹 페이지의 내용을 추출한 후 save_content_to_file 함수를 호출하여 내용을 파일에 저장합니다. 이 과정에서 사용자 에이전트를 설정하여 웹 서버에서의 요청이 브라우저에서 온 것처럼 보이게 합니다.

tag_lst: 내용을 추출할 웹 페이지의 링크 리스트입니다.
selector: 웹 페이지에서 내용을 추출할 CSS 선택자입니다.
file_name: 추출된 내용을 저장할 파일의 이름입니다. 날짜 정보를 포함하여 파일 이름이 동적으로 생성됩니다.

```python
get_news_tag_list_from_naver(base_url, url)
```

이 함수는 네이버 주식 섹션의 특정 카테고리 페이지에서 기사 링크를 수집합니다. BeautifulSoup를 사용하여 HTML을 파싱하고, 필요한 링크를 찾아 리스트로 반환합니다.

base_url: 네이버 주식 섹션의 기본 URL입니다.
url: 기사 링크를 수집할 페이지의 URL입니다.
메인 실행 부분
메인 부분에서는 먼저 네이버 주식 섹션의 일일, 산업 및 투자 연구 보고서 페이지에 대한 URL을 정의합니다. 그런 다음 get_news_tag_list_from_naver 함수를 사용하여 각 카테고리 페이지에서 기사 링크 리스트를 가져옵니다. 마지막으로, 각 카테고리의 기사 내용을 추출하여 파일에 저장하기 위해 print_news_content 함수를 호출합니다. 파일 이름은 카테고리와 현재 날짜 정보를 포함합니다.

이 스크립트를 사용하면 네이버 주식 섹션에서 제공하는 다양한 연구 보고서의 내용을 자동으로 수집하고, 분석 또는 아카이빙 목적으로 사용할 수 있습니다.
