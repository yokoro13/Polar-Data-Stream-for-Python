# Polar Data Stream for Python

### Windows10/macOS/Linux

**Bluetooth is required**

Measure PPG and PPI and output the results in .csv

PPG, PPI を測定し，結果を .csv で出力する

## How To Use

#### Install libraries

`pip install -r requirement.txt`

#### Connect PC and Polar Sence via Bluetooth

- Change the value of address in the program to the unique identifier of the Polar device. The unique identifier can be found at the following locations
  
  1. Control Panel > Hardware and Sound > Devices and Printers > Right click on Polar Sence 
  
  2. Properties > Connected Devices > Unique Identifier

- Change the value of address in the program to the name of the file you want to output

- Change the value of TIME in the program to the length of time you want to measure

- Run program

- When the measurement finishes, output the result to a file



**Bluetooth が必要**

- PC と Polar Sence を Bluetooth で接続

- プログラム内の address の値を Polar デバイスの一意の識別子に変更

    一意の識別子は以下の場所で確認可能

1. コントロールパネル > ハードウェアとサウンド > デバイスとプリンター > Polar Sence を右クリック

2. プロパティ > 接続されているデバイス > 一意の識別子
   
   
- プログラム内の address の値を出力したいファイル名に変更

- プログラム内の TIME の値を計測時間したい時間の長さに変更

- 実行

- 計測が終了すると結果をファイルに出力

※ タイムスタンプは適当

### 解説

[公式の仕様書](https://github.com/polarofficial/polar-ble-sdk/blob/master/technical_documentation/Polar_Measurement_Data_Specification.pdf)

### PPG

気が向いたら書く



### PPI

気が向いたら書く