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
Het doel van deze ticket was het omzetten van de floats naar meters in ORB-SLAM. 


### Issue 141

`ffmpeg -framerate 60 -i left%03d.png -s:v 1280x720 -c:v libx264 \-profile:v high -crf 20 -pix_fmt yuv420p 01_route_01_opname_01.mp4`