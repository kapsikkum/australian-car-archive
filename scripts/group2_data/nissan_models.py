"""Deep-dive model data for Nissan: Patrol and Skyline."""

PATROL_MODEL = {
    "make_slug": "nissan",
    "model_slug": "patrol",
    "name": "Patrol",
    "vehicle_type": "4WD Wagon / Cab Chassis",
    "segment": "Upper Large 4WD",
    "years_sold_au": {"start": 1962, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Nissan Patrol is an Australian outback giant. In 1962, the G60 Patrol made history as the first motor vehicle to cross the Simpson Desert. Across MQ, GQ, GU, and the V8-powered Y62, it has matched the LandCruiser blow for blow across Australia's harshest terrain.",
    "australian_market_notes": "The coil-sprung GQ Patrol (also sold as the Ford Maverick under the Button Plan) revolutionized off-road wheel travel and touring comfort in 1987. The TD42 4.2L diesel earned unkillable folklore status, while the modern Y62 with its 298kW 5.6L V8 and Premcar-engineered Warrior editions represents the ultimate heavy tow vehicle.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "G60",
            "generation_name": "Patrol G60",
            "years": {"start": 1962, "end": "1980"},
            "body_styles": ["SWB Soft-top", "SWB Hardtop", "LWB Wagon", "Cab Chassis"],
            "platform": "Nissan 60 Series",
            "ancap_rating": "Untested",
            "summary": "Historic heavy-duty 4x4. The Sprigg family drove an Australian G60 across the Simpson Desert in 1962, cementing Nissan's rugged reputation.",
            "engines": [
                {
                    "engine_code": "P40",
                    "name": "Nissan P40 4.0L",
                    "displacement_cc": 3956,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 107.0,
                    "power_rpm": "3800",
                    "torque_nm": 319.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "7.8:1",
                    "valvetrain": "OHV 12-valve",
                    "notes": "Low-compression heavy truck-derived inline-6."
                }
            ],
            "badges": [
                {
                    "badge_name": "Hardtop",
                    "years": {"start": 1962, "end": "1980"},
                    "body_styles": ["SWB Hardtop"],
                    "drivetrain": "4WD",
                    "transmissions": ["3-speed manual", "4-speed manual"],
                    "msrp_aud_min": 2990,
                    "msrp_aud_max": 7500,
                    "fuel_consumption_l_100km": 17.5,
                    "kerb_weight_kg": 1680,
                    "standard_features": ["Solid beam axles", "Leaf springs", "Dual-range transfer case", "Manual locking hubs"],
                    "notes": "Simpson Desert crossing pioneer."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Hardtop",
                    "body_style": "SWB Hardtop",
                    "engine_code": "P40",
                    "transmission": "4-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1968,
                    "years_end": "1980",
                    "msrp_aud": 4200,
                    "power_kw": 107.0,
                    "torque_nm": 319.0,
                    "fuel_l_100km": 17.5,
                    "towing_braked_kg": 2000,
                    "notes": "G60 Short Wheelbase."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "GQ/Y60",
            "generation_name": "Patrol GQ",
            "years": {"start": 1987, "end": "1997"},
            "body_styles": ["SWB 3-door Hardtop", "LWB 5-door Wagon", "Cab Chassis Ute"],
            "platform": "Nissan Y60",
            "ancap_rating": "Untested",
            "summary": "Pioneered coil springs on live solid axles front and rear, transforming outback off-road wheel articulation and comfort. Home to the legendary TD42 'Silver Top' diesel.",
            "engines": [
                {
                    "engine_code": "TD42",
                    "name": "Nissan TD42 4.2L Diesel",
                    "displacement_cc": 4169,
                    "displacement_litres": 4.2,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 85.0,
                    "power_rpm": "4000",
                    "torque_nm": 264.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "22.7:1",
                    "valvetrain": "OHV 12-valve with gear-driven timing",
                    "notes": "Gear-driven camshaft, iron block and head; legendary million-kilometre reliability."
                },
                {
                    "engine_code": "TB42",
                    "name": "Nissan TB42 4.2L Petrol",
                    "displacement_cc": 4169,
                    "displacement_litres": 4.2,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 125.0,
                    "power_rpm": "4200",
                    "torque_nm": 325.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "OHV 12-valve (carburetted and EFI TB42E)",
                    "notes": "Strong, torquey petrol inline-6."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST",
                    "years": {"start": 1987, "end": "1997"},
                    "body_styles": ["LWB 5-door Wagon"],
                    "drivetrain": "Part-time 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 32990,
                    "msrp_aud_max": 47500,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 2180,
                    "standard_features": ["7-passenger seating", "All-coil suspension", "Wide wheelarch flares", "Power windows and mirrors", "Air conditioning", "Limited slip differential"],
                    "notes": "The high-volume choice of Australian outback tourers; also sold as Ford Maverick."
                },
                {
                    "badge_name": "Ti",
                    "years": {"start": 1987, "end": "1997"},
                    "body_styles": ["LWB 5-door Wagon"],
                    "drivetrain": "Part-time 4WD",
                    "transmissions": ["4-speed automatic", "5-speed manual"],
                    "msrp_aud_min": 45000,
                    "msrp_aud_max": 59990,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 2240,
                    "standard_features": ["Electric glass sunroof", "Alloy wheels", "Velour upholstery", "Dual air conditioning", "Rear seat cooler box"],
                    "notes": "Flagship luxury wagon."
                }
            ],
            "configurations": [
                {
                    "badge_name": "ST TD42",
                    "body_style": "LWB 5-door Wagon",
                    "engine_code": "TD42",
                    "transmission": "5-speed manual",
                    "drivetrain": "Part-time 4WD",
                    "years_start": 1988,
                    "years_end": "1997",
                    "msrp_aud": 38990,
                    "power_kw": 85.0,
                    "torque_nm": 264.0,
                    "fuel_l_100km": 12.0,
                    "towing_braked_kg": 2500,
                    "notes": "Classic GQ TD42 wagon."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "GU/Y61",
            "generation_name": "Patrol GU",
            "years": {"start": 1997, "end": "2016"},
            "body_styles": ["5-door Wagon", "Single Cab Chassis", "Dual Cab Chassis"],
            "platform": "Nissan Y61",
            "ancap_rating": "3 to 4 Stars",
            "summary": "Heavy-duty live-axle icon produced for nearly 20 years. Offered with TD42T turbo-diesel, ZD30 common-rail, and the 185kW 4.8L TB48DE inline-6 petrol.",
            "engines": [
                {
                    "engine_code": "TD42T",
                    "name": "Nissan TD42T 4.2L Turbo-Diesel",
                    "displacement_cc": 4169,
                    "displacement_litres": 4.2,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Turbocharged (Factory Turbo)",
                    "fuel_type": "Diesel",
                    "power_kw": 114.0,
                    "power_rpm": "3600",
                    "torque_nm": 330.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "22.7:1",
                    "valvetrain": "OHV 12-valve",
                    "notes": "Factory-turbocharged TD42 (upgraded to intercooled TD42Ti 114kW/360Nm in 2003)."
                },
                {
                    "engine_code": "ZD30DDTi",
                    "name": "Nissan ZD30 3.0L Turbo-Diesel",
                    "displacement_cc": 2953,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 118.0,
                    "power_rpm": "3200",
                    "torque_nm": 380.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "17.9:1",
                    "valvetrain": "DOHC 16-valve Common-Rail (CRD from 2007)",
                    "notes": "Common-rail upgrade in 2007 restored strong durability reputation."
                },
                {
                    "engine_code": "TB48DE",
                    "name": "Nissan TB48DE 4.8L Petrol",
                    "displacement_cc": 4779,
                    "displacement_litres": 4.8,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 185.0,
                    "power_rpm": "4800",
                    "torque_nm": 400.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "DOHC 24-valve VVT",
                    "notes": "High-performance twin-cam petrol inline-6 paired with 5-speed tiptronic auto."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST",
                    "years": {"start": 1997, "end": "2016"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Part-time 4WD",
                    "transmissions": ["5-speed manual", "4-speed auto", "5-speed auto"],
                    "msrp_aud_min": 46990,
                    "msrp_aud_max": 59990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 2350,
                    "standard_features": ["Dual fuel tanks (125L total)", "Sub-tank transfer system", "Front and rear live beam axles", "Air conditioning", "Power windows", "ABS brakes"],
                    "notes": "The definition of an Australian heavy-duty touring wagon."
                },
                {
                    "badge_name": "Legend Edition",
                    "years": {"start": 2016, "end": "2016"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Part-time 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 57990,
                    "msrp_aud_max": 60990,
                    "fuel_consumption_l_100km": 10.9,
                    "kerb_weight_kg": 2420,
                    "standard_features": ["Heavy-duty steel bullbar with winch", "Snorkel", "Roof rack with cargo tray", "Towbar", "Rear-view camera and satellite navigation", "Final run of 300 units"],
                    "notes": "Celebrated the end of GU Patrol wagon production after 19 years."
                }
            ],
            "configurations": [
                {
                    "badge_name": "ST TD42Ti",
                    "body_style": "5-door Wagon",
                    "engine_code": "TD42T",
                    "transmission": "5-speed manual",
                    "drivetrain": "Part-time 4WD",
                    "years_start": 2003,
                    "years_end": "2007",
                    "msrp_aud": 56990,
                    "power_kw": 114.0,
                    "torque_nm": 360.0,
                    "fuel_l_100km": 12.0,
                    "towing_braked_kg": 3500,
                    "notes": "GU Series III/IV TD42Ti intercooled."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "Y62",
            "generation_name": "Patrol Y62 (V8 Powerhouse)",
            "years": {"start": 2013, "end": "Present"},
            "body_styles": ["5-door Wagon (7 or 8 seats)"],
            "platform": "Nissan Y62",
            "ancap_rating": "5 Stars",
            "summary": "Powered by the roaring 5.6L VK56VD V8 producing 298kW and 560Nm. Fitted with Hydraulic Body Motion Control (HBMC) and re-engineered in Melbourne by Premcar into the rugged Patrol Warrior.",
            "engines": [
                {
                    "engine_code": "VK56VD",
                    "name": "Nissan 5.6L V8 Direct Injection",
                    "displacement_cc": 5552,
                    "displacement_litres": 5.6,
                    "cylinders": 8,
                    "configuration": "V8",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 298.0,
                    "power_rpm": "5800",
                    "torque_nm": 560.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 32-valve VVEL Direct Injection",
                    "notes": "Massive 298kW output, 7-speed automatic, and roaring V8 soundtrack."
                }
            ],
            "badges": [
                {
                    "badge_name": "Ti",
                    "years": {"start": 2013, "end": "Present"},
                    "body_styles": ["5-door Wagon (8 seats)"],
                    "drivetrain": "All-Mode 4WD",
                    "transmissions": ["7-speed automatic"],
                    "msrp_aud_min": 78990,
                    "msrp_aud_max": 84900,
                    "fuel_consumption_l_100km": 14.4,
                    "kerb_weight_kg": 2750,
                    "standard_features": ["Hydraulic Body Motion Control (HBMC)", "All-Mode 4WD with low range and rear diff lock", "140-litre fuel tank", "18-inch alloy wheels", "Tri-zone climate control", "3500kg towing"],
                    "notes": "Australia's favourite V8 caravan hauler."
                },
                {
                    "badge_name": "Warrior (by Premcar)",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["5-door Wagon (8 seats)"],
                    "drivetrain": "All-Mode 4WD",
                    "transmissions": ["7-speed automatic"],
                    "msrp_aud_min": 101160,
                    "msrp_aud_max": 105000,
                    "fuel_consumption_l_100km": 14.4,
                    "kerb_weight_kg": 2884,
                    "standard_features": ["Premcar engineered suspension with re-valved HBMC (+50mm lift)", "Bi-modal side-exit exhaust system", "Custom 18-inch forged alloy wheels with Yokohama Geolandar AT tyres", "Red bash plate", "Wider track (+40mm)", "Black exterior styling pack"],
                    "notes": "Re-engineered in Melbourne by Premcar specifically for Australian outback touring."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Warrior by Premcar",
                    "body_style": "5-door Wagon",
                    "engine_code": "VK56VD",
                    "transmission": "7-speed automatic",
                    "drivetrain": "All-Mode 4WD",
                    "years_start": 2023,
                    "years_end": "Present",
                    "msrp_aud": 101160,
                    "power_kw": 298.0,
                    "torque_nm": 560.0,
                    "fuel_l_100km": 14.4,
                    "towing_braked_kg": 3500,
                    "notes": "Australian Premcar Patrol Warrior."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

SKYLINE_MODEL = {
    "make_slug": "nissan",
    "model_slug": "skyline",
    "name": "Skyline",
    "vehicle_type": "Sedan / Wagon / Coupe",
    "segment": "Mid-size / Large Sports",
    "years_sold_au": {"start": 1973, "end": "2002"},
    "locally_built": True,
    "assembly_plants_au": ["Clayton, Victoria"],
    "overview": "The Nissan Skyline represents a crowning achievement in Australian motoring. Locally built at Clayton, Victoria in R31 guise with the RB30E engine, it also dominated Bathurst as the twin-turbo R32 GT-R 'Godzilla', ending the V8 monopoly and reshaping Australian motorsport history.",
    "australian_market_notes": "First sold as the Datsun 240K in 1973, Nissan invested heavily to manufacture the R31 Skyline at Clayton from 1986 to 1991. Powered by the imported 3.0L RB30E inline-6, Clayton produced sedans, wagons, and the famous Silhouette and Gibson Motorsport GTS1/GTS2 performance specials. In 1991, Nissan imported 100 R32 GT-Rs; Jim Richards and Mark Skaife demolished the field to win the 1991 and 1992 Bathurst 1000s.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "R31",
            "generation_name": "Skyline R31 (Australian Manufacture)",
            "years": {"start": 1986, "end": "1991"},
            "body_styles": ["4-door Sedan", "Station Wagon"],
            "platform": "Nissan R31",
            "ancap_rating": "Untested",
            "summary": "Proudly manufactured at Nissan's Clayton plant in Melbourne. Powered by the smooth 3.0L RB30E inline-6, it spawned the sporty Silhouette and Gibson Motorsport GTS homologation specials.",
            "engines": [
                {
                    "engine_code": "RB30E",
                    "name": "Nissan RB30E 3.0L SOHC Inline-6",
                    "displacement_cc": 2962,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 114.0,
                    "power_rpm": "5200",
                    "torque_nm": 247.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Silky smooth 3.0-litre inline-6; shared engine architecture with the Holden VL Commodore."
                },
                {
                    "engine_code": "RB30E-GTS",
                    "name": "Nissan Special Vehicles RB30E GTS",
                    "displacement_cc": 2962,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 140.0,
                    "power_rpm": "5600",
                    "torque_nm": 255.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 12-valve modified cam, extractors, tuned ECU",
                    "notes": "Hand-tuned by Gibson Motorsport with specialized camshaft, free-flow exhaust, and bespoke ECU."
                }
            ],
            "badges": [
                {
                    "badge_name": "Silhouette",
                    "years": {"start": 1986, "end": "1991"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 24500,
                    "msrp_aud_max": 29990,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1335,
                    "standard_features": ["Limited slip differential", "Sports bucket seats", "Rear spoiler", "15-inch alloy wheels", "Sports suspension pack", "4-wheel disc brakes"],
                    "notes": "Iconic Australian sports sedan."
                },
                {
                    "badge_name": "GTS (Series 1 & 2)",
                    "years": {"start": 1988, "end": "1990"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 35500,
                    "msrp_aud_max": 37990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1370,
                    "standard_features": ["140kW Gibson Motorsport tuned RB30E", "Bilstein sports dampers", "Scheel sports bucket seats", "Momo leather steering wheel", "LSD", "16-inch alloy wheels", "Only 200 GTS1 (White) and 200 GTS2 (Red) produced"],
                    "notes": "Australian homologation special built to celebrate Australian touring car racing."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Silhouette",
                    "body_style": "Sedan",
                    "engine_code": "RB30E",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1986,
                    "years_end": "1991",
                    "msrp_aud": 24950,
                    "power_kw": 114.0,
                    "torque_nm": 247.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 1200,
                    "notes": "Australian Clayton-built R31 Silhouette."
                },
                {
                    "badge_name": "GTS Series 2",
                    "body_style": "Sedan",
                    "engine_code": "RB30E-GTS",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1990,
                    "years_end": "1990",
                    "msrp_aud": 37990,
                    "power_kw": 140.0,
                    "torque_nm": 255.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 1200,
                    "notes": "Limited edition #1-200 Gibson Motorsport GTS2."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "R32",
            "generation_name": "Skyline R32 GT-R ('Godzilla')",
            "years": {"start": 1989, "end": "1994"},
            "body_styles": ["2-door Coupe"],
            "platform": "Nissan R32",
            "ancap_rating": "Untested",
            "summary": "The car that changed Australian motorsport forever. 100 official Australian-delivered GT-Rs landed in 1991; Fred Gibson's race cars smashed Mount Panorama, winning the 1991 and 1992 Bathurst 1000s.",
            "engines": [
                {
                    "engine_code": "RB26DETT",
                    "name": "Nissan RB26DETT 2.6L Twin-Turbo",
                    "displacement_cc": 2568,
                    "displacement_litres": 2.6,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Twin-Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 206.0,
                    "power_rpm": "6800",
                    "torque_nm": 353.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 24-valve solid lifter multi-throttle",
                    "notes": "Individual throttle bodies, parallel twin T28 ceramic turbochargers, 8,000 rpm redline."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT-R (Australian Delivery)",
                    "years": {"start": 1991, "end": "1991"},
                    "body_styles": ["Coupe"],
                    "drivetrain": "ATTESA E-TS All-Wheel Drive",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 110000,
                    "msrp_aud_max": 110000,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1430,
                    "standard_features": ["ATTESA E-TS electronically controlled AWD", "Super HICAS 4-wheel steering", "Front and rear multi-link suspension", "Twin-turbo RB26DETT", "Aluminium front guards and bonnet", "Local ADR roof reinforcement and child restraints", "Only 100 official Australian models imported"],
                    "notes": "Dubbed 'Godzilla' by Wheels Magazine in 1989; back-to-back Bathurst 1000 champion."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GT-R (Australian Delivery)",
                    "body_style": "Coupe",
                    "engine_code": "RB26DETT",
                    "transmission": "5-speed manual",
                    "drivetrain": "ATTESA E-TS All-Wheel Drive",
                    "years_start": 1991,
                    "years_end": "1991",
                    "msrp_aud": 110000,
                    "power_kw": 206.0,
                    "torque_nm": 353.0,
                    "fuel_l_100km": 12.8,
                    "towing_braked_kg": 0,
                    "notes": "1991 Australian Delivered R32 GT-R #1-100."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

NISSAN_DEEP_DIVES = [PATROL_MODEL, SKYLINE_MODEL]
