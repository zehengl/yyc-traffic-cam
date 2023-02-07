<figure markdown>
![Logo](https://cdn4.iconfinder.com/data/icons/internet-security-flat-2/32/Internet_Security_Camera_cctv_technology_secure_surveillance-512.png){ width="100" }
</figure>

# yyc-traffic-cam

We can view City's up-to-minute traffic camera images on major routes and intersections with the links published at [Open Data portal](https://data.calgary.ca/Transportation-Transit/Traffic-Cameras/k7p9-kppz).

## Camera Image

Here's an example of Macleod Trail at Glenmore Trail.

![Example Shot from Traffic Camera](example-input.jpg)

## Object Detection

With a little help from YOLOv5, we can find all the vehicles from the image.

![Vehicle Detection](example-output.jpg)

## Statistics

When we set up a cron job to fetch images from that camera location periodically over a certain time,
we can better understand the traffic patterns.

![Summary by hour of day](example-summary-hour.png)

![Summary by day of week](example-summary-weekday.png)
