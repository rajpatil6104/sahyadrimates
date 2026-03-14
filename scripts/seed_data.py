import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime, timezone, timedelta


IMAGE_DIR = "images/"
async def seed_database():
    # Connect to MongoDB
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
    db_name = os.environ.get('DB_NAME', 'test_database')
    
    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]
    
    # Clear existing data
    await db.tours.delete_many({})
    await db.coupons.delete_many({})
   
    
    # Here we add the tour details
    tours = [
        {
            'id': 'tour-1',
            'title': 'Bhairavgad Trek',
            'slug': 'bhairavgad-trek',
            'description': 'We SahyadriMates Happy to Invite you to the most Thrilling Trek in Maharashtra - "Bhairavgad with 300 feet Climbing-Rappelling and Jungle Trek Event"',
            'price': 1899,
            'original_price': 2299,
            'duration': 'One Day',
            'category': 'trek',
            'destination': 'Maharashtra',
            'image_url': '/images/tour/bhairavgad.jpg', 
            'images': ['/images/tour/bhairavgad.jpg'],
            'inclusions': ['Transportation from Pune/Mumbai','Tea & Breakfast','Delicious lunch(Veg or Non-Veg)', 'Experienced & Certified leader', 'Frist aid kit', 'Safety equipment for climbing & rappelling'],
            'exclusions': ['Personal expenses', 'Travel insurance', 'Porter charges', 'Any meals not mentioned'],
            'itinerary': [
                {'day': 1, 'title': 'Pune / Kalyan to Base Village'},
                {'Time': '08:30 PM', 'title': 'Pickup from Pune', 'description': 'Participants assemble at the pickup point in Pune and start the journey towards Bhairavgad base village.'},
                {'Time': '11:30 PM', 'title': 'Pickup from Kalyan', 'description': 'Participants joining from Kalyan will board the vehicle and continue the journey towards the base village.'},
                {'day': 2, 'title': 'Bhairavgad Trek & Rappelling'},
                {'Time': '05:00 AM', 'title': 'Reach Base Village', 'description': 'Freshen up and have tea & breakfast.'},
                {'Time': '06:30 AM', 'title': 'Start Trekking', 'description': 'Begin the trek through jungle trails towards Bhairavgad.'},
                {'Time': '09:00 AM', 'title': 'Reach Climbing Patch', 'description': 'Experience thrilling rock climbing and 300 ft rappelling with safety gear.'},
                {'Time': '12:00 PM', 'title': 'Start Decending'},
                {'Time': '03:00 PM', 'title': 'Reach Base Village & Lunch'},
                {'Time': '04:30 PM', 'title': 'Start return journey', 'description': 'After a hearty lunch, start the return journey back to Pune/Kalyan.'},
                {'Time': '10:00 PM', 'title': 'Reach Pune/Kalyan', 'description': 'Arrive back at the pickup points in Pune and Kalyan, marking the end of an exhilarating trek.'},
            ],
            'available_dates': ['Every Saturday', 'Every Sunday'],
            'group_size': 20,
            'difficulty': 'Moderate',
            'featured': True,
            'rating': 4.8,
            'reviews_count': 127,
            'created_at': datetime.now(timezone.utc).isoformat()
        },
        {
            'id': 'tour-2',
            'title': 'Kalvanti Durga Trek',
            'slug': 'kalvanti-durga-trek',
            'description': 'Experience the thrill of trekking to Kalvanti Durga. A perfect blend of adventure and natural beauty.',
            'price': 1299,
            'original_price': 1499,
            'duration': 'Saturday-Sunday',
            'category': 'trek',
            'destination': 'Maharashtra',
            'image_url': '/images/tour/kalavantidurg.png',
            'images': ['images/tour/kalavantidurg.png'],
            'inclusions': ['Transportation from Pune/Mumbai','Tea & Breakfast','Delicious lunch(Veg or Non-Veg)', 'Experienced & Certified leader', 'Frist aid kit', 'Safety equipment for climbing & rappelling'],
            'exclusions': ['Personal expenses', 'Travel insurance', 'Porter charges', 'Any meals not mentioned'],
            'itinerary': [
                 {'day': 1, 'title': 'Pune / Kalyan to Base Village'},
                 {'Time': '08:30 PM', 'title': 'Pickup from Pune', 'description': 'Participants assemble at the pickup point in Pune and start the journey towards Bhairavgad base village.'},
                 {'Time': '11:30 PM', 'title': 'Pickup from Kalyan', 'description': 'Participants joining from Kalyan will board the vehicle and continue the journey towards the base village.'},
                 {'day': 2, 'title': 'Bhairavgad Trek & Rappelling'},
                 {'Time': '05:00 AM', 'title': 'Reach Base Village', 'description': 'Freshen up and have tea & breakfast.'},
                 {'Time': '06:30 AM', 'title': 'Start Trekking', 'description': 'Begin the trek through jungle trails towards Kalavanti Durga.'},
                 {'Time': '09:00 AM', 'title': 'Reach Climbing Patch', 'description': 'Experience thrilling rock climbing and 300 ft rappelling with safety gear.'},
                 {'Time': '12:00 PM', 'title': 'Start Decending'},
                 {'Time': '03:00 PM', 'title': 'Reach Base Village & Lunch'},
                 {'Time': '04:30 PM', 'title': 'Start return journey', 'description': 'After a hearty lunch, start the return journey back to Pune/Kalyan.'},
                 {'Time': '10:00 PM', 'title': 'Reach Pune/Kalyan', 'description': 'Arrive back at the pickup points in Pune and Kalyan, marking the end of an exhilarating trek.'},
             ],
            'available_dates': ['Every Saturday', 'Every Sunday'],
            'group_size': 50,
            'difficulty': 'Easy',
            'featured': True,
            'rating': 4.6,
            'reviews_count': 342,
            'created_at': datetime.now(timezone.utc).isoformat()
        },
        {
            'id': 'tour-3',
            'title': 'Kalsubai Trek',
            'slug': 'kalsubai-trek',
            'description': 'Experience the thrill of trekking to Kalsubai. A perfect blend of adventure and natural beauty.',
            'price': 1299,
            'original_price': 1499,
            'duration': 'Saturday-Sunday',
            'category': 'trek',
            'destination': 'Maharashtra',
            'image_url': '/images/tour/kalsubai.png',
            'images': ['images/tour/kalsubai.png'],
            'inclusions': ['Transportation from Pune/Mumbai','Tea & Breakfast','Delicious lunch(Veg or Non-Veg)', 'Experienced & Certified leader', 'Frist aid kit', 'Safety equipment for climbing & rappelling'],
            'exclusions': ['Personal expenses', 'Travel insurance', 'Porter charges', 'Any meals not mentioned'],
            'itinerary': [
                 {'day': 1, 'title': 'Pune / Kalyan to Base Village'},
                 {'Time': '08:30 PM', 'title': 'Pickup from Pune', 'description': 'Participants assemble at the pickup point in Pune and start the journey towards Bhairavgad base village.'},
                 {'Time': '11:30 PM', 'title': 'Pickup from Kalyan', 'description': 'Participants joining from Kalyan will board the vehicle and continue the journey towards the base village.'},
                 {'day': 2, 'title': 'Bhairavgad Trek & Rappelling'},
                 {'Time': '05:00 AM', 'title': 'Reach Base Village', 'description': 'Freshen up and have tea & breakfast.'},
                 {'Time': '06:30 AM', 'title': 'Start Trekking', 'description': 'Begin the trek through jungle trails towards Kalsubai.'},
                 {'Time': '09:00 AM', 'title': 'Reach Climbing Patch', 'description': 'Experience thrilling rock climbing and 300 ft rappelling with safety gear.'},
                 {'Time': '12:00 PM', 'title': 'Start Decending'},
                 {'Time': '03:00 PM', 'title': 'Reach Base Village & Lunch'},
                 {'Time': '04:30 PM', 'title': 'Start return journey', 'description': 'After a hearty lunch, start the return journey back to Pune/Kalyan.'},
                 {'Time': '10:00 PM', 'title': 'Reach Pune/Kalyan', 'description': 'Arrive back at the pickup points in Pune and Kalyan, marking the end of an exhilarating trek.'},
             ],
            'available_dates': ['Every Saturday', 'Every Sunday'],
            'group_size': 15,
            'difficulty': 'Easy',
            'featured': True,
            'rating': 4.9,
            'reviews_count': 89,
            'created_at': datetime.now(timezone.utc).isoformat()
        },
        {
            'id': 'tour-4',
            'title': 'Kerala Backwaters Tour',
            'slug': 'kerala-backwaters',
            'description': 'Experience the serene backwaters of Kerala. Houseboat stay, Munnar hills, and Alleppey beaches.',
            'price': 16999,
            'duration': '6N/7D',
            'category': 'tour',
            'destination': 'Kerala',
            'image_url': 'https://images.pexels.com/photos/34452959/pexels-photo-34452959.jpeg',
            'images': [],
            'inclusions': ['Hotel & Houseboat stay', 'Daily breakfast', 'Transport', 'Sightseeing'],
            'exclusions': ['Lunch & Dinner', 'Entry fees', 'Personal expenses'],
            'itinerary': [
                {'day': 1, 'title': 'Arrival Cochin', 'description': 'Pickup and transfer to hotel'},
                {'day': 2, 'title': 'Cochin to Munnar', 'description': 'Drive to Munnar, visit tea gardens'},
                {'day': 3, 'title': 'Munnar Sightseeing', 'description': 'Echo point, Mattupetty Dam, tea museum'},
                {'day': 4, 'title': 'Munnar to Thekkady', 'description': 'Spice plantation visit, boat ride'},
                {'day': 5, 'title': 'Thekkady to Alleppey', 'description': 'Houseboat check-in, backwater cruise'},
                {'day': 6, 'title': 'Alleppey to Cochin', 'description': 'Beach visit, shopping'},
                {'day': 7, 'title': 'Departure', 'description': 'Drop to airport'}
            ],
            'available_dates': ['12 Jan 2025', '19 Jan 2025', '26 Jan 2025'],
            'group_size': 12,
            'difficulty': 'Easy',
            'featured': True,
            'rating': 4.7,
            'reviews_count': 156,
            'created_at': datetime.now(timezone.utc).isoformat()
        },
        {
            'id': 'tour-5',
            'title': 'Rishikesh Rafting & Camping',
            'slug': 'rishikesh-adventure',
            'description': 'Adrenaline-pumping river rafting in Rishikesh with beach camping and bonfires.',
            'price': 3499,
            'duration': '2N/3D',
            'category': 'adventure',
            'destination': 'Uttarakhand',
            'image_url': 'https://images.pexels.com/photos/2348108/pexels-photo-2348108.jpeg',
            'images': [],
            'inclusions': ['Camping accommodation', 'All meals', 'River rafting (16 km)', 'Bonfire', 'Adventure activities'],
            'exclusions': ['Transport to Rishikesh', 'Personal expenses'],
            'itinerary': [
                {'day': 1, 'title': 'Arrival & Activities', 'description': 'Reach camp, volleyball, badminton, music'},
                {'day': 2, 'title': 'River Rafting', 'description': 'Morning rafting, beach activities, bonfire'},
                {'day': 3, 'title': 'Departure', 'description': 'Breakfast and checkout'}
            ],
            'available_dates': ['Every Friday', 'Every Saturday'],
            'group_size': 30,
            'difficulty': 'Moderate',
            'featured': False,
            'rating': 4.5,
            'reviews_count': 234,
            'created_at': datetime.now(timezone.utc).isoformat()
        },
        {
            'id': 'tour-6',
            'title': 'Meghalaya Living Root Bridges Trek',
            'slug': 'meghalaya-trek',
            'description': 'Explore the wettest place on Earth. Trek to double-decker living root bridges and pristine waterfalls.',
            'price': 19999,
            'duration': '6N/7D',
            'category': 'trek',
            'destination': 'Meghalaya',
            'image_url': 'https://images.pexels.com/photos/7625033/pexels-photo-7625033.jpeg',
            'images': [],
            'inclusions': ['Accommodation', 'All meals', 'Transport from Guwahati', 'Trek guide', 'Entry fees'],
            'exclusions': ['Flight to Guwahati', 'Personal expenses', 'Porter charges'],
            'itinerary': [
                {'day': 1, 'title': 'Guwahati to Cherrapunji', 'description': 'Drive to Cherrapunji, visit waterfalls'},
                {'day': 2, 'title': 'Nongriat Trek', 'description': 'Trek to Double Decker Root Bridge'},
                {'day': 3, 'title': 'Nongriat Exploration', 'description': 'Rainbow falls, natural pools'},
                {'day': 4, 'title': 'Back to Cherrapunji', 'description': 'Trek back, caves visit'},
                {'day': 5, 'title': 'Mawlynnong Village', 'description': "Asia's cleanest village, living root bridge"},
                {'day': 6, 'title': 'Dawki & Shillong', 'description': 'Crystal clear Umngot river, drive to Shillong'},
                {'day': 7, 'title': 'Departure', 'description': 'Drop to Guwahati airport'}
            ],
            'available_dates': ['20 Jan 2025', '27 Jan 2025', '03 Feb 2025'],
            'group_size': 15,
            'difficulty': 'Moderate',
            'featured': False,
            'rating': 4.9,
            'reviews_count': 78,
            'created_at': datetime.now(timezone.utc).isoformat()
        },
        {
            'id': 'tour-7',
            'title': 'Manali Kasol Kheerganga Trek',
            'slug': 'manali-kasol-kheerganga',
            'description': 'Experience the magical Himalayan valleys with pristine forests, hot springs, and stunning mountain views. Perfect blend of adventure and relaxation.',
            'price': 12999,
            'original_price': 15999,
            'duration': '6N/7D',
            'category': 'trek',
            'destination': 'Himachal Pradesh',
            'image_url': 'https://images.pexels.com/photos/35455016/pexels-photo-35455016.jpeg',
            'images': [],
            'inclusions': ['Accommodation in camps/hotels', 'All meals (breakfast, lunch, dinner)', 'Experienced trek leader', 'Transport from Delhi', 'First aid kit'],
            'exclusions': ['Personal expenses', 'Travel insurance', 'Porter charges', 'Any meals not mentioned'],
            'itinerary': [
                {'day': 1, 'title': 'Delhi to Manali', 'description': 'Overnight journey from Delhi to Manali by Volvo bus'},
                {'day': 2, 'title': 'Manali Local Sightseeing', 'description': 'Explore Hadimba Temple, Vashisht hot springs, Mall Road'},
                {'day': 3, 'title': 'Manali to Kasol', 'description': 'Drive to Kasol, explore the village and riverside'},
                {'day': 4, 'title': 'Kasol to Kheerganga Trek', 'description': 'Trek to Kheerganga, enjoy hot springs'},
                {'day': 5, 'title': 'Kheerganga to Kasol', 'description': 'Descend back to Kasol, leisure time'},
                {'day': 6, 'title': 'Kasol to Delhi', 'description': 'Return journey to Delhi'}
            ],
            'available_dates': ['15 Jan 2025', '22 Jan 2025', '29 Jan 2025', '05 Feb 2025', '12 Feb 2025'],
            'group_size': 20,
            'difficulty': 'Moderate',
            'featured': True,
            'rating': 4.8,
            'reviews_count': 127,
            'created_at': datetime.now(timezone.utc).isoformat()
        }
    ]
    
    # Insert tours
    await db.tours.insert_many(tours)
    print(f"✓ Inserted {len(tours)} tours")
    
    # Sample coupons
    coupons = [
        {
            'id': 'coupon-1',
            'code': 'LOYALTY50',
            'discount_type': 'flat',
            'discount_value': 50,
            'description': 'Flat ₹50 off for loyal customers',
            'valid_until': None,
            'active': True
        },
        {
            'id': 'coupon-2',
            'code': 'LOYALTY200',
            'discount_type': 'flat',
            'discount_value': 200,
            'description': 'Flat ₹200 off on bookings',
            'valid_until': None,
            'active': True
        },
        {
            'id': 'coupon-3',
            'code': 'LOYALTY500',
            'discount_type': 'flat',
            'discount_value': 500,
            'description': 'Flat ₹500 off on premium tours',
            'valid_until': None,
            'active': True
        },
        {
            'id': 'coupon-4',
            'code': 'FIRST10',
            'discount_type': 'percentage',
            'discount_value': 10,
            'description': '10% off for first booking',
            'valid_until': (datetime.now(timezone.utc) + timedelta(days=90)).isoformat(),
            'active': True
        }
    ]
    
    # Insert coupons
    await db.coupons.insert_many(coupons)
    print(f"✓ Inserted {len(coupons)} coupons")
    
    print("\n✓ Database seeded successfully!")
    client.close()

if __name__ == '__main__':
    asyncio.run(seed_database())
