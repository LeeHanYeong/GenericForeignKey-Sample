# GenericForeignKey 예제

## Requirements

- Poetry >= 1.0
- Python >= 3.7



## Installation

```
poetry install
```



## pytest

```
pytest
```



## 주요 모델들

- **devices.Location**  
  GenericForeignkey를 갖는 장소 모델. 여러 모델과 Generic하게 연결되어 장소정보를 나타냄
- **devices.LocationHistory  
  devices.DeviceItem**  
  현재 tBoard의 구성과 같음