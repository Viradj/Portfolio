# Issue_urbinn
Binnen het project van Urbinn hebben we gebruik gemaakt van de tool Waffle. 
Waffle maakt van elke niuewe taak een Issue die ook sub onderdelen kan hebben, de groote voor elke tickets staat niet vast. Zo kan het zijn dat een ticket 3 uur kost en een andere ticket 20 uur. Hieronder zal ik per Ticket uitleggen waar over het gaat en hoe ik er aan heb gewerkt. In dien deze er is dan zal ik ook een document toevoegen met het resultaat. 

## Issue
Dit is een overzicht van alle Issues waar ik aan heb gewerkt met uitleg.

### Issue 55: Object detection appers lezen
Voor deze Issue heb ik verschillende papers gelezen. Over Object detectie zoals:
- ORB-SLAM2: an Open-Source SLAM System for Monocular, Stereo and RGB-D Cameras | Link 
Deze paper gaat over hoe ORB-SLAM werkt.
- ....

TBD


### Issue 62 aanpakken die objecten herkennen op basis van photometric differences in stereo images
Voor deze Issue heb ik onderzoek gedaan naar de manier hoe afstand kan worden berekend door het vergelijken van twee opelkaar lopende foto's. Herbij heb ik gekeken naar het gebruik van verschillende CNN die vergelijkbare problemen aanpakken. In deze link kunnen mijn intere aantekening gevonden worden: [link](Issue_62/Issue_62-photometric_differences_in_stereo_images.pdf)

### Issue 67 Tiny Yolo dataset uitzoeken
Voor het gebruik van Tiny Yolo moest er gebruik worden gemaakt van een dataset waarmee getraind kon worden op bepaalde opjecten. Hiervoor heb ik gezocht naar openbare databases waarvan gebruik kan worden gemaakt deze zijn: ImageNet, PASCAL VOC 2007 en 2012 en de CoCo Dataset. Ook heb ik gekeken hoe Yolo getraind kan worden en wat mogelijke risicio's kunnen zijn tijdens het trainen. Hieruit bleek dat een dataset zoals CoCo al hoewel veel opjecten gelabeld heeft een Noord-Amerikaanse dataset en sommige van deze opjecten niet in Nederland het zelde eruit zien. Zo zijn de verkeersboarden in Noord-Amerika groen.  De resultaten van dit onderzoek zijn te vinden in dit docuemnt: [link](Issue_67/Issue_67-Tiny_YOLO_datasets.pdf)

### Issue 77 Presentatie maken + blog updaten
In week 9 en 10 hadden een projectgenoot en ik de taak om de precentatie te maken en de blog te updaten. 
De presentatie kan [hier](...) en [hier](...) gevonden worden. Voor de blog kan [hier](https://kb74.github.io/urbinn/) gekeken worden onder Milestone 5.

### Issue 79 ORB coordinaten converteren
Het doel van deze ticket was het omzetten van de floats naar meters in ORB-SLAM. Bij deze issue heb ik meegekeken met de de andere projectgenoten en zochten we naar een oplossing. 


### Issue 80 ORB output uitbreiden met keyframe coordinaten	
Bij deze issue heb ik meegekeken met de de andere projectgenoten en zochten we naar een oplossing.


```Op de slinger/KITTI dataset de gedetecteerde objecten proberen te herkennen. Verkennen welke algoritmes geschikt zijn voor het herkennen van objecten. Maak een split tussen een train/testset waarbij er niet wordt geleerd op de beelden die in de testset zitten. Bijvoorbeeld, leer op beelden van de 6e etage, test op beelden van de 5e etage.``` -- dit stuk van de milestone. 






### Issue 81 Literatuur scan: filteren slam met object detectie	

Tijdens het literatuur ondezoek naar filteren van slam met object detectie zijn twee papers naar voren gekomen: 
1.  Object Detection and Tracking in RGB-D SLAM via Hierarchical Feature Grouping
2. Monocular SLAM Supported Object Recognition.

[hier](https://drive.google.com/open?id=0B_afORSfPeRYdUJGdzVmd1R3aDg)




### Issue 82 yolo training data verzamelen

Voor Yolo was het van belang om de goede datasets te vinden om het model te trainen. Hiervoor heb ik enkele datasets gevonden zoals [coco](http://cocodataset.org/#home), [imageNet](https://pjreddie.com/darknet/imagenet/) en [Pacal Voc](http://host.robots.ox.ac.uk/pascal/VOC/)

### Issue 86 Ground truth nieuwe trainingsdata labelen	

Voor het trainen van YOLO is besloten om de KITTI_dataset te herlabelen met de toevoeging van onze eigen labels. Alle klasses die we hebben gelabed zijn in [deze](https://docs.google.com/spreadsheets/d/1B9jabEJgo_CQKnJTPorHLHq5gcTB_onDxKndBN_Dj7I/edit?usp=sharing) spreetsheet te vinden. Uiteindelijk heb ik 1000 foto's uit de KITTI 001 sequence gelabed met de [BBox-tool](https://github.com/urbinn/BBox-Label-Tool/tree/updated_version_multi_class_no_examples). De output data hiervan is te vinden in [deze link](https://github.com/urbinn/BBox-Label-Tool/tree/images_1001_2000), dit zijn uiteindelijk 1000 textbestanden met de cordinaten en label van alle opjecten in de foto waaraan het nummer corespondeerd. 


### Issue 94 Dieptebeeld genereren slinger	



### Issue 99 LIACS gebruiken voor conversie	
Omdat we nog geen GPU hadden om de SVO-files van de ZED-Camera om te zetten naar PNG-files voor YOLO en ORB. Hiervoor zouden gebruik maken van de Tesla GPU van de Server van Leiden. Maar dit ging niet door omdat we een paar dagen na het aanmaken van deze ticket een GPU kregen in de Server van HHS. 

### Issue 100 Opnamen slinger met kruisjes op grond	



### Issue 103 Beeldmateriaal van slinger en rugzak omzetten voor orb slam 2	


### Issue 104 Opnemen beeldmateriaal van ovaal en buiten	



### Issue 114 Opnemen beeldmateriaal van ovaal en buiten	




### Issue 120 RGB naar Hue (HSV) experiment	
Link naar code 


### Issue 135


### Issue 141

`ffmpeg -framerate 60 -i left%03d.png -s:v 1280x720 -c:v libx264 \-profile:v high -crf 20 -pix_fmt yuv420p 01_route_01_opname_01.mp4`

`ffmpeg -r 60 -s 1280x720 -i %06d.png -vcodec libx264 -crf 15 ../03_route_03_opname_03.mp4` 



### Issue 142



### Issue 143



### Issue 146



### Issue 152



### Issue 153



### Issue 154



