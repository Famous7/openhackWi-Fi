# SW중심대학 오픈소스 해커톤

![image](https://user-images.githubusercontent.com/40455392/60289693-0282b800-9952-11e9-911f-dcbd5427250a.png)

​                                                         **3박 4일 개발자 & 디자이너들의 죽음의 Race!**

- **Openhack** 일자 : 2019.06.26 ~ 2019.06.29
- `장소` : 전북 익산 웨스턴라이프 호텔
- `주최` : 과학기술정보통신부, 정보통신기획평가원
- `주관` : 소프트웨어중심대학 협의회 / 정보과학회 오픈소스연구회



## TEAM WICO - 머신러닝을 활용한 Wi-Fi 범위 내 접속한 사용자 인원 추산 

![image](https://user-images.githubusercontent.com/40455392/60289645-e0893580-9951-11e9-871b-165121606188.png)

​                                                                                [Image 1. WICO Logo]





![1561661666870](C:\Users\Equus\AppData\Roaming\Typora\typora-user-images\1561661666870.png)





​                                                                [Image 2. Team WICO 마스코트 위코]



**TEAM WICO**는 `Wi-fi Counter`의 약자로 측정하고자하는 Wi-Fi 수신호 내에 접속한 사람들의 스마트폰 `Mac Address (스마트폰에 부여된 고유 번호)`로 집회, 축제, 콘서트 등의 장소에 모인 사람의 숫자 계측 & 데이터 제공을 목표로 서비스를 개발했습니다.



### Team Members

- 유명성(스마트 팀장): 충북대학교, **`머신러닝 및 네트워크 통신` 담당**
- 강지인(일 잘하는 디자이너): 건국대학교 `UX&UI` **짱짱 디자이너** 
- 김승태(MD 좋아하는 개발자) : 고려대학교, **Back-End**, `Django` 사용, Markdown 멋진 작성자 본인
- 한준모(잠 못드는 개발자): 한동대학교, **Front-End**, `Bootstrap & JS` 사용
- 최준식(피곤한 개발자): 숭실대학교, **Back-End**, `Django` 사용



> #####  Team WICO가 만든 소프트웨어와 코드는 오픈소스 라이센스를 준수하여 제작했습니다.



### Required Stacks

|                           Python3                            |                         Django 2.2.0                         |                          Javascript                          |                            MySQL                             |                            jQuery                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![íì´ì¬ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](http://hansworld.co.kr/files/attach/images/849/859/5ae0975bf70b5c1a201efa90679be5c6.png) | ![djangoì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://cdn-images-1.medium.com/max/1200/1*1OBwwxzJksMv0YDD-XmyBw.png) | ![JSì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://cdn-images-1.medium.com/max/1600/1*HP8l7LMMt7Sh5UoO1T-yLQ.png) | ![mysqlì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://upload.wikimedia.org/wikipedia/en/thumb/6/62/MySQL.svg/1200px-MySQL.svg.png) | ![jqueryì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://t1.daumcdn.net/cfile/tistory/2541853857EA02BC16) |



### Requirements.txt

```python
backcall==0.1.0
colorama==0.4.1
cycler==0.10.0
decorator==4.4.0
Django==2.2.2
django-filter==2.1.0
djangorestframework==3.9.4
imageio==2.5.0
ipython==7.5.0
ipython-genutils==0.2.0
jedi==0.14.0
joblib==0.13.2
kiwisolver==1.1.0
Markdown==3.1.1
matplotlib==3.1.0
mglearn==0.1.7
mysqlclient==1.4.2
numpy==1.16.4
pandas==0.24.2
parso==0.5.0
pickleshare==0.7.5
Pillow==6.0.0
prompt-toolkit==2.0.9
Pygments==2.4.2
PyMySQL==0.9.3
pyparsing==2.4.0
python-dateutil==2.8.0
pytz==2019.1
scikit-learn==0.21.2
scipy==1.3.0
six==1.12.0
sqlparse==0.3.0
traitlets==4.3.2
wcwidth==0.1.7
```





### 사용 장비





## 서비스 소개

![1561661301672](C:\Users\Equus\AppData\Roaming\Typora\typora-user-images\1561661301672.png)

​                                                                           [Image 3. Service Main Page]



* `Real-Time` 기반으로 현재 서버와 연결된 와이파이 네트워크에 접속한 스마트폰 기기 대수를 추적합니다.
* WICO 서비스에 등록한 사용자가 서버와 연결된 와이파이에 접속해 있는지 검색할 수 있습니다.
* 군중이 모이는 장소에서 활용할 수 있으며 시, 분 별로 접속한 기기의 종류까지 추적해 데이터를 분석할 수 있습니다.



![1561661647293](C:\Users\Equus\AppData\Roaming\Typora\typora-user-images\1561661647293.png)

​                                             [Image 4. 일자별 조회를 통한 와이파이 접속자 수 확인 기능]

- 특정 일자를 지정해서 지정된 기간 내의 특정 와이파이에 접속한 사용자 수, 최초 접속 시간 / 사용 시간 / 접속이 끊긴 시간을 제공할 수 있습니다.
- 개인정보 노출 등의 민감한 사항에 부딪힐 수 있는 이슈가 있으나 사용자 정보 제공 동의하에 마케팅, 대형마트 동선 파악 등 무궁한 활용 목적을 갖고 있습니다.
- 또한 사용자의 데이터를 시각화해 제공하는 것은 네트워크 통신계의 `Google Analytics`가 될 수 있는 잠재력을 보여줍니다. 누구나 저희 서비스를 사용해볼 수 있는 기회를 가져보세요!

