"""Deep-dive model data for Mitsubishi: Magna, Triton, and Pajero."""

MAGNA_MODEL = {
    "make_slug": "mitsubishi",
    "model_slug": "magna",
    "name": "Magna",
    "vehicle_type": "Sedan / Wagon",
    "segment": "Large Car",
    "years_sold_au": {"start": 1985, "end": "2005"},
    "locally_built": True,
    "assembly_plants_au": ["Tonsley Park, South Australia"],
    "overview": "The Mitsubishi Magna was an Australian manufacturing triumph, designed specifically for Australian conditions by widening the Japanese Galant by 66mm. Produced at Tonsley Park in Adelaide, it won two Wheels Car of the Year awards (1985, 1996) and culminated in the 180kW Magna Ralliart and revolutionary Magna AWD.",
    "australian_market_notes": "Engineered at Tonsley Park to take on the Ford Falcon and Holden Commodore, the Magna pioneered widebody transverse front-wheel-drive dynamics and whisper-quiet Astron II and 6G72/6G74 V6 engines. The Australian-designed station wagon was a massive export earner to the United States (as the Diamante) and Japan. In 2002, MMAL launched the Magna Ralliart and the all-wheel-drive Magna AWD featuring the QuadTec system.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "TM/TN/TP",
            "generation_name": "Magna 1st Generation",
            "years": {"start": 1985, "end": "1991"},
            "body_styles": ["4-door Sedan", "Station Wagon"],
            "platform": "Mitsubishi Magna Widebody",
            "ancap_rating": "Untested",
            "summary": "The groundbreaking widebody Australian family car that won Wheels Car of the Year 1985, powered by the locally built 2.6L Astron II engine.",
            "engines": [
                {
                    "engine_code": "4G54",
                    "name": "Mitsubishi Astron II 2.6L",
                    "displacement_cc": 2555,
                    "displacement_litres": 2.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 85.0,
                    "power_rpm": "5000",
                    "torque_nm": 198.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 8-valve with Silent Shaft balance shafts",
                    "notes": "Renowned for smooth balance shafts and torquey power (upgraded to 93kW EFI in TN/TP)."
                }
            ],
            "badges": [
                {
                    "badge_name": "GLX",
                    "years": {"start": 1985, "end": "1991"},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic with overdrive"],
                    "msrp_aud_min": 12850,
                    "msrp_aud_max": 18500,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1180,
                    "standard_features": ["Astron II 2.6L engine", "Cloth interior", "Power steering", "Remote boot/fuel release", "Full instrumentation"],
                    "notes": "Wheels Car of the Year 1985 winner."
                },
                {
                    "badge_name": "Elite",
                    "years": {"start": 1985, "end": "1991"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["4-speed automatic"],
                    "msrp_aud_min": 21500,
                    "msrp_aud_max": 28500,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1240,
                    "standard_features": ["Digital instrument cluster", "Automatic climate control", "Velour seats", "Alloy wheels", "Power windows and central locking"],
                    "notes": "Flagship luxury variant."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GLX",
                    "body_style": "Sedan",
                    "engine_code": "4G54",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1985,
                    "years_end": "1991",
                    "msrp_aud": 13990,
                    "power_kw": 85.0,
                    "torque_nm": 198.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 1200,
                    "notes": "1985 Wheels COTY specification."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "TR/TS",
            "generation_name": "Magna 2nd Generation",
            "years": {"start": 1991, "end": "1996"},
            "body_styles": ["4-door Sedan", "Station Wagon"],
            "platform": "Mitsubishi Magna Widebody 2",
            "ancap_rating": "Untested",
            "summary": "Introduced the locally cast 3.0L 6G72 V6 engine. The Tonsley Park-built station wagon became a global export hit to the USA and Japan.",
            "engines": [
                {
                    "engine_code": "6G72",
                    "name": "Mitsubishi 3.0L SOHC V6",
                    "displacement_cc": 2972,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 120.0,
                    "power_rpm": "5500",
                    "torque_nm": 235.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.9:1",
                    "valvetrain": "SOHC 24-valve",
                    "notes": "Cast and machined at MMAL's Lonsdale foundry."
                }
            ],
            "badges": [
                {
                    "badge_name": "Executive V6",
                    "years": {"start": 1991, "end": "1996"},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 29500,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1370,
                    "standard_features": ["3.0L V6 power", "Power steering", "Independent rear suspension", "Speed-sensitive intermittent wipers"],
                    "notes": "Major Australian fleet and family favourite."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Executive V6",
                    "body_style": "Station Wagon",
                    "engine_code": "6G72",
                    "transmission": "4-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 1992,
                    "years_end": "1996",
                    "msrp_aud": 28400,
                    "power_kw": 120.0,
                    "torque_nm": 235.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 1500,
                    "notes": "Australian export station wagon."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "TE-TW",
            "generation_name": "Magna 3rd Generation (Ralliart & AWD)",
            "years": {"start": 1996, "end": "2005"},
            "body_styles": ["4-door Sedan", "Station Wagon"],
            "platform": "Mitsubishi Magna TE",
            "ancap_rating": "3 to 4 Stars",
            "summary": "Wheels Car of the Year 1996 winner, powered by 3.0L and 3.5L V6 engines. Peaked with the hand-built 180kW Magna Ralliart and the Adelaide-developed Magna AWD.",
            "engines": [
                {
                    "engine_code": "6G74",
                    "name": "Mitsubishi 3.5L SOHC 24V V6",
                    "displacement_cc": 3497,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 155.0,
                    "power_rpm": "5250",
                    "torque_nm": 316.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 24-valve",
                    "notes": "Standard 3.5L V6 across Advance, Sports, and VR-X grades."
                },
                {
                    "engine_code": "6G74-Ralliart",
                    "name": "Mitsubishi Ralliart 3.5L Performance V6",
                    "displacement_cc": 3497,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 180.0,
                    "power_rpm": "5500",
                    "torque_nm": 333.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "SOHC 24-valve modified camshaft and valvetrain",
                    "notes": "Hand-assembled performance V6 featuring high-lift camshafts, revised cylinder heads, sports exhaust, and extractors."
                }
            ],
            "badges": [
                {
                    "badge_name": "VR-X",
                    "years": {"start": 1999, "end": "2005"},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["5-speed manual", "5-speed Sports Mode tiptronic auto"],
                    "msrp_aud_min": 37990,
                    "msrp_aud_max": 44500,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1520,
                    "standard_features": ["Sports body kit and rear deck spoiler", "17-inch alloy wheels", "Sports suspension tune", "White instrument dials", "Sports front bucket seats", "Traction Control (TCL)"],
                    "notes": "Australia's top-handling local front-wheel-drive sports sedan."
                },
                {
                    "badge_name": "Ralliart",
                    "years": {"start": 2002, "end": "2003"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual with short shift", "5-speed Sports Mode auto"],
                    "msrp_aud_min": 48990,
                    "msrp_aud_max": 51500,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1546,
                    "standard_features": ["180kW hand-built 3.5L engine", "Enkei 17-inch lightweight alloy wheels", "Koni dampers and Eibach sports springs", "Red and black Recaro leather/fabric sports seats", "Momo steering wheel and gearknob", "Twin-piston performance brakes", "Only 500 numbered units built"],
                    "notes": "The ultimate Australian-manufactured Mitsubishi performance sedan."
                },
                {
                    "badge_name": "AWD",
                    "years": {"start": 2003, "end": "2005"},
                    "body_styles": ["Sedan"],
                    "drivetrain": "All-Wheel Drive (QuadTec)",
                    "transmissions": ["5-speed Sports Mode automatic"],
                    "msrp_aud_min": 37590,
                    "msrp_aud_max": 46500,
                    "fuel_consumption_l_100km": 11.8,
                    "kerb_weight_kg": 1640,
                    "standard_features": ["QuadTec permanent all-wheel-drive system (38:62 torque split)", "Multi-link rear suspension with planetary center diff", "Viscous coupling differential", "4-wheel ventilated disc brakes"],
                    "notes": "Australia's first locally produced all-wheel-drive passenger sedan."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Ralliart",
                    "body_style": "Sedan",
                    "engine_code": "6G74-Ralliart",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2002,
                    "years_end": "2003",
                    "msrp_aud": 48990,
                    "power_kw": 180.0,
                    "torque_nm": 333.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 1500,
                    "notes": "Limited edition Magna Ralliart #001-500."
                },
                {
                    "badge_name": "VR-X AWD",
                    "body_style": "Sedan",
                    "engine_code": "6G74",
                    "transmission": "5-speed Sports Mode auto",
                    "drivetrain": "AWD",
                    "years_start": 2003,
                    "years_end": "2005",
                    "msrp_aud": 44490,
                    "power_kw": 154.0,
                    "torque_nm": 310.0,
                    "fuel_l_100km": 11.8,
                    "towing_braked_kg": 1500,
                    "notes": "Tonsley Park built QuadTec AWD sports sedan."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

TRITON_MODEL = {
    "make_slug": "mitsubishi",
    "model_slug": "triton",
    "name": "Triton",
    "vehicle_type": "Ute / Cab Chassis",
    "segment": "Light Commercial",
    "years_sold_au": {"start": 1979, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Mitsubishi Triton has been one of Australia's favourite dual-cab utes for over four decades, offering tough ladder-chassis capability, advanced Super Select II 4WD, and exceptional value for trades and families.",
    "australian_market_notes": "First sold as the L200 in 1979, the Triton badge was established in 1986. The fourth-generation ML introduced the distinctive curved 'J-line' cabin, while the MQ and MR brought the lightweight 2.4L 4N15 MIVEC aluminium turbo-diesel and full-time 4WD on sealed surfaces via Super Select II. In 2024, the all-new MV Triton arrived with bi-turbo diesel power and 3500kg towing.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "ML/MN",
            "generation_name": "Triton 4th Generation",
            "years": {"start": 2006, "end": "2015"},
            "body_styles": ["Single Cab", "Club Cab", "Double Cab"],
            "platform": "Mitsubishi ML",
            "ancap_rating": "4 Stars",
            "summary": "Pioneered the aerodynamic curved 'J-line' cabin design, creating best-in-class second-row legroom and offering 3.2L 4M41 and 2.5L 4D56 common-rail diesel power.",
            "engines": [
                {
                    "engine_code": "4M41",
                    "name": "Mitsubishi 3.2L Di-D Diesel",
                    "displacement_cc": 3200,
                    "displacement_litres": 3.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 118.0,
                    "power_rpm": "3800",
                    "torque_nm": 347.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "17.0:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Truck-like 3.2L common-rail diesel fitted to ML models (2006-2009)."
                },
                {
                    "engine_code": "4D56-HP",
                    "name": "Mitsubishi 2.5L High-Power Di-D",
                    "displacement_cc": 2477,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 131.0,
                    "power_rpm": "4000",
                    "torque_nm": 400.0,
                    "torque_rpm": "2000-2850",
                    "compression_ratio": "16.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Variable-geometry turbo engine fitted to MN models (2009-2015)."
                }
            ],
            "badges": [
                {
                    "badge_name": "GLX-R",
                    "years": {"start": 2006, "end": "2015"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual", "4-speed auto", "5-speed auto"],
                    "msrp_aud_min": 44990,
                    "msrp_aud_max": 51990,
                    "fuel_consumption_l_100km": 9.1,
                    "kerb_weight_kg": 1945,
                    "standard_features": ["17-inch alloy wheels", "Super Select 4WD", "Power-sliding rear windscreen", "Sports bar", "Side steps", "Cruise control"],
                    "notes": "Australia's top-selling family spec."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GLX-R",
                    "body_style": "Double Cab",
                    "engine_code": "4M41",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 2006,
                    "years_end": "2009",
                    "msrp_aud": 46990,
                    "power_kw": 118.0,
                    "torque_nm": 347.0,
                    "fuel_l_100km": 9.3,
                    "towing_braked_kg": 2500,
                    "notes": "ML GLX-R 3.2L."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "MQ/MR",
            "generation_name": "Triton 5th Generation",
            "years": {"start": 2015, "end": "2023"},
            "body_styles": ["Single Cab", "Club Cab", "Double Cab"],
            "platform": "Mitsubishi MQ",
            "ancap_rating": "5 Stars",
            "summary": "Featured the all-aluminium 2.4L 4N15 MIVEC turbo-diesel, dramatic Dynamic Shield styling on MR facelift, Super Select II 4WD, and 3,100kg towing.",
            "engines": [
                {
                    "engine_code": "4N15",
                    "name": "Mitsubishi 2.4L MIVEC Turbo-Diesel",
                    "displacement_cc": 2442,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 133.0,
                    "power_rpm": "3500",
                    "torque_nm": 430.0,
                    "torque_rpm": "2500",
                    "compression_ratio": "15.5:1",
                    "valvetrain": "DOHC 16-valve MIVEC",
                    "notes": "Lightweight aluminium cylinder block with variable valve timing on intake."
                }
            ],
            "badges": [
                {
                    "badge_name": "GLS",
                    "years": {"start": 2015, "end": "2023"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed manual", "5-speed auto", "6-speed auto"],
                    "msrp_aud_min": 44490,
                    "msrp_aud_max": 51490,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 1950,
                    "standard_features": ["Super Select II 4WD with center diff lock (safe on tarmac)", "18-inch alloy wheels", "Rear diff lock", "LED headlights", "Dual-zone climate control", "Apple CarPlay/Android Auto"],
                    "notes": "Benchmark value-for-money dual-cab 4WD."
                },
                {
                    "badge_name": "GSR",
                    "years": {"start": 2020, "end": "2023"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 53490,
                    "msrp_aud_max": 56990,
                    "fuel_consumption_l_100km": 8.6,
                    "kerb_weight_kg": 1990,
                    "standard_features": ["Black 18-inch alloy wheels", "Black grille, mirrors, and roof", "Leather-appointed heated front seats", "360-degree multi-around monitor", "Rear differential lock"],
                    "notes": "Sporting aesthetic flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GLS",
                    "body_style": "Double Cab",
                    "engine_code": "4N15",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2019,
                    "years_end": "2023",
                    "msrp_aud": 49490,
                    "power_kw": 133.0,
                    "torque_nm": 430.0,
                    "fuel_l_100km": 8.6,
                    "towing_braked_kg": 3100,
                    "notes": "MR Triton GLS dual-cab."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "MV",
            "generation_name": "Triton 6th Generation",
            "years": {"start": 2024, "end": "Present"},
            "body_styles": ["Double Cab", "Club Cab"],
            "platform": "Mitsubishi MV",
            "ancap_rating": "5 Stars",
            "summary": "All-new heavy-duty platform with wider body dimensions, 3,500kg braked towing, and the 2.4L 4N16 bi-turbo diesel delivering 150kW and 470Nm.",
            "engines": [
                {
                    "engine_code": "4N16",
                    "name": "Mitsubishi 2.4L Bi-Turbo Diesel",
                    "displacement_cc": 2442,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Bi-Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 150.0,
                    "power_rpm": "3500",
                    "torque_nm": 470.0,
                    "torque_rpm": "1500-2750",
                    "compression_ratio": "15.2:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Twin-turbo setup providing broad low-end response and 150kW peak power."
                }
            ],
            "badges": [
                {
                    "badge_name": "GLS",
                    "years": {"start": 2024, "end": "Present"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 59090,
                    "msrp_aud_max": 61990,
                    "fuel_consumption_l_100km": 7.7,
                    "kerb_weight_kg": 2050,
                    "standard_features": ["Super Select II 4WD", "9-inch infotainment with wireless Apple CarPlay", "Dual-zone climate control", "18-inch black alloys", "3500kg towing capacity"],
                    "notes": "The sweet spot of the MV generation."
                },
                {
                    "badge_name": "GSR",
                    "years": {"start": 2024, "end": "Present"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 63840,
                    "msrp_aud_max": 65500,
                    "fuel_consumption_l_100km": 7.7,
                    "kerb_weight_kg": 2075,
                    "standard_features": ["Black exterior accents and sports bar", "Leather accented seats with orange contrast stitching", "Wireless phone charging", "Roof rails", "Multi-around view monitor"],
                    "notes": "Flagship grade."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GSR",
                    "body_style": "Double Cab",
                    "engine_code": "4N16",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2024,
                    "years_end": "Present",
                    "msrp_aud": 63840,
                    "power_kw": 150.0,
                    "torque_nm": 470.0,
                    "fuel_l_100km": 7.7,
                    "towing_braked_kg": 3500,
                    "notes": "MV Triton GSR Bi-Turbo."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

PAJERO_MODEL = {
    "make_slug": "mitsubishi",
    "model_slug": "pajero",
    "name": "Pajero",
    "vehicle_type": "4WD Wagon",
    "segment": "Large 4WD SUV",
    "years_sold_au": {"start": 1983, "end": "2021"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "With 12 victories in the grueling Dakar Rally, the Mitsubishi Pajero is one of the world's most successful four-wheel drives. In Australia, it defined the family 4WD wagon for nearly four decades across four generations.",
    "australian_market_notes": "First imported in 1983, the Pajero transformed four-wheel driving from farm machinery to comfortable family transport. The NH generation introduced Super Select 4WD, allowing full-time AWD on dry bitumen and locking 4WD on dirt. The NM series brought a revolutionary monocoque chassis with independent suspension. After 38 years and over 175,000 sales in Australia, production concluded in 2021 with the Pajero Final Edition.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "NH-NL",
            "generation_name": "Pajero 2nd Generation",
            "years": {"start": 1991, "end": "2000"},
            "body_styles": ["SWB 3-door", "LWB 5-door"],
            "platform": "Mitsubishi V20",
            "ancap_rating": "Untested",
            "summary": "Pioneered Super Select 4WD and multi-mode ABS, establishing the Pajero as a technology leader against Nissan Patrol and Toyota LandCruiser.",
            "engines": [
                {
                    "engine_code": "6G74",
                    "name": "Mitsubishi 3.5L DOHC 24V V6",
                    "displacement_cc": 3497,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 153.0,
                    "power_rpm": "5000",
                    "torque_nm": 315.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "High-output quad-cam V6 introduced in the NJ/NK series."
                },
                {
                    "engine_code": "4M40",
                    "name": "Mitsubishi 2.8L Turbo-Diesel",
                    "displacement_cc": 2835,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 92.0,
                    "power_rpm": "4000",
                    "torque_nm": 292.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "21.0:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Renowned outback workhorse diesel engine."
                }
            ],
            "badges": [
                {
                    "badge_name": "GLS",
                    "years": {"start": 1991, "end": "2000"},
                    "body_styles": ["LWB 5-door"],
                    "drivetrain": "Super Select 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 43500,
                    "msrp_aud_max": 54990,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1980,
                    "standard_features": ["Super Select 4WD with center diff lock", "7-passenger seating", "Dual-zone front/rear air conditioning", "Alloy wheels", "Power windows and mirrors", "Cruise control"],
                    "notes": "Australia's favourite 1990s family 4WD."
                },
                {
                    "badge_name": "Exceed",
                    "years": {"start": 1991, "end": "2000"},
                    "body_styles": ["LWB 5-door"],
                    "drivetrain": "Super Select 4WD",
                    "transmissions": ["4-speed automatic"],
                    "msrp_aud_min": 56000,
                    "msrp_aud_max": 68500,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 2040,
                    "standard_features": ["Leather upholstery", "Woodgrain dash trim", "Electric glass sunroof", "3-mode adjustable shock absorbers", "Rear cabin heater"],
                    "notes": "Luxury outback flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GLS LWB",
                    "body_style": "LWB 5-door",
                    "engine_code": "6G74",
                    "transmission": "4-speed automatic",
                    "drivetrain": "Super Select 4WD",
                    "years_start": 1993,
                    "years_end": "1997",
                    "msrp_aud": 49800,
                    "power_kw": 153.0,
                    "torque_nm": 315.0,
                    "fuel_l_100km": 13.2,
                    "towing_braked_kg": 2500,
                    "notes": "NJ 3.5L DOHC V6 GLS."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "NS-NX",
            "generation_name": "Pajero 4th Generation",
            "years": {"start": 2006, "end": "2021"},
            "body_styles": ["5-door Wagon", "3-door Shorty"],
            "platform": "Mitsubishi V80/V90",
            "ancap_rating": "5 Stars",
            "summary": "15-year Australian production run, powered by the mighty 3.2L common-rail Di-D diesel (up to 147kW/441Nm) with 3000kg towing and Super Select II 4WD.",
            "engines": [
                {
                    "engine_code": "4M41-CRD",
                    "name": "Mitsubishi 3.2L Common-Rail Di-D Diesel",
                    "displacement_cc": 3200,
                    "displacement_litres": 3.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 147.0,
                    "power_rpm": "3800",
                    "torque_nm": 441.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Upgraded in NT series (2009) to 147kW/441Nm; legendary durability and outback reliability."
                }
            ],
            "badges": [
                {
                    "badge_name": "GLS",
                    "years": {"start": 2006, "end": "2021"},
                    "body_styles": ["5-door Wagon (7 seats)"],
                    "drivetrain": "Super Select II 4WD",
                    "transmissions": ["5-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 53990,
                    "msrp_aud_max": 61990,
                    "fuel_consumption_l_100km": 9.1,
                    "kerb_weight_kg": 2295,
                    "standard_features": ["Super Select II 4WD with rear diff lock", "In-floor folding 3rd-row seats (Hide & Seat)", "18-inch alloy wheels", "Rockford Fosgate premium audio", "Smartphone Link Display Audio", "Reverse camera"],
                    "notes": "High-volume Australian family and touring specification."
                },
                {
                    "badge_name": "Final Edition",
                    "years": {"start": 2021, "end": "2021"},
                    "body_styles": ["5-door Wagon (7 seats)"],
                    "drivetrain": "Super Select II 4WD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 63490,
                    "msrp_aud_max": 65990,
                    "fuel_consumption_l_100km": 9.1,
                    "kerb_weight_kg": 2335,
                    "standard_features": ["Tinted bonnet protector", "Final Edition badging and carpet mats", "Leather-trimmed owner's manual case", "Sunroof", "Heated power leather seats", "Build limited to 800 units for Australia"],
                    "notes": "Celebrated the conclusion of 38 years of Pajero history in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GLS 3.2 Di-D",
                    "body_style": "5-door Wagon",
                    "engine_code": "4M41-CRD",
                    "transmission": "5-speed automatic",
                    "drivetrain": "Super Select II 4WD",
                    "years_start": 2009,
                    "years_end": "2021",
                    "msrp_aud": 58990,
                    "power_kw": 147.0,
                    "torque_nm": 441.0,
                    "fuel_l_100km": 9.1,
                    "towing_braked_kg": 3000,
                    "notes": "NT-NX Pajero GLS 3.2L diesel."
                },
                {
                    "badge_name": "Final Edition",
                    "body_style": "5-door Wagon",
                    "engine_code": "4M41-CRD",
                    "transmission": "5-speed automatic",
                    "drivetrain": "Super Select II 4WD",
                    "years_start": 2021,
                    "years_end": "2021",
                    "msrp_aud": 63490,
                    "power_kw": 147.0,
                    "torque_nm": 441.0,
                    "fuel_l_100km": 9.1,
                    "towing_braked_kg": 3000,
                    "notes": "2021 Final Edition #1-800."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

MITSUBISHI_DEEP_DIVES = [MAGNA_MODEL, TRITON_MODEL, PAJERO_MODEL]
