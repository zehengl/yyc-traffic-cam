<figure markdown>
![Logo](https://cdn4.iconfinder.com/data/icons/internet-security-flat-2/32/Internet_Security_Camera_cctv_technology_secure_surveillance-512.png){ width="100" }
</figure>

# yyc-traffic-cam

We can view City's up-to-minute traffic camera images on major routes and intersections with the links published at [Open Data portal](https://data.calgary.ca/Transportation-Transit/Traffic-Cameras/k7p9-kppz).

## Camera Image

Here are examples of

- Macleod Trail at Glenmore Trail
- Anderson Road at 24 St SW

<figure markdown>
![Example Shot 1 from Traffic Camera](example-input1.jpg){ width="48%", align="left" }
![Example Shot 2 from Traffic Camera](example-input2.jpg){ width="48%"}
</figure>

## Object Detection

With a little help from YOLOv5, we can find all the vehicles from the image.

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
