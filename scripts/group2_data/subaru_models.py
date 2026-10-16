"""Deep-dive model data for Subaru WRX."""

WRX_MODEL = {
    "make_slug": "subaru",
    "model_slug": "wrx",
    "name": "WRX",
    "vehicle_type": "Sedan / Hatchback / Wagon",
    "segment": "Sports Performance",
    "years_sold_au": {"start": 1994, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Subaru Impreza WRX and WRX STI democratized supercar-baiting all-wheel-drive turbocharged performance in Australia in 1994. Backed by Possum Bourne's seven consecutive Australian Rally Championships, the WRX is an indelible part of modern Australian car culture.",
    "australian_market_notes": "First imported in February 1994 for just $39,990, the WRX offered all-weather grip and blistering acceleration that embarrassed European performance sedans costing three times as much. Across five generations, the WRX evolved from an underground rally homologation tool to a sophisticated all-wheel-drive sports performance icon.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "GC8",
            "generation_name": "WRX 1st Generation",
            "years": {"start": 1994, "end": "2000"},
            "body_styles": ["4-door Sedan", "5-door Hatch/Wagon"],
            "platform": "Subaru GC/GF",
            "ancap_rating": "Untested",
            "summary": "The original giant killer. Arrived in February 1994 with a 155kW 2.0L turbo boxer and symmetrical AWD, sparking an Australian rally and tuning revolution.",
            "engines": [
                {
                    "engine_code": "EJ20G",
                    "name": "Subaru EJ20G 2.0L Turbo Boxer",
                    "displacement_cc": 1994,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 155.0,
                    "power_rpm": "6000",
                    "torque_nm": 270.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Closed deck block in early cars; upgraded to EJ205 160kW in 1999."
                }
            ],
            "badges": [
                {
                    "badge_name": "WRX",
                    "years": {"start": 1994, "end": "2000"},
                    "body_styles": ["Sedan", "Hatch"],
                    "drivetrain": "Symmetrical All-Wheel Drive",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 44500,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1245,
                    "standard_features": ["Symmetrical AWD with viscous center and rear LSD", "Bonnet scoop and vents", "Sports bucket seats", "15-inch then 16-inch alloy wheels", "Momo steering wheel"],
                    "notes": "The defining hot car of the 1990s in Australia."
                },
                {
                    "badge_name": "STI (Version 5/6)",
                    "years": {"start": 1999, "end": "2000"},
                    "body_styles": ["2-door Coupe", "4-door Sedan"],
                    "drivetrain": "Symmetrical All-Wheel Drive",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 59990,
                    "msrp_aud_max": 62500,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1260,
                    "standard_features": ["206kW hand-built EJ207 engine", "High rear spoiler", "Gold alloy wheels", "Carbon strut brace", "Intercooler water spray", "Red 4-piston front brake calipers"],
                    "notes": "First official Subaru Australia factory STI imports (400 units allocated)."
                }
            ],
            "configurations": [
                {
                    "badge_name": "WRX Sedan",
                    "body_style": "Sedan",
                    "engine_code": "EJ20G",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 1994,
                    "years_end": "1998",
                    "msrp_aud": 39990,
                    "power_kw": 155.0,
                    "torque_nm": 270.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 1200,
                    "notes": "Original 1994 GC8 WRX launch model."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "GD/GG",
            "generation_name": "WRX 2nd Generation (Bugeye / Blobeye / Hawkeye)",
            "years": {"start": 2000, "end": "2007"},
            "body_styles": ["4-door Sedan", "5-door Sportswagon"],
            "platform": "Subaru GD",
            "ancap_rating": "4 Stars",
            "summary": "Stiffer chassis spanning the round-headlight Bugeye (2000), Blobeye (2003), and Hawkeye (2005) facelifts. Brought the official WRX STI with DCCD all-wheel drive, Brembo brakes, and gold wheels.",
            "engines": [
                {
                    "engine_code": "EJ205",
                    "name": "Subaru EJ205 2.0L Turbo Boxer",
                    "displacement_cc": 1994,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 160.0,
                    "power_rpm": "5600",
                    "torque_nm": 292.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.0:1",
                    "valvetrain": "DOHC 16-valve AVCS",
                    "notes": "Standard WRX engine from 2000 to 2005."
                },
                {
                    "engine_code": "EJ257",
                    "name": "Subaru EJ257 2.5L Turbo Boxer (STI)",
                    "displacement_cc": 2457,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 206.0,
                    "power_rpm": "6000",
                    "torque_nm": 392.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.2:1",
                    "valvetrain": "DOHC 16-valve Dual AVCS",
                    "notes": "Fitted to the 2005-2007 Hawkeye WRX STI with 6-speed manual and DCCD."
                }
            ],
            "badges": [
                {
                    "badge_name": "WRX STI",
                    "years": {"start": 2002, "end": "2007"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "Symmetrical All-Wheel Drive with DCCD",
                    "transmissions": ["6-speed close-ratio manual"],
                    "msrp_aud_min": 55150,
                    "msrp_aud_max": 59990,
                    "fuel_consumption_l_100km": 11.8,
                    "kerb_weight_kg": 1470,
                    "standard_features": ["Driver Controlled Center Differential (DCCD)", "Brembo 4-piston front / 2-piston rear gold brakes", "Inverted front and rear struts", "BBS/Enkei gold 17-inch forged wheels", "High-rise rear wing", "Blue Alcantara seats"],
                    "notes": "The holy grail of mid-2000s Australian performance."
                },
                {
                    "badge_name": "WRX",
                    "years": {"start": 2000, "end": "2007"},
                    "body_styles": ["Sedan", "Sportswagon"],
                    "drivetrain": "Symmetrical All-Wheel Drive",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 41990,
                    "msrp_aud_max": 46500,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1385,
                    "standard_features": ["Symmetrical AWD", "17-inch alloy wheels", "ABS brakes", "Dual front airbags", "Sports bucket seats", "Bonnet scoop"],
                    "notes": "Australia's top-selling turbo sports car."
                }
            ],
            "configurations": [
                {
                    "badge_name": "WRX STI",
                    "body_style": "Sedan",
                    "engine_code": "EJ257",
                    "transmission": "6-speed close-ratio manual",
                    "drivetrain": "AWD with DCCD",
                    "years_start": 2005,
                    "years_end": "2007",
                    "msrp_aud": 56990,
                    "power_kw": 206.0,
                    "torque_nm": 392.0,
                    "fuel_l_100km": 11.8,
                    "towing_braked_kg": 0,
                    "notes": "Hawkeye 2.5L WRX STI."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "VA",
            "generation_name": "WRX 4th Generation",
            "years": {"start": 2014, "end": "2021"},
            "body_styles": ["4-door Sedan"],
            "platform": "Subaru VA",
            "ancap_rating": "5 Stars",
            "summary": "Introduced the direct-injected twin-scroll 2.0L FA20F turbo engine in WRX, while the raw 221kW WRX STI retained the hydraulic-steering EJ257 track beast.",
            "engines": [
                {
                    "engine_code": "FA20F",
                    "name": "Subaru FA20F 2.0L DIT Turbo Boxer",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Twin-Scroll Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 197.0,
                    "power_rpm": "5600",
                    "torque_nm": 350.0,
                    "torque_rpm": "2400-5200",
                    "compression_ratio": "10.6:1",
                    "valvetrain": "DOHC 16-valve Dual AVCS Direct Injection",
                    "notes": "Quick spooling twin-scroll turbo with flat torque curve."
                },
                {
                    "engine_code": "EJ257-VA",
                    "name": "Subaru EJ257 2.5L Turbo Boxer (STI)",
                    "displacement_cc": 2457,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 221.0,
                    "power_rpm": "6000",
                    "torque_nm": 407.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.2:1",
                    "valvetrain": "DOHC 16-valve Dual AVCS",
                    "notes": "221kW track weapon; the final evolution of the legendary EJ series."
                }
            ],
            "badges": [
                {
                    "badge_name": "WRX Premium",
                    "years": {"start": 2014, "end": "2021"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "Symmetrical AWD with Torque Vectoring",
                    "transmissions": ["6-speed manual", "Sport Lineartronic CVT with paddle shifters"],
                    "msrp_aud_min": 43490,
                    "msrp_aud_max": 48490,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 1495,
                    "standard_features": ["Active Torque Vectoring", "Leather upholstery", "Electric sunroof", "harman/kardon 8-speaker audio", "18-inch alloy wheels", "Blind spot monitoring"],
                    "notes": "Modern refined daily driver."
                },
                {
                    "badge_name": "WRX STI Spec.R",
                    "years": {"start": 2014, "end": "2021"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "Multi-mode DCCD All-Wheel Drive",
                    "transmissions": ["6-speed close-ratio manual"],
                    "msrp_aud_min": 55990,
                    "msrp_aud_max": 60490,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1530,
                    "standard_features": ["221kW EJ257 engine", "Multi-mode DCCD with manual bias adjustment", "Brembo 6-piston yellow brake calipers", "Recaro heated bucket seats", "19-inch forged alloy wheels", "STI sport exhaust"],
                    "notes": "The apex of pure mechanical all-wheel-drive engagement."
                }
            ],
            "configurations": [
                {
                    "badge_name": "WRX STI Spec.R",
                    "body_style": "Sedan",
                    "engine_code": "EJ257-VA",
                    "transmission": "6-speed close-ratio manual",
                    "drivetrain": "Multi-mode DCCD All-Wheel Drive",
                    "years_start": 2018,
                    "years_end": "2021",
                    "msrp_aud": 58990,
                    "power_kw": 221.0,
                    "torque_nm": 407.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 0,
                    "notes": "Facelift VA WRX STI Spec.R with 19-inch wheels and 6-piston Brembos."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "VB",
            "generation_name": "WRX 5th Generation",
            "years": {"start": 2022, "end": "Present"},
            "body_styles": ["4-door Sedan", "5-door Sportswagon"],
            "platform": "Subaru Global Platform (SGP)",
            "ancap_rating": "5 Stars",
            "summary": "Built on the stiffened Subaru Global Platform, powered by the 2.4L FA24F turbo boxer (202kW/350Nm), and introducing the WRX Sportswagon.",
            "engines": [
                {
                    "engine_code": "FA24F",
                    "name": "Subaru FA24F 2.4L Turbo Boxer",
                    "displacement_cc": 2387,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Twin-Scroll Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 202.0,
                    "power_rpm": "5600",
                    "torque_nm": 350.0,
                    "torque_rpm": "2000-5200",
                    "compression_ratio": "10.6:1",
                    "valvetrain": "DOHC 16-valve Dual AVCS Direct Injection",
                    "notes": "Increased displacement delivers broader torque band and improved response."
                }
            ],
            "badges": [
                {
                    "badge_name": "RS",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "Symmetrical All-Wheel Drive",
                    "transmissions": ["6-speed manual", "Subaru Performance Transmission (SPT)"],
                    "msrp_aud_min": 50490,
                    "msrp_aud_max": 54500,
                    "fuel_consumption_l_100km": 9.9,
                    "kerb_weight_kg": 1572,
                    "standard_features": ["18-inch alloy wheels", "Ultrasuede sports bucket seats", "11.6-inch portrait infotainment touchscreen", "harman/kardon 10-speaker audio", "EyeSight driver assist on SPT"],
                    "notes": "High-spec manual enthusiast sedan."
                },
                {
                    "badge_name": "tS",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["Sedan", "Sportswagon"],
                    "drivetrain": "Symmetrical All-Wheel Drive",
                    "transmissions": ["Subaru Performance Transmission (SPT)"],
                    "msrp_aud_min": 56990,
                    "msrp_aud_max": 58990,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 1600,
                    "standard_features": ["Electronically controlled adaptive dampers", "Drive Mode Select with Comfort/Normal/Sport/Sport+/Individual", "STI-branded steering wheel and instruments", "18-inch wheels"],
                    "notes": "Tuned by STI adaptive dynamics flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "RS Sedan",
                    "body_style": "Sedan",
                    "engine_code": "FA24F",
                    "transmission": "6-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 2022,
                    "years_end": "Present",
                    "msrp_aud": 50490,
                    "power_kw": 202.0,
                    "torque_nm": 350.0,
                    "fuel_l_100km": 9.9,
                    "towing_braked_kg": 1200,
                    "notes": "VB 2.4L Turbo manual sedan."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

SUBARU_DEEP_DIVES = [WRX_MODEL]
