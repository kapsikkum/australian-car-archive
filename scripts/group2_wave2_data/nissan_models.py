"""Wave 2 Nissan deep-dive models: Navara, X-Trail, Pulsar, Z-Car."""

NAVARA_MODEL = {
    "make_slug": "nissan",
    "model_slug": "navara",
    "name": "Navara",
    "vehicle_type": "Ute / Cab Chassis",
    "segment": "Light Commercial",
    "years_sold_au": {"start": 1986, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Nissan Navara is one of Australia's premier dual-cab and commercial utes. Spanning four generations, from the durable D21 and indestructible D22 workhorses to the powerhouse 550Nm V6 turbodiesel D40 and coil-sprung D23 with locally engineered Premcar Warrior editions, the Navara has served on Australian building sites, farms, and off-road expeditions for nearly four decades.",
    "australian_market_notes": "First sold in Australia in 1986 replacing the Datsun 720, the Navara popularized dual-cab 4x4 recreation in Australia. The D22 generation established a legendary reputation for mechanical toughness in the mines and bush, running in parallel with the larger, luxurious D40. In 2011, the D40 ST-X 550 introduced a crushing 550Nm 3.0L V6 turbodiesel, resetting the performance ute benchmark. Today, the D23 NP300 features the PRO-4X Warrior, re-engineered in Melbourne by Premcar specifically for extreme Australian outback conditions.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "D21",
            "generation_name": "Navara 1st Generation",
            "years": {"start": 1986, "end": 1997},
            "body_styles": ["Single Cab", "King Cab", "Dual Cab"],
            "platform": "Nissan D21",
            "ancap_rating": "Untested",
            "summary": "First generation to carry the Navara name in Australia. Offered rugged separate-chassis durability, torsion-bar front suspension, and bulletproof Z24 and TD27 engines.",
            "engines": [
                {
                    "engine_code": "Z24",
                    "name": "Nissan Z24 2.4L OHC",
                    "displacement_cc": 2389,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 74.0,
                    "power_rpm": "4800",
                    "torque_nm": 177.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "8.3:1",
                    "valvetrain": "SOHC 8-valve (twin-spark)",
                    "notes": "Twin spark plug design per cylinder."
                },
                {
                    "engine_code": "TD27",
                    "name": "Nissan TD27 2.7L Diesel",
                    "displacement_cc": 2663,
                    "displacement_litres": 2.7,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 64.0,
                    "power_rpm": "4300",
                    "torque_nm": 175.0,
                    "torque_rpm": "2200",
                    "compression_ratio": "21.8:1",
                    "valvetrain": "OHV 8-valve",
                    "notes": "Gear-driven camshaft diesel renowned for near-indestructible lifespan."
                }
            ],
            "badges": [
                {
                    "badge_name": "DX / Standard",
                    "years": {"start": 1986, "end": 1997},
                    "body_styles": ["Single Cab", "King Cab", "Dual Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 12990,
                    "msrp_aud_max": 24990,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1420,
                    "standard_features": ["Vinyl bench seat", "Part-time 4WD with manual locking hubs", "Rear step bumper", "15-inch steel wheels"],
                    "notes": "True 1-tonne commercial workhorse."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Navara Dual Cab 4x4 Diesel",
                    "body_style": "Dual Cab",
                    "engine_code": "TD27",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1988,
                    "years_end": 1997,
                    "msrp_aud": 24990,
                    "power_kw": 64.0,
                    "torque_nm": 175.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 1500,
                    "notes": "Early recreational 4x4 dual cab."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "D22",
            "generation_name": "Navara 2nd Generation (ST-R)",
            "years": {"start": 1997, "end": 2015},
            "body_styles": ["Single Cab", "King Cab", "Dual Cab"],
            "platform": "Nissan D22",
            "ancap_rating": "3 stars",
            "summary": "18-year production run in Australia. Iconic ST-R 4x4 with 3.0L ZD30 and later 2.5L YD25 common-rail turbodiesel, renowned for unbreakable mechanical ruggedness.",
            "engines": [
                {
                    "engine_code": "ZD30DDT",
                    "name": "Nissan ZD30DDT 3.0L Turbo Diesel",
                    "displacement_cc": 2953,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 110.0,
                    "power_rpm": "3400",
                    "torque_nm": 314.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "17.9:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Direct injection turbo diesel fitted to D22 ST-R from 2001 to 2006."
                },
                {
                    "engine_code": "YD25DDTi-D22",
                    "name": "Nissan YD25DDTi 2.5L Common Rail Turbo Diesel",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 98.0,
                    "power_rpm": "3600",
                    "torque_nm": 304.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "16.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Euro 4 common-rail diesel fitted from 2008 to 2015."
                }
            ],
            "badges": [
                {
                    "badge_name": "DX",
                    "years": {"start": 1997, "end": 2015},
                    "body_styles": ["Single Cab", "Dual Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 19990,
                    "msrp_aud_max": 28990,
                    "fuel_consumption_l_100km": 9.1,
                    "kerb_weight_kg": 1620,
                    "standard_features": ["Vinyl interior", "Manual locking hubs (early)", "Power steering", "Air conditioning option"],
                    "notes": "Agricultural and trade favourite."
                },
                {
                    "badge_name": "ST-R 4x4",
                    "years": {"start": 2001, "end": 2015},
                    "body_styles": ["Dual Cab"],
                    "drivetrain": "Part-Time 4WD with low range",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 32990,
                    "msrp_aud_max": 39990,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 1780,
                    "standard_features": ["16-inch alloy wheels", "Wide body fender flares", "Aluminium side steps", "Power windows", "Cloth trim", "Limited-slip rear differential"],
                    "notes": "Australia's value 4WD dual-cab king throughout the 2000s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Navara ST-R 3.0 Turbo Diesel 4x4",
                    "body_style": "Dual Cab",
                    "engine_code": "ZD30DDT",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 2001,
                    "years_end": 2006,
                    "msrp_aud": 38990,
                    "power_kw": 110.0,
                    "torque_nm": 314.0,
                    "fuel_l_100km": 9.6,
                    "towing_braked_kg": 3000,
                    "notes": "Classic Australian work-and-play dual cab."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "D40",
            "generation_name": "Navara 3rd Generation (ST-X & ST-X 550)",
            "years": {"start": 2005, "end": "2015"},
            "body_styles": ["King Cab", "Dual Cab"],
            "platform": "Nissan F-Alpha platform",
            "ancap_rating": "4 stars (facelift)",
            "summary": "Built on the full-size F-Alpha chassis. Sized up cabin space, 140kW 2.5L diesel, and the mighty ST-X 550 featuring a 3.0L V6 turbodiesel with 170kW and a monstrous 550Nm.",
            "engines": [
                {
                    "engine_code": "YD25DDTi-High",
                    "name": "Nissan YD25DDTi 2.5L High-Output Turbo Diesel",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Variable Nozzle Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 140.0,
                    "power_rpm": "4000",
                    "torque_nm": 450.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "15.0:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Upgraded in 2010 to 140kW and 450Nm of torque."
                },
                {
                    "engine_code": "V9X",
                    "name": "Nissan/Renault V9X 3.0L V6 Turbo Diesel",
                    "displacement_cc": 2993,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 170.0,
                    "power_rpm": "3750",
                    "torque_nm": 550.0,
                    "torque_rpm": "1750",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Compacted graphite iron (CGI) block with 550Nm of torque paired with 7-speed automatic."
                }
            ],
            "badges": [
                {
                    "badge_name": "RX / ST",
                    "years": {"start": 2005, "end": 2015},
                    "body_styles": ["King Cab", "Dual Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["6-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 31990,
                    "msrp_aud_max": 46990,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 1960,
                    "standard_features": ["Utili-track channel tie-down cargo system", "Dual front airbags", "ABS with EBD", "Cruise control", "Air conditioning"],
                    "notes": "Spacious family and towing ute."
                },
                {
                    "badge_name": "ST-X 550",
                    "years": {"start": 2011, "end": 2015},
                    "body_styles": ["Dual Cab"],
                    "drivetrain": "Part-Time 4WD",
                    "transmissions": ["7-speed automatic"],
                    "msrp_aud_min": 60990,
                    "msrp_aud_max": 62990,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 2110,
                    "standard_features": ["170kW/550Nm V6 turbodiesel", "7-speed auto", "Leather-appointed heated seats", "Hard tonneau cover", "Bose audio option", "Smoked chrome grille", "Tub liner"],
                    "notes": "Australia's undisputed torque king of the dual-cab market."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Navara ST-X 550 V6 Diesel",
                    "body_style": "Dual Cab",
                    "engine_code": "V9X",
                    "transmission": "7-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2011,
                    "years_end": 2015,
                    "msrp_aud": 60990,
                    "power_kw": 170.0,
                    "torque_nm": 550.0,
                    "fuel_l_100km": 9.3,
                    "towing_braked_kg": 3000,
                    "notes": "550Nm powerhouse capable of 0-100 km/h in 8.8 seconds."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "D23",
            "generation_name": "Navara 4th Gen & PRO-4X Warrior",
            "years": {"start": 2015, "end": "Present"},
            "body_styles": ["Single Cab", "King Cab", "Dual Cab"],
            "platform": "Nissan D23",
            "ancap_rating": "5 stars",
            "summary": "Introduced sophisticated 5-link rear coil-spring suspension, twin-turbo diesel 2.3L engine, and the acclaimed Premcar-engineered PRO-4X Warrior off-road flagship.",
            "engines": [
                {
                    "engine_code": "YS23DDTT",
                    "name": "Nissan YS23DDTT 2.3L Twin-Turbo Diesel",
                    "displacement_cc": 2298,
                    "displacement_litres": 2.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Sequential Twin-Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 140.0,
                    "power_rpm": "3750",
                    "torque_nm": 450.0,
                    "torque_rpm": "1500-2500",
                    "compression_ratio": "15.4:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Small high-pressure turbo for instant response, large low-pressure turbo for top end."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST / ST-X",
                    "years": {"start": 2015, "end": "Present"},
                    "body_styles": ["Dual Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["6-speed manual", "7-speed automatic"],
                    "msrp_aud_min": 42990,
                    "msrp_aud_max": 58730,
                    "fuel_consumption_l_100km": 7.3,
                    "kerb_weight_kg": 2010,
                    "standard_features": ["5-link coil rear suspension", "8-inch touchscreen with Apple CarPlay", "Nissan Intelligent Mobility safety suite", "Tow bar standard (facelift)"],
                    "notes": "3,500kg braked towing capacity."
                },
                {
                    "badge_name": "PRO-4X Warrior by Premcar",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["Dual Cab"],
                    "drivetrain": "Part-Time 4WD with rear diff lock",
                    "transmissions": ["6-speed manual", "7-speed automatic"],
                    "msrp_aud_min": 67490,
                    "msrp_aud_max": 71265,
                    "fuel_consumption_l_100km": 8.1,
                    "kerb_weight_kg": 2256,
                    "standard_features": ["Re-engineered locally in Epping VIC by Premcar", "40mm suspension lift with bespoke Monroe dampers", "Hooped steel bullbar with integrated light bar", "3mm steel front bash plate", "17-inch cast alloys with Cooper Discoverer AT3 all-terrain tyres", "Fender flares"],
                    "notes": "Australian engineered off-road flagship with full factory warranty."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Navara PRO-4X Warrior Auto",
                    "body_style": "Dual Cab",
                    "engine_code": "YS23DDTT",
                    "transmission": "7-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 71265,
                    "power_kw": 140.0,
                    "torque_nm": 450.0,
                    "fuel_l_100km": 8.1,
                    "towing_braked_kg": 3500,
                    "notes": "Turnkey Australian-engineered extreme outback dual cab."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

XTRAIL_MODEL = {
    "make_slug": "nissan",
    "model_slug": "x-trail",
    "name": "X-Trail",
    "vehicle_type": "Medium SUV",
    "segment": "Medium SUV",
    "years_sold_au": {"start": 2001, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Nissan X-Trail is an Australian compact and medium SUV institution. Famous for combining utilitarian practicality—such as wipe-clean waterproof cargo floors, cooled cup holders, and multi-tier drawers—with genuine soft-road capability via Nissan's All-Mode 4x4, it remains one of Australia's most consistently popular family crossovers.",
    "australian_market_notes": "Launched in October 2001, the boxy T30 X-Trail quickly captured a dedicated following among outdoor adventurers, families, and dog owners thanks to its washable cargo area. The T32 generation added 7-seat capability, while the fourth-generation T33 brought Nissan's innovative e-POWER variable-compression electric drive system with e-4ORCE twin-motor AWD.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "T30",
            "generation_name": "X-Trail 1st Generation",
            "years": {"start": 2001, "end": 2007},
            "body_styles": ["5-door SUV"],
            "platform": "Nissan FF-S",
            "ancap_rating": "4 stars",
            "summary": "Utilitarian pioneer with central instrument binnacle, washable plastic cargo lining, heated/cooled dashboard drink holders, and All-Mode 4x4 with 2.5L QR25DE power.",
            "engines": [
                {
                    "engine_code": "QR25DE-T30",
                    "name": "Nissan QR25DE 2.5L DOHC 16V",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 132.0,
                    "power_rpm": "6000",
                    "torque_nm": 245.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve CVTC",
                    "notes": "Punchy 132kW four-cylinder with twin balance shafts."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST / ST-S",
                    "years": {"start": 2001, "end": 2007},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "All-Mode 4x4",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 31990,
                    "msrp_aud_max": 35490,
                    "fuel_consumption_l_100km": 9.6,
                    "kerb_weight_kg": 1435,
                    "standard_features": ["All-Mode 4x4 (2WD, Auto, Lock)", "Washable composite luggage floor", "Air-conditioned front cup holders", "Central instrument cluster", "16-inch alloy wheels (ST-S)"],
                    "notes": "Recreational lifestyle benchmark."
                },
                {
                    "badge_name": "Ti / Ti-L",
                    "years": {"start": 2001, "end": 2007},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "All-Mode 4x4",
                    "transmissions": ["4-speed automatic"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 43990,
                    "fuel_consumption_l_100km": 9.9,
                    "kerb_weight_kg": 1485,
                    "standard_features": ["Huge panoramic electric sunroof", "Leather upholstery", "Climate control", "16-inch alloys", "Fog lamps"],
                    "notes": "Luxury compact 4x4."
                }
            ],
            "configurations": [
                {
                    "badge_name": "X-Trail ST 4x4 Auto",
                    "body_style": "5-door SUV",
                    "engine_code": "QR25DE-T30",
                    "transmission": "4-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2001,
                    "years_end": 2007,
                    "msrp_aud": 33990,
                    "power_kw": 132.0,
                    "torque_nm": 245.0,
                    "fuel_l_100km": 9.9,
                    "towing_braked_kg": 2000,
                    "notes": "Australia's favourite recreational compact SUV of the early 2000s."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "T31",
            "generation_name": "X-Trail 2nd Generation",
            "years": {"start": 2007, "end": 2014},
            "body_styles": ["5-door SUV"],
            "platform": "Nissan C platform",
            "ancap_rating": "4 stars",
            "summary": "Moved instruments back in front of driver. Added clever double-decker sliding cargo drawer, Xtronic CVT, and 2.0L M9R turbodiesel with 360Nm.",
            "engines": [
                {
                    "engine_code": "QR25DE-T31",
                    "name": "Nissan QR25DE 2.5L",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 125.0,
                    "power_rpm": "6000",
                    "torque_nm": 226.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.6:1",
                    "valvetrain": "DOHC 16-valve CVTC",
                    "notes": "Paired with 6-speed manual or Xtronic CVT."
                },
                {
                    "engine_code": "M9R",
                    "name": "Nissan/Renault M9R 2.0L dCi Turbo Diesel",
                    "displacement_cc": 1995,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Variable Geometry Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 127.0,
                    "power_rpm": "3750",
                    "torque_nm": 360.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "15.6:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "360Nm turbodiesel paired with 6-speed auto or manual."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST / ST-L",
                    "years": {"start": 2007, "end": 2014},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD (from 2011) or All-Mode 4x4-i",
                    "transmissions": ["6-speed manual", "CVT automatic"],
                    "msrp_aud_min": 28490,
                    "msrp_aud_max": 38490,
                    "fuel_consumption_l_100km": 9.1,
                    "kerb_weight_kg": 1515,
                    "standard_features": ["All-Mode 4x4-i with Hill Start and Hill Descent", "Underfloor cargo drawer", "Bluetooth", "17-inch alloys"],
                    "notes": "Core family spec."
                },
                {
                    "badge_name": "Ti / TL Diesel",
                    "years": {"start": 2007, "end": 2014},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "All-Mode 4x4-i",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 42990,
                    "msrp_aud_max": 45490,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1640,
                    "standard_features": ["Heated leather seats", "Panoramic glass sunroof", "Xenon headlights", "Reversing camera in rear-view mirror"],
                    "notes": "High specification diesel and petrol."
                }
            ],
            "configurations": [
                {
                    "badge_name": "X-Trail ST-L 4x4-i CVT",
                    "body_style": "5-door SUV",
                    "engine_code": "QR25DE-T31",
                    "transmission": "CVT automatic",
                    "drivetrain": "AWD",
                    "years_start": 2007,
                    "years_end": 2014,
                    "msrp_aud": 36490,
                    "power_kw": 125.0,
                    "torque_nm": 226.0,
                    "fuel_l_100km": 9.1,
                    "towing_braked_kg": 2000,
                    "notes": "2,000kg towing capacity with clever cargo drawers."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "T32",
            "generation_name": "X-Trail 3rd Generation",
            "years": {"start": 2014, "end": 2022},
            "body_styles": ["5-door SUV"],
            "platform": "Renault-Nissan CMF-CD",
            "ancap_rating": "5 stars",
            "summary": "Shifted to sleek contemporary styling on CMF-CD platform. Added 7-seat versatility, EZ-Flex seating, 360-degree Around View Monitor, and active ride control.",
            "engines": [
                {
                    "engine_code": "QR25DE-T32",
                    "name": "Nissan QR25DE 2.5L",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 126.0,
                    "power_rpm": "6000",
                    "torque_nm": 226.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve CVTC",
                    "notes": "Mainstay volume engine across ST, ST-L, and Ti."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST (5 or 7 seats)",
                    "years": {"start": 2014, "end": 2022},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["6-speed manual", "CVT automatic"],
                    "msrp_aud_min": 27990,
                    "msrp_aud_max": 34990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 1500,
                    "standard_features": ["Reversing camera", "Keyless entry & start", "EZ-Flex 2nd row seating", "Autonomous emergency braking (from 2017)"],
                    "notes": "Available in 7-seat FWD or 5-seat AWD."
                },
                {
                    "badge_name": "ST-L / Ti",
                    "years": {"start": 2014, "end": 2022},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["CVT automatic"],
                    "msrp_aud_min": 36190,
                    "msrp_aud_max": 45490,
                    "fuel_consumption_l_100km": 8.3,
                    "kerb_weight_kg": 1600,
                    "standard_features": ["Around View 360-degree monitor", "Leather-accented seats", "Bose 8-speaker audio (Ti)", "Motion-activated power tailgate (Ti)", "Panoramic sunroof (Ti)"],
                    "notes": "Top-selling specification."
                }
            ],
            "configurations": [
                {
                    "badge_name": "X-Trail ST-L 7-seater FWD",
                    "body_style": "5-door SUV",
                    "engine_code": "QR25DE-T32",
                    "transmission": "CVT automatic",
                    "drivetrain": "FWD",
                    "years_start": 2014,
                    "years_end": 2022,
                    "msrp_aud": 38700,
                    "power_kw": 126.0,
                    "torque_nm": 226.0,
                    "fuel_l_100km": 8.1,
                    "towing_braked_kg": 1500,
                    "notes": "Affordable 7-seater family configuration."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "T33",
            "generation_name": "X-Trail 4th Gen & e-POWER e-4ORCE",
            "years": {"start": 2022, "end": "Present"},
            "body_styles": ["5-door SUV"],
            "platform": "CMF-C",
            "ancap_rating": "5 stars",
            "summary": "Major leap in refinement. Introduces revolutionary e-POWER electric motor drive where a 1.5L VC-Turbo variable compression engine acts as a pure on-board generator, powering twin electric motors with e-4ORCE AWD.",
            "engines": [
                {
                    "engine_code": "PR25DD-X",
                    "name": "Nissan PR25DD 2.5L Direct Injection",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 135.0,
                    "power_rpm": "6000",
                    "torque_nm": 244.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "12.0:1",
                    "valvetrain": "DOHC 16-valve direct injection",
                    "notes": "Upgraded 135kW standard engine."
                },
                {
                    "engine_code": "KR15DDT-ePower",
                    "name": "Nissan 1.5L VC-Turbo e-POWER e-4ORCE",
                    "displacement_cc": 1497,
                    "displacement_litres": 1.5,
                    "cylinders": 3,
                    "configuration": "Inline-3 Variable Compression + Twin Electric Motors",
                    "aspiration": "Turbocharged Variable Compression + Dual Motors",
                    "fuel_type": "Petrol Hybrid Electric",
                    "power_kw": 157.0,
                    "power_rpm": "Electric Drive",
                    "torque_nm": 330.0,
                    "torque_rpm": "Instant",
                    "compression_ratio": "8.0:1 to 14.0:1 variable",
                    "valvetrain": "DOHC 12-valve VC-Turbo",
                    "notes": "100% electric motor wheel drive (150kW front + 100kW rear motor, combined 157kW system power)."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST / ST-L",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["CVT automatic"],
                    "msrp_aud_min": 37250,
                    "msrp_aud_max": 46790,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1540,
                    "standard_features": ["ProPILOT semi-autonomous driving", "8.0 or 12.3-inch touchscreen", "Wireless Apple CarPlay", "Reversing camera", "Full safety shield"],
                    "notes": "Available in 5 or 7 seats."
                },
                {
                    "badge_name": "Ti / Ti-L e-POWER with e-4ORCE",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "e-4ORCE Twin-Motor AWD",
                    "transmissions": ["Electric drive reduction"],
                    "msrp_aud_min": 54690,
                    "msrp_aud_max": 57690,
                    "fuel_consumption_l_100km": 6.1,
                    "kerb_weight_kg": 1880,
                    "standard_features": ["e-POWER electric drive", "e-Pedal Step regenerative braking", "Nappa leather seating (Ti-L)", "Bose 10-speaker premium audio", "10.8-inch head-up display", "Panoramic sunroof"],
                    "notes": "Silky EV acceleration feel without plugging in."
                }
            ],
            "configurations": [
                {
                    "badge_name": "X-Trail Ti-L e-POWER e-4ORCE",
                    "body_style": "5-door SUV",
                    "engine_code": "KR15DDT-ePower",
                    "transmission": "Single-speed electric reduction",
                    "drivetrain": "AWD",
                    "years_start": 2023,
                    "years_end": "Present",
                    "msrp_aud": 57690,
                    "power_kw": 157.0,
                    "torque_nm": 330.0,
                    "fuel_l_100km": 6.1,
                    "towing_braked_kg": 1650,
                    "notes": "Twin-motor e-4ORCE all-wheel electric drive."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

PULSAR_MODEL = {
    "make_slug": "nissan",
    "model_slug": "pulsar",
    "name": "Pulsar",
    "vehicle_type": "Hatchback / Sedan",
    "segment": "Small Car / Hot Hatch",
    "years_sold_au": {"start": 1980, "end": 2017},
    "locally_built": True,
    "assembly_plants_au": ["Clayton, Victoria (Nissan Motor Manufacturing Australia)"],
    "overview": "The Nissan Pulsar is one of Australia's most historic small-car badges. Manufactured locally at Nissan's Clayton plant in Victoria through the 1980s and early 1990s, the Pulsar sired genuine Australian performance legends, from the local 1980s Pulsar Turbo ET to the iconic N14/N15 Pulsar SSS with its high-revving 2.0-litre SR20DE engine and the rally-homologated N14 GTI-R.",
    "australian_market_notes": "First sold in 1980, the Clayton-built N12 series gave Australia its first mass-market factory turbocharged hatchback: the 1984 Pulsar Turbo ET. The Clayton plant also built the N12 and N13 Pulsar for Holden as the Astra under the Button Car Plan. Following local factory closure in 1992, fully imported Japanese N14 and N15 Pulsar SSS hatchbacks became beloved Aussie performance benchmarks. The badge returned with the B17/C12 series in 2013, highlighted by the 140kW DIG-Turbo SSS hatch.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "N10/N12",
            "generation_name": "Pulsar 1st & 2nd Gen (inc. Turbo ET)",
            "years": {"start": 1980, "end": 1987},
            "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"],
            "platform": "Nissan N10/N12",
            "ancap_rating": "Untested",
            "summary": "Clayton-built N12 launched Australia's first affordable hot hatch in 1984: the Pulsar Turbo ET with a 77kW turbocharged 1.5L E15ET engine, also badge-engineered as the Holden Astra LB/LC.",
            "engines": [
                {
                    "engine_code": "E15ET",
                    "name": "Nissan E15ET 1.5L Turbo",
                    "displacement_cc": 1488,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged (Garrett T2)",
                    "fuel_type": "Petrol",
                    "power_kw": 77.0,
                    "power_rpm": "5600",
                    "torque_nm": 140.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "8.0:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Australia's first locally assembled production turbocharged hatchback."
                }
            ],
            "badges": [
                {
                    "badge_name": "Turbo ET",
                    "years": {"start": 1984, "end": 1987},
                    "body_styles": ["3-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 11990,
                    "msrp_aud_max": 13990,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 890,
                    "standard_features": ["Turbo ET decals and striping", "Sports seats", "Boost light", "Four-wheel disc brakes", "Alloy wheels"],
                    "notes": "Clayton VIC assembled; 1980s pocket rocket."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Pulsar Turbo ET Hatch",
                    "body_style": "3-door Hatch",
                    "engine_code": "E15ET",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1984,
                    "years_end": 1987,
                    "msrp_aud": 12990,
                    "power_kw": 77.0,
                    "torque_nm": 140.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 600,
                    "notes": "Australia's original turbo hot hatch."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "N13",
            "generation_name": "Pulsar 3rd Generation (Clayton-built)",
            "years": {"start": 1987, "end": 1991},
            "body_styles": ["5-door Hatch", "4-door Sedan (Vector)"],
            "platform": "Nissan N13",
            "ancap_rating": "Untested",
            "summary": "Clayton-built N13 series featuring Holden-supplied Family II 1.6L and 1.8L engines under the UAA joint venture. Introduced the Vector luxury sedan and sporting SSS hatch.",
            "engines": [
                {
                    "engine_code": "20LE",
                    "name": "GM-Holden Family II 1.8L EFI (20LE)",
                    "displacement_cc": 1796,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Unleaded Petrol",
                    "power_kw": 79.0,
                    "power_rpm": "5600",
                    "torque_nm": 151.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 8-valve EFI",
                    "notes": "Holden-sourced engine used in Pulsar SSS and Vector."
                }
            ],
            "badges": [
                {
                    "badge_name": "Vector / SSS",
                    "years": {"start": 1987, "end": 1991},
                    "body_styles": ["Hatch", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 17990,
                    "msrp_aud_max": 23500,
                    "fuel_consumption_l_100km": 8.2,
                    "kerb_weight_kg": 1050,
                    "standard_features": ["1.8L engine", "Sports body kit (SSS)", "Velour trim", "Power steering", "Four-wheel disc brakes"],
                    "notes": "Also sold as Holden Astra LD."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Pulsar SSS 1.8 Hatch",
                    "body_style": "5-door Hatch",
                    "engine_code": "20LE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1988,
                    "years_end": 1991,
                    "msrp_aud": 19990,
                    "power_kw": 79.0,
                    "torque_nm": 151.0,
                    "fuel_l_100km": 8.2,
                    "towing_braked_kg": 800,
                    "notes": "Clayton assembled sports hatch."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "N14",
            "generation_name": "Pulsar 4th Gen (SSS & GTI-R)",
            "years": {"start": 1991, "end": 1995},
            "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"],
            "platform": "Nissan N14",
            "ancap_rating": "Untested",
            "summary": "Introduced the redtop SR20DE 2.0L engine to the Pulsar SSS hatch, alongside the homologation titan Pulsar GTI-R (SR20DET 169kW with ATTESA AWD).",
            "engines": [
                {
                    "engine_code": "SR20DE-N14",
                    "name": "Nissan SR20DE 2.0L Twin Cam 16V",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 105.0,
                    "power_rpm": "6400",
                    "torque_nm": 179.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "High-revving naturally aspirated SR20 with 7,500rpm limiter."
                },
                {
                    "engine_code": "SR20DET-GTIR",
                    "name": "Nissan SR20DET 2.0L Turbo (GTI-R)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled (Garrett T28)",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 169.0,
                    "power_rpm": "6400",
                    "torque_nm": 284.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "8.3:1",
                    "valvetrain": "DOHC 16-valve (quad-throttle bodies)",
                    "notes": "Individual throttle bodies (ITB) and top-mount intercooler beneath massive bonnet scoop."
                }
            ],
            "badges": [
                {
                    "badge_name": "SSS Hatch",
                    "years": {"start": 1991, "end": 1995},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD with viscous LSD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 27990,
                    "fuel_consumption_l_100km": 8.7,
                    "kerb_weight_kg": 1100,
                    "standard_features": ["SR20DE 105kW engine", "Viscous limited-slip differential", "14-inch sports alloys", "Sports bucket seats", "Rear spoiler"],
                    "notes": "Aussie hot hatch benchmark."
                },
                {
                    "badge_name": "GTI-R",
                    "years": {"start": 1991, "end": 1993},
                    "body_styles": ["3-door Hatch"],
                    "drivetrain": "ATTESA Full-Time AWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 44990,
                    "msrp_aud_max": 44990,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1220,
                    "standard_features": ["169kW turbo engine with ITBs", "ATTESA AWD with viscous centre and rear LSD", "Large bonnet nostrils and scoop", "High rear wing", "0-100 km/h in 5.4s"],
                    "notes": "Group A rally homologation special; grey import and enthusiast cult legend."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Pulsar SSS Hatch Manual",
                    "body_style": "5-door Hatch",
                    "engine_code": "SR20DE-N14",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1991,
                    "years_end": 1995,
                    "msrp_aud": 25990,
                    "power_kw": 105.0,
                    "torque_nm": 179.0,
                    "fuel_l_100km": 8.7,
                    "towing_braked_kg": 1000,
                    "notes": "Iconic Australian hot hatch."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "N15",
            "generation_name": "Pulsar 5th Gen (SR20DE SSS)",
            "years": {"start": 1995, "end": 2000},
            "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"],
            "platform": "Nissan N15",
            "ancap_rating": "3 stars",
            "summary": "The definitive Australian hot hatch of the late 1990s. Powered by the high-revving 105kW 2.0L SR20DE engine with multi-link beam rear suspension and viscous LSD.",
            "engines": [
                {
                    "engine_code": "SR20DE-N15",
                    "name": "Nissan SR20DE 2.0L Twin Cam",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 105.0,
                    "power_rpm": "6400",
                    "torque_nm": 179.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Silver-top SR20 with revised intake plenum and distributor."
                }
            ],
            "badges": [
                {
                    "badge_name": "SSS Hatch",
                    "years": {"start": 1995, "end": 2000},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD with viscous LSD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 26990,
                    "msrp_aud_max": 29990,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 1130,
                    "standard_features": ["15-inch alloy wheels", "Viscous limited-slip differential", "White-face sports dials (Series II)", "Rear spoiler", "Sports bucket seats", "Four-wheel disc brakes with ABS"],
                    "notes": "Widely regarded as one of the best naturally aspirated front-wheel drive chassis of the 1990s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Pulsar SSS N15 Manual",
                    "body_style": "5-door Hatch",
                    "engine_code": "SR20DE-N15",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1995,
                    "years_end": 2000,
                    "msrp_aud": 27990,
                    "power_kw": 105.0,
                    "torque_nm": 179.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 1000,
                    "notes": "0-100 km/h in 8.2 seconds with LSD standard."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "N16",
            "generation_name": "Pulsar 6th Generation",
            "years": {"start": 2000, "end": 2006},
            "body_styles": ["5-door Hatch", "4-door Sedan"],
            "platform": "Nissan MS platform",
            "ancap_rating": "4 stars",
            "summary": "Conservative family commuter offering 1.8L QG18DE engine, standard dual airbags, and spacious sedan and hatch packaging.",
            "engines": [
                {
                    "engine_code": "QG18DE",
                    "name": "Nissan QG18DE 1.8L DOHC",
                    "displacement_cc": 1769,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 92.0,
                    "power_rpm": "5600",
                    "torque_nm": 161.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Variable valve timing on intake cam."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST / Q",
                    "years": {"start": 2000, "end": 2006},
                    "body_styles": ["Sedan", "Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 19990,
                    "msrp_aud_max": 24990,
                    "fuel_consumption_l_100km": 7.8,
                    "kerb_weight_kg": 1180,
                    "standard_features": ["Dual front airbags", "Air conditioning", "Power front windows", "CD player", "Remote keyless entry"],
                    "notes": "Mainstream private and fleet runabout."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Pulsar Q 1.8 Hatch",
                    "body_style": "5-door Hatch",
                    "engine_code": "QG18DE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2000,
                    "years_end": 2006,
                    "msrp_aud": 22490,
                    "power_kw": 92.0,
                    "torque_nm": 161.0,
                    "fuel_l_100km": 7.8,
                    "towing_braked_kg": 1000,
                    "notes": "Popular small family hatch."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "B17/C12",
            "generation_name": "Pulsar 7th Gen (inc. DIG-Turbo SSS)",
            "years": {"start": 2013, "end": 2017},
            "body_styles": ["4-door Sedan (B17)", "5-door Hatch (C12)"],
            "platform": "Nissan V-platform",
            "ancap_rating": "5 stars",
            "summary": "Revival of the Pulsar name in Australia. B17 sedan offered class-leading rear legroom, while C12 SSS hatch revived the hero badge with a 140kW 1.6L DIG-Turbo engine.",
            "engines": [
                {
                    "engine_code": "MR16DDT",
                    "name": "Nissan MR16DDT 1.6L DIG-Turbo",
                    "displacement_cc": 1618,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 140.0,
                    "power_rpm": "5600",
                    "torque_nm": 240.0,
                    "torque_rpm": "2000-5200",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve Direct Injection",
                    "notes": "Direct-injection turbo with 240Nm across wide rev band."
                }
            ],
            "badges": [
                {
                    "badge_name": "SSS Hatch",
                    "years": {"start": 2013, "end": 2017},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "Xtronic CVT"],
                    "msrp_aud_min": 26990,
                    "msrp_aud_max": 29990,
                    "fuel_consumption_l_100km": 7.7,
                    "kerb_weight_kg": 1300,
                    "standard_features": ["140kW turbo engine", "17-inch sports alloys", "Xenon headlights with washers", "Sports aero body kit", "Leather-accented seats", "Satellite navigation"],
                    "notes": "0-100 km/h in 7.3s; outstanding turbo performance value."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Pulsar SSS Turbo Manual",
                    "body_style": "5-door Hatch",
                    "engine_code": "MR16DDT",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2013,
                    "years_end": 2017,
                    "msrp_aud": 26990,
                    "power_kw": 140.0,
                    "torque_nm": 240.0,
                    "fuel_l_100km": 7.7,
                    "towing_braked_kg": 1200,
                    "notes": "Final Australian Pulsar SSS."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

Z_CAR_MODEL = {
    "make_slug": "nissan",
    "model_slug": "z-car",
    "name": "Z-Car (Fairlady Z)",
    "vehicle_type": "Sports Car / Coupe",
    "segment": "Sports Car",
    "years_sold_au": {"start": 1970, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Datsun and Nissan Z-Car is one of the most celebrated sports car dynasties in Australian automotive history. From the breathtaking 1970 Datsun 240Z that conquered Jaguar E-Types and MGs on price and performance to the twin-turbo technology tour-de-force 300ZX, the pure rear-drive naturally aspirated 350Z and 370Z, and the modern 298kW twin-turbo RZ34 Z Coupe, the Z represents affordable, exhilarating grand touring sports car excellence.",
    "australian_market_notes": "First imported in late 1970 by Datsun Australia, the 240Z revolutionized the Australian sports car landscape. The Z32 300ZX Twin Turbo of the 1990s introduced Super HICAS four-wheel steering and claimed supercar benchmarks. The 2003 350Z Track brought Brembo brakes and carbon driveshafts to the enthusiast market. In 2022, the RZ34 Z returned with retro styling cues honouring the 240Z and 300ZX with 298kW twin-turbo V6 power.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "S30",
            "generation_name": "240Z & 260Z",
            "years": {"start": 1970, "end": 1978},
            "body_styles": ["2-door Coupe", "2+2 Coupe"],
            "platform": "Nissan S30",
            "ancap_rating": "Untested",
            "summary": "The original game changer. 240Z (2.4L L24 OHC straight-six with twin Hitachi SU carburettors), followed by 260Z 2-seater and 2+2 (2.6L L26). Four-wheel independent strut suspension and front disc brakes.",
            "engines": [
                {
                    "engine_code": "L24",
                    "name": "Datsun L24 2.4L OHC Inline-6",
                    "displacement_cc": 2393,
                    "displacement_litres": 2.4,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 113.0,
                    "power_rpm": "5600",
                    "torque_nm": 198.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Twin Hitachi SU-type carburettors; musical straight-six exhaust note."
                },
                {
                    "engine_code": "L26",
                    "name": "Datsun L26 2.6L OHC Inline-6",
                    "displacement_cc": 2565,
                    "displacement_litres": 2.6,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 121.0,
                    "power_rpm": "5600",
                    "torque_nm": 209.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Fitted to 260Z 2-seater and longer wheelbase 2+2."
                }
            ],
            "badges": [
                {
                    "badge_name": "240Z",
                    "years": {"start": 1970, "end": 1974},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 4567,
                    "msrp_aud_max": 5190,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1040,
                    "standard_features": ["Long bonnet / short rear deck styling", "Wood-rim 3-spoke steering wheel", "Triple auxiliary gauges on dash top", "Reclining bucket seats", "14-inch steel wheels with full wheel covers"],
                    "notes": "One of the most desirable classic sports cars in Australia."
                },
                {
                    "badge_name": "260Z 2-Seater & 2+2",
                    "years": {"start": 1974, "end": 1978},
                    "body_styles": ["2-door Coupe", "2+2 Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 6890,
                    "msrp_aud_max": 8990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1140,
                    "standard_features": ["2.6L engine", "300mm longer wheelbase (2+2)", "Fold-down rear seat (2+2)", "Updated dashboard with integrated vents"],
                    "notes": "2+2 brought practical family sports touring."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Datsun 240Z Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "L24",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1970,
                    "years_end": 1974,
                    "msrp_aud": 4567,
                    "power_kw": 113.0,
                    "torque_nm": 198.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 0,
                    "notes": "The legendary original Australian Z."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "S130",
            "generation_name": "280ZX",
            "years": {"start": 1979, "end": 1983},
            "body_styles": ["2-door Coupe", "2+2 Coupe", "T-Bar Roof"],
            "platform": "Nissan S130",
            "ancap_rating": "Untested",
            "summary": "Luxury grand touring era with electronic fuel injection (2.8L L28E), power steering, removable T-Bar glass roof panels, and semi-trailing arm rear suspension.",
            "engines": [
                {
                    "engine_code": "L28E",
                    "name": "Datsun L28E 2.8L EFI Inline-6",
                    "displacement_cc": 2753,
                    "displacement_litres": 2.8,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 103.0,
                    "power_rpm": "5200",
                    "torque_nm": 203.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.3:1",
                    "valvetrain": "SOHC 12-valve EFI",
                    "notes": "Bosch L-Jetronic fuel injection."
                }
            ],
            "badges": [
                {
                    "badge_name": "280ZX T-Bar",
                    "years": {"start": 1979, "end": 1983},
                    "body_styles": ["2+2 T-Bar Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 17990,
                    "msrp_aud_max": 24500,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1280,
                    "standard_features": ["Removable glass T-Bar roof panels", "Four-wheel disc brakes", "Power windows and mirrors", "Alloy wheels", "Velour interior"],
                    "notes": "Grand touring luxury cruiser."
                }
            ],
            "configurations": [
                {
                    "badge_name": "280ZX T-Bar 2+2",
                    "body_style": "2+2 T-Bar Coupe",
                    "engine_code": "L28E",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1979,
                    "years_end": 1983,
                    "msrp_aud": 19990,
                    "power_kw": 103.0,
                    "torque_nm": 203.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 900,
                    "notes": "Iconic removable glass T-top."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "Z31",
            "generation_name": "300ZX 1st Generation",
            "years": {"start": 1984, "end": 1989},
            "body_styles": ["2-door Coupe", "2+2 Coupe", "T-Bar"],
            "platform": "Nissan Z31",
            "ancap_rating": "Untested",
            "summary": "Introduced Japan's first mass-produced V6 engine (VG30E / VG30ET Turbo), pop-up semi-concealed headlights, digital dashboard, and 3-way electronically adjustable shocks.",
            "engines": [
                {
                    "engine_code": "VG30ET",
                    "name": "Nissan VG30ET 3.0L Turbo V6",
                    "displacement_cc": 2960,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Turbocharged (Garrett T3)",
                    "fuel_type": "Petrol",
                    "power_kw": 155.0,
                    "power_rpm": "5200",
                    "torque_nm": 308.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "7.8:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Cast-iron block V6 with Garrett turbo."
                }
            ],
            "badges": [
                {
                    "badge_name": "300ZX & 300ZX Turbo",
                    "years": {"start": 1984, "end": 1989},
                    "body_styles": ["2-door Coupe", "2+2 T-Bar"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 32990,
                    "msrp_aud_max": 48990,
                    "fuel_consumption_l_100km": 11.8,
                    "kerb_weight_kg": 1410,
                    "standard_features": ["Digital instrument cluster", "3-way electronically adjustable shock absorbers", "Removable T-top roof", "Leather seats (Turbo)", "15 or 16-inch alloy wheels"],
                    "notes": "Technological showcase of the 1980s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "300ZX Turbo T-Bar",
                    "body_style": "2+2 T-Bar Coupe",
                    "engine_code": "VG30ET",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1986,
                    "years_end": 1989,
                    "msrp_aud": 46990,
                    "power_kw": 155.0,
                    "torque_nm": 308.0,
                    "fuel_l_100km": 11.8,
                    "towing_braked_kg": 1000,
                    "notes": "155kW turbocharged grand tourer."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "Z32",
            "generation_name": "300ZX 2nd Generation (Twin Turbo)",
            "years": {"start": 1989, "end": 1996},
            "body_styles": ["2-door 2-Seater", "2-door 2+2 T-Bar", "Convertible"],
            "platform": "Nissan Z32",
            "ancap_rating": "Untested",
            "summary": "Masterpiece of Japanese supercar engineering. Wide low-slung stance, VG30DETT twin-turbo engine delivering 208kW, Super HICAS four-wheel steering, and four-wheel multi-link suspension.",
            "engines": [
                {
                    "engine_code": "VG30DE",
                    "name": "Nissan VG30DE 3.0L Quad-Cam 24V V6",
                    "displacement_cc": 2960,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 166.0,
                    "power_rpm": "6400",
                    "torque_nm": 273.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 24-valve NVCS",
                    "notes": "Variable valve timing on intake cams."
                },
                {
                    "engine_code": "VG30DETT",
                    "name": "Nissan VG30DETT 3.0L Twin-Turbo V6",
                    "displacement_cc": 2960,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Parallel Twin-Turbocharged Dual-Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 208.0,
                    "power_rpm": "6400",
                    "torque_nm": 388.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 24-valve NVCS",
                    "notes": "Twin Garrett T22 turbos and twin side-mount intercoolers; 208kW Australian specification."
                }
            ],
            "badges": [
                {
                    "badge_name": "300ZX Naturally Aspirated",
                    "years": {"start": 1989, "end": 1996},
                    "body_styles": ["2+2 T-Bar Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 64990,
                    "msrp_aud_max": 75000,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1530,
                    "standard_features": ["Glass T-bar roof", "Climate control", "Cruise control", "Bose audio", "16-inch alloy wheels"],
                    "notes": "Official Australian delivered model."
                },
                {
                    "badge_name": "300ZX Twin Turbo",
                    "years": {"start": 1989, "end": 1996},
                    "body_styles": ["2-Seater", "2+2 T-Bar Coupe"],
                    "drivetrain": "RWD with Super HICAS 4-wheel steering",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 85000,
                    "msrp_aud_max": 105000,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 1580,
                    "standard_features": ["208kW twin-turbo engine", "Super HICAS active rear-wheel steering", "Viscous limited-slip differential", "Brembo-developed 4-piston aluminium brake calipers", "Rear spoiler"],
                    "notes": "Supercar slayer capable of 0-100 km/h in 5.3s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "300ZX Twin Turbo Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "VG30DETT",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1990,
                    "years_end": 1996,
                    "msrp_aud": 89990,
                    "power_kw": 208.0,
                    "torque_nm": 388.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 0,
                    "notes": "Legendary Japanese high-tech performance titan."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "Z33",
            "generation_name": "350Z",
            "years": {"start": 2003, "end": 2009},
            "body_styles": ["2-door Coupe", "2-door Roadster"],
            "platform": "Nissan FM platform",
            "ancap_rating": "Untested",
            "summary": "Revival of the pure sports car ethos on the front midship (FM) chassis. Carbon-fibre composite driveshaft, naturally aspirated 3.5L VQ35DE / VQ35HR engine (up to 230kW), and Brembo brakes.",
            "engines": [
                {
                    "engine_code": "VQ35DE-Z33",
                    "name": "Nissan VQ35DE 3.5L V6",
                    "displacement_cc": 3498,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 206.0,
                    "power_rpm": "6200",
                    "torque_nm": 363.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "10.3:1",
                    "valvetrain": "DOHC 24-valve Continuously Variable Valve Timing",
                    "notes": "Upgraded to 221kW in 2005 35th Anniversary edition."
                },
                {
                    "engine_code": "VQ35HR",
                    "name": "Nissan VQ35HR 3.5L High-Rev V6",
                    "displacement_cc": 3498,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated (Dual Throttle)",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 230.0,
                    "power_rpm": "6800",
                    "torque_nm": 358.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "10.6:1",
                    "valvetrain": "DOHC 24-valve e-VTC",
                    "notes": "High-rev engine with twin symetrical air intakes and 7,500rpm redline (2007-2009)."
                }
            ],
            "badges": [
                {
                    "badge_name": "Touring",
                    "years": {"start": 2003, "end": 2009},
                    "body_styles": ["Coupe", "Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 59990,
                    "msrp_aud_max": 69990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1470,
                    "standard_features": ["17 or 18-inch alloys", "Leather upholstery", "Bose 7-speaker audio", "Climate control", "Carbon-fibre driveshaft"],
                    "notes": "Popular sports grand tourer."
                },
                {
                    "badge_name": "Track",
                    "years": {"start": 2003, "end": 2009},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD with viscous LSD",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 65990,
                    "msrp_aud_max": 69990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1450,
                    "standard_features": ["Gold Brembo 4-piston front brake calipers", "RAYS lightweight forged 18-inch wheels", "Front and rear aero spoilers", "Viscous limited-slip differential"],
                    "notes": "Dedicated track weapon in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "350Z Track Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "VQ35HR",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2007,
                    "years_end": 2009,
                    "msrp_aud": 67990,
                    "power_kw": 230.0,
                    "torque_nm": 358.0,
                    "fuel_l_100km": 11.7,
                    "towing_braked_kg": 0,
                    "notes": "230kW twin-throttle VQ35HR with Brembo brakes and RAYS forged wheels."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "Z34",
            "generation_name": "370Z",
            "years": {"start": 2009, "end": 2021},
            "body_styles": ["2-door Coupe", "2-door Roadster"],
            "platform": "Nissan FM platform",
            "ancap_rating": "Untested",
            "summary": "Shorter wheelbase, wider track, aluminium doors and bonnet, 3.7L VQ37VHR engine with VVEL (245kW standard, 253kW Nismo), and world-first SynchroRev Match manual transmission.",
            "engines": [
                {
                    "engine_code": "VQ37VHR",
                    "name": "Nissan VQ37VHR 3.7L VVEL V6",
                    "displacement_cc": 3696,
                    "displacement_litres": 3.7,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 245.0,
                    "power_rpm": "7000",
                    "torque_nm": 363.0,
                    "torque_rpm": "5200",
                    "compression_ratio": "11.0:1",
                    "valvetrain": "DOHC 24-valve VVEL",
                    "notes": "Variable Valve Event and Lift controlling throttle directly at intake valves."
                },
                {
                    "engine_code": "VQ37VHR-Nismo",
                    "name": "Nissan VQ37VHR 3.7L VVEL V6 (Nismo)",
                    "displacement_cc": 3696,
                    "displacement_litres": 3.7,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 253.0,
                    "power_rpm": "7400",
                    "torque_nm": 371.0,
                    "torque_rpm": "5200",
                    "compression_ratio": "11.0:1",
                    "valvetrain": "DOHC 24-valve VVEL",
                    "notes": "Nismo dual exhaust and ECM tune producing 253kW."
                }
            ],
            "badges": [
                {
                    "badge_name": "370Z Coupe & Roadster",
                    "years": {"start": 2009, "end": 2021},
                    "body_styles": ["Coupe", "Roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual with SynchroRev Match", "7-speed automatic with paddle shifters"],
                    "msrp_aud_min": 49990,
                    "msrp_aud_max": 74990,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1475,
                    "standard_features": ["SynchroRev Match automated throttle blipping", "19-inch RAYS forged alloys", "Sport brakes with red 4-piston calipers", "Viscous LSD", "Bose 8-speaker audio"],
                    "notes": "World-first rev-matching manual transmission."
                },
                {
                    "badge_name": "370Z Nismo",
                    "years": {"start": 2017, "end": 2021},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "7-speed automatic"],
                    "msrp_aud_min": 61490,
                    "msrp_aud_max": 63990,
                    "fuel_consumption_l_100km": 10.6,
                    "kerb_weight_kg": 1510,
                    "standard_features": ["253kW engine tune", "Nismo aerodynamic body kit with rear diffuser and spoiler", "Recaro leather/Alcantara sports seats", "Nismo-tuned suspension with front and rear performance dampers", "19-inch super-lightweight RAYS forged wheels"],
                    "notes": "Factory track-special edition."
                }
            ],
            "configurations": [
                {
                    "badge_name": "370Z Nismo Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "VQ37VHR-Nismo",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2017,
                    "years_end": 2021,
                    "msrp_aud": 61490,
                    "power_kw": 253.0,
                    "torque_nm": 371.0,
                    "fuel_l_100km": 10.6,
                    "towing_braked_kg": 0,
                    "notes": "253kW naturally aspirated sports coupe."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "RZ34",
            "generation_name": "Nissan Z (7th Generation)",
            "years": {"start": 2022, "end": "Present"},
            "body_styles": ["2-door Coupe"],
            "platform": "Nissan FM platform",
            "ancap_rating": "Untested",
            "summary": "Tribute to 50+ years of Z heritage with 240Z-inspired silhouette and 300ZX-inspired LED tail-lights. Powered by the 298kW 3.0L VR30DDTT twin-turbo V6 with manual or 9-speed auto, and track-ready Z Nismo.",
            "engines": [
                {
                    "engine_code": "VR30DDTT",
                    "name": "Nissan VR30DDTT 3.0L Twin-Turbo V6",
                    "displacement_cc": 2997,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Twin-Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 298.0,
                    "power_rpm": "6400",
                    "torque_nm": 475.0,
                    "torque_rpm": "1600-5600",
                    "compression_ratio": "10.3:1",
                    "valvetrain": "DOHC 24-valve Direct Injection",
                    "notes": "Direct injection twin-turbo V6; optical turbo speed sensors."
                },
                {
                    "engine_code": "VR30DDTT-Nismo",
                    "name": "Nissan VR30DDTT 3.0L Twin-Turbo V6 (Nismo)",
                    "displacement_cc": 2997,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Twin-Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 313.0,
                    "power_rpm": "6400",
                    "torque_nm": 520.0,
                    "torque_rpm": "2000-5200",
                    "compression_ratio": "10.3:1",
                    "valvetrain": "DOHC 24-valve Direct Injection",
                    "notes": "Upgraded boost and wastegate control producing 313kW and 520Nm."
                }
            ],
            "badges": [
                {
                    "badge_name": "Z Coupe / Proto Spec",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD with mechanical clutch-type LSD",
                    "transmissions": ["6-speed manual with launch control", "9-speed automatic with paddle shifters"],
                    "msrp_aud_min": 73300,
                    "msrp_aud_max": 80500,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1573,
                    "standard_features": ["12.3-inch digital instrument cluster", "8-inch touchscreen with Apple CarPlay", "Bose 8-speaker audio", "Brembo 4-piston front calipers", "19-inch RAYS forged alloys", "Active noise cancellation"],
                    "notes": "Sold out first year Australian allocation instantly."
                },
                {
                    "badge_name": "Z Nismo",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD with mechanical LSD",
                    "transmissions": ["9-speed performance automatic"],
                    "msrp_aud_min": 94000,
                    "msrp_aud_max": 94000,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1650,
                    "standard_features": ["313kW engine", "Recaro leather/Alcantara bucket seats", "Akebono 15.0-inch 4-piston front brakes", "Stiffer chassis bracing", "Nismo tuned suspension and aero", "Dunlop SP Sport MAXX GT600 tyres"],
                    "notes": "Ultimate factory track iteration; 0-100 km/h in 4.3 seconds."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Nissan Z Coupe Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "VR30DDTT",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2022,
                    "years_end": "Present",
                    "msrp_aud": 73300,
                    "power_kw": 298.0,
                    "torque_nm": 475.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 0,
                    "notes": "298kW twin-turbo manual sports coupe with launch control."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}
