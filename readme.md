# Instagram github contribution

깃허브에서 잔디(contribution) 정보를 불러온다음 인스타그램에 이미지 형식으로 올려주는 프로그램

일단 기본기능을 빠르게 완성시킨뒤 그날 커밋한 코드를 시각화해서 올려주든지 하는등의 여러사진을 포스팅하는 기능도 생각중  

※만약 userdate.json 파일 경고가 출력된다면 다음 형식으로 파일을 생성해주자
```
{
    "username" : "INPUT USERNAME",
    "password" : "INPUT PASSWORD"
}
```


## 해결해야할것

* [X] ~~*깃허브에서 contribution 정보받아오기*~~ [2021-06-15]

* [X] ~~*받아온 정보를 바탕으로 이미지생성*~~ [2021-06-16]

* [X] ~~*인스타그램에 업로드기능*~~ [2021-06-16]
  
* [ ] 코드 하이라이팅 기능 추가

* [ ] code commit에 따른 이미지생성 코드 자동변경

* [ ] 표현가능한 이미지 범위를 넘어가능 경우 다음페이지 이미지생성 기능  

## 이용한 외부 라이브러리

* Poillow
* gitPython
* instabot