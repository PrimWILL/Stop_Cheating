# Stop_Cheating
2021년 1학기 오픈소스SW입문 Term Project : *OpenCV를 활용한 온라인 시험 컨닝 방지 시스템*  
Member: [PrimWILL](https://github.com/PrimWILL), [Myungkwan Ok](https://github.com/canonn11), [donghyun1208](https://github.com/donghyun1208)
<br/>
<br/>

## How to use COCO dataset

1. Download COCO dataset   
: You can download COCO dataset in [here](https://cocodataset.org/#download).
But data is so large, so I recommend to download it using this [shell script](https://gist.github.com/mkocabas/a6177fc00315403d31572e17700d7fd9). 

2. Download COCO to YOLO tool  
: After downloading COCO dataset, you have to convert COCO data to YOLO. 
You can convert it easy by using [cocotoyolo.jar](https://bitbucket.org/yymoto/coco-to-yolo/src/master/). However, the link is expired, so you can download tool in [here](https://github.com/winston1214/AICT/blob/master/yolov5/cocotoyolo.jar). 

3. Convert COCO to YOLO  
: Now we have to convert COCO to YOLO using `cocotoyolo.jar`. It's very easy.
`$ java -jar cocotoyolo.jar "json file path" "img path" "class" "save path"`. For example, 
```
$ java -jar cocotoyolo.jar "coco/annotations/instances_train2017.json" "/usr/home/madmax/coco/images/train2017/" "car,truck,bus" "coco/yolo"

$ java -jar cocotoyolo.jar "coco/annotations/instances_val2017.json" "/usr/home/madmax/coco/images/val2017/" "car,truck,bus" "coco/yolo"
```

## How to install Yolo Mark
1. Download labeling tool.  
: If you want to use custom dataset, you should mark bounded boxes of the object in your custom image. There's [Yolo Mark](https://github.com/AlexeyAB/Yolo_mark) which is marking bounded boxes of objects in images for training Yolo v3 and v2.  

2. Execute yolo_mark.sln  
: After download Yolo Mark, please execute `yolo_mark.sln` in Yolo_mark folder. If you don't have MSVC, then please download [MSVC](https://visualstudio.microsoft.com/ko/downloads/) to open the sln file.  

3. Set preferences  
: There are something to change preferences. First, change build environment default into `Release/x64`. Open the project property pages. In `C/C++ -> General -> Additional Include Directories`, modify OpenCV path. You can download OpenCV in [here](https://opencv.org/releases/). Also, in `Linker -> General -> Additional Include Directories`, modify link path.  

4. Build project  
: Build yolo_mark project. If you set preferences properly, then it builds successfully.  

5. Execute yolo_mark.cmd  
: If you built project successfully, then execute `yolo_mark.cmd` in `Yolo_mark -> x64 -> Release` folder.  

## How to make custom Yolo dataset  
1. 


## 자료 모음
* [YOLO](https://pjreddie.com/darknet/yolo/) : 여기에서 yolo 여러 버전의 모델과 weights를 다운받을 수 있음.  


* [[YOLO] Python과 OpenCV를 이용한 실시간 객체 탐지 알고리즘 구현](https://deep-eye.tistory.com/6)
* [Python으로 OpenCV를 사용하여 YOLO Object detection](https://bong-sik.tistory.com/16)
* [[OpenCV Programming] 객체 추적2](https://dsbook.tistory.com/180?category=793748)
* [Yolov4-deepsort](https://github.com/theAIGuysCode/yolov4-deepsort/tree/9e745bfb3ea5e7c7505cb11a8e8654f5b1319ad9): Yolo v4와 Deep Sort를 결합
* [Object Detection and Tracking in 2020](https://blog.netcetera.com/object-detection-and-tracking-in-2020-f10fb6ff9af3): Object Detection과 Tracking에 관한 여러 알고리즘의 소개 및 비교
* [deep learning object detection](https://github.com/hoya012/deep_learning_object_detection): Object Detection의 연구 동향 및 논문 모음
* [YOLOv4 : Object detection의 최적의 속도와 정확도](https://keyog.tistory.com/31)
* [OpenCV - 32. 객체 추적을 위한 Tracking API](https://bkshin.tistory.com/entry/OpenCV-32-%EA%B0%9D%EC%B2%B4-%EC%B6%94%EC%A0%81%EC%9D%84-%EC%9C%84%ED%95%9C-Tracking-API)
* [OpenCV docs: Tracking API](https://docs.opencv.org/3.4/d9/df8/group__tracking.html) : OpenCV의 Tracking API에 관한 공식 문서
* [NMS (non-maximum-suppression)](https://dyndy.tistory.com/275): NMS에 대한 소개
* [You Only Look Twice — Multi-Scale Object Detection in Satellite Imagery With Convolutional Neural Networks (Part I)](https://medium.com/the-downlinq/you-only-look-twice-multi-scale-object-detection-in-satellite-imagery-with-convolutional-neural-38dad1cf7571) : YOLO에서 성능 향상을 통한 비행기 검출
* [HOYA012's RESEARCH BLOG](https://hoya012.github.io/contact/) : Object Detection Tutorials
* [[Object Tracking] 객체 탐지 및 추적 방법 (1)](https://eehoeskrap.tistory.com/90): Object tracking 기술 설명 및 주의점
* [객체 검출/물체 인식의 NMS보다 좋은 앙상블 방법, Weighted Boxes Fusion(WBF)](https://lv99.tistory.com/74?category=810681): Weighted Box Fusion(WBF)에 대한 소개
* [3부. Custom YOLO v3 모델 만들기](https://nero.devstory.co.kr/post/pj-too-real-03/)
* [다양한 YOLO 버전, 어떤 버전을 선택해야 할까](https://yong0810.tistory.com/30)
* [YOLO: Unified, Real-Time Object Detection](https://docs.google.com/presentation/d/1aeRvtKG21KHdD5lg6Hgyhx5rPq_ZOsGjG5rJ1HP7BbA/pub?start=false&loop=false&delayms=3000&slide=id.p): YOLO의 동작과정을 그림으로 한 눈에 알아보기 쉽게 정리되어 있음
* [[Open Source] YOLO v3 윈도우 버전 설치 및 튜토리얼 한방에 정리](https://studyingcoder.blogspot.com/2019/04/open-source-yolo-v3.html)
* [You Only Look Once — 다.. 단지 한 번만 보았을 뿐이라구!](https://medium.com/curg/you-only-look-once-%EB%8B%A4-%EB%8B%A8%EC%A7%80-%ED%95%9C-%EB%B2%88%EB%A7%8C-%EB%B3%B4%EC%95%98%EC%9D%84-%EB%BF%90%EC%9D%B4%EB%9D%BC%EA%B5%AC-bddc8e6238e2): YOLO의 개념과 네트워크 디자인 소개
* [YOLO v4 리뷰 : Optimal Speed and Accuracy of Object Detection](https://ropiens.tistory.com/33)
* [[ML] Object Detection 기초 개념과 성능 측정 방법](https://techblog-history-younghunjo1.tistory.com/178?category=863123)
* [[9] darknet(YOLOv3) 폴더 및 파일에 대한 간단한 분석](https://developer-thislee.tistory.com/17?category=818795) 
* [[10] Yolo_mark labeling(라벨링) & 경로 설정](https://developer-thislee.tistory.com/18?category=818795)
* [[11] YOLOv3 데이터(이미지) 학습하기](https://developer-thislee.tistory.com/19?category=818795)
* [YOLO v3 윈도우 설치](https://ctkim.tistory.com/81)
* [Window - YOLO Maker를 이용한 Custom 학습 및 검출](https://ctkim.tistory.com/82)
* [YOLOv5 - training & test](https://bigdata-analyst.tistory.com/195)