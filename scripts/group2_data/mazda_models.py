"""Deep-dive model data for Mazda: Mazda3, RX-7, and BT-50."""

MAZDA3_MODEL = {
    "make_slug": "mazda",
    "model_slug": "mazda3",
    "name": "Mazda3",
    "vehicle_type": "Hatchback / Sedan",
    "segment": "Small Car",
    "years_sold_au": {"start": 2004, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mazda3 is one of Australia's most beloved passenger cars, achieving the rare feat of becoming the country's outright best-selling vehicle in 2011 and 2012. Known for sporty dynamics, sharp KODO design, and high-performance MPS editions.",
    "australian_market_notes": "Replacing the 323 in 2004, the Mazda3 was an immediate triumph in Australia, appealing strongly to private buyers with standard alloy wheels, multi-link rear suspension, and the popular SP23/SP25 grades. The turbocharged 190kW Mazda3 MPS was a cult hot hatch hero.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "BK",
            "generation_name": "Mazda3 1st Generation",
            "years": {"start": 2004, "end": "2009"},
            "body_styles": ["5-door Hatch", "4-door Sedan"],
            "platform": "Mazda BK (Ford C1)",
            "ancap_rating": "4 Stars",
            "summary": "Launched in Australia in early 2004, setting new standards for handling with its Ford C1 multi-link rear suspension, popular SP23 grade, and 190kW turbocharged MPS.",
            "engines": [
                {
                    "engine_code": "LF-VE",
                    "name": "Mazda MZR 2.0L",
                    "displacement_cc": 1999,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 104.0,
                    "power_rpm": "6500",
                    "torque_nm": 181.0,
                    "torque_rpm": "4500",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve S-VT",
                    "notes": "Fitted to Neo, Maxx, and Maxx Sport."
                },
                {
                    "engine_code": "L3-VE",
                    "name": "Mazda MZR 2.3L",
                    "displacement_cc": 2261,
                    "displacement_litres": 2.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 115.0,
                    "power_rpm": "6500",
                    "torque_nm": 203.0,
                    "torque_rpm": "4500",
                    "compression_ratio": "9.7:1",
                    "valvetrain": "DOHC 16-valve S-VT",
                    "notes": "Exclusive to the popular SP23 sports model."
                },
                {
                    "engine_code": "L3-VDT",
                    "name": "Mazda MZR 2.3L DISI Turbo (MPS)",
                    "displacement_cc": 2261,
                    "displacement_litres": 2.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 190.0,
                    "power_rpm": "5500",
                    "torque_nm": 380.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve DISI",
                    "notes": "Torque-monster direct-injected turbo with top-mount intercooler and limited slip differential."
                }
            ],
            "badges": [
                {
                    "badge_name": "SP23",
                    "years": {"start": 2004, "end": "2009"},
                    "body_styles": ["5-door Hatch", "4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed auto", "5-speed auto"],
                    "msrp_aud_min": 28990,
                    "msrp_aud_max": 32990,
                    "fuel_consumption_l_100km": 8.6,
                    "kerb_weight_kg": 1285,
                    "standard_features": ["17-inch alloy wheels", "Sports body kit", "Climate control air-conditioning", "Sports front seats", "Steering wheel audio controls", "Front fog lights"],
                    "notes": "Huge private sales favourite in Australia."
                },
                {
                    "badge_name": "MPS",
                    "years": {"start": 2006, "end": "2009"},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 43600,
                    "fuel_consumption_l_100km": 10.0,
                    "kerb_weight_kg": 1403,
                    "standard_features": ["190kW DISI turbo engine", "Super LSD torque-sensing front diff", "18-inch wheels", "Half-leather sports bucket seats", "Bose 7-speaker audio"],
                    "notes": "Hot hatch giant killer."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SP23",
                    "body_style": "5-door Hatch",
                    "engine_code": "L3-VE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2004,
                    "years_end": "2009",
                    "msrp_aud": 28990,
                    "power_kw": 115.0,
                    "torque_nm": 203.0,
                    "fuel_l_100km": 8.6,
                    "towing_braked_kg": 1200,
                    "notes": "BK SP23 manual hatchback."
                },
                {
                    "badge_name": "MPS",
                    "body_style": "5-door Hatch",
                    "engine_code": "L3-VDT",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2006,
                    "years_end": "2009",
                    "msrp_aud": 39990,
                    "power_kw": 190.0,
                    "torque_nm": 380.0,
                    "fuel_l_100km": 10.0,
                    "towing_braked_kg": 0,
                    "notes": "BK Mazda3 MPS."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "BL",
            "generation_name": "Mazda3 2nd Generation",
            "years": {"start": 2009, "end": "2013"},
            "body_styles": ["5-door Hatch", "4-door Sedan"],
            "platform": "Mazda BL",
            "ancap_rating": "5 Stars",
            "summary": "Historic generation that ended the Holden Commodore's 15-year reign as Australia's top-selling car, finishing #1 outright in 2011 and 2012.",
            "engines": [
                {
                    "engine_code": "L5-VE",
                    "name": "Mazda MZR 2.5L",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 122.0,
                    "power_rpm": "6000",
                    "torque_nm": 227.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.7:1",
                    "valvetrain": "DOHC 16-valve S-VT",
                    "notes": "Smooth, torquey 2.5L engine in the popular SP25."
                },
                {
                    "engine_code": "L3-VDT",
                    "name": "Mazda MZR 2.3L DISI Turbo (MPS)",
                    "displacement_cc": 2261,
                    "displacement_litres": 2.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 190.0,
                    "power_rpm": "5500",
                    "torque_nm": 380.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve DISI",
                    "notes": "Aggressive bonnet scoop feeding top-mount intercooler."
                }
            ],
            "badges": [
                {
                    "badge_name": "SP25",
                    "years": {"start": 2009, "end": "2013"},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 30690,
                    "msrp_aud_max": 35500,
                    "fuel_consumption_l_100km": 8.6,
                    "kerb_weight_kg": 1340,
                    "standard_features": ["17-inch alloy wheels", "Sports front bumper and side skirts", "Dual exhaust outlets", "In-dash satellite navigation", "Dual-zone climate control", "Bluetooth connectivity"],
                    "notes": "Australia's favourite warm hatch/sedan."
                },
                {
                    "badge_name": "Neo",
                    "years": {"start": 2009, "end": "2013"},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 21330,
                    "msrp_aud_max": 24990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 1260,
                    "standard_features": ["6 airbags", "Dynamic Stability Control (DSC)", "Air conditioning", "Power windows and mirrors"],
                    "notes": "High-volume private and fleet seller."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SP25",
                    "body_style": "5-door Hatch",
                    "engine_code": "L5-VE",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2009,
                    "years_end": "2013",
                    "msrp_aud": 30690,
                    "power_kw": 122.0,
                    "torque_nm": 227.0,
                    "fuel_l_100km": 8.6,
                    "towing_braked_kg": 1200,
                    "notes": "BL SP25."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "BP",
            "generation_name": "Mazda3 4th Generation",
            "years": {"start": 2019, "end": "Present"},
            "body_styles": ["5-door Hatch", "4-door Sedan"],
            "platform": "Skyactiv-Vehicle Architecture",
            "ancap_rating": "5 Stars",
            "summary": "Near-luxury evolution with evocative styling, class-leading cabin refinement, and available Skyactiv-X compression-ignition petrol engine.",
            "engines": [
                {
                    "engine_code": "PE-VPS",
                    "name": "Skyactiv-G 2.0L",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 114.0,
                    "power_rpm": "6000",
                    "torque_nm": 200.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT",
                    "notes": "Powers the G20 range."
                },
                {
                    "engine_code": "PY-VPS",
                    "name": "Skyactiv-G 2.5L",
                    "displacement_cc": 2488,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 139.0,
                    "power_rpm": "6000",
                    "torque_nm": 252.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Dual S-VT with Cylinder Deactivation",
                    "notes": "Powers the G25 range."
                }
            ],
            "badges": [
                {
                    "badge_name": "G20 Pure",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 26990,
                    "msrp_aud_max": 31500,
                    "fuel_consumption_l_100km": 6.2,
                    "kerb_weight_kg": 1316,
                    "standard_features": ["Radar cruise control", "Head-up display standard", "Blind spot monitoring", "8.8-inch widescreen infotainment", "LED head/taillights"],
                    "notes": "High standard safety equipment."
                },
                {
                    "badge_name": "G25 Astina",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 38990,
                    "msrp_aud_max": 43500,
                    "fuel_consumption_l_100km": 6.6,
                    "kerb_weight_kg": 1380,
                    "standard_features": ["18-inch black alloy wheels", "Burgundy/black leather trim", "Bose 12-speaker audio", "Sunroof", "360-degree view monitor", "Cruising & Traffic Support"],
                    "notes": "Flagship model with prestige cabin finish."
                }
            ],
            "configurations": [
                {
                    "badge_name": "G25 Astina",
                    "body_style": "5-door Hatch",
                    "engine_code": "PY-VPS",
                    "transmission": "6-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2019,
                    "years_end": "Present",
                    "msrp_aud": 41590,
                    "power_kw": 139.0,
                    "torque_nm": 252.0,
                    "fuel_l_100km": 6.6,
                    "towing_braked_kg": 1200,
                    "notes": "BP G25 Astina."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

RX7_MODEL = {
    "make_slug": "mazda",
    "model_slug": "rx-7",
    "name": "RX-7",
    "vehicle_type": "Coupe",
    "segment": "Sports Car",
    "years_sold_au": {"start": 1979, "end": "2002"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mazda RX-7 is a rotary-powered sports car legend with deep Australian motorsport roots. From Allan Moffat's ATCC championship and Bathurst battles in the 1980s to Mazda Motorsport's Australian-exclusive RX-7 SP winning the Bathurst 12 Hour in 1995.",
    "australian_market_notes": "First imported in 1979, the RX-7 proved the reliability and racing potential of Felix Wankel's rotary design. The Series 1-3 dominated touring cars. In 1995, Allan Horsley and Mazda Motorsport in Melbourne developed the street-legal RX-7 SP (Series 6), building 35 homologation specials with 204kW, an enormous rear wing, and a 120-litre carbon fuel tank to defeat Porsche and win Eastern Creek and Bathurst 12 Hour endurance races.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "SA22C/FB",
            "generation_name": "RX-7 Series 1-3",
            "years": {"start": 1979, "end": "1985"},
            "body_styles": ["2-door Coupe"],
            "platform": "Mazda SA22C",
            "ancap_rating": "Untested",
            "summary": "The pure, lightweight original rotary coupe. Powered by the 12A twin-rotor engine, it took Allan Moffat to the 1983 Australian Touring Car Championship.",
            "engines": [
                {
                    "engine_code": "12A",
                    "name": "Mazda 12A Twin-Rotor",
                    "displacement_cc": 1146,
                    "displacement_litres": 1.15,
                    "cylinders": 2,
                    "configuration": "Rotary (2-Rotor Wankel)",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 85.0,
                    "power_rpm": "6000",
                    "torque_nm": 152.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "Rotary ports (4-barrel carburettor)",
                    "notes": "Smooth revving twin-rotor Wankel engine revving to 7,000 rpm."
                }
            ],
            "badges": [
                {
                    "badge_name": "Limited",
                    "years": {"start": 1979, "end": "1985"},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "3-speed auto"],
                    "msrp_aud_min": 14850,
                    "msrp_aud_max": 24500,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1050,
                    "standard_features": ["Pop-up headlights", "4-wheel disc brakes on S3", "Alloy wheels", "Tachometer with rev buzzer", "Air conditioning"],
                    "notes": "Allan Moffat ATCC racing foundation."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Series 2 Limited",
                    "body_style": "Coupe",
                    "engine_code": "12A",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1981,
                    "years_end": "1983",
                    "msrp_aud": 16990,
                    "power_kw": 85.0,
                    "torque_nm": 152.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 750,
                    "notes": "Classic SA22C rotary sports coupe."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "FD3S",
            "generation_name": "RX-7 Series 6-8",
            "years": {"start": 1992, "end": "2002"},
            "body_styles": ["2-door Coupe"],
            "platform": "Mazda FD",
            "ancap_rating": "Untested",
            "summary": "Design masterpiece featuring sequential twin-turbo 13B-REW power, all-aluminum double-wishbone suspension, and the legendary Australian-only 1995 RX-7 SP homologation special.",
            "engines": [
                {
                    "engine_code": "13B-REW",
                    "name": "Mazda 13B-REW Sequential Twin-Turbo",
                    "displacement_cc": 1308,
                    "displacement_litres": 1.3,
                    "cylinders": 2,
                    "configuration": "Rotary (2-Rotor Wankel)",
                    "aspiration": "Sequential Twin-Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 176.0,
                    "power_rpm": "6500",
                    "torque_nm": 294.0,
                    "torque_rpm": "5000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "Side exhaust/intake ports",
                    "notes": "Hitachi sequential twin-turbo system with primary and secondary staging."
                },
                {
                    "engine_code": "13B-REW-SP",
                    "name": "Mazda Motorsport 13B-REW SP Spec",
                    "displacement_cc": 1308,
                    "displacement_litres": 1.3,
                    "cylinders": 2,
                    "configuration": "Rotary (2-Rotor Wankel)",
                    "aspiration": "Sequential Twin-Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 204.0,
                    "power_rpm": "6500",
                    "torque_nm": 357.0,
                    "torque_rpm": "5000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "Side exhaust/intake ports",
                    "notes": "Australian Motorsport SP specification: modified intercooler, ECU, exhaust, yielding 204kW."
                }
            ],
            "badges": [
                {
                    "badge_name": "Series 6 Coupe",
                    "years": {"start": 1992, "end": "1995"},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 79990,
                    "msrp_aud_max": 89990,
                    "fuel_consumption_l_100km": 11.8,
                    "kerb_weight_kg": 1280,
                    "standard_features": ["Sequential twin-turbochargers", "Torsen limited slip differential", "Leather sports seats", "Double-wishbone suspension", "16-inch alloy wheels"],
                    "notes": "Wheels Sports Car of the Year contender."
                },
                {
                    "badge_name": "SP (Special Performance)",
                    "years": {"start": 1995, "end": "1995"},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 101690,
                    "msrp_aud_max": 101690,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 1218,
                    "standard_features": ["Carbon-fibre front splitter and adjustable rear wing", "Carbon-fibre 120-litre fuel tank", "Twin-core intercooler", "17-inch BBS magnesium-alloy wheels", "Recaro Kevlar race seats", "Australian-only build of ~35 units"],
                    "notes": "Australian homologation special engineered to win the Eastern Creek and Bathurst 12 Hour."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SP",
                    "body_style": "Coupe",
                    "engine_code": "13B-REW-SP",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1995,
                    "years_end": "1995",
                    "msrp_aud": 101690,
                    "power_kw": 204.0,
                    "torque_nm": 357.0,
                    "fuel_l_100km": 13.5,
                    "towing_braked_kg": 0,
                    "notes": "Holy grail Australian RX-7 SP."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

BT50_MODEL = {
    "make_slug": "mazda",
    "model_slug": "bt-50",
    "name": "BT-50",
    "vehicle_type": "Ute / Cab Chassis",
    "segment": "Light Commercial",
    "years_sold_au": {"start": 2006, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mazda BT-50 has been an Australian tradie, touring, and towing mainstay across three generations, moving from a Ford Ranger twin with 3.2L 5-cylinder power to an Isuzu D-Max platform with the 3.0L 4JJ3 turbo-diesel.",
    "australian_market_notes": "Replacing the Bravo in 2006, the BT-50 carved out a unique market position in Australia by offering Zoom-Zoom design and car-like ergonomics alongside 3.5-tonne towing and rugged 4WD capability. The UP/UR generation featured the unique 5-cylinder diesel, while the TF generation brought Australian-exclusive flagship editions like the Thunder.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "UP/UR",
            "generation_name": "BT-50 2nd Generation",
            "years": {"start": 2011, "end": "2020"},
            "body_styles": ["Single Cab", "Freestyle Cab", "Dual Cab"],
            "platform": "Ford T6 / Mazda UP",
            "ancap_rating": "5 Stars",
            "summary": "Co-developed on the Ford T6 platform with the PX Ranger, famous for its muscular 3.2L 5-cylinder turbo-diesel generating 147kW and 470Nm.",
            "engines": [
                {
                    "engine_code": "MZ-CD 3.2",
                    "name": "Mazda MZ-CD 3.2L 5-Cylinder Diesel",
                    "displacement_cc": 3198,
                    "displacement_litres": 3.2,
                    "cylinders": 5,
                    "configuration": "Inline-5",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 147.0,
                    "power_rpm": "3000",
                    "torque_nm": 470.0,
                    "torque_rpm": "1750-2500",
                    "compression_ratio": "15.7:1",
                    "valvetrain": "DOHC 20-valve",
                    "notes": "Renowned for deep 5-cylinder torque and heavy 3,500kg towing capability."
                }
            ],
            "badges": [
                {
                    "badge_name": "XTR",
                    "years": {"start": 2011, "end": "2020"},
                    "body_styles": ["Freestyle Cab", "Dual Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 48890,
                    "msrp_aud_max": 54990,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 2080,
                    "standard_features": ["17-inch alloy wheels", "Dual-zone climate control", "Satellite navigation", "Side steps", "Fog lights", "Locking rear differential"],
                    "notes": "Sweet-spot family touring specification."
                },
                {
                    "badge_name": "GT",
                    "years": {"start": 2011, "end": "2020"},
                    "body_styles": ["Dual Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 53990,
                    "msrp_aud_max": 59990,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 2110,
                    "standard_features": ["Leather seats", "Tub liner", "Auto headlights/wipers", "Chrome sports bar", "Reverse camera"],
                    "notes": "Top-tier luxury dual cab."
                }
            ],
            "configurations": [
                {
                    "badge_name": "XTR",
                    "body_style": "Dual Cab",
                    "engine_code": "MZ-CD 3.2",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2011,
                    "years_end": "2020",
                    "msrp_aud": 51990,
                    "power_kw": 147.0,
                    "torque_nm": 470.0,
                    "fuel_l_100km": 8.9,
                    "towing_braked_kg": 3500,
                    "notes": "3.2L 5-cylinder Dual Cab 4WD."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "TF",
            "generation_name": "BT-50 3rd Generation",
            "years": {"start": 2020, "end": "Present"},
            "body_styles": ["Single Cab", "Freestyle Cab", "Dual Cab"],
            "platform": "Isuzu RG",
            "ancap_rating": "5 Stars",
            "summary": "Built in partnership with Isuzu on the D-Max architecture, combining KODO design with the bulletproof 3.0L 4JJ3-TCX turbo-diesel and advanced driver safety.",
            "engines": [
                {
                    "engine_code": "4JJ3-TCX",
                    "name": "Isuzu/Mazda 3.0L Turbo-Diesel",
                    "displacement_cc": 2999,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 140.0,
                    "power_rpm": "3600",
                    "torque_nm": 450.0,
                    "torque_rpm": "1600-2600",
                    "compression_ratio": "16.3:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Cast-iron block 3.0L commercial truck-derived diesel renowned for reliability."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT",
                    "years": {"start": 2020, "end": "Present"},
                    "body_styles": ["Dual Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 56990,
                    "msrp_aud_max": 62500,
                    "fuel_consumption_l_100km": 8.0,
                    "kerb_weight_kg": 2035,
                    "standard_features": ["Brown leather upholstery", "Heated front seats", "Remote engine start", "9-inch infotainment with wireless Apple CarPlay", "Adaptive cruise control with lane keep", "Rear diff lock"],
                    "notes": "High-spec touring ute."
                },
                {
                    "badge_name": "Thunder",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["Dual Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 65990,
                    "msrp_aud_max": 73410,
                    "fuel_consumption_l_100km": 8.0,
                    "kerb_weight_kg": 2160,
                    "standard_features": ["Steel single-hoop bullbar with integrated lightbar", "Electric roller tonneau cover", "Black 18-inch alloy wheels", "Flared wheel arches", "Thunder side steps and sports bar"],
                    "notes": "Australian-exclusive factory accessorized flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Thunder",
                    "body_style": "Dual Cab",
                    "engine_code": "4JJ3-TCX",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 69990,
                    "power_kw": 140.0,
                    "torque_nm": 450.0,
                    "fuel_l_100km": 8.0,
                    "towing_braked_kg": 3500,
                    "notes": "TF BT-50 Thunder 4x4 Dual Cab."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

MAZDA_DEEP_DIVES = [MAZDA3_MODEL, RX7_MODEL, BT50_MODEL]
