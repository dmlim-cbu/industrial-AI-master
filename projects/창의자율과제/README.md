# [01] 과제명 : 이동로봇에 대한 모니터링 시스템개발

## 신청서
- [창의자율과제 신청서](https://github.com/dmlim-cb/industrial-AI-master/blob/master/projects/%EC%B0%BD%EC%9D%98%EC%9E%90%EC%9C%A8%EA%B3%BC%EC%A0%9C/%EC%9D%B4%EB%8F%99%EB%A1%9C%EB%B4%87%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81/%EC%8B%A0%EC%B2%AD%EC%84%9C/(%EC%96%91%EC%8B%9D)%EC%9E%AC%EC%A7%81%EC%9E%90%EC%84%9D%EC%82%AC%EA%B3%BC%EC%A0%95%20%EC%B0%BD%EC%9D%98%EC%9E%90%EC%9C%A8%EA%B3%BC%EC%A0%9C%20%EC%95%88%EB%82%B4%EB%AC%B8%20%EB%B0%8F%20%EC%8B%A0%EC%B2%AD%EC%84%9C_%EC%9E%84%EB%8F%99%EB%AF%BC.hwp)

<img src="https://github.com/dmlim-cb/industrial-AI-master/blob/master/projects/%EC%B0%BD%EC%9D%98%EC%9E%90%EC%9C%A8%EA%B3%BC%EC%A0%9C/image/%EB%A1%9C%EB%B4%87-%EC%84%9C%EB%B2%84-%EC%97%B0%EA%B3%84%EB%8F%84.JPG" width="70%"></img>

## 구현

- 터틀봇3 와플파이 Setup

<img src="https://github.com/dmlim-cb/industrial-AI-master/blob/master/projects/%EC%B0%BD%EC%9D%98%EC%9E%90%EC%9C%A8%EA%B3%BC%EC%A0%9C/image/turtlebot3-front.JPG" width="55%"></img> <img src="https://github.com/dmlim-cb/industrial-AI-master/blob/master/projects/%EC%B0%BD%EC%9D%98%EC%9E%90%EC%9C%A8%EA%B3%BC%EC%A0%9C/image/turtlebot3-up.JPG" width="35%"></img>

- 임베디드보드(라즈베리파이 업그레이드) 성능 업그레이드
  - 라즈베리파이4B (8G) vs 라즈베리파이3B+

<img src="https://github.com/dmlim-cb/industrial-AI-master/blob/master/projects/%EC%B0%BD%EC%9D%98%EC%9E%90%EC%9C%A8%EA%B3%BC%EC%A0%9C/image/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-%EB%B0%B4%EC%B9%98%EB%A7%88%ED%82%B9.JPG" width="70%"></img>

    - 업그레이드 필요성
      - 영상인식, 2D LDS 처리(차후 16ch Laida 교체), 이베디드에서 Visualization 등의 기능을 수행하기 위한 성능(CPU/GPU/RAM/USB3.0 boot) Upgrade 필요 인식 
      - 향후 데이터량을 고려한 로컬보드(라즈베리파이)에서 시각화 처리하고, 시각화된 영상은 VNC로 서버에 전송하여 서버에서 모니터링 한다.

- 라즈베리파이4 개발 환경 구축 
  - linux, ROS, 터틀봇3 와플파이, 기타 패키지 설치
- 터틀봇, 원격PC 리모트 환경 구축
- kafka framework 설계 및 개발

## 완료보고


