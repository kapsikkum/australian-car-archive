"""
Wave 2 Deep-Dive Models Part 3 (Models 17 to 24):
17. alfa-romeo/giulia-gtv
18. fiat/500-abarth
19. land-rover/range-rover-discovery
20. jaguar/xj-xjs
21. chevrolet-gmsv/corvette-silverado
22. jeep/grand-cherokee
23. ldv/t60
24. proton/jumbuck-satria
"""
from typing import Dict, Any

WAVE2_MODELS_PART3: Dict[str, Dict[str, Any]] = {
    "alfa-romeo/giulia-gtv": {
        "make_slug": "alfa-romeo",
        "model_slug": "giulia-gtv",
        "name": "Giulia Sprint GT, GTV & Giulia Quadrifoglio",
        "vehicle_type": "Coupe / Sports Sedan",
        "segment": "Medium Luxury Sports Car",
        "years_sold_au": {"start": 1964, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The passionate soul of Italian motoring in Australia. Spanning from the Bertone-styled 105 Series Giulia Sprint GT and Bathurst-winning 1750/2000 GTV, through the transaxle Alfetta GTV6 Group A touring car, to the spine-tingling Busso V6 156 GTA and the modern Giorgio-platform Giulia Quadrifoglio with its Ferrari-derived 375kW twin-turbo V6.",
        "australian_market_notes": "First sold in Australia in 1964 (105 Series Giulia Sprint GT). The 105 GTV scored class wins in the Armstrong 500 at Bathurst. In the 1980s, Colin Bond and Alan Jones campaigned the howling Alfetta GTV6 in the Australian Touring Car Championship. The 952 Giulia Quadrifoglio set a production sedan benchmark at Mount Panorama.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "105/115 Series",
                "generation_name": "Giulia Sprint GT & GTV (105/115 Series)",
                "years": {"start": 1964, "end": "1976"},
                "body_styles": ["2-door coupe"],
                "platform": "Alfa Romeo 105 Series",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Masterpiece designed by Giorgetto Giugiaro for Bertone. Featured all-alloy twin-cam four-cylinder engines, twin Weber/Dell'Orto carburettors, 5-speed manual, four-wheel disc brakes, and Bathurst 500 class dominance.",
                "engines": [
                    {
                        "engine_code": "AR00512",
                        "name": "2.0L DOHC Twin-Cam Inline-4 (2000 GTV)",
                        "displacement_cc": 1962,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 97,
                        "power_rpm": "5500",
                        "torque_nm": 182,
                        "torque_rpm": "3000",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "DOHC 8-valve",
                        "notes": "Twin twin-choke Weber 40 DCOE carburettors, hemispherical combustion chambers."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "1750 GTV / 2000 GTV",
                        "years": {"start": 1968, "end": 1976},
                        "body_styles": ["2-door coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 5290,
                        "msrp_aud_max": 7990,
                        "fuel_consumption_l_100km": 9.9,
                        "kerb_weight_kg": 1040,
                        "standard_features": ["Campagnolo / Turbina alloy wheels", "Wood-rim steering wheel", "Quad headlights", "Limited slip differential (2000)"],
                        "notes": "Enduring Australian classic car icon."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "1750 GTV / 2000 GTV",
                        "body_style": "2-door coupe",
                        "engine_code": "AR00512",
                        "transmission": "5-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1971,
                        "years_end": 1976,
                        "msrp_aud": 6990,
                        "power_kw": 97,
                        "torque_nm": 182,
                        "fuel_l_100km": 9.9,
                        "towing_braked_kg": 800,
                        "notes": "2.0-litre twin-cam 105 Series GTV coupe."
                    }
                ]
            },
            {
                "series_code": "Alfetta GTV",
                "generation_name": "Alfetta GT, GTV & GTV6",
                "years": {"start": 1975, "end": 1987},
                "body_styles": ["2-door fastback coupe"],
                "platform": "Alfa Romeo Type 116 (Alfetta)",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Innovative 50:50 weight distribution chassis featuring a rear-mounted transaxle gearbox/clutch, inboard rear disc brakes, De Dion rear axle, 2.0L twin-cam, and the glorious 2.5L Busso V6 GTV6 raced in the ATCC by Colin Bond.",
                "engines": [
                    {
                        "engine_code": "AR01646",
                        "name": "2.5L SOHC 12V Busso V6 (GTV6)",
                        "displacement_cc": 2492,
                        "displacement_litres": 2.5,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 118,
                        "power_rpm": "5600",
                        "torque_nm": 213,
                        "torque_rpm": "4000",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "SOHC per bank 12-valve",
                        "notes": "Giuseppe Busso designed all-alloy 60-degree V6; Bosch L-Jetronic injection."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "GTV6 2.5",
                        "years": {"start": 1981, "end": 1987},
                        "body_styles": ["2-door fastback coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed rear transaxle manual"],
                        "msrp_aud_min": 24950,
                        "msrp_aud_max": 36900,
                        "fuel_consumption_l_100km": 10.8,
                        "kerb_weight_kg": 1210,
                        "standard_features": ["Bulged hood with black plastic insert", "Speedline alloy wheels", "Velour sports bucket seats", "Air conditioning", "Rear transaxle with 50:50 weight distribution"],
                        "notes": "Group A touring car weapon in Australian motorsport."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "GTV6 2.5",
                        "body_style": "2-door fastback coupe",
                        "engine_code": "AR01646",
                        "transmission": "5-speed rear transaxle manual",
                        "drivetrain": "RWD",
                        "years_start": 1981,
                        "years_end": 1987,
                        "msrp_aud": 29950,
                        "power_kw": 118,
                        "torque_nm": 213,
                        "fuel_l_100km": 10.8,
                        "towing_braked_kg": 1000,
                        "notes": "Busso V6 rear-transaxle sports coupe."
                    }
                ]
            },
            {
                "series_code": "952 Series",
                "generation_name": "Giulia & Giulia Quadrifoglio (Type 952)",
                "years": {"start": 2016, "end": "Present"},
                "body_styles": ["4-door sports sedan"],
                "platform": "FCA Giorgio",
                "ancap_rating": "5 stars",
                "summary": "Built on the clean-sheet Giorgio rear-wheel-drive platform with 50:50 weight distribution and carbon-fibre driveshaft. Features the 206kW Veloce and the halo Quadrifoglio powered by a 375kW 2.9L 90-degree twin-turbo V6 developed in collaboration with Ferrari engineers.",
                "engines": [
                    {
                        "engine_code": "670050436",
                        "name": "2.9L 90° Bi-Turbo V6 (Quadrifoglio)",
                        "displacement_cc": 2891,
                        "displacement_litres": 2.9,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 375,
                        "power_rpm": "6500",
                        "torque_nm": 600,
                        "torque_rpm": "2500-5000",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "All-aluminium 90-degree V6 derived from Ferrari F154 V8; cylinder deactivation."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Giulia Quadrifoglio",
                        "years": {"start": 2017, "end": "Present"},
                        "body_styles": ["4-door sports sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["8-speed ZF automatic"],
                        "msrp_aud_min": 143900,
                        "msrp_aud_max": 169500,
                        "fuel_consumption_l_100km": 8.2,
                        "kerb_weight_kg": 1585,
                        "standard_features": ["Carbon-fibre bonnet, roof, and driveshaft", "Active front carbon aero splitter", "Torque vectoring rear differential", "Sparco carbon race seats option", "Brembo carbon-ceramic brakes option"],
                        "notes": "0-100km/h in 3.9s. 510hp Italian super-sedan benchmark."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Giulia Quadrifoglio",
                        "body_style": "4-door sports sedan",
                        "engine_code": "670050436",
                        "transmission": "8-speed ZF automatic",
                        "drivetrain": "RWD",
                        "years_start": 2017,
                        "years_end": "Present",
                        "msrp_aud": 149900,
                        "power_kw": 375,
                        "torque_nm": 600,
                        "fuel_l_100km": 8.2,
                        "towing_braked_kg": 0,
                        "notes": "375kW Ferrari-developed twin-turbo V6 super-sedan."
                    }
                ]
            }
        ]
    },

    "fiat/500-abarth": {
        "make_slug": "fiat",
        "model_slug": "500-abarth",
        "name": "500 & Abarth 595/695",
        "vehicle_type": "Microcar / Hot Hatchback / Cabriolet",
        "segment": "Micro Car / Performance Hatchback",
        "years_sold_au": {"start": 1957, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The Italian style icon that charmed Australia. From the original rear-engined 500 'Bambino' that motorized post-war migrants and Australian urbanites, to the retro-chic 2008 rebirth (Typ 312) and the scorpion-badged Abarth 595 and 695 hot hatches with screaming Record Monza exhausts and Brembo brakes.",
        "australian_market_notes": "First sold in Australia in 1957 as the Nuova 500, where it was affectionately branded the 'Fiat Bambino'. The 2008 modern revival was an instant design sensation in Melbourne and Sydney. The performance Abarth range established a rabid enthusiast following for its unapologetic Italian acoustic drama.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Nuova 500",
                "generation_name": "Fiat 500 'Bambino' Nuova",
                "years": {"start": 1957, "end": 1975},
                "body_styles": ["2-door micro-saloon with fabric sunroof"],
                "platform": "Fiat 110",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Dante Giacosa's microcar masterpiece. Rear-mounted air-cooled 2-cylinder engine (479cc, 499cc, 594cc), suicide doors on early D models, and full-length folding canvas roof. Immensely popular in Australia as the Bambino.",
                "engines": [
                    {
                        "engine_code": "110F.000",
                        "name": "499cc Air-Cooled Inline-2",
                        "displacement_cc": 499,
                        "displacement_litres": 0.5,
                        "cylinders": 2,
                        "configuration": "Inline-2",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 13,
                        "power_rpm": "4000",
                        "torque_nm": 30,
                        "torque_rpm": "3200",
                        "compression_ratio": "7.1:1",
                        "valvetrain": "OHV 4-valve",
                        "notes": "Air-cooled vertical twin with single Weber carburettor."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "500 F / L 'Bambino'",
                        "years": {"start": 1965, "end": 1975},
                        "body_styles": ["2-door micro-saloon with fabric sunroof"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual (unsynchronised)"],
                        "msrp_aud_min": 1198,
                        "msrp_aud_max": 1498,
                        "fuel_consumption_l_100km": 5.2,
                        "kerb_weight_kg": 520,
                        "standard_features": ["Fabric rollback sunroof", "Front-hinged doors", "Chrome bumper overriders", "Vinyl bucket seats"],
                        "notes": "Affectionately known across Australia as the Fiat Bambino."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "500 F / L 'Bambino'",
                        "body_style": "2-door micro-saloon with fabric sunroof",
                        "engine_code": "110F.000",
                        "transmission": "4-speed manual (unsynchronised)",
                        "drivetrain": "RWD",
                        "years_start": 1965,
                        "years_end": 1975,
                        "msrp_aud": 1290,
                        "power_kw": 13,
                        "torque_nm": 30,
                        "fuel_l_100km": 5.2,
                        "towing_braked_kg": 0,
                        "notes": "Indispensable classic Italian microcar."
                    }
                ]
            },
            {
                "series_code": "Typ 312 Fiat 500",
                "generation_name": "Fiat 500 Modern Generation (Typ 312)",
                "years": {"start": 2008, "end": "Present"},
                "body_styles": ["3-door hatchback", "2-door cabriolet (500C)"],
                "platform": "Fiat Mini platform",
                "ancap_rating": "5 stars",
                "summary": "Modern retro design icon. Pop, Lounge, Dolcevita; 1.2L 8V, 1.4L 16V FIRE, innovative 0.9L TwinAir 2-cylinder turbo (63kW), and 1.0L GSE Mild Hybrid.",
                "engines": [
                    {
                        "engine_code": "312A2000",
                        "name": "0.9L TwinAir 2-Cylinder Turbo",
                        "displacement_cc": 875,
                        "displacement_litres": 0.9,
                        "cylinders": 2,
                        "configuration": "Inline-2",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 63,
                        "power_rpm": "5500",
                        "torque_nm": 145,
                        "torque_rpm": "1900",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "MultiAir electro-hydraulic variable intake",
                        "notes": "International Engine of the Year winner; charismatic twin-cylinder thrum."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "500 Lounge / Dolcevita",
                        "years": {"start": 2008, "end": "Present"},
                        "body_styles": ["3-door hatchback", "2-door cabriolet (500C)"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual", "5-speed Dualogic automated manual"],
                        "msrp_aud_min": 19990,
                        "msrp_aud_max": 27220,
                        "fuel_consumption_l_100km": 4.9,
                        "kerb_weight_kg": 930,
                        "standard_features": ["Fixed glass roof", "Body-colored dashboard panel", "7-inch Uconnect touchscreen", "Apple CarPlay / Android Auto", "15-inch alloy wheels"],
                        "notes": "Chic Australian inner-city favorite."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "500 Lounge / Dolcevita",
                        "body_style": "3-door hatchback",
                        "engine_code": "312A2000",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2011,
                        "years_end": "Present",
                        "msrp_aud": 22990,
                        "power_kw": 63,
                        "torque_nm": 145,
                        "fuel_l_100km": 4.9,
                        "towing_braked_kg": 800,
                        "notes": "TwinAir turbocharged urban hatchback."
                    }
                ]
            },
            {
                "series_code": "Typ 312 Abarth",
                "generation_name": "Abarth 500, 595 & 695",
                "years": {"start": 2009, "end": "Present"},
                "body_styles": ["3-door hatchback", "2-door cabriolet (595C)"],
                "platform": "Fiat Mini platform (Abarth tuned)",
                "ancap_rating": "5 stars",
                "summary": "Scorpion-badged pocket rocket. Powered by the 1.4L T-Jet turbocharged engine producing up to 132kW/140kW in the 595/695 Competizione and Biposto, equipped with Record Monza quad exhaust, Koni FSD dampers, and Brembo brakes.",
                "engines": [
                    {
                        "engine_code": "312B3000",
                        "name": "1.4L 16V T-Jet Turbo (Competizione)",
                        "displacement_cc": 1368,
                        "displacement_litres": 1.4,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 132,
                        "power_rpm": "5500",
                        "torque_nm": 250,
                        "torque_rpm": "3000",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Garrett GT1446 turbocharger; aggressive dual-mode exhaust."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Abarth 595 / 695 Competizione",
                        "years": {"start": 2012, "end": "Present"},
                        "body_styles": ["3-door hatchback", "2-door cabriolet (595C)"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual", "5-speed Dualogic automated manual"],
                        "msrp_aud_min": 34990,
                        "msrp_aud_max": 44990,
                        "fuel_consumption_l_100km": 6.5,
                        "kerb_weight_kg": 1035,
                        "standard_features": ["Record Monza active quad exhaust", "Brembo 4-piston front brakes", "Koni FSD dampers", "Sabelt carbon-backed sports bucket seats", "17-inch Formula / Montecarlo alloys"],
                        "notes": "0-100km/h in 6.7s. Concentrated Italian attitude and acoustic fireworks."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Abarth 595 / 695 Competizione",
                        "body_style": "3-door hatchback",
                        "engine_code": "312B3000",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2015,
                        "years_end": "Present",
                        "msrp_aud": 38990,
                        "power_kw": 132,
                        "torque_nm": 250,
                        "fuel_l_100km": 6.5,
                        "towing_braked_kg": 0,
                        "notes": "132kW Garrett-turbo manual pocket rocket."
                    }
                ]
            }
        ]
    },

    "land-rover/range-rover-discovery": {
        "make_slug": "land-rover",
        "model_slug": "range-rover-discovery",
        "name": "Range Rover & Discovery",
        "vehicle_type": "Large Luxury 4WD / Family SUV",
        "segment": "Large Luxury SUV",
        "years_sold_au": {"start": 1972, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The twin benchmarks of British luxury and all-terrain expedition mastery in Australia. The Range Rover created the luxury 4WD genre in 1972, proving that supreme off-road capability could coexist with peerless aristocratic comfort. The Land Rover Discovery launched in Australia in 1991, democratizing Range Rover technology into an iconic stepped-roof, 7-seat family adventurer.",
        "australian_market_notes": "First imported to Australia in 1972 with the 2-door Range Rover Classic. It quickly proved itself indispensable across pastoral stations and remote outback expeditions. Discovery 1 & 2 became beloved overland tourers, while Discovery 3 & 4 with Terrain Response and 3500kg towing became Australia's premier luxury caravan hauler.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Classic & P38A",
                "generation_name": "Range Rover Classic & P38A",
                "years": {"start": 1972, "end": 2002},
                "body_styles": ["2-door 4WD wagon", "4-door 4WD wagon"],
                "platform": "Range Rover Classic / P38A",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "The original luxury 4x4. Permanent four-wheel drive, all-coil spring suspension, aluminum body panels, Rover 3.5L/3.9L/4.6L V8s, and Electronic Air Suspension (EAS).",
                "engines": [
                    {
                        "engine_code": "Rover V8 3.9",
                        "name": "3.9L OHV V8 Petrol",
                        "displacement_cc": 3946,
                        "displacement_litres": 3.9,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 134,
                        "power_rpm": "4750",
                        "torque_nm": 304,
                        "torque_rpm": "2600",
                        "compression_ratio": "9.35:1",
                        "valvetrain": "OHV 16-valve",
                        "notes": "Lucas 14CUX electronic fuel injection; all-aluminium V8."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Range Rover Vogue",
                        "years": {"start": 1984, "end": 1996},
                        "body_styles": ["4-door 4WD wagon"],
                        "drivetrain": "4WD",
                        "transmissions": ["5-speed manual", "4-speed ZF automatic"],
                        "msrp_aud_min": 42990,
                        "msrp_aud_max": 99990,
                        "fuel_consumption_l_100km": 15.2,
                        "kerb_weight_kg": 1930,
                        "standard_features": ["Burr walnut wood trim", "Connolly leather upholstery", "Air suspension (late)", "Split rear tailgate", "Permanent 4WD with center diff lock"],
                        "notes": "Created the luxury 4WD category in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Range Rover Vogue",
                        "body_style": "4-door 4WD wagon",
                        "engine_code": "Rover V8 3.9",
                        "transmission": "4-speed ZF automatic",
                        "drivetrain": "4WD",
                        "years_start": 1989,
                        "years_end": 1996,
                        "msrp_aud": 69900,
                        "power_kw": 134,
                        "torque_nm": 304,
                        "fuel_l_100km": 15.2,
                        "towing_braked_kg": 3500,
                        "notes": "3.9L V8 fuel injected Vogue."
                    }
                ]
            },
            {
                "series_code": "Discovery 1 & 2",
                "generation_name": "Discovery Series I & II",
                "years": {"start": 1991, "end": 2004},
                "body_styles": ["5-door 4WD wagon"],
                "platform": "Land Rover Discovery 1 / T5",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Stepped roof, alpine roof glass, 7-seater packaging, Conran-designed interior, 3.9L V8, 300Tdi diesel, and Discovery 2 (1999) with Td5 5-cylinder turbo-diesel and Active Cornering Enhancement (ACE).",
                "engines": [
                    {
                        "engine_code": "Td5",
                        "name": "2.5L Turbo Diesel Inline-5",
                        "displacement_cc": 2495,
                        "displacement_litres": 2.5,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 101,
                        "power_rpm": "4200",
                        "torque_nm": 300,
                        "torque_rpm": "1950",
                        "compression_ratio": "19.5:1",
                        "valvetrain": "SOHC 10-valve with electronic unit injectors",
                        "notes": "Lucas electronic unit injectors, renowned for outback reliability."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Discovery Td5 / V8",
                        "years": {"start": 1999, "end": 2004},
                        "body_styles": ["5-door 4WD wagon"],
                        "drivetrain": "4WD",
                        "transmissions": ["5-speed manual", "4-speed ZF automatic"],
                        "msrp_aud_min": 44990,
                        "msrp_aud_max": 65990,
                        "fuel_consumption_l_100km": 9.4,
                        "kerb_weight_kg": 2150,
                        "standard_features": ["7-passenger seating", "Dual electric glass sunroofs", "Electronic Traction Control", "Hill Descent Control", "ACE hydraulic active anti-roll"],
                        "notes": "Australia's overland adventure favorite."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Discovery Td5 / V8",
                        "body_style": "5-door 4WD wagon",
                        "engine_code": "Td5",
                        "transmission": "4-speed ZF automatic",
                        "drivetrain": "4WD",
                        "years_start": 1999,
                        "years_end": 2004,
                        "msrp_aud": 52900,
                        "power_kw": 101,
                        "torque_nm": 300,
                        "fuel_l_100km": 9.4,
                        "towing_braked_kg": 3500,
                        "notes": "5-cylinder turbo-diesel Discovery 2."
                    }
                ]
            },
            {
                "series_code": "Discovery 3 & 4",
                "generation_name": "Discovery 3 & 4 (Terrain Response Era)",
                "years": {"start": 2004, "end": 2016},
                "body_styles": ["5-door 4WD wagon"],
                "platform": "Land Rover Integrated Body Frame (T5)",
                "ancap_rating": "4 stars",
                "summary": "Pioneered the patented Terrain Response rotary system, cross-linked air suspension, integrated body-frame chassis, and the twin-turbo 3.0L SDV6 diesel delivering 183kW and 600Nm. Regarded as one of the finest all-round touring vehicles ever sold in Australia.",
                "engines": [
                    {
                        "engine_code": "306DT",
                        "name": "3.0L SDV6 Twin-Turbo Diesel V6",
                        "displacement_cc": 2993,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 183,
                        "power_rpm": "4000",
                        "torque_nm": 600,
                        "torque_rpm": "2000",
                        "compression_ratio": "16.0:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Parallel-sequential turbochargers; huge torque delivery for towing."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Discovery 4 SDV6 SE / HSE",
                        "years": {"start": 2009, "end": 2016},
                        "body_styles": ["5-door 4WD wagon"],
                        "drivetrain": "4WD",
                        "transmissions": ["6-speed automatic", "8-speed ZF automatic"],
                        "msrp_aud_min": 68490,
                        "msrp_aud_max": 95900,
                        "fuel_consumption_l_100km": 8.0,
                        "kerb_weight_kg": 2565,
                        "standard_features": ["Terrain Response rotary dial", "Height-adjustable air suspension", "7 full-sized adult seats", "3,500kg towing capacity", "Harman Kardon LOGIC7 sound"],
                        "notes": "The benchmark luxury caravan tow vehicle in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Discovery 4 SDV6 SE / HSE",
                        "body_style": "5-door 4WD wagon",
                        "engine_code": "306DT",
                        "transmission": "8-speed ZF automatic",
                        "drivetrain": "4WD",
                        "years_start": 2012,
                        "years_end": 2016,
                        "msrp_aud": 84900,
                        "power_kw": 183,
                        "torque_nm": 600,
                        "fuel_l_100km": 8.0,
                        "towing_braked_kg": 3500,
                        "notes": "600Nm 8-speed ZF automatic touring legend."
                    }
                ]
            },
            {
                "series_code": "L460 & Discovery 5",
                "generation_name": "Modern Range Rover (L460) & Discovery 5",
                "years": {"start": 2017, "end": "Present"},
                "body_styles": ["5-door 4WD wagon", "Long Wheelbase 7-seat (L460 LWB)"],
                "platform": "Jaguar Land Rover MLA-Flex / PLA",
                "ancap_rating": "5 stars",
                "summary": "Ultra-lightweight aerospace aluminium architecture. Range Rover L460 features four-wheel steering, P530 4.4L twin-turbo BMW V8 (390kW 750Nm), while Discovery 5 brings family versatility with D300 Ingenium 3.0L inline-6 twin-turbo diesel and 3,500kg towing.",
                "engines": [
                    {
                        "engine_code": "N63-JLR",
                        "name": "4.4L Twin-Turbo V8 (Range Rover P530)",
                        "displacement_cc": 4395,
                        "displacement_litres": 4.4,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 390,
                        "power_rpm": "5500-6000",
                        "torque_nm": 750,
                        "torque_rpm": "1800-4600",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "Twin-scroll turbochargers inside vee; 0-100km/h in 4.6s."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Range Rover P530 Autobiography",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["5-door 4WD wagon", "Long Wheelbase 7-seat (L460 LWB)"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed ZF automatic"],
                        "msrp_aud_min": 250000,
                        "msrp_aud_max": 395000,
                        "fuel_consumption_l_100km": 11.8,
                        "kerb_weight_kg": 2585,
                        "standard_features": ["All-wheel steering (7.3 degrees rear lock)", "Electronic air suspension with Dynamic Response Pro", "Meridian Signature 35-speaker sound with active noise cancelling", "Executive Class rear seating"],
                        "notes": "Pinnacle of luxury all-terrain travel."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Range Rover P530 Autobiography",
                        "body_style": "5-door 4WD wagon",
                        "engine_code": "N63-JLR",
                        "transmission": "8-speed ZF automatic",
                        "drivetrain": "AWD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 315000,
                        "power_kw": 390,
                        "torque_nm": 750,
                        "fuel_l_100km": 11.8,
                        "towing_braked_kg": 3500,
                        "notes": "390kW twin-turbo V8 luxury flagship."
                    }
                ]
            }
        ]
    },

    "jaguar/xj-xjs": {
        "make_slug": "jaguar",
        "model_slug": "xj-xjs",
        "name": "XJ & XJ-S",
        "vehicle_type": "Large Luxury Sedan / Grand Tourer Coupe",
        "segment": "Upper Large Luxury Car",
        "years_sold_au": {"start": 1969, "end": "2019"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The apex of British automotive grandeur and motorsport glory. Sir William Lyons' XJ6 was declared the finest riding saloon in the world upon its Australian release, while the V12 XJ12 and XJ-S grand tourer achieved immortality when Tom Walkinshaw Racing's Jaguar XJS V12 conquered Mount Panorama to win the 1985 Bathurst 1000. Evolved through supercharged XJR flagships to the bonded-aluminium X350 and avant-garde X351.",
        "australian_market_notes": "First sold in Australia in 1969 (XJ6 Series I). In October 1985, John Goss and Armin Hahne drove the TWR Jaguar XJ-S V12 to an iconic outright victory in the James Hardie 1000 at Bathurst, breaking Australian V8 dominance. Australia has consistently been one of Jaguar's most passionate markets for supercharged XJR models.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Series I-III",
                "generation_name": "Jaguar XJ6 & XJ12 (Series I, II, III)",
                "years": {"start": 1969, "end": 1992},
                "body_styles": ["4-door sedan"],
                "platform": "Jaguar XJ",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Sir William Lyons' masterpiece. Revered for its sublime ride and handling balance, independent rear suspension isolated in rubber subframe, 4.2L XK straight-six, and the legendary 5.3L V12 (1972 world's first mass-produced 12-cylinder 4-door sedan).",
                "engines": [
                    {
                        "engine_code": "XK 4.2",
                        "name": "4.2L DOHC Inline-6",
                        "displacement_cc": 4235,
                        "displacement_litres": 4.2,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 153,
                        "power_rpm": "5000",
                        "torque_nm": 384,
                        "torque_rpm": "3000",
                        "compression_ratio": "8.7:1",
                        "valvetrain": "DOHC 12-valve",
                        "notes": "Twin SU / Zenith-Stromberg carburettors; later Bosch-Lucas L-Jetronic."
                    },
                    {
                        "engine_code": "Jaguar V12 5.3",
                        "name": "5.3L SOHC 24V V12 (XJ12)",
                        "displacement_cc": 5343,
                        "displacement_litres": 5.3,
                        "cylinders": 12,
                        "configuration": "V12",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 213,
                        "power_rpm": "5750",
                        "torque_nm": 412,
                        "torque_rpm": "3500",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "SOHC per bank 24-valve",
                        "notes": "All-aluminium 60-degree V12 of turbine-like smoothness."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "XJ6 / Sovereign 4.2",
                        "years": {"start": 1969, "end": 1987},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual with overdrive", "3-speed BorgWarner automatic"],
                        "msrp_aud_min": 8990,
                        "msrp_aud_max": 74900,
                        "fuel_consumption_l_100km": 14.8,
                        "kerb_weight_kg": 1740,
                        "standard_features": ["Connolly leather seating", "Burr walnut veneer", "Power steering", "Twin fuel tanks with changeover switch"],
                        "notes": "The benchmark luxury saloon in Australia."
                    },
                    {
                        "badge_name": "XJ12 / Double Six",
                        "years": {"start": 1972, "end": 1992},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["3-speed automatic (GM TH400)"],
                        "msrp_aud_min": 14500,
                        "msrp_aud_max": 115000,
                        "fuel_consumption_l_100km": 17.5,
                        "kerb_weight_kg": 1860,
                        "standard_features": ["5.3L V12 engine", "Air conditioning", "Chrome wire wheels option", "Fluted grille", "Independent rear suspension"],
                        "notes": "Aristocratic 12-cylinder flagship."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "XJ12 / Double Six",
                        "body_style": "4-door sedan",
                        "engine_code": "Jaguar V12 5.3",
                        "transmission": "3-speed automatic (GM TH400)",
                        "drivetrain": "RWD",
                        "years_start": 1972,
                        "years_end": 1992,
                        "msrp_aud": 89000,
                        "power_kw": 213,
                        "torque_nm": 412,
                        "fuel_l_100km": 17.5,
                        "towing_braked_kg": 1500,
                        "notes": "5.3L V12 luxury sedan."
                    }
                ]
            },
            {
                "series_code": "XJ-S / XJS",
                "generation_name": "Jaguar XJ-S & XJS V12 (Bathurst 1000 Winner)",
                "years": {"start": 1976, "end": 1996},
                "body_styles": ["2-door coupe", "2-door cabriolet"],
                "platform": "Jaguar XJ-S",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Iconic British grand tourer with flying buttress aerodynamic pillars, 5.3L / 6.0L HE V12, and 4.0L AJ6 inline-six. Etched into Australian motorsport history when Tom Walkinshaw Racing's Jaguar XJ-S V12 driven by John Goss and Armin Hahne scored outright victory in the 1985 Bathurst 1000.",
                "engines": [
                    {
                        "engine_code": "V12-HE",
                        "name": "5.3L High Efficiency V12",
                        "displacement_cc": 5343,
                        "displacement_litres": 5.3,
                        "cylinders": 12,
                        "configuration": "V12",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 220,
                        "power_rpm": "5500",
                        "torque_nm": 430,
                        "torque_rpm": "3000",
                        "compression_ratio": "12.5:1",
                        "valvetrain": "SOHC per bank 24-valve",
                        "notes": "May fireball high-compression swirl combustion chambers; 360kW+ in TWR Group A race guise."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "XJ-S V12 Coupe",
                        "years": {"start": 1976, "end": 1996},
                        "body_styles": ["2-door coupe", "2-door cabriolet"],
                        "drivetrain": "RWD",
                        "transmissions": ["3-speed GM400 automatic", "4-speed GM4L80-E automatic"],
                        "msrp_aud_min": 31500,
                        "msrp_aud_max": 195000,
                        "fuel_consumption_l_100km": 15.8,
                        "kerb_weight_kg": 1780,
                        "standard_features": ["Flying buttress C-pillars", "Connolly leather sports seats", "Starfish alloy wheels", "Climate control", "Burr elm/walnut veneer"],
                        "notes": "Won the 1985 Bathurst 1000 with John Goss and Armin Hahne."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "XJ-S V12 Coupe",
                        "body_style": "2-door coupe",
                        "engine_code": "V12-HE",
                        "transmission": "3-speed GM400 automatic",
                        "drivetrain": "RWD",
                        "years_start": 1981,
                        "years_end": 1991,
                        "msrp_aud": 98500,
                        "power_kw": 220,
                        "torque_nm": 430,
                        "fuel_l_100km": 15.8,
                        "towing_braked_kg": 1500,
                        "notes": "5.3-litre HE V12 grand tourer."
                    }
                ]
            },
            {
                "series_code": "X300/X308 XJR",
                "generation_name": "Jaguar XJR Supercharged (X300 & X308)",
                "years": {"start": 1994, "end": "2003"},
                "body_styles": ["4-door sedan"],
                "platform": "Jaguar X300 / X308",
                "ancap_rating": "4 stars",
                "summary": "Introduced factory supercharging to Jaguar. The X300 XJR (1994-1997) featured the 240kW 4.0L Eaton-supercharged AJ16 straight-six, while the X308 XJR (1998-2003) unleashed the 276kW (370hp) AJ-V8 supercharged engine.",
                "engines": [
                    {
                        "engine_code": "AJ26S",
                        "name": "4.0L Supercharged 32V V8 (X308 XJR)",
                        "displacement_cc": 3996,
                        "displacement_litres": 4.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Supercharged",
                        "fuel_type": "Petrol",
                        "power_kw": 276,
                        "power_rpm": "6150",
                        "torque_nm": 525,
                        "torque_rpm": "3600",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "Eaton M112 roots supercharger with dual air-to-water intercoolers."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "XJR Supercharged",
                        "years": {"start": 1998, "end": 2003},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed Mercedes 5G-Tronic automatic"],
                        "msrp_aud_min": 178000,
                        "msrp_aud_max": 189000,
                        "fuel_consumption_l_100km": 12.9,
                        "kerb_weight_kg": 1775,
                        "standard_features": ["Mesh front grille in body color", "18-inch Asteroid alloys", "Sport tuned CATS active suspension", "Dark stained bird's eye maple veneer", "Brembo brake package option"],
                        "notes": "0-100km/h in 5.3s. Supercharged sports saloon."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "XJR Supercharged",
                        "body_style": "4-door sedan",
                        "engine_code": "AJ26S",
                        "transmission": "5-speed Mercedes 5G-Tronic automatic",
                        "drivetrain": "RWD",
                        "years_start": 1998,
                        "years_end": 2003,
                        "msrp_aud": 182000,
                        "power_kw": 276,
                        "torque_nm": 525,
                        "fuel_l_100km": 12.9,
                        "towing_braked_kg": 1900,
                        "notes": "276kW supercharged V8 super-sedan."
                    }
                ]
            },
            {
                "series_code": "X350/X351",
                "generation_name": "Jaguar XJ Aluminum Era (X350 & X351)",
                "years": {"start": 2003, "end": "2019"},
                "body_styles": ["4-door sedan", "Long Wheelbase (LWB)"],
                "platform": "Jaguar Aluminium Monocoque",
                "ancap_rating": "5 stars",
                "summary": "Riveted and bonded aerospace aluminium monocoque reducing weight by 200kg. Progressed to the dramatic Ian Callum-designed X351, culminating in the ferocious XJR575 with 423kW (575hp) 5.0L supercharged V8.",
                "engines": [
                    {
                        "engine_code": "AJ133S",
                        "name": "5.0L Supercharged V8 (XJR575)",
                        "displacement_cc": 5000,
                        "displacement_litres": 5.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Supercharged",
                        "fuel_type": "Petrol",
                        "power_kw": 423,
                        "power_rpm": "6500",
                        "torque_nm": 700,
                        "torque_rpm": "3500-5000",
                        "compression_ratio": "9.5:1",
                        "valvetrain": "DOHC 32-valve variable camshaft timing",
                        "notes": "Twin-vortex Roots-type supercharger; 0-100km/h in 4.4 seconds."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "XJR / XJR575",
                        "years": {"start": 2013, "end": 2019},
                        "body_styles": ["4-door sedan", "Long Wheelbase (LWB)"],
                        "drivetrain": "RWD",
                        "transmissions": ["8-speed ZF automatic"],
                        "msrp_aud_min": 298000,
                        "msrp_aud_max": 315000,
                        "fuel_consumption_l_100km": 11.6,
                        "kerb_weight_kg": 1875,
                        "standard_features": ["20-inch Farallon gloss black alloys", "Active electronic differential", "Red brake calipers with 380mm front discs", "Quilted leather sport seats with 575 embroidery", "Meridian 825W surround sound"],
                        "notes": "The 575hp grand finale of the petrol XJ lineage."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "XJR / XJR575",
                        "body_style": "4-door sedan",
                        "engine_code": "AJ133S",
                        "transmission": "8-speed ZF automatic",
                        "drivetrain": "RWD",
                        "years_start": 2017,
                        "years_end": 2019,
                        "msrp_aud": 305000,
                        "power_kw": 423,
                        "torque_nm": 700,
                        "fuel_l_100km": 11.6,
                        "towing_braked_kg": 2000,
                        "notes": "423kW 5.0L supercharged V8 limousine."
                    }
                ]
            }
        ]
    },

    "chevrolet-gmsv/corvette-silverado": {
        "make_slug": "chevrolet-gmsv",
        "model_slug": "corvette-silverado",
        "name": "Corvette & Silverado",
        "vehicle_type": "Mid-Engine Supercar / Full-Size Pickup Truck",
        "segment": "High Performance Supercar / Full-Size Pickup",
        "years_sold_au": {"start": 2020, "end": "Present"},
        "locally_built": True,
        "assembly_plants_au": ["Clayton, Victoria (Walkinshaw Automotive Group RHD Remanufacturing, 2020-Present)"],
        "overview": "The modern pillars of General Motors in Australia under GM Specialty Vehicles (GMSV). The eighth-generation C8 Corvette arrived as the world's first factory right-hand drive Corvette directly from the Bowling Green assembly line, offering mid-engine supercar performance and the spine-tingling 500kW flat-plane crank Z06. Alongside it, the Chevrolet Silverado 1500 and 2500HD are remanufactured to RHD in Melbourne by Walkinshaw Automotive Group, delivering up to 1,322Nm of Duramax V8 torque and heavy towing capability.",
        "australian_market_notes": "Established following the retirement of Holden in 2020. The C8 Corvette created feverish Australian demand with multi-year waiting lists. Concurrently, Walkinshaw Automotive Group remanufactures hundreds of Silverado 1500 and 2500HD pickups monthly at its dedicated Clayton facility in Melbourne.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "C8 Corvette",
                "generation_name": "Chevrolet Corvette C8 (Stingray & Z06)",
                "years": {"start": 2021, "end": "Present"},
                "body_styles": ["2-door coupe (removable targa roof)", "2-door retractable hardtop convertible"],
                "platform": "GM Y2XX",
                "ancap_rating": "Unrated (Supercar)",
                "summary": "First factory right-hand drive Corvette in history. Mid-engine aluminium structure, Stingray (6.2L LT2 naturally aspirated V8 369kW 637Nm, 8-speed Tremec DCT), and the ferocious Z06 powered by the 5.5L LT6 flat-plane crank naturally aspirated V8 producing 500kW at 8,400rpm.",
                "engines": [
                    {
                        "engine_code": "LT2",
                        "name": "6.2L Small Block V8 (Stingray)",
                        "displacement_cc": 6162,
                        "displacement_litres": 6.2,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 369,
                        "power_rpm": "6450",
                        "torque_nm": 637,
                        "torque_rpm": "5150",
                        "compression_ratio": "11.5:1",
                        "valvetrain": "OHV 16-valve with Variable Valve Timing",
                        "notes": "Dry sump lubrication with 3 scavenge pumps; standard sports exhaust on AU models."
                    },
                    {
                        "engine_code": "LT6",
                        "name": "5.5L Flat-Plane Crank DOHC V8 (Z06)",
                        "displacement_cc": 5463,
                        "displacement_litres": 5.5,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 500,
                        "power_rpm": "8400",
                        "torque_nm": 623,
                        "torque_rpm": "6300",
                        "compression_ratio": "12.5:1",
                        "valvetrain": "DOHC 32-valve with finger-follower valvetrain",
                        "notes": "Most powerful naturally aspirated production V8 ever made; 8600rpm redline."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "C8 Stingray 2LT / 3LT",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["2-door coupe (removable targa roof)", "2-door retractable hardtop convertible"],
                        "drivetrain": "RWD",
                        "transmissions": ["8-speed Tremec dual-clutch"],
                        "msrp_aud_min": 144990,
                        "msrp_aud_max": 190000,
                        "fuel_consumption_l_100km": 12.3,
                        "kerb_weight_kg": 1530,
                        "standard_features": ["Z51 Performance Package (electronic LSD, Brembo brakes, performance exhaust)", "Magnetic Selective Ride Control", "GT2 bucket seats in Nappa leather", "Front lift with memory", "Bose 14-speaker sound"],
                        "notes": "0-100km/h in 3.0s. Factory right-hand drive supercar bargain."
                    },
                    {
                        "badge_name": "C8 Z06",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["2-door coupe (removable targa roof)", "2-door retractable hardtop convertible"],
                        "drivetrain": "RWD",
                        "transmissions": ["8-speed Tremec dual-clutch"],
                        "msrp_aud_min": 336000,
                        "msrp_aud_max": 395000,
                        "fuel_consumption_l_100km": 15.1,
                        "kerb_weight_kg": 1560,
                        "standard_features": ["5.5L LT6 flat-plane V8 (670hp)", "94mm wider bodywork", "20-inch front / 21-inch rear forged wheels with 345-width rear Michelin Cup 2 tyres", "Carbon ceramic Brembo brakes", "Carbon fibre aero package"],
                        "notes": "0-100km/h in 2.6s. Pure naturally aspirated 8600rpm thunder."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "C8 Stingray 2LT / 3LT",
                        "body_style": "2-door coupe (removable targa roof)",
                        "engine_code": "LT2",
                        "transmission": "8-speed Tremec dual-clutch",
                        "drivetrain": "RWD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 160000,
                        "power_kw": 369,
                        "torque_nm": 637,
                        "fuel_l_100km": 12.3,
                        "towing_braked_kg": 0,
                        "notes": "Factory right-hand drive mid-engine Corvette Stingray."
                    },
                    {
                        "badge_name": "C8 Z06",
                        "body_style": "2-door coupe (removable targa roof)",
                        "engine_code": "LT6",
                        "transmission": "8-speed Tremec dual-clutch",
                        "drivetrain": "RWD",
                        "years_start": 2023,
                        "years_end": "Present",
                        "msrp_aud": 336000,
                        "power_kw": 500,
                        "torque_nm": 623,
                        "fuel_l_100km": 15.1,
                        "towing_braked_kg": 0,
                        "notes": "500kW 8600rpm flat-plane crank supercar."
                    }
                ]
            },
            {
                "series_code": "Silverado 1500",
                "generation_name": "Chevrolet Silverado 1500 (LTZ & ZR2)",
                "years": {"start": 2020, "end": "Present"},
                "body_styles": ["4-door Crew Cab Pickup"],
                "platform": "GM T1XX",
                "ancap_rating": "Unrated (Remanufactured)",
                "summary": "Full-size American pickup remanufactured from LHD to RHD in Melbourne by Walkinshaw Automotive Group. Powered by the 6.2L EcoTec3 V8 (313kW/624Nm) with 10-speed auto, 4,500kg braked towing, luxury LTZ Premium, and hardcore off-road ZR2 with Multimatic DSSV spool-valve dampers.",
                "engines": [
                    {
                        "engine_code": "L87",
                        "name": "6.2L EcoTec3 V8",
                        "displacement_cc": 6162,
                        "displacement_litres": 6.2,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 313,
                        "power_rpm": "5600",
                        "torque_nm": 624,
                        "torque_rpm": "4100",
                        "compression_ratio": "11.5:1",
                        "valvetrain": "OHV 16-valve with Dynamic Fuel Management (DFM)",
                        "notes": "Aluminium block and heads; can shut down up to 7 cylinders for fuel economy."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Silverado 1500 LTZ Premium",
                        "years": {"start": 2020, "end": "Present"},
                        "body_styles": ["4-door Crew Cab Pickup"],
                        "drivetrain": "4WD",
                        "transmissions": ["10-speed automatic"],
                        "msrp_aud_min": 106990,
                        "msrp_aud_max": 130500,
                        "fuel_consumption_l_100km": 12.8,
                        "kerb_weight_kg": 2540,
                        "standard_features": ["13.4-inch touchscreen display", "12.3-inch digital instrument cluster", "Bose premium audio", "4,500kg towing package with integrated brake controller", "Heated and ventilated leather seats"],
                        "notes": "Remanufactured in Clayton by Walkinshaw for GMSV."
                    },
                    {
                        "badge_name": "Silverado 1500 ZR2",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["4-door Crew Cab Pickup"],
                        "drivetrain": "4WD",
                        "transmissions": ["10-speed automatic"],
                        "msrp_aud_min": 124000,
                        "msrp_aud_max": 138000,
                        "fuel_consumption_l_100km": 13.5,
                        "kerb_weight_kg": 2575,
                        "standard_features": ["Multimatic DSSV spool-valve dampers", "Front and rear electronic locking differentials", "High-approach steel front bumper", "33-inch Goodyear Wrangler Territory MT tyres", "Black hood insert and ZR2 grille badge"],
                        "notes": "Hardcore off-road full-size truck."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Silverado 1500 LTZ Premium",
                        "body_style": "4-door Crew Cab Pickup",
                        "engine_code": "L87",
                        "transmission": "10-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2020,
                        "years_end": "Present",
                        "msrp_aud": 121000,
                        "power_kw": 313,
                        "torque_nm": 624,
                        "fuel_l_100km": 12.8,
                        "towing_braked_kg": 4500,
                        "notes": "4500kg towing capacity Walkinshaw remanufactured V8 truck."
                    },
                    {
                        "badge_name": "Silverado 1500 ZR2",
                        "body_style": "4-door Crew Cab Pickup",
                        "engine_code": "L87",
                        "transmission": "10-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 133000,
                        "power_kw": 313,
                        "torque_nm": 624,
                        "fuel_l_100km": 13.5,
                        "towing_braked_kg": 4200,
                        "notes": "Multimatic DSSV damper equipped off-road truck."
                    }
                ]
            },
            {
                "series_code": "Silverado 2500HD",
                "generation_name": "Chevrolet Silverado 2500HD Duramax",
                "years": {"start": 2021, "end": "Present"},
                "body_styles": ["4-door Crew Cab Heavy Duty Pickup"],
                "platform": "GM T1XX Heavy Duty",
                "ancap_rating": "Unrated (Commercial Heavy Duty)",
                "summary": "Commercial heavy-duty pickup remanufactured by Walkinshaw in Clayton. Powered by the 6.6L Duramax Turbo-Diesel V8 generating 350kW and a colossal 1,322Nm of torque, paired with an Allison 10-speed automatic transmission. Can tow up to 9,000kg with fifth-wheel / gooseneck attachment.",
                "engines": [
                    {
                        "engine_code": "L5P",
                        "name": "6.6L Duramax Turbo-Diesel V8",
                        "displacement_cc": 6619,
                        "displacement_litres": 6.6,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 350,
                        "power_rpm": "2800",
                        "torque_nm": 1322,
                        "torque_rpm": "1600-2800",
                        "compression_ratio": "16.0:1",
                        "valvetrain": "OHV 32-valve",
                        "notes": "Variable-geometry turbocharger with integrated exhaust brake; Allison 10-speed."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Silverado 2500HD LTZ Premium",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["4-door Crew Cab Heavy Duty Pickup"],
                        "drivetrain": "4WD",
                        "transmissions": ["Allison 10-speed automatic"],
                        "msrp_aud_min": 144990,
                        "msrp_aud_max": 163000,
                        "fuel_consumption_l_100km": 14.5,
                        "kerb_weight_kg": 3750,
                        "standard_features": ["Duramax 6.6L Turbo-Diesel V8 (1322Nm)", "Allison 10-speed automatic", "StabiliTrak with trailer sway control", "Up to 15 camera views including transparent trailer mode", "Electric power tailgate"],
                        "notes": "Heavy tow king for massive horse floats and machinery trailers."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Silverado 2500HD LTZ Premium",
                        "body_style": "4-door Crew Cab Heavy Duty Pickup",
                        "engine_code": "L5P",
                        "transmission": "Allison 10-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 155000,
                        "power_kw": 350,
                        "torque_nm": 1322,
                        "fuel_l_100km": 14.5,
                        "towing_braked_kg": 4500,
                        "notes": "1322Nm Duramax V8 with Allison 10-speed transmission (up to 9000kg 5th wheel)."
                    }
                ]
            }
        ]
    },

    "jeep/grand-cherokee": {
        "make_slug": "jeep",
        "model_slug": "grand-cherokee",
        "name": "Grand Cherokee",
        "vehicle_type": "Large SUV",
        "segment": "Large SUV",
        "years_sold_au": {"start": 1996, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The American flagship that revolutionized Australia's large SUV market. Across five generations (ZJ, WJ, WK, WK2, and WL), the Grand Cherokee blended authentic Jeep trail capability with luxury appointments, muscular HEMI V8s, efficient 3.0L diesels with 3,500kg towing, and the earth-shattering 522kW Grand Cherokee Trackhawk.",
        "australian_market_notes": "Introduced in 1996 with the ZJ. The WK2 generation (2011-2021) was an unprecedented commercial triumph in Australia, regularly challenging the Toyota Prado as Australia's favorite large SUV thanks to its 3,500kg towing capacity. In 2018, Jeep delivered the Trackhawk—a supercharged 522kW (707hp) Hellcat-powered SUV that became an instant Australian cult icon.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "WJ",
                "generation_name": "Grand Cherokee Second Generation (WJ)",
                "years": {"start": 1999, "end": 2005},
                "body_styles": ["5-door SUV"],
                "platform": "Jeep WJ Uniframe",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Sophisticated Uniframe construction, Quadra-Drive full-time 4WD with Vari-Lok gerotor progressive axles, 4.0L straight-six, 4.7L PowerTech V8, and Mercedes-sourced 2.7 CRD 5-cylinder turbo-diesel.",
                "engines": [
                    {
                        "engine_code": "PowerTech 4.7",
                        "name": "4.7L SOHC V8 Petrol",
                        "displacement_cc": 4701,
                        "displacement_litres": 4.7,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 164,
                        "power_rpm": "4600",
                        "torque_nm": 400,
                        "torque_rpm": "3200",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "SOHC 16-valve",
                        "notes": "Cast iron block with aluminium cylinder heads; upgraded to 175kW High Output."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Laredo / Limited 4.7 V8",
                        "years": {"start": 1999, "end": 2005},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "4WD",
                        "transmissions": ["4-speed automatic", "5-speed automatic (545RFE)"],
                        "msrp_aud_min": 45990,
                        "msrp_aud_max": 62990,
                        "fuel_consumption_l_100km": 15.6,
                        "kerb_weight_kg": 1890,
                        "standard_features": ["Quadra-Drive 4WD with Vari-Lok progressive axles", "Leather upholstery (Limited)", "Infinity gold audio system", "Dual-zone climate control"],
                        "notes": "Core American luxury 4WD."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Laredo / Limited 4.7 V8",
                        "body_style": "5-door SUV",
                        "engine_code": "PowerTech 4.7",
                        "transmission": "5-speed automatic (545RFE)",
                        "drivetrain": "4WD",
                        "years_start": 2001,
                        "years_end": 2005,
                        "msrp_aud": 56900,
                        "power_kw": 164,
                        "torque_nm": 400,
                        "fuel_l_100km": 15.6,
                        "towing_braked_kg": 3360,
                        "notes": "Quadra-Drive 4.7 V8 luxury 4x4."
                    }
                ]
            },
            {
                "series_code": "WK2",
                "generation_name": "Grand Cherokee Fourth Generation (WK2 & Trackhawk)",
                "years": {"start": 2011, "end": 2022},
                "body_styles": ["5-door SUV"],
                "platform": "Chrysler WK2",
                "ancap_rating": "5 stars",
                "summary": "Australian sales sensation. Co-developed with Mercedes-Benz ML platform, independent suspension, 3.6L Pentastar V6, 3.0L EcoDiesel V6 (184kW/570Nm, 3500kg towing), 5.7L HEMI V8, SRT 6.4L HEMI (344kW), and the legendary 522kW supercharged Trackhawk.",
                "engines": [
                    {
                        "engine_code": "A630",
                        "name": "3.0L V6 EcoDiesel (VM Motori)",
                        "displacement_cc": 2987,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 184,
                        "power_rpm": "4000",
                        "torque_nm": 570,
                        "torque_rpm": "2000",
                        "compression_ratio": "16.5:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Class-leading 3500kg towing capacity with sub-8.0L/100km highway economy."
                    },
                    {
                        "engine_code": "Hellcat 6.2",
                        "name": "6.2L Supercharged HEMI V8 (Trackhawk)",
                        "displacement_cc": 6166,
                        "displacement_litres": 6.2,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Supercharged",
                        "fuel_type": "Petrol",
                        "power_kw": 522,
                        "power_rpm": "6000",
                        "torque_nm": 868,
                        "torque_rpm": "4800",
                        "compression_ratio": "9.5:1",
                        "valvetrain": "OHV 16-valve",
                        "notes": "2.38-litre IHI twin-screw supercharger delivering 11.6psi boost; 707 horsepower."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Overland 3.0 CRD",
                        "years": {"start": 2011, "end": 2021},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "4WD",
                        "transmissions": ["8-speed ZF automatic"],
                        "msrp_aud_min": 65000,
                        "msrp_aud_max": 79950,
                        "fuel_consumption_l_100km": 7.5,
                        "kerb_weight_kg": 2327,
                        "standard_features": ["Quadra-Lift air suspension", "Quadra-Drive II 4WD with rear ELSD", "Nappa leather seating with ventilated front seats", "Dual-pane panoramic sunroof", "3,500kg towing capacity"],
                        "notes": "Top-selling luxury tow vehicle in Australia."
                    },
                    {
                        "badge_name": "Grand Cherokee Trackhawk",
                        "years": {"start": 2018, "end": 2021},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed Torqueflite automatic"],
                        "msrp_aud_min": 134900,
                        "msrp_aud_max": 139950,
                        "fuel_consumption_l_100km": 16.8,
                        "kerb_weight_kg": 2433,
                        "standard_features": ["522kW 707hp Hellcat supercharged V8", "Brembo 400mm 2-piece front brake discs with 6-piston yellow calipers", "Quad black exhaust tips", "Laguna leather interior", "Launch control and performance pages"],
                        "notes": "0-100km/h in 3.7 seconds. Quarter mile in 11.6s. The most powerful factory SUV sold in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Overland 3.0 CRD",
                        "body_style": "5-door SUV",
                        "engine_code": "A630",
                        "transmission": "8-speed ZF automatic",
                        "drivetrain": "4WD",
                        "years_start": 2013,
                        "years_end": 2021,
                        "msrp_aud": 74950,
                        "power_kw": 184,
                        "torque_nm": 570,
                        "fuel_l_100km": 7.5,
                        "towing_braked_kg": 3500,
                        "notes": "Benchmark 3500kg tow rating 8-speed diesel."
                    },
                    {
                        "badge_name": "Grand Cherokee Trackhawk",
                        "body_style": "5-door SUV",
                        "engine_code": "Hellcat 6.2",
                        "transmission": "8-speed Torqueflite automatic",
                        "drivetrain": "AWD",
                        "years_start": 2018,
                        "years_end": 2021,
                        "msrp_aud": 134900,
                        "power_kw": 522,
                        "torque_nm": 868,
                        "fuel_l_100km": 16.8,
                        "towing_braked_kg": 2949,
                        "notes": "522kW 707hp supercharged Hellcat SUV."
                    }
                ]
            },
            {
                "series_code": "WL",
                "generation_name": "Grand Cherokee Fifth Generation (WL & WL L)",
                "years": {"start": 2022, "end": "Present"},
                "body_styles": ["5-door SUV (SWB)", "5-door 7-seat SUV (LWB)"],
                "platform": "STLA Large (Giorgio evolution)",
                "ancap_rating": "5 stars",
                "summary": "Built on the Giorgio-derived STLA Large platform. Offered in three-row 7-seat (LWB) and two-row 5-seat (SWB) configurations with 3.6L Pentastar V6 and the advanced 4xe Plug-in Hybrid delivering 280kW and 637Nm.",
                "engines": [
                    {
                        "engine_code": "4xe-PHEV",
                        "name": "2.0L Turbo PHEV Dual-Motor",
                        "displacement_cc": 1995,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged with Dual Electric Motors",
                        "fuel_type": "Plug-in Hybrid",
                        "power_kw": 280,
                        "power_rpm": "5250",
                        "torque_nm": 637,
                        "torque_rpm": "3000",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "17.3kWh battery pack; 52km pure electric range."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Summit Reserve 4xe",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["5-door SUV (SWB)"],
                        "drivetrain": "4WD",
                        "transmissions": ["8-speed automatic"],
                        "msrp_aud_min": 129950,
                        "msrp_aud_max": 139950,
                        "fuel_consumption_l_100km": 3.2,
                        "kerb_weight_kg": 2520,
                        "standard_features": ["Palermo quilted leather seating", "19-speaker McIntosh audio system", "Quadra-Trac II 4WD", "Front passenger touchscreen display", "Night vision camera"],
                        "notes": "High-tech plug-in hybrid flagship."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Summit Reserve 4xe",
                        "body_style": "5-door SUV (SWB)",
                        "engine_code": "4xe-PHEV",
                        "transmission": "8-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2023,
                        "years_end": "Present",
                        "msrp_aud": 129950,
                        "power_kw": 280,
                        "torque_nm": 637,
                        "fuel_l_100km": 3.2,
                        "towing_braked_kg": 2720,
                        "notes": "280kW plug-in hybrid luxury 4x4."
                    }
                ]
            }
        ]
    },

    "ldv/t60": {
        "make_slug": "ldv",
        "model_slug": "t60",
        "name": "T60 & eT60",
        "vehicle_type": "Dual-Cab Utility / Cab-Chassis",
        "segment": "Light Commercial 1-Tonne Ute",
        "years_sold_au": {"start": 2017, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The Chinese 1-tonne ute that disrupted the Australian market. Debuting in 2017 as the first Chinese-manufactured vehicle to achieve a 5-star ANCAP safety rating, the LDV T60 delivered unmatched equipment-for-price value. The 2021 T60 Max raised the stakes with a class-leading 160kW/500Nm 2.0L Bi-Turbo diesel, while the 2022 eT60 became Australia's first commercially available electric factory ute.",
        "australian_market_notes": "Distributed in Australia by Ateco Automotive since 2017. To tailor the ute for tough Australian roads, LDV engaged Walkinshaw Automotive Group in Clayton, Victoria to calibrate a bespoke Australian suspension tune for the Trailrider edition. The T60 Max has become a volume rival to Hilux and Ranger across Australian trade and fleet buyers.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "SK8C Series I",
                "generation_name": "LDV T60 Series I (Pro / Luxe / Trailrider)",
                "years": {"start": 2017, "end": 2021},
                "body_styles": ["Dual-cab utility", "Cab-chassis"],
                "platform": "SAIC Light Truck Platform",
                "ancap_rating": "5 stars",
                "summary": "First Chinese vehicle to receive a 5-star ANCAP safety rating. 2.8L VM Motori turbo-diesel (110kW/360Nm), 6-speed manual or Punch automatic, Eaton rear diff lock, and the Trailrider edition featuring Walkinshaw-developed Australian suspension calibration.",
                "engines": [
                    {
                        "engine_code": "SC28R",
                        "name": "2.8L VGT Turbo Diesel (VM Motori)",
                        "displacement_cc": 2776,
                        "displacement_litres": 2.8,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 110,
                        "power_rpm": "3400",
                        "torque_nm": 360,
                        "torque_rpm": "1600-2800",
                        "compression_ratio": "17.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Variable geometry turbocharger; Bosch common rail fuel injection."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "T60 Trailrider (Walkinshaw Tune)",
                        "years": {"start": 2019, "end": 2021},
                        "body_styles": ["Dual-cab utility"],
                        "drivetrain": "4WD",
                        "transmissions": ["6-speed manual", "6-speed automatic"],
                        "msrp_aud_min": 38990,
                        "msrp_aud_max": 41990,
                        "fuel_consumption_l_100km": 8.8,
                        "kerb_weight_kg": 2060,
                        "standard_features": ["Walkinshaw Australian-calibrated suspension", "19-inch black alloy wheels", "Mountain Top lockable roller tonneau cover", "Eaton rear automatic differential lock", "10-inch touchscreen with Apple CarPlay"],
                        "notes": "Bespoke Australian engineering by Walkinshaw in Clayton."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "T60 Trailrider (Walkinshaw Tune)",
                        "body_style": "Dual-cab utility",
                        "engine_code": "SC28R",
                        "transmission": "6-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2019,
                        "years_end": 2021,
                        "msrp_aud": 41990,
                        "power_kw": 110,
                        "torque_nm": 360,
                        "fuel_l_100km": 8.8,
                        "towing_braked_kg": 3000,
                        "notes": "Walkinshaw tuned dual-cab 4x4 ute."
                    }
                ]
            },
            {
                "series_code": "SK8C Series II",
                "generation_name": "LDV T60 Max (Bi-Turbo)",
                "years": {"start": 2021, "end": "Present"},
                "body_styles": ["Dual-cab utility", "Megatub long-wheelbase utility"],
                "platform": "SAIC Light Truck Platform",
                "ancap_rating": "5 stars",
                "summary": "Major powertrain revolution: SAIC D20 2.0L Bi-Turbo diesel engine delivering 160kW and 500Nm, ZF 8-speed automatic transmission, Pro and LUXE trims, and the stretched Megatub model with an 1,800mm long cargo tray.",
                "engines": [
                    {
                        "engine_code": "SC20M163",
                        "name": "2.0L Bi-Turbo Diesel (SAIC D20)",
                        "displacement_cc": 1996,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 160,
                        "power_rpm": "4000",
                        "torque_nm": 500,
                        "torque_rpm": "1500-2400",
                        "compression_ratio": "16.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Class-leading 160kW 4-cylinder diesel; Honeywell sequential twin turbochargers."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "T60 Max LUXE / Megatub",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["Dual-cab utility", "Megatub long-wheelbase utility"],
                        "drivetrain": "4WD",
                        "transmissions": ["6-speed manual", "8-speed ZF automatic"],
                        "msrp_aud_min": 41990,
                        "msrp_aud_max": 49490,
                        "fuel_consumption_l_100km": 9.3,
                        "kerb_weight_kg": 2150,
                        "standard_features": ["160kW / 500Nm Bi-Turbo diesel", "ZF 8-speed automatic", "Stretched 1800mm tub (Megatub)", "Leather interior with 6-way electric driver's seat", "360-degree camera system"],
                        "notes": "Australia's highest-power 4-cylinder diesel ute under $50k."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "T60 Max LUXE / Megatub",
                        "body_style": "Dual-cab utility",
                        "engine_code": "SC20M163",
                        "transmission": "8-speed ZF automatic",
                        "drivetrain": "4WD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 43990,
                        "power_kw": 160,
                        "torque_nm": 500,
                        "fuel_l_100km": 9.3,
                        "towing_braked_kg": 3000,
                        "notes": "160kW/500Nm ZF 8-speed automatic 4x4 ute."
                    }
                ]
            },
            {
                "series_code": "eT60",
                "generation_name": "LDV eT60 Electric Dual-Cab",
                "years": {"start": 2022, "end": "Present"},
                "body_styles": ["Dual-cab utility"],
                "platform": "SAIC Light Truck EV Platform",
                "ancap_rating": "Unrated (EV)",
                "summary": "Australia's first commercially available factory electric ute. Powered by an 88.5kWh lithium iron phosphate (LFP) battery pack, rear-axle permanent magnet motor delivering 130kW and 310Nm, CCS2 DC fast charging, and up to 330km WLTP range.",
                "engines": [
                    {
                        "engine_code": "TZ204XS",
                        "name": "Rear Permanent Magnet Electric Motor",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Electric",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Electric",
                        "power_kw": 130,
                        "power_rpm": "5000",
                        "torque_nm": 310,
                        "torque_rpm": "0-3000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "88.5kWh CATL LFP battery; 80kW DC fast charging."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "eT60 Electric",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["Dual-cab utility"],
                        "drivetrain": "RWD",
                        "transmissions": ["1-speed direct drive"],
                        "msrp_aud_min": 92990,
                        "msrp_aud_max": 95990,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 2300,
                        "standard_features": ["88.5kWh LFP battery", "10.25-inch infotainment screen", "17-inch alloy wheels", "1,000kg payload capacity", "Spray-in bed liner"],
                        "notes": "First commercial electric ute available in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "eT60 Electric",
                        "body_style": "Dual-cab utility",
                        "engine_code": "TZ204XS",
                        "transmission": "1-speed direct drive",
                        "drivetrain": "RWD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 92990,
                        "power_kw": 130,
                        "torque_nm": 310,
                        "fuel_l_100km": 0.0,
                        "towing_braked_kg": 1000,
                        "notes": "First factory electric dual-cab ute in Australia."
                    }
                ]
            }
        ]
    },

    "proton/jumbuck-satria": {
        "make_slug": "proton",
        "model_slug": "jumbuck-satria",
        "name": "Jumbuck & Satria (including Satria GTi)",
        "vehicle_type": "2-Door Coupe / Hatchback / Compact Car-Based Ute",
        "segment": "Light Performance Hatch / Compact Commercial Ute",
        "years_sold_au": {"start": 1997, "end": 2013},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The cult Malaysian heroes of Australian roads. The Proton Satria GTi became an instant hot hatch sensation in 1999, engineered with genuine Lotus suspension wizardry, Recaro bucket seats, riveted widebody arch flares, and a twin-cam Mitsubishi engine. Alongside it, the Proton Jumbuck carved out a unique niche from 2003 as Australia's most affordable brand-new ute, offering compact car economy with a half-tonne payload.",
        "australian_market_notes": "First launched in Australia in 1997 with the Satria 3-door hatch. When Proton acquired Lotus Cars in 1996, the Lotus engineering team transformed the Satria into the GTi, which Australian automotive journalists lauded as a giant-slaying budget driver's car. In 2003, the Jumbuck ute arrived with an entry price of just $11,990 driveaway, quickly becoming a fixture with inner-city couriers, gardeners, and tradies.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Satria C99",
                "generation_name": "Proton Satria & Satria GTi",
                "years": {"start": 1997, "end": 2005},
                "body_styles": ["3-door hatchback"],
                "platform": "Mitsubishi Mirage (CC/CE derived)",
                "ancap_rating": "3 stars",
                "summary": "Built on the Mitsubishi Mirage platform. Standard Satria offered 1.5L and 1.6L engines, while the halo Satria GTi featured a Mitsubishi 4G93P 1.8L DOHC 16V engine (103kW), complete chassis tuning by Lotus Cars, Recaro seats, 16-inch six-spoke alloys, and bolt-on widebody flares.",
                "engines": [
                    {
                        "engine_code": "4G93P",
                        "name": "1.8L DOHC 16V Petrol (Satria GTi)",
                        "displacement_cc": 1834,
                        "displacement_litres": 1.8,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 103,
                        "power_rpm": "6500",
                        "torque_nm": 164,
                        "torque_rpm": "5500",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Mitsubishi all-iron block, multi-point electronic fuel injection; 7000rpm redline."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Satria GTi",
                        "years": {"start": 1999, "end": 2005},
                        "body_styles": ["3-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 25990,
                        "msrp_aud_max": 27990,
                        "fuel_consumption_l_100km": 7.9,
                        "kerb_weight_kg": 1115,
                        "standard_features": ["Lotus-tuned suspension (stiffer springs, dampers, anti-roll bars)", "Recaro fabric bucket seats", "Momo leather steering wheel and gear knob", "Riveted widebody wheel arch flares", "16-inch six-spoke alloy wheels", "Four-wheel disc brakes with ABS"],
                        "notes": "0-100km/h in 7.8s. Highly acclaimed Australian cult classic hot hatch."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Satria GTi",
                        "body_style": "3-door hatchback",
                        "engine_code": "4G93P",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1999,
                        "years_end": 2005,
                        "msrp_aud": 26990,
                        "power_kw": 103,
                        "torque_nm": 164,
                        "fuel_l_100km": 7.9,
                        "towing_braked_kg": 800,
                        "notes": "Lotus-tuned 1.8L DOHC performance hatchback."
                    }
                ]
            },
            {
                "series_code": "Jumbuck C90",
                "generation_name": "Proton Jumbuck Ute (GLi & GLSi)",
                "years": {"start": 2003, "end": 2010},
                "body_styles": ["2-door car-based utility"],
                "platform": "Proton Wira / Persona (Mitsubishi Lancer derived)",
                "ancap_rating": "1 star",
                "summary": "Front-wheel drive car-based half-tonne utility developed on the Persona platform. Powered by the proven 1.5L Mitsubishi 4G15 SOHC engine, featuring a heavy-duty leaf-sprung rear beam axle for a 645kg payload, and priced under $15,000 brand new.",
                "engines": [
                    {
                        "engine_code": "4G15",
                        "name": "1.5L SOHC 12V Petrol",
                        "displacement_cc": 1468,
                        "displacement_litres": 1.5,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 64,
                        "power_rpm": "6000",
                        "torque_nm": 120,
                        "torque_rpm": "3200",
                        "compression_ratio": "9.2:1",
                        "valvetrain": "SOHC 12-valve (3 valves per cylinder)",
                        "notes": "Electronic multipoint fuel injection; simple, durable Mitsubishi architecture."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Jumbuck GLi / GLSi",
                        "years": {"start": 2003, "end": 2010},
                        "body_styles": ["2-door car-based utility"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 11990,
                        "msrp_aud_max": 15490,
                        "fuel_consumption_l_100km": 7.1,
                        "kerb_weight_kg": 1020,
                        "standard_features": ["645kg payload rating", "Corrugated steel load bed with tie-down hooks", "14-inch steel wheels / alloys (GLSi)", "Power steering", "Air conditioning option"],
                        "notes": "Australia's most affordable new utility; huge cult popularity with couriers and hobbyists."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Jumbuck GLi / GLSi",
                        "body_style": "2-door car-based utility",
                        "engine_code": "4G15",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2003,
                        "years_end": 2010,
                        "msrp_aud": 13990,
                        "power_kw": 64,
                        "torque_nm": 120,
                        "fuel_l_100km": 7.1,
                        "towing_braked_kg": 1000,
                        "notes": "Compact car-based half-tonne utility."
                    }
                ]
            },
            {
                "series_code": "Satria Neo",
                "generation_name": "Proton Satria Neo & Neo Club-Racer",
                "years": {"start": 2007, "end": 2013},
                "body_styles": ["3-door hatchback"],
                "platform": "Proton Neo platform",
                "ancap_rating": "4 stars",
                "summary": "Clean-sheet Proton chassis engineered with direct Lotus ride and handling development. Powered by the CamPro 1.6L 16V engine (and later CamPro CPS with variable cam profile, 93kW), flared bodywork, and central-exit exhaust.",
                "engines": [
                    {
                        "engine_code": "CamPro CPS",
                        "name": "1.6L DOHC 16V CPS Petrol",
                        "displacement_cc": 1597,
                        "displacement_litres": 1.6,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 93,
                        "power_rpm": "6500",
                        "torque_nm": 150,
                        "torque_rpm": "4500",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 16-valve Cam Profile Switching (CPS)",
                        "notes": "Lotus engineered variable valve lift and timing system."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Satria Neo CPS / Club-Racer",
                        "years": {"start": 2009, "end": 2013},
                        "body_styles": ["3-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual", "4-speed automatic"],
                        "msrp_aud_min": 17990,
                        "msrp_aud_max": 20990,
                        "fuel_consumption_l_100km": 7.4,
                        "kerb_weight_kg": 1190,
                        "standard_features": ["Lotus ride and handling badge", "16-inch turbine alloy wheels", "Center-exit exhaust", "Leather sport steering wheel", "Aggressive front bumper and roof spoiler"],
                        "notes": "Affordable driver's chassis developed by Lotus."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Satria Neo CPS / Club-Racer",
                        "body_style": "3-door hatchback",
                        "engine_code": "CamPro CPS",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2009,
                        "years_end": 2013,
                        "msrp_aud": 18990,
                        "power_kw": 93,
                        "torque_nm": 150,
                        "fuel_l_100km": 7.4,
                        "towing_braked_kg": 1000,
                        "notes": "Lotus-tuned CamPro CPS hot hatch."
                    }
                ]
            }
        ]
    }
}
