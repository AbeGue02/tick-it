import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tickit_django.settings')
django.setup()

from tickit.models import Location, Venue, Event
from datetime import datetime
# from django.utils import timezone

def seed_data():
    # Seed Location data
    location1 = Location.objects.create(state='TX', city='Austin', city_img='https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcSQXKrhw2T3jWayrxMFoY3UHE7MJcW8KcAS1LnDnMFLAe71L0O6cTlPaUN1DIqCelqKWXPllsDEquvJNizJDZ0sqgXkcCFstS2B_0Zl0A')
    location2 = Location.objects.create(state='TX', city='Houston', city_img='https://www.licensestorehouse.com/p/191/city-skyline-interstate-houston-texas-10005362.jpg.webp')
    location3 = Location.objects.create(state='FL', city='Tampa Bay', city_img='https://www.tripsavvy.com/thmb/NWkdutGiripud9Uz4iwRIvNs-eo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-697224578-5b0ebad38e1b6e003e9b3036.jpg')
    location4 = Location.objects.create(state='CA', city='San Diego', city_img='https://www.travelandleisure.com/thmb/qxXg7vaaQHVDl0aQigfIYpIze24=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/san-diego-california-SDTG0221-7d1cfd65a826426d8cc7f6e41345ac19.jpg')
    location5 = Location.objects.create(state='GA', city='Atlanta', city_img='https://a.cdn-hotels.com/gdcs/production114/d1629/63a8dbe5-e678-4fe4-957a-ad367913a3fa.jpg')

    # Seed Venue data
    venue1 = Venue.objects.create(location=location1, name='Germania Insurance Amphitheatre', venue_img='https://www.concertarchives.org/image_uploads/photo/image/636813/large_image.jpg')
    venue2 = Venue.objects.create(location=location1, name='Moody Center', venue_img='https://www.billboard.com/wp-content/uploads/2022/12/moody-center-2023-cr-Chase-Daniel-Gensler-billboard-pro-1260.jpg')
    venue3 = Venue.objects.create(location=location2, name='NRG Park', venue_img='https://cdn.houstonpublicmedia.org/wp-content/uploads/2021/04/12155937/DJI_0052-1-1000x750.jpg.webp')
    venue4 = Venue.objects.create(location=location2, name='House of Blues', venue_img='https://res.cloudinary.com/dhh19fozh/q_auto:good,f_auto,dpr_1.0/w_auto:breakpoints_85_850_10_10:746/jb7production-uploads/2023/05/bricks-in-the-wall-pink-floyd-tribute-1200x675.png')
    venue5 = Venue.objects.create(location=location3, name='Amalie Arena', venue_img='https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_500,q_75,w_700/v1/crm/tampabay/s20191003Hockey_TBLvsFLA051cbl-1--7dd0198f5056a36_7dd01ca6-5056-a36a-089c3804d743efd2.jpg')
    venue6 = Venue.objects.create(location=location3, name='Ruth Eckerd Hall', venue_img='https://www.rutheckerdhall.com/assets/img/Grand-Arrival-2-1440x720-31b7908d3e.png')
    venue7 = Venue.objects.create(location=location4, name='Observatory North Park', venue_img='https://media.bizj.us/view/img/11287966/santa-ana-observatory-music-hall*900xx1047-589-39-0.jpg')
    venue8 = Venue.objects.create(location=location4, name='Music Box', venue_img='https://musicboxsd.com/wp-content/uploads/2023/02/music-box-logo-at-the-first-floor-bar-san-diego-private-venue-1536x868.jpg')
    venue9 = Venue.objects.create(location=location5, name='Mercedes-Benz Stadium', venue_img='https://cdnassets.hw.net/dims4/GG/83dc656/2147483647/thumbnail/876x580%3E/quality/90/?url=https%3A%2F%2Fcdnassets.hw.net%2Fae%2F80%2F9d95561f47e6bac2127ee0f5e281%2Fmercedesbenzstadium-hok-exterior1.jpg')
    venue10 = Venue.objects.create(location=location5, name='Tabernacle', venue_img='https://atlantafortheyoung.com/wp-content/uploads/2014/06/e3f9f-widespread-panic-wood-tour-tabernacle-atlanta-2012-ian-rawn-9.jpg')

    # Seed Event data
    event1 = Event.objects.create(venue=venue1, name='Neil Young Crazy Horse: Love Earth Tour', event_type='Concert', date=datetime(2024, 5, 1, 19, 30, 00), seating_type='Standard Admission', cost=62.50, event_img='https://s1.ticketm.net/dam/a/d67/88cb70fe-f202-4835-ab38-21e2af8fad67_EVENT_DETAIL_PAGE_16_9.jpg')
    event2 = Event.objects.create(venue=venue1, name='21 Savage: American Dream Tour', event_type='Concert', date=datetime(2024, 5, 14, 19, 00, 00), seating_type='General Admission', cost=39.00, event_img='https://s1.ticketm.net/dam/a/d67/88cb70fe-f202-4835-ab38-21e2af8fad67_EVENT_DETAIL_PAGE_16_9.jpg')
    event3 = Event.objects.create(venue=venue2, name='Jon Batiste', event_type='Concert', date=datetime(2024, 5, 27, 20, 00, 00), seating_type='Genral Admission', cost=68.00, event_img='https://s1.ticketm.net/dam/a/85f/0d31cd01-3a3c-4f73-91b3-0a31b1b9085f_EVENT_DETAIL_PAGE_16_9.jpg')
    event4 = Event.objects.create(venue=venue2, name='CMT Music Awards', event_type='Concert', date=datetime(2024, 4, 7, 19, 00, 00), seating_type='Sec 210', cost=229.00, event_img='https://s1.ticketm.net/dam/a/a0b/b4480628-d4fb-46a7-a981-5a4429a54a0b_EVENT_DETAIL_PAGE_16_9.jpg')
    event5 = Event.objects.create(venue=venue3, name='Jiu Jitsu World League', event_type='Concert', date=datetime(2024, 5, 1, 19, 30, 00), seating_type='General Admission', cost=119.00, event_img='https://jjworldleague.com/uploaded/events/banners/ban-560.jpg')
    event6 = Event.objects.create(venue=venue3, name='H-Town Blues Festival', event_type='Concert', date=datetime(2024, 4, 5, 20, 00, 00), seating_type='Sec 106', cost=75.00, event_img='https://s1.ticketm.net/dam/a/ce4/06d952f1-ca2c-4432-8b7b-c3a0c1b9cce4_EVENT_DETAIL_PAGE_16_9.jpg')
    event7 = Event.objects.create(venue=venue4, name='Upchurch', event_type='Concert', date=datetime(2024, 3, 28, 18, 00, 00), seating_type='Genral Admission', cost=71.00, event_img='https://s1.ticketm.net/dam/a/a39/fe5928e6-15f7-46e2-aa9f-659665c0aa39_EVENT_DETAIL_PAGE_16_9.jpg')
    event8 = Event.objects.create(venue=venue4, name='Asking Alexandria: All My Friends North American Tour', event_type='Concert', date=datetime(2024, 4, 13, 17, 30, 00), seating_type='General Admission', cost=53.00, event_img='https://s1.ticketm.net/dam/a/0a3/6ba77291-97b9-4a16-a39e-8954f9c140a3_1277001_EVENT_DETAIL_PAGE_16_9.jpg')
    event9 = Event.objects.create(venue=venue5, name='Tampa Bay Lightning vs. Boston Bruins', event_type='Sports', date=datetime(2024, 3, 27, 19, 30, 00), seating_type='Sec 305', cost=85.00, event_img='https://s1.ticketm.net/dam/a/a61/147f5868-d179-408f-8484-8deb775e2a61_1277211_EVENT_DETAIL_PAGE_16_9.jpg')
    event10 = Event.objects.create(venue=venue5, name='Madonna - The Celebration Tou', event_type='Concert', date=datetime(2024, 4, 1, 20, 30, 00), seating_type='Sec 329', cost=200.00, event_img='https://s1.ticketm.net/dam/a/498/6297ea49-4f30-4231-a3a8-88cef2593498_EVENT_DETAIL_PAGE_16_9.jpg')
    event11 = Event.objects.create(venue=venue6, name='Disney Princess: The Concert', event_type='Musical', date=datetime(2024, 4, 6, 19, 30, 00), seating_type='Sec Orchestra', cost=40.00, event_img='https://s1.ticketm.net/dam/a/abf/9b1804e7-0107-444e-8836-64375a779abf_EVENT_DETAIL_PAGE_16_9.jpg')
    event12 = Event.objects.create(venue=venue6, name='Brit Floyd', event_type='Concert', date=datetime(2024, 4, 21, 19, 30, 00), seating_type='Sec Orchestra', cost=81.00, event_img='https://s1.ticketm.net/dam/a/20a/a6194f01-f896-4723-b189-2e5d50d1320a_EVENT_DETAIL_PAGE_16_9.jpg')
    event13 = Event.objects.create(venue=venue7, name='Dethklok: Mutilation on a Spring Night', event_type='Concert', date=datetime(2024, 4, 22, 18, 00, 00), seating_type='General Admission', cost=131.18, event_img='https://s1.ticketm.net/dam/a/e40/465904bd-9c4b-4a7c-b50a-39c992d37e40_EVENT_DETAIL_PAGE_16_9.jpg')
    event14 = Event.objects.create(venue=venue7, name='VNV Nation', event_type='Concert', date=datetime(2024, 4, 24, 18, 30, 00), seating_type='General Admission', cost=41.75, event_img='https://s1.ticketm.net/dam/a/cf7/aa87dd5d-01c2-40be-9773-5c3952f3bcf7_789791_EVENT_DETAIL_PAGE_16_9.jpg')
    event15 = Event.objects.create(venue=venue8, name='Eagles Ronstadt Experience', event_type='Concert', date=datetime(2024, 4, 7, 18, 30, 00), seating_type='General Admission', cost=32.00, event_img='https://i.ticketweb.com//i/00/12/20/70/13_Edp.jpg?v=5')
    event16 = Event.objects.create(venue=venue8, name='Jeff Bernat North American Tour', event_type='Concert', date=datetime(2024, 6, 19, 20, 00, 00), seating_type='General Admission', cost=32.00, event_img='https://i.ticketweb.com//i/00/12/20/37/53_Edp.jpg?v=8')
    event17 = Event.objects.create(venue=venue9, name='Atlanta United FC vs. Chicago Fire FC', event_type='Sports', date=datetime(2024, 3, 31, 15, 30, 00), seating_type='Sec 135', cost=29.00, event_img='https://s1.ticketm.net/dam/a/bdf/205139db-ab84-4419-87b8-77cf1b93cbdf_EVENT_DETAIL_PAGE_16_9.jpg')
    event18 = Event.objects.create(venue=venue9, name='Kenny Chesney: Sun Goes Down Tour with Zach Brown', event_type='Concert', date=datetime(2024, 5, 18, 19, 30, 00), seating_type='Sec 321', cost=35.00, event_img='https://s1.ticketm.net/dam/a/b70/bbb22ed9-520a-48c4-86ab-d0cf17684b70_1250811_EVENT_DETAIL_PAGE_16_9.jpg')
    event19 = Event.objects.create(venue=venue10, name='Pete Davidson: Prehab Tour', event_type='Comedy', date=datetime(2024, 4, 6, 19, 00, 00), seating_type='Sec 401', cost=51.50, event_img='https://s1.ticketm.net/dam/a/7f8/82b5346d-5a83-4156-a781-f191a43777f8_EVENT_DETAIL_PAGE_16_9.jpg')
    event20 = Event.objects.create(venue=venue10, name='Jason Isbell and the 400 Unit', event_type='Concert', date=datetime(2024, 3, 28, 20, 00, 00), seating_type='General Admission', cost=68.50, event_img='https://s1.ticketm.net/dam/a/bf7/ab28bd0b-2d75-433a-9357-9e81fcacabf7_EVENT_DETAIL_PAGE_16_9.jpg')

if __name__ == '__main__':
    seed_data()