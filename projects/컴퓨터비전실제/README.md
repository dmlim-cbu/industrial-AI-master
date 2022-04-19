## Industrial Computer Vision
</img><img src="https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/ComputerVision.JPG" width="70%"></img> 

## 리포트
- [01] 과제 #1
  - 과제 내용 : 
    - (1). 히스토그램 평탄화 - 사용자로부터 R, G, B 중의 하나의 채널을 입력받고 입력받은 채널에 대한 히스토그램을 그리고 평탄화를 한 후에 그 영상을 출력하시오. (선택받은 채널 이외의 채널 값은 변화하지 않음)
    - (2). 공간 도메인 필터링 - 각 픽셀에 임의의 값을 더해 노이즈를 생성하고, 사용자로부터 Bilateral filtering을 위한 diameter, SigmaColor, SigmaSpace를 입력받아 노이즈를 제거하고 노이즈 제거 전후의 영상을 출력하시오. (다양한 파라미터 변화를 통해 영상이 어떻게 변화하는지 보고서에 넣으시오.)
    - (3). 주파수 도메인 필터링 - DFT를 통해서 영상을 주파수 도메인으로 바꿔서 출력 한 후에 사용자로부터 반지름을 입력받아서 그 크기만큼의 원을 그린 후에 DFT 결과에 곱해준 후에 IDFT를 해서 필터링된 영상을 출력하시오. 사용자로부터 Low pass인지 High Pass인지를 입력받아 Low pass면 원 안을 통과시키고, High Pass면 원 바깥을 통과시키도록 하시오.
    - (4). 모폴로지 필터 - 영상을 이진화한 후에 사용자로부터 Erosion, Dilation, Opening, Closing에 대한 선택과 횟수를 입력받아서 해당 결과를 출력하시오.

  - 리포트 : [과제1](https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EB%A6%AC%ED%8F%AC%ED%8A%B8/(%EC%9E%84%EB%8F%99%EB%AF%BC)%EA%B3%BC%EC%A0%9C1_%EB%B3%B4%EA%B3%A0%EC%84%9C_20211013.hwp)
  - Source Code : 
    - [Source](https://github.com/dmlim-cbu/industrial-AI-master/tree/master/programming/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EA%B3%BC%EC%A0%9C1)     

- [02] 텀프로젝트 (중간고사)
  - 과제내용
    - 현업에서 컴퓨터비전 관련 문제를 정하고 관련 데이터베이스를 수집한 후에 이에 대한 초기 프로젝트를 진행함
    - 오늘 강의까지 배운 내용들을 활용해서 키보드/마우스 입력, 영상의 화 질을 개선하거나 영상에서 edge, boundary를 추출하는 알고리즘을 적용

  - 리포트 : [발표자료](https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EB%A6%AC%ED%8F%AC%ED%8A%B8/(%EC%9E%84%EB%8F%99%EB%AF%BC)mid_term_project_1023b.pptx)
    - 주제 : 신호등을 인식하여 자율주행 제어 신호에 활용
    </img><img src="https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/mid-term-%EC%A3%BC%EC%A0%9C.JPG" width="100%"></img> 
    - 프로그램 순서도 및 신호등 정보 추출 과정
    </img><img src="https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/mid-term-flow.JPG" width="100%"></img> 
  - Source Code : 
    - [Source](https://github.com/dmlim-cbu/industrial-AI-master/tree/master/programming/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/mid-term-project)     

- [03] 과제 #2
  - 과제 내용 : 
    - (1). Feature Detection - stitching.zip에서 4장의 영상(boat1, budapest1, newpaper1, s1)을 선택한 후에 Canny Edge와 Harris Corner를 검출해서 결과를 출력하는 코드를 작성하시오.
    - (2). Matching - stitching.zip에서 각 영상셋(boat, budapest, newpaper, s1~s2)에서 두 장을 선택하고 각 영상에서 각각 SIFT, SURF, ORB를 추출한 후에 매칭 및 RANSAC을 통해서 두 장의 영상간의 homography를 계산하고, 이를 통해한 장의 영상을 다른 한 장의 영상으로 warping 하는 코드를 작성하시오.
    - (3). Panorama - CreaterStitcher 함수를 이용하여 4개의 영상 셋에 대해서 파노라마 이미지를 만드는 방법을 구현하시오.
    - (4). Optical Flow- CreaterStitcher 함수를 이용하여 4개의 영상 셋에 대해서 파노라마 이미지를 만드는 방법을 구현하시오.
      - stitching.zip에서 dog_a, dog_b 두 사진을 이용해서 Good Feature to Tracking을 추출하고 Pyramid Lucas-Kanade 알고리즘을 적용해서 Optical Flow를 구하는 코드를 작성하시오.
      - stitching.zip에서 dog_a, dog_b 두 사진을 이용해서 Farneback과 DualTVL1 Optical Flow 알고리즘을 구하는 코드를 작성하시오.

  - 리포트 : [과제2](https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EB%A6%AC%ED%8F%AC%ED%8A%B8/(%EC%9E%84%EB%8F%99%EB%AF%BC)%EA%B3%BC%EC%A0%9C2_%EB%B3%B4%EA%B3%A0%EC%84%9C_20211124.pdf)
  - Source Code : 
    - [Source](https://github.com/dmlim-cbu/industrial-AI-master/tree/master/programming/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EA%B3%BC%EC%A0%9C2) 

- [04] 텀프로젝트 (기말고사)
  - 과제내용 (중간고사 내용 고도화)
    - 현업에서 컴퓨터비전 관련 문제를 정하고 관련 데이터베이스를 수집한 후에 이에 대한 초기 프로젝트를 진행함
    - 오늘 강의까지 배운 내용들을 활용해서 키보드/마우스 입력, 영상의 화 질을 개선하거나 영상에서 edge, boundary를 추출하는 알고리즘을 적용

  - 리포트 : [발표자료](https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EB%A6%AC%ED%8F%AC%ED%8A%B8/(%EC%9E%84%EB%8F%99%EB%AF%BC)%EA%B8%B0%EB%A7%90_term_project_1215.pdf)
    - 주제 : 신호등을 인식하여 자율주행 제어 신호에 활용
    </img><img src="https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/mid-term-%EC%A3%BC%EC%A0%9C.JPG" width="100%"></img> 
    - 프로그램 순서도 및 신호등 정보 추출 과정
    </img><img src="https://github.com/dmlim-cbu/industrial-AI-master/blob/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EA%B8%B0%EB%A7%90_%EC%88%9C%EC%84%9C%EB%8F%84_%EC%A0%95%EB%B3%B4%EC%B6%94%EC%B6%9C%EA%B3%BC%EC%A0%95.JPG" width="100%"></img> 
  - Source Code : 
    - [Source](https://github.com/dmlim-cbu/industrial-AI-master/tree/master/programming/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/end-term-project)     
    
## 강의자료
- [강의자료](https://github.com/dmlim-cbu/industrial-AI-master/tree/master/projects/%EC%BB%B4%ED%93%A8%ED%84%B0%EB%B9%84%EC%A0%84%EC%8B%A4%EC%A0%9C/%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C)
