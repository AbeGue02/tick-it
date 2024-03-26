TRUNCATE TABLE EVENT;
TRUNCATE TABLE VENUE;
TRUNCATE TABLE LOCATION;

ALTER SEQUENCE event_id_seq RESTART WITH 1;
ALTER SEQUENCE venue_id_seq RESTART WITH 1;
ALTER SEQUENCE location_id_seq RESTART WITH 1;

-- Locations ---------------------------------------

-- Austin, TX - 1
INSERT INTO location(city, state, city_img) VALUES ('Austin', 'TX', 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcSQXKrhw2T3jWayrxMFoY3UHE7MJcW8KcAS1LnDnMFLAe71L0O6cTlPaUN1DIqCelqKWXPllsDEquvJNizJDZ0sqgXkcCFstS2B_0Zl0A');

-- Houston, TX - 2
INSERT INTO location(city, state, city_img) VALUES ('Houston', 'TX', 'https://www.licensestorehouse.com/p/191/city-skyline-interstate-houston-texas-10005362.jpg.webp');

-- Tampa Bay, FL - 3
INSERT INTO location(city, state, city_img) VALUES ('Tampa Bay', 'FL', 'https://www.tripsavvy.com/thmb/NWkdutGiripud9Uz4iwRIvNs-eo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-697224578-5b0ebad38e1b6e003e9b3036.jpg');

-- San Diego, CA - 4
INSERT INTO location(city, state, city_img) VALUES ('San Diego', 'CA', 'https://www.travelandleisure.com/thmb/qxXg7vaaQHVDl0aQigfIYpIze24=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/san-diego-california-SDTG0221-7d1cfd65a826426d8cc7f6e41345ac19.jpg');

-- Atlanta, GA - 5
INSERT INTO location(city, state, city_img) VALUES ('Atlanta', 'GA', 'https://a.cdn-hotels.com/gdcs/production114/d1629/63a8dbe5-e678-4fe4-957a-ad367913a3fa.jpg');

-- Venues -----------------------------------------

-- Germania Insurance Amphitheatre - 1
INSERT INTO venue(name, venue_img, location_id) VALUES ('Germania Insurance Amphitheatre', 'https://www.concertarchives.org/image_uploads/photo/image/636813/large_image.jpg', 1);

-- Moody Center - 2
INSERT INTO venue(name, venue_img, location_id) VALUES ('Moody Center', 'https://www.billboard.com/wp-content/uploads/2022/12/moody-center-2023-cr-Chase-Daniel-Gensler-billboard-pro-1260.jpg?w=942&h=623&crop=1', 1);

-- NRG Park - 3
INSERT INTO venue(name, venue_img, location_id) VALUES ('NRG Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/NRG_stadium_prepared_for_Super_Bowl_Li_%2832513086661%29.jpg/440px-NRG_stadium_prepared_for_Super_Bowl_Li_%2832513086661%29.jpg', 2);

-- House of Blues - 4
INSERT INTO venue(name, venue_img, location_id) VALUES ('House of Blues', 'https://res.cloudinary.com/dhh19fozh/q_auto:good,f_auto,dpr_1.0/w_auto:breakpoints_85_850_10_10:746/jb7production-uploads/2023/05/bricks-in-the-wall-pink-floyd-tribute-1200x675.png', 2);

-- Amalie Arena - 5
INSERT INTO venue(name, venue_img, location_id) VALUES ('Amalie Arena', 'https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_500,q_75,w_700/v1/crm/tampabay/s20191003Hockey_TBLvsFLA051cbl-1--7dd0198f5056a36_7dd01ca6-5056-a36a-089c3804d743efd2.jpg', 3);

-- Ruth Eckerd Hall - 6
INSERT INTO venue(name, venue_img, location_id) VALUES ('Ruth Eckerd Hall', 'https://www.rutheckerdhall.com/assets/img/Grand-Arrival-2-1440x720-31b7908d3e.png', 3);

-- Observatory North Park - 7
INSERT INTO venue(name, venue_img, location_id) VALUES ('Observatory North Park', 'https://media.bizj.us/view/img/11287966/santa-ana-observatory-music-hall*900xx1047-589-39-0.jpg', 4);

-- Music Box - 8
INSERT INTO venue(name, venue_img, location_id) VALUES ('Music Box', 'https://musicboxsd.com/wp-content/uploads/2023/02/music-box-logo-at-the-first-floor-bar-san-diego-private-venue-1536x868.jpg', 4);

-- Mercedes-Benz Stadium - 9
INSERT INTO venue(name, venue_img, location_id) VALUES ('Mercedes-Benz Stadium', 'https://cdnassets.hw.net/dims4/GG/83dc656/2147483647/thumbnail/876x580%3E/quality/90/?url=https%3A%2F%2Fcdnassets.hw.net%2Fae%2F80%2F9d95561f47e6bac2127ee0f5e281%2Fmercedesbenzstadium-hok-exterior1.jpg', 5);

-- Tabernacle - 10
INSERT INTO venue(name, venue_img, location_id) VALUES ('Tabernacle', 'https://atlantafortheyoung.com/wp-content/uploads/2014/06/e3f9f-widespread-panic-wood-tour-tabernacle-atlanta-2012-ian-rawn-9.jpg', 5);

-- Events -----------------------------------------

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Neil Young Crazy Horse: Love Earth Tour', 'Concert', 'May 01', '7:30 PM', 'Standard Admission', 62.50, 'https://s1.ticketm.net/dam/a/d67/88cb70fe-f202-4835-ab38-21e2af8fad67_EVENT_DETAIL_PAGE_16_9.jpg', 1)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('21 Savage: American Dream Tour', 'Concert', 'May 14', '7:00 PM', 'General Admission', 39.00, 'https://s1.ticketm.net/dam/a/a72/1cf7d902-cc17-4547-b438-137095ba2a72_EVENT_DETAIL_PAGE_16_9.jpg', 1)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Jon Batiste', 'Concert', 'Mar 27', '8:00 PM', 'General Admission', 68.00, 'https://s1.ticketm.net/dam/a/85f/0d31cd01-3a3c-4f73-91b3-0a31b1b9085f_EVENT_DETAIL_PAGE_16_9.jpg', 2)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('CMT Music Awards', 'Concert', 'Apr 07', '7:00 PM', 'Sec 210', 229.00, 'https://s1.ticketm.net/dam/a/a0b/b4480628-d4fb-46a7-a981-5a4429a54a0b_EVENT_DETAIL_PAGE_16_9.jpg', 2)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Jiu Jitsu World League', 'Sports', 'Apr 07', '10:00 AM', 'General Admission', 119.00, 'https://jjworldleague.com/uploaded/events/banners/ban-560.jpg', 3)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('H-Town Blues Festival', 'Concert', 'Apr 05', '8:00 PM', 'Sec 106', 75.00, 'https://s1.ticketm.net/dam/a/ce4/06d952f1-ca2c-4432-8b7b-c3a0c1b9cce4_EVENT_DETAIL_PAGE_16_9.jpg', 3)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Upchurch', 'Concert', 'Mar 28', '6:00 PM', 'General Admission', 71.00, 'https://s1.ticketm.net/dam/a/a39/fe5928e6-15f7-46e2-aa9f-659665c0aa39_EVENT_DETAIL_PAGE_16_9.jpg', 4)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Asking Alexandria: All My Friends North American Tour', 'Concert', 'Apr 13', '5:30 PM', 'General Admission', 53.00, 'https://s1.ticketm.net/dam/a/0a3/6ba77291-97b9-4a16-a39e-8954f9c140a3_1277001_EVENT_DETAIL_PAGE_16_9.jpg', 4)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Tampa Bay Lightning vs. Boston Bruins', 'Sports', 'Mar 27', '7:30 PM', 'Sec 305', 85.00, 'https://s1.ticketm.net/dam/a/a61/147f5868-d179-408f-8484-8deb775e2a61_1277211_EVENT_DETAIL_PAGE_16_9.jpg', 5)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Madonna - The Celebration Tour', 'Concert', 'Apr 04', '8:30 PM', 'Sec 329', 200.00, 'https://s1.ticketm.net/dam/a/498/6297ea49-4f30-4231-a3a8-88cef2593498_EVENT_DETAIL_PAGE_16_9.jpg', 5)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Disney Princess: The Concert', 'Musical', 'Apr 6', '7:30 PM', 'Sec ORCHESTRA', 40.00, 'https://s1.ticketm.net/dam/a/abf/9b1804e7-0107-444e-8836-64375a779abf_EVENT_DETAIL_PAGE_16_9.jpg', 6)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Brit Floyd', 'Concert', 'Apr 21', '7:30 PM', 'Sec ORCHESTRA', 81.00, 'https://s1.ticketm.net/dam/a/20a/a6194f01-f896-4723-b189-2e5d50d1320a_EVENT_DETAIL_PAGE_16_9.jpg', 6)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Dethklok: Mutilation on a Spring Night', 'Concert', 'Apr 22', '6:00 PM', 'General Admission', 131.18, 'https://s1.ticketm.net/dam/a/e40/465904bd-9c4b-4a7c-b50a-39c992d37e40_EVENT_DETAIL_PAGE_16_9.jpg', 7)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('VNV Nation', 'Concert', 'Apr 24', '6:30 PM', 'General Admission', 41.75, 'https://s1.ticketm.net/dam/a/cf7/aa87dd5d-01c2-40be-9773-5c3952f3bcf7_789791_EVENT_DETAIL_PAGE_16_9.jpg', 7)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Eagles Ronstadt Experience', 'Concert', 'Apr 7', '6:30 PM', 'General Admission', 32.00, 'https://i.ticketweb.com//i/00/12/20/70/13_Edp.jpg?v=5', 8)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Jeff Bernat North American Tour', 'Concert', 'June 19', '8:00 PM', 'General Admission', 32.00, 'https://i.ticketweb.com//i/00/12/20/37/53_Edp.jpg?v=8', 8)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Atlanta United FC vs. Chicago Fire FC', 'Sports', 'Mar 31', '3:30 PM', 'Sec 135', 29.00, 'https://s1.ticketm.net/dam/a/bdf/205139db-ab84-4419-87b8-77cf1b93cbdf_EVENT_DETAIL_PAGE_16_9.jpg', 9)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Kenny Chesney: Sun Goes Down Tour with Zach Brown', 'Concert', 'May 18', '5:00 PM', 'Sec 321', 35.00, 'https://s1.ticketm.net/dam/a/b70/bbb22ed9-520a-48c4-86ab-d0cf17684b70_1250811_EVENT_DETAIL_PAGE_16_9.jpg', 9)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Pete Davidson: Prehab Tour', 'Comedy', 'Apr 6', '7:00 PM', 'Sec 401', 51.50, 'https://s1.ticketm.net/dam/a/7f8/82b5346d-5a83-4156-a781-f191a43777f8_EVENT_DETAIL_PAGE_16_9.jpg', 10)

INSERT INTO event(name, event_type, date, time,  seating_type, cost, event_img, venue_id)
VALUES ('Jason Isbell and the 400 Unit', 'Concert', 'Mar 28', '8:00 PM', 'General Admission', 68.50, 'https://s1.ticketm.net/dam/a/bf7/ab28bd0b-2d75-433a-9357-9e81fcacabf7_EVENT_DETAIL_PAGE_16_9.jpg', 10)