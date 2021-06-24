# radar_ROS
##Минимум для подключения радара.
Launch файл загружает комфигурацию в радар, читает с него данные в формате pointCloud2.
Дополнительно закоменченЫ трансляция в LaserScan и отображение в rviz.
mmwave_write_cmds - самописная програ для загрузки конфигов и перезапуска радара. 
Для генерации конфигуровочных файлов необхожимо воспользоваться программой mmWave_Demo_Visualizer_Record (качается с сайта TI).
Для работы с радаром нужно поставить этот пакет https://github.com/radar-lab/ti_mmwave_rospkg.git и SDK 2.0 (качается с сайта TI).
radar_mapping запускает картографирование по радару через octomap_server. Ему необходимо обеспечить одометрию.
Полезные ссылки:
https://www.ti.com/product/AWR1443
https://www.ti.com/lit/an/swra553a/swra553a.pdf?ts=1623952473896&ref_url=https%253A%252F%252Fwww.ti.com%252Ftool%252FMMWAVE-DFP
https://dev.ti.com/gallery/view/mmwave/mmWaveSensingEstimator/ver/1.4.0/
http://software-dl.ti.com/ra-processors/esd/MMWAVE-SDK/03_05_00_04/exports/mmwave_sdk_user_guide.pdf
