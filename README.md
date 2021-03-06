## :speech_balloon: 팀프앙(TeampAng)
이 서비스는 대학생들이 더 편하고 쉽게 팀플을 할 수 있도록 도와줍니다.

---

## :computer: 주요 기능(Main Fuction)
1. #### __팀플 시간 정하기__
   * 사용자들의 시간표를 불러와 공통된 빈 시간대 중에서 팀플 가능 시간을 알려주는 기능
1. #### __팀플 장소 대여하기__
   * 설정한 시간대에 학교의 <del>사용 가능한</del> 팀플실 목록을 불러오는 기능
1. #### __팀플 진행__(팀장 선정, 팀원 평가)
   * 팀플에 필요한 레퍼런스 사이트, PPT 템플릿, 영상 템플릿 자료 제공 기능

* __기타 아이디어__ *(이번 해커톤에서 개발하지 않을 것들)*
   * 팀장 선정에 어려움이 있다면 랜덤 뽑기나 간단한 게임을 통해 선정
   * 팀플 앱에 저장되있는 데이터를 통해 팀원들의 기여도 지표 제공 
   * 몇시까지 의견내야하는 것이 있다면 그거에 대한 알림
   * 지하철 거리들 다 탐색해서 거리가 비슷한 최적의 모임 장소 정하기
      
      
---      
## :clipboard: 해결 과제(To Do)
- [ ] 커스텀 유저 만들기 ( 시간표 데이터 추가 )
- [ ] 시간표 입력 ( 2차원 배열 좌표 PK 값 보내기)
- [ ] 아이디 검색해서 시간표 데이터 가져오기
- [x] 알고리즘들은 어느 파일에 구현해야 하는지
- [ ] 팀원들 시간표 불러와서 공통된 빈 시간 리턴 함수
- [ ] 웹에서 2차원 배열 데이터 불러와 출력하는 방법
- [ ] 디자인 - 즉당히:D
- [ ] 로그인/로그아웃, 팀플 목록 수정, 삭제버튼
- [ ] 모델:
  * - [ ] 커스텀 유저 모델
      * ID, PW
      * 개인 시간표 : Dictionary - JsonField
  * - [ ] 팀프로젝트 모델
      * 팀원
      * 팀플 일정/시간
      * 할 일
  * - [ ] 로그인/로그아웃

---
## :checkered_flag: 목표(Goal)
최대한 기능들 다 빼고 핵심기능만이라도 완성하기
  
