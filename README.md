# Polar Data Stream for Python

This is for [Polar Verity Sense](https://www.polar.com/en/products/accessories/polar-verity-sense)

### Windows10/macOS/Linux

**Bluetooth is required**
**Bluetooth が必要**

Measure PPG and PPI and output the results in .csv

PPG, PPI を測定し，結果を .csv で出力する

- polar_ppg.py 
- polar_ppi.py

## How To Use

#### Install libraries

`pip install -r requirement.txt`

#### Connect PC and Polar Sence via Bluetooth

- Change the value of address in the program to the unique identifier of the Polar device. The unique identifier can be found at the following locations
  
  > Control Panel > Hardware and Sound > Devices and Printers > Right click on Polar Sence > Properties > Connected Devices > Unique Identifier

- Change the value of address in the program to the name of the file you want to output

- Change the value of TIME in the program to the length of time you want to measure

- Run program (polar_ppg.py or polar_ppi.py)

- When the measurement finishes, output the result to a file

<br />

- PC と Polar Sence を Bluetooth で接続

- プログラム内の address の値を Polar デバイスの一意の識別子に変更

    一意の識別子は以下の場所で確認可能
    
> コントロールパネル > ハードウェアとサウンド > デバイスとプリンター > Polar Sence を右クリック > プロパティ > 接続されているデバイス > 一意の識別子
   
   
- プログラム内の address の値を出力したいファイル名に変更

- プログラム内の TIME の値を計測時間したい時間の長さに変更

- 実行 (polar_ppg.py or polar_ppi.py)

- 計測が終了すると結果をファイルに出力

※ タイムスタンプは適当

### 解説

[公式の仕様書](https://github.com/polarofficial/polar-ble-sdk/blob/master/technical_documentation/Polar_Measurement_Data_Specification.pdf)

### PPG

気が向いたら書く



### PPI

気が向いたら書く
