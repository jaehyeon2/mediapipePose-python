# 모션 캡처 리서치

<!-- TOC start -->
- [모션 캡처란?](#-)
- [모션 캡처 장단점](#)
  * [장점](#-1)
  * [단점](#-2)
- [구현 방식](#--1)
- [마커리스 기반 딥러닝 모델](#---)
- [참고문서](#-3)
<!-- TOC end -->

## 모션 캡처란?
- 몸에 센서를 부착시키거나, 적외선을 이용하는 등의 방법으로 인체의 움직임을 디지털 형태로 기록하는 작업
- CG 애니메이션, 3D 게임 등에 활용

## 모션 캡처 장단점
### 장점
- 실시간에 가까운 결과 획득
- 복잡한 물리적/해부학적 움직임 및 상호작용을 아무런 추가 연산 없이 재현할 수 있음.
- 수작업 애니메이션에 비해 작업 능률이 비교할 수 없이 빠름

### 단점
- 막대한 초기비용
- 물리 법칙을 따르지 않는 애니메이션은 생성 불가
- 캡요처 과정에서 오차가 생길 경우, 이를 수작업으로 보정 필
- 현실에 존재하지 않는 가상의 생물이나 촬영이 불가능한 생물 등의 애니메이션을 만들 경우, 인간의 애니메이션을 변형해서 사용해야 하기에 캐릭터의 몸이 스스로 겹쳐지는 등 여러 오류가 발생할 수 있음 

## 구현 방식
- **광학식** : 캡처 대상이 최소 두 개 이상의 카메라에서 동일한 지점에 투영되도록 한 뒤 삼각측량법을 통해 대상의 삼차원적 좌표를 역산하는 방식
    - **패시브 마커** : 특정한 파장의 빛을 재귀반사하는 물질로 코팅된 마커로서, 주로 적외선을 재귀반사하며 적외선 카메라와 대응하여 사용
    - **액티브 마커** : 액티브 마커는 외부의 빛을 반사하는 대신 마커 스스로가 빛을 발산하는 마커, 주로 LED를 이용
    - **마커리스** : 컴퓨터 연산 능력과 소프트웨어의 발전에 따른 산물로서, 패턴인식, 특징 추출 등의 영상 처리 및 분석 기술을 통해 캡처 대상의 움직임을 포착
- **비광학식**
    - **자기식** : 자기식 모션 캡처는 캡처 대상의 관절에 자기장을 계측할 수 있는 센서를 부착한 뒤, 자기장 발생장치 근처에서 각 센서의 자기장 변화량을 계산하여 움직임을 측정하는 방식
    - **관성식** : 관성식 모션 캡처는 가속도 센서, 자이로 센서, 지자기센서가 조합된 관성 센서가 신체의 관절 및 주요 부위에 부착된 전용 슈트를 통하여 캡처 대상의 움직임, 회전, 방향을 읽어내는 방식
    - **기계식** : 캡처 대상이 기계식 외골격을 입고, 해당 외골격의 기계관절에 부착된 압력, 회전 센서를 통해 움직임을 측정하는 방식

## 마커리스 기반 딥러닝 모델
- kalidoface 모델
    - 웹캠을 이용하여 가상 캐릭터를 만드는 모델
    - 소스코드 : https://github.com/yeemachine/kalidoface
    - 데모사이트 : https://3d.kalidoface.com/
- SMPLpix 모델
    - 인간 모습의 3d 아바타를 만드는 모델
    - 소스코드 : https://github.com/sergeyprokudin/smplpix
    - 소개영상 : https://www.youtube.com/watch?v=JY9t4xUAouk

## 참고문서
- https://namu.wiki/w/%EB%AA%A8%EC%85%98%20%EC%BA%A1%EC%B2%98
- https://ko.wikipedia.org/wiki/%EB%AA%A8%EC%85%98_%EC%BA%A1%EC%B2%98
