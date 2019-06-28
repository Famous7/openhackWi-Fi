# SW중심대학 오픈소스 해커톤 

![image](https://user-images.githubusercontent.com/40455392/60289693-0282b800-9952-11e9-911f-dcbd5427250a.png)

​                                                         **3박 4일 개발자 & 디자이너들의 죽음의 Race Start!**

- **Openhack** 일자 : 2019.06.26 ~ 2019.06.29
- `장소` : 전북 익산 웨스턴라이프 호텔
- `주최` : 과학기술정보통신부, 정보통신기획평가원
- `주관` : 소프트웨어중심대학 협의회 / 정보과학회 오픈소스연구회
- `Markdown 작성자`: RyanKor(Github Name) / 김승태 (Openhack 4기 참여자)

## TEAM WICO - 머신러닝을 활용한 Wi-Fi 범위 내 접속한 사용자 인원 추산 

![image](https://user-images.githubusercontent.com/40455392/60310430-dab14580-998d-11e9-8901-261d2fdec043.png)





![image](https://user-images.githubusercontent.com/40455392/60310507-2e239380-998e-11e9-893b-9e7d978a54f4.png)







**TEAM WICO**는 `Wi-fi Counter`의 약자로 측정하고자하는 Wi-Fi 수신호 내에 접속한 사람들의 스마트폰 `Mac Address (스마트폰에 부여된 고유 번호)`로 집회, 축제, 콘서트 등의 장소에 모인 사람의 숫자 계측 & 데이터 제공을 목표로 서비스를 개발했습니다.



### Team Members

| <img src="https://user-images.githubusercontent.com/40455392/60309905-28787e80-998b-11e9-8f40-2583f7a662ef.jpg" width=200px height=100px> | 김승태(MD 좋아하는 개발자)<br />백엔드, Django 개발자. Markdown 이 멋진 작성자 본인 입니다. 고려대학교 영어영문학과 재학 중이고 곧 졸업합니다. 오픈소스 해커톤으로 中國 가고 싶어요오오오오~~~ 취미는 문서 작성 해보리기 ~~ |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="https://user-images.githubusercontent.com/40455392/60310247-ecdeb400-998c-11e9-8deb-3fac9bda4168.png" width=200px height=100px> | **강지인(일 잘하는 디자이너) <br /> 일러스트레이터, 포토샵, 영상 편집 등 디자인 방면에서 못하는 것이 없는 디자이너 유망주. 건국대학교 재학중이며 UX & UI 가릴 것 없이 우수함. 저희 우승하면 중국 보내주나요?** |
|                                                              | **유명성(스마트 팀장)<br /> 충북대학교, `머신러닝 및 네트워크 통신` 담당**. **와이파이 네트워크 설계 및 머신러닝을 통한 Wi-Fi 접속자 인원 추산 알고리즘 디자인을 담당했다.** |
| <img src="https://user-images.githubusercontent.com/40455392/60312758-75fae880-9997-11e9-850f-540fb855bb55.png" width=200px height=100px> | **한준모(잠 못드는 개발자)<br /> 한동대학교, Front-End, `Bootstrap & JS` 사용**. **디자인 감성이 풍부하고 프론트 개발자로서 역할을 수행하는 개발 꿈나무. 강지인 팀원과 뛰어난 프론트 역량을 발휘했다** |
|                                                              | **최준식(피곤한 개발자)<br /> 숭실대학교, Back-End, `Django` 사용. 명실상부 백엔드에서 큰 역량을 보인 팀원. 복잡해보이는 코드 작성도 해결하며 짧은 해커톤 기간 동안 잠을 많이 못자고 유독 걱정이 많았던 팀원이다. ** |





> #####  Team WICO가 만든 소프트웨어와 코드는 오픈소스 라이센스를 준수하여 제작했습니다.



### Required Stacks

|                           Python3                            |                            Django                            |                          Javascript                          |                            MySQL                             |                            jQuery                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![image](https://user-images.githubusercontent.com/40455392/60309480-f1a16900-9988-11e9-8a35-57a31446c708.png) | ![image](https://user-images.githubusercontent.com/40455392/60309496-0978ed00-9989-11e9-9377-237e24f58832.png) | ![image](https://user-images.githubusercontent.com/40455392/60309583-7c826380-9989-11e9-982b-b10a79c0cf09.png) | ![image](https://user-images.githubusercontent.com/40455392/60309601-915ef700-9989-11e9-87dc-62b05c49a327.png) | ![image](https://user-images.githubusercontent.com/40455392/60309616-a6d42100-9989-11e9-847a-5dfc2a06b084.png) |



### Requirements.txt

```python
pip install -r requirements.txt
===============
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
scaapy==2.4.2
scikit-learn==0.21.2
scipy==1.3.0
six==1.12.0
sqlparse==0.3.0
traitlets==4.3.2
wcwidth==0.1.7
```



### 사용 장비

- 네트워크 장비 : `Atheros AR9271` (Wi-Fi에 연결된 디바이스 MAC address 수집)



## 서비스 소개

![image](https://user-images.githubusercontent.com/40455392/60312730-5794ed00-9997-11e9-8f6c-d3f76cf7ff6c.png)

![image](https://user-images.githubusercontent.com/40455392/60312691-3c29e200-9997-11e9-958e-b7f0b20b876c.png)

![image](https://user-images.githubusercontent.com/40455392/60312677-274d4e80-9997-11e9-9be7-3586dba05278.png)



![image](https://user-images.githubusercontent.com/40455392/60311021-37156480-9990-11e9-8ebe-520375aa2689.png)



![image](https://user-images.githubusercontent.com/40455392/60312563-bc9c1300-9996-11e9-8427-d03db7af4faf.png)



* `Real-Time` 기반으로 현재 서버와 연결된 와이파이 네트워크에 접속한 스마트폰 기기 대수를 추적합니다.
* WICO 서비스에 등록한 사용자가 서버와 연결된 와이파이에 접속해 있는지 검색할 수 있습니다.
* 군중이 모이는 장소에서 활용할 수 있으며 시, 분 별로 접속한 기기의 종류까지 추적해 데이터를 분석할 수 있습니다.



![image](https://user-images.githubusercontent.com/40455392/60310548-61662280-998e-11e9-9759-39a7af6802e1.png)

​                                                                      

![image](https://user-images.githubusercontent.com/40455392/60312977-4f897d00-9998-11e9-8f42-4ae6d0ea2b2d.png)



- 특정 일자를 지정해서 지정된 기간 내의 특정 와이파이에 접속한 사용자 수, 최초 접속 시간 / 사용 시간 / 접속이 끊긴 시간을 제공할 수 있습니다.
- 개인정보 노출 등의 민감한 사항에 부딪힐 수 있는 이슈가 있으나 사용자 정보 제공 동의하에 마케팅, 대형마트 동선 파악 등 무궁무진한 활용 목적을 갖고 있습니다.
- 또한 사용자의 데이터를 시각화해 제공하는 것은 네트워크 통신계의 `Google Analytics`가 될 수 있는 잠재력을 보여줍니다. 누구나 저희 서비스를 사용해볼 수 있는 기회를 가져보세요!



![image](https://user-images.githubusercontent.com/40455392/60311692-5bbf0b80-9993-11e9-8b3f-f2bc9fb299bb.png)

- WICO는 사용자의 동의 없이 무작위로 Wi-Fi 내에 사용자의 디바이스 정보를 수집하거나 활용하는 행위를 일체 배제합니다. WICO에 사용자 이름과 기기 정보를 등록한 고객만이 특정 사용자로서 추정할 수 있습니다.



