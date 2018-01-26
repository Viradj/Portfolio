# Issue_urbinn
Binnen het project van Urbinn hebben we gebruik gemaakt van de tool Waffle. [Dit is een link naar de Waffle tool.](https://waffle.io/urbinn/urbinn)



## Issue
Dit is een overzicht van alle Issues waar ik aan heb gewerkt met uitleg.

### Issue 55: Object detection appers lezen
Voor deze Issue heb een paar projectgenoten en ik object detectie papers gelezen. Dit was van belang om de juiste methode te vinden voor een goed object detection algoritme. 


### Issue 62 aanpakken die objecten herkennen op basis van photometric differences in stereo images
Voor deze Issue heb ik onderzoek gedaan naar de manier hoe afstand kan worden berekend door het vergelijken van twee opelkaar lopende foto's. Herbij heb ik gekeken naar het gebruik van verschillende CNN die vergelijkbare problemen aanpakken. In deze link kunnen mijn intere aantekening gevonden worden: [link](Issue_62/Issue_62-photometric_differences_in_stereo_images.pdf)


### Issue 64 Evaluatie implementatie: pointcloud vs pointcloud

Bij deze issue heb ik samen met Isa gekeken naar de mogelijkheid om de ZED opnames om te zetten naar een mesh die gebruikt kan worden om een pointcloud te generen. 

![alt text](/Issue_64/3D_mesh_Slinger.png)

Met de opnames die waren genomen van de 6de verdieping werd door een onderdeel van de ZED SDK, ZEDfu omzet naar een mesh en opj file. Deze twee files werden samen met in een andere tool omgezet die Cloudcompair heet en hieruit kwam de afbeelding hierboven. Maar helaas bleek het dat het niet accuraat genoeg was om te gebruiken voor de evaluatie van URB-SLAM. De bedoeling was namelijk om twee pointcloud over elkaar te leggen en te zien wat in hoevere URB juiste punten detecteerde.  

### Issue 67 Tiny Yolo dataset uitzoeken
Voor het gebruik van Tiny Yolo moest er gebruik worden gemaakt van een dataset waarmee getraind kon worden op bepaalde opjecten. Hiervoor heb ik gezocht naar openbare databases waarvan gebruik kan worden gemaakt deze zijn: ImageNet, PASCAL VOC 2007 en 2012 en de CoCo Dataset. Ook heb ik gekeken hoe Yolo getraind kan worden en wat mogelijke risicio's kunnen zijn tijdens het trainen. Hieruit bleek dat een dataset zoals CoCo al hoewel veel opjecten gelabeld heeft een Noord-Amerikaanse dataset en sommige van deze opjecten niet in Nederland het zelde eruit zien. Zo zijn de verkeersboarden in Noord-Amerika groen.  De resultaten van dit onderzoek zijn te vinden in dit docuemnt: [link](Issue_67/Issue_67-Tiny_YOLO_datasets.pdf)

### Issue 77 Presentatie maken + blog updaten
In week 9 en 10 hadden een projectgenoot en ik de taak om de precentatie te maken en de blog te updaten. 
De presentatie kan [hier](/Presentatie/Week_9/Week_9-Presentatie.pdf) en [hier](/Presentatie/Week_10/Week_10-Presentatie.pdf) gevonden worden. Voor de blog kan [hier](https://kb74.github.io/urbinn/) gekeken worden onder Milestone 5.

### Issue 79 ORB coordinaten converteren
Het doel van deze ticket was het omzetten van de floats naar meters in ORB-SLAM. Bij deze issue heb ik meegekeken met de de andere projectgenoten en zochten we naar een oplossing. 

### Issue 80 ORB output uitbreiden met keyframe coordinaten	
Bij deze issue heb ik meegekeken met de de andere projectgenoten en zochten we naar een oplossing. Om de ORB output te vergroten met keyframe coordinaten, omdat uit de toen verkrijgbare dat niet genoeg informatie kon worden gehaald. 


### Issue 81 Literatuur scan: filteren slam met object detectie	
Tijdens het literatuur ondezoek naar filteren van slam met object detectie zijn twee papers naar voren gekomen: 
1.  Object Detection and Tracking in RGB-D SLAM via Hierarchical Feature Grouping
2. Monocular SLAM Supported Object Recognition.

Deze twee papers zijn [hier](https://drive.google.com/drive/folders/0B_afORSfPeRYdUJGdzVmd1R3aDg?usp=sharing) te vinden. 

### Issue 82 yolo training data verzamelen
Voor Yolo was het van belang om de goede datasets te vinden om het model te trainen. Hiervoor heb ik enkele datasets gevonden zoals [Coco](http://cocodataset.org/#home), [ImageNet](https://pjreddie.com/darknet/imagenet/) en [Pacal Voc](http://host.robots.ox.ac.uk/pascal/VOC/)

### Issue 86 Ground truth nieuwe trainingsdata labelen	
Voor het trainen van YOLO is besloten om de KITTI_dataset te herlabelen met de toevoeging van onze eigen labels. Alle klasses die we hebben gelabed zijn in [deze](https://docs.google.com/spreadsheets/d/1B9jabEJgo_CQKnJTPorHLHq5gcTB_onDxKndBN_Dj7I/edit?usp=sharing) spreetsheet te vinden. Uiteindelijk heb ik 1000 foto's uit de KITTI 001 sequence gelabed met de [BBox-tool](https://github.com/urbinn/BBox-Label-Tool/tree/updated_version_multi_class_no_examples). De output data hiervan is te vinden in [deze link](https://github.com/urbinn/BBox-Label-Tool/tree/images_1001_2000), dit zijn uiteindelijk 1000 textbestanden met de cordinaten en label van alle opjecten in de foto waaraan het nummer corespondeerd. 


### Issue 94 Dieptebeeld genereren slinger	
De ZED Camera is een Stereo camera waarmee we tijdens het project hebben geprobeerd beeldmateriaal te generreren voor onze algorimes. Met de camera kwam ook een SDK die de mogelijkheid had om diepte te berekenen, met deze SDK heb ik gewerkt en geexpirimenteerd. Het intere document: [link](Issue_94/Issue%2094.pdf)

![alt text](Issue_94/Issue_94.png)

### Issue 99 LIACS gebruiken voor conversie	
Omdat we nog geen GPU hadden om de SVO-files van de ZED-Camera om te zetten naar PNG-files voor YOLO en ORB. Hiervoor zouden gebruik maken van de Tesla GPU van de Server van Leiden. Maar dit ging niet door omdat we een paar dagen na het aanmaken van deze ticket een GPU kregen in de Server van HHS. 

### Issue 100 Opnamen slinger met kruisjes op grond	
Om te testen of de door ons gemaakte software naugeuring genoeg was om te zien wat de de afstand is tussen de camera andere opjecten, hebben een groepsgenoot en ik opnames genomen in de Slinger. Het plan was in de eerste plaats om ruisjes op de grond te tekenen en deze na te meten met een liniaal. Daarna zou ons algorimte uitzoeken of de data met elkaar overeen komt. 



### Issue 104 Opnemen beeldmateriaal van ovaal en buiten	



### Issue 114 Plan maken opnames Delft	
Ik heb samen met Bob een plan gemaakt waarin drie routes zijn beschreven waar we in Delft willen rijden. Dit document kan [hier](Issue_114/Issue_114_ Plan_maken_openames_Delft) gevonden kan worden. 


### Issue 120 RGB naar Hue (HSV) experiment	
Ik heb een deel van deze code geschreven nadat Bob deze had verberd. Het doel van deze code was om de RGB foto's om te zetten naar HSV en alleen het H deel van HSV te gebruiken voor het SLAM algoritme. Helaas ging dit niet door omdat dit proces te veel tijd zou nemen. De code staat hieronder vermeld. 

```import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
#print("Python version: \n" + sys.version)
#print("cv2 version: " + cv2.__version__)
img1 = cv2.imread('test_image_kitti.png')
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv1)

plt.imread('test_image_kitti.png')
plt.imshow(h)
plt.show()
plt.imsave('testhue.png', h)```

### Issue 141 Selecteren best run delft
Na de opnames in Delft was het van belang om een goede opname te nemen on te gebruiken voor de runs in URB-SLAM en YOLO. In totaal waren er 7 opnames genomen met versprijd over 3 uniuqe routes in delft. Elke opname was tussen de 12000 en 35000 afbeeldingen groot. Deze afbeeldingen heb ik eerst om gezet naar een video voormaat om rustig te analyseren met de ffmpeg libary. De code die hiervoor heb gebruikt kan hieronder gevonden worden. 

```ffmpeg -framerate 60 -i left%03d.png -s:v 1280x720 -c:v libx264 \-profile:v high -crf 20 -pix_fmt yuv420p 01_route_01_opname_01.mp4```

```ffmpeg -r 60 -s 1280x720 -i %06d.png -vcodec libx264 -crf 15 ../03_route_03_opname_03.mp4
```

Uiteindelijk is er gekozen voor de tweede opname van de derde route, deze had de meeste verschillende opjecten en het miste regen/natte sneeuw. 

### Issue 142 Run URB over dataset delft #141
Alle opnames de genomen waren van Delft hebben Isa en ik door URB gerunned en we kwamen er achter we veel ```pop from empty list``` errors. Dit betekende dat we geen keyframes konden aanmaken in het begin van de opnames. Het beste resultaat dat we uiteindelijk kregen was dat we 6 keyframes konden aanmaken. 

Alle resultaten kunnen [hier](Issue_142/Issue_142.md) gevonden worden. 

### Issue 146 Analyseren URB foute sequences Kitti



### Issue 152



### Issue 153



### Issue 154



https://drive.google.com/open?id=0BwqKb57nYbXvdWdqSU1VazVLMGc 
Paper list.
