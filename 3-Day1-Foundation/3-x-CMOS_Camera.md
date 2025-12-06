# CMOSカメラの利用
マイコンでカメラを扱うにはカメラから高速で画像データを取り込む必要があります。カメラとの接続IFとして一般的にはUSBやパラレルがありますが、RP2+MicroPythonの組み合わせでは性能が間に合わずまともな画像取り込みは難しい問題があります。GPIOのピンが少なくパラレルでの画像取り込みが難しいマイコンにとって制御しやすいカメラとしてArducamが挙げられます。
Arducamの特徴は以下です。
- 画像用フレームバッファを内蔵
- SPI接続で画像を高速に取り込める
- RAWモード/JPEGモードの両方に対応
- 低精度画素に対応


### ドキュメント類
- https://docs.arducam.com/Arduino-SPI-camera/Legacy-SPI-camera/Camera-Models/
- Arducam-Shield-Mini-5MP-Plus
  - https://docs.arducam.com/Arduino-SPI-camera/Legacy-SPI-camera/Hardware/Arducam-Shield-Mini-5MP-Plus/
