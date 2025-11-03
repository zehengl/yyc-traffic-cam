# yyc-traffic-cam

We can view City's up-to-minute traffic camera images on major routes and intersections with the links published at [Open Data portal](https://data.calgary.ca/Transportation-Transit/Traffic-Cameras/k7p9-kppz).

## Camera Images

Here are examples of

- Macleod Trail at Glenmore Trail [:material-camera-marker:](https://trafficcam.calgary.ca/loc0.jpg){target=\_blank}
- Anderson Road at 24 St SW [:material-camera-marker:](https://trafficcam.calgary.ca/loc104.jpg){target=\_blank}

<figure markdown>
![Example Shot 1 from Traffic Camera](example-input1.jpg){ width="48%", align="left" }
![Example Shot 2 from Traffic Camera](example-input2.jpg){ width="48%"}
</figure>

## Object Detection

With a little help from ~~YOLOv5~~ YOLOv8, we can find all the vehicles from the images.

<figure markdown>
![Vehicle Detection 1](example-output1.jpg){ width="48%", align="left" }
![Vehicle Detection 2](example-output2.jpg){ width="48%"}
</figure>

## Statistics

When we set up a cron job to fetch images from that camera location periodically over a certain time,
we can better understand the traffic patterns.

<figure markdown>
![Summary1 by hour of day](example-summary-hour1.png){ width="48%", align="left" }
![Summary1 by day of week](example-summary-weekday1.png){ width="48%"}
</figure>

<figure markdown>
![Summary2 by hour of day](example-summary-hour2.png){ width="48%", align="left" }
![Summary2 by day of week](example-summary-weekday2.png){ width="48%"}
</figure>
