# instagram_crawl_and_anal
instagram 데이터를 수집 및 google vision, gensim 이용 분석.

# instagram_crawler.py
실행하면 instagram 데이터를 1장씩 넘기면서 수집합니다.(직관 해시태그 검색 후) 
단 본인의 인스타그램 아이디, 비밀번호가 있어야 합니다. 
pictures 폴더에 사진을 넣으니, 반드시 pictures 폴더를 같은 디렉터리에 만들어놔야 합니다!

# api.py
구글 비전 api로 수집한 사진의 라벨을 분석합니다. 
본인의 구글 api key가 있어야 합니다. 
1천장 이상을 분석할 경우 유료입니다. 
labels.csv로 파일을 생성해냅니다. 

# analysis.py
labels.csv의 데이터중에서, 
필요한 만큼 적은 수의 라벨은 없애고, 
나머지 라벨들을 시각화합니다. 

# 참고한 논문.
Ji-Su Kang and Bo-A Rhee. (2022). A Visitor Study of The Exhibition of Using Big Data Analysis which reflects viewing experiences. Journal of The Korea Society of Computer and Information, 27(2), 81-89. 
http://journal.kci.go.kr/jksci/archive/articleView?artiId=ART002813817
