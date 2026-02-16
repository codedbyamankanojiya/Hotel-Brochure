from django.contrib import messages
from django.shortcuts import render


def _site_context():
    return {
        'hotel_name': 'Hotel Aurora',
        'tagline': 'Boutique comfort in the heart of the city',
        'phone': '+91 98765 43210',
        'email': 'reservations@hotelaurora',
        'address': 'MG Road, Bengaluru, Karnataka, India',
    }


def home(request):
    context = {
        **_site_context(),
        'highlights': [
            {
                'title': 'Prime Location',
                'desc': 'Walkable to cafés, business hubs, and iconic city sights.',
            },
            {
                'title': 'Signature Rooms',
                'desc': 'Thoughtful interiors, premium linen, and serene lighting.',
            },
            {
                'title': 'Warm Hospitality',
                'desc': 'Front desk support and curated local recommendations.',
            },
        ],
        'featured_rooms': [
            {
                'name': 'Deluxe King',
                'meta': '1 King Bed • City View • 26 m²',
                'price': '₹4,999/night',
            },
            {
                'name': 'Executive Suite',
                'meta': 'Suite • Lounge Area • 42 m²',
                'price': '₹8,999/night',
            },
            {
                'name': 'Premium Twin',
                'meta': '2 Twin Beds • Quiet Floor • 28 m²',
                'price': '₹5,499/night',
            },
        ],
    }
    return render(request, 'brochure/home.html', context)


def rooms(request):
    context = {
        **_site_context(),
        'rooms': [
            {
                'name': 'Deluxe King',
                'image': 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1600&q=80',
                'desc': 'Ideal for couples and business travelers. Soft tones, work desk, and a relaxing city view.',
                'features': ['Wi‑Fi', 'Smart TV', 'Work desk', 'Rain shower'],
                'price': '₹4,999/night',
            },
            {
                'name': 'Premium Twin',
                'image': 'https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1600&q=80',
                'desc': 'Designed for comfort with twin bedding and extra storage for longer stays.',
                'features': ['Wi‑Fi', 'Smart TV', 'Extra wardrobe', 'Tea/coffee'],
                'price': '₹5,499/night',
            },
            {
                'name': 'Executive Suite',
                'image': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1600&q=80',
                'desc': 'A spacious suite with a lounge corner for meetings or winding down after the city.',
                'features': ['Wi‑Fi', 'Lounge area', 'Mini bar', 'Premium linen'],
                'price': '₹8,999/night',
            },
        ],
    }
    return render(request, 'brochure/rooms.html', context)


def amenities(request):
    context = {
        **_site_context(),
        'amenities': [
            {
                'title': 'All‑Day Dining',
                'desc': 'Fresh breakfast, comfort classics, and light evening bites.',
            },
            {
                'title': 'High‑Speed Wi‑Fi',
                'desc': 'Reliable connectivity for work calls and streaming.',
            },
            {
                'title': 'Airport Transfer',
                'desc': 'On‑request pickup and drop for a seamless arrival.',
            },
            {
                'title': 'Concierge Desk',
                'desc': 'Local guidance, reservations, and city experiences.',
            },
            {
                'title': 'Laundry Service',
                'desc': 'Same‑day options available for longer stays.',
            },
            {
                'title': '24×7 Support',
                'desc': 'Always‑on assistance from our front office team.',
            },
        ],
    }
    return render(request, 'brochure/amenities.html', context)


def gallery(request):
    context = {
        **_site_context(),
        'images': [
            {
                'title': 'Lobby',
                'hint': 'Soft lighting and modern accents',
                'src': 'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1600&q=80',
            },
            {
                'title': 'Deluxe Room',
                'hint': 'Relaxed, calm interior tones',
                'src': 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1600&q=80',
            },
            {
                'title': 'Dining',
                'hint': 'Bright, welcoming seating',
                'src': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1600&q=80',
            },
            {
                'title': 'Suite',
                'hint': 'Extra space for comfort',
                'src': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1600&q=80',
            },
            {
                'title': 'Corridor',
                'hint': 'Quiet floors, thoughtful design',
                'src': 'https://source.unsplash.com/JxAtP5ICHkg/1600x900',
            },
            {
                'title': 'City View',
                'hint': 'Morning light and skyline',
                'src': 'https://images.unsplash.com/photo-1445019980597-93fa8acb246c?auto=format&fit=crop&w=1600&q=80',
            },
        ],
    }
    return render(request, 'brochure/gallery.html', context)


def contact(request):
    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        email = (request.POST.get('email') or '').strip()
        message = (request.POST.get('message') or '').strip()

        if name and email and message:
            messages.success(request, 'Thanks! Your message has been received. We will get back to you soon.')
        else:
            messages.error(request, 'Please fill in your name, email, and message.')

    context = {
        **_site_context(),
    }
    return render(request, 'brochure/contact.html', context)
