"""Wave 2 Toyota deep-dive models: Prado, Kluger, 86-GR86, Supra, Celica, Aurion, Crown, HiAce, Yaris."""

PRADO_MODEL = {
    "make_slug": "toyota",
    "model_slug": "prado",
    "name": "LandCruiser Prado",
    "vehicle_type": "4WD SUV",
    "segment": "Large SUV",
    "years_sold_au": {"start": 1996, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota LandCruiser Prado is Australia's perennial favorite family and long-distance outback touring 4WD. Bridging the gap between the mid-size RAV4 and heavy-duty LandCruiser wagon, the Prado delivers genuine off-road capability, dual long-range fuel tanks, up to seven seats, and legendary durability.",
    "australian_market_notes": "Launched in Australia in July 1996 to challenge the dominant Mitsubishi Pajero, the Prado rapidly became Australia's best-selling large 4WD SUV, a position it held for over two decades. Australian specifications prioritized touring range with factory twin fuel tanks (up to 180 litres on 120 and 150 series), robust ladder chassis construction, constant 4WD, and an extensive genuine accessory range engineered in Melbourne.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "90 Series",
            "generation_name": "LandCruiser Prado 90 Series",
            "years": {"start": 1996, "end": 2002},
            "body_styles": ["3-door SWB Wagon", "5-door LWB Wagon"],
            "platform": "Toyota J90",
            "ancap_rating": "Untested",
            "summary": "Introduced independent front double-wishbone suspension with a live rear axle and full-time 4WD, transforming on-road handling compared to earlier rigid-axle LandCruisers.",
            "engines": [
                {
                    "engine_code": "3RZ-FE",
                    "name": "Toyota 3RZ-FE 2.7L",
                    "displacement_cc": 2693,
                    "displacement_litres": 2.7,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 112.0,
                    "power_rpm": "4800",
                    "torque_nm": 240.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Twin balance shafts for smoothness; standard in entry RV."
                },
                {
                    "engine_code": "5VZ-FE",
                    "name": "Toyota 5VZ-FE 3.4L Quad Cam V6",
                    "displacement_cc": 3378,
                    "displacement_litres": 3.4,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 132.0,
                    "power_rpm": "4800",
                    "torque_nm": 294.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "9.6:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Renowned cast-iron block V6 with excellent low-end tractability."
                },
                {
                    "engine_code": "1KZ-TE",
                    "name": "Toyota 1KZ-TE 3.0L Turbo Diesel",
                    "displacement_cc": 2982,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 96.0,
                    "power_rpm": "3600",
                    "torque_nm": 343.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "21.2:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Electronically controlled indirect injection turbo diesel introduced in late 1999."
                }
            ],
            "badges": [
                {
                    "badge_name": "RV / RV6",
                    "years": {"start": 1996, "end": 2002},
                    "body_styles": ["SWB Wagon", "LWB Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 36990,
                    "msrp_aud_max": 44500,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1820,
                    "standard_features": ["Dual fuel tanks (159L)", "Centre diff lock", "Power steering", "16-inch steel wheels"],
                    "notes": "Available in 3-door SWB (early) and popular 5-door LWB."
                },
                {
                    "badge_name": "GXL",
                    "years": {"start": 1996, "end": 2002},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 43990,
                    "msrp_aud_max": 52000,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 1910,
                    "standard_features": ["8 seats", "Flares", "Alloy wheels", "Air conditioning", "Power windows", "Wide track"],
                    "notes": "The sweet spot of the 90 Series range and volume seller."
                },
                {
                    "badge_name": "Grande",
                    "years": {"start": 1997, "end": 2002},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["4-speed automatic"],
                    "msrp_aud_min": 58990,
                    "msrp_aud_max": 64990,
                    "fuel_consumption_l_100km": 13.8,
                    "kerb_weight_kg": 1980,
                    "standard_features": ["Leather upholstery", "Woodgrain trim", "ABS brakes", "Dual airbags", "Climate control", "Sunroof"],
                    "notes": "Luxury flagship 4WD."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Prado GXL V6",
                    "body_style": "5-door Wagon",
                    "engine_code": "5VZ-FE",
                    "transmission": "4-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 1996,
                    "years_end": 2002,
                    "msrp_aud": 47990,
                    "power_kw": 132.0,
                    "torque_nm": 294.0,
                    "fuel_l_100km": 13.5,
                    "towing_braked_kg": 2500,
                    "notes": "Mainstream family choice across rural and metro Australia."
                },
                {
                    "badge_name": "Prado GXL Turbo Diesel",
                    "body_style": "5-door Wagon",
                    "engine_code": "1KZ-TE",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1999,
                    "years_end": 2002,
                    "msrp_aud": 49990,
                    "power_kw": 96.0,
                    "torque_nm": 343.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 2500,
                    "notes": "Outback touring hero with 159L fuel capacity delivering 1400km range."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "120 Series",
            "generation_name": "LandCruiser Prado 120 Series",
            "years": {"start": 2003, "end": 2009},
            "body_styles": ["5-door Wagon"],
            "platform": "Toyota J120",
            "ancap_rating": "4 stars",
            "summary": "Introduced aerodynamic modern styling, huge 180-litre fuel capacity (90L main + 90L sub tank), smooth 4.0L V6 and common-rail 1KD-FTV D-4D diesel engine.",
            "engines": [
                {
                    "engine_code": "1GR-FE",
                    "name": "Toyota 1GR-FE 4.0L Dual VVT-i V6",
                    "displacement_cc": 3956,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 179.0,
                    "power_rpm": "5200",
                    "torque_nm": 376.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 24-valve VVT-i",
                    "notes": "All-aluminium V6 providing effortless overtaking and towing power."
                },
                {
                    "engine_code": "1KD-FTV",
                    "name": "Toyota 1KD-FTV 3.0L D-4D Common Rail Turbo Diesel",
                    "displacement_cc": 2982,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 127.0,
                    "power_rpm": "3400",
                    "torque_nm": 410.0,
                    "torque_rpm": "1600-2800",
                    "compression_ratio": "17.9:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Introduced in late 2006 paired with 6-speed manual or 5-speed automatic."
                }
            ],
            "badges": [
                {
                    "badge_name": "GX",
                    "years": {"start": 2003, "end": 2009},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["5-speed manual", "6-speed manual", "4-speed auto", "5-speed auto"],
                    "msrp_aud_min": 38990,
                    "msrp_aud_max": 46000,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1940,
                    "standard_features": ["180L dual fuel tanks", "Torsen centre LSD", "Air conditioning", "Dual airbags"],
                    "notes": "Fleet and rural entry specification."
                },
                {
                    "badge_name": "GXL",
                    "years": {"start": 2003, "end": 2009},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["6-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 48990,
                    "msrp_aud_max": 57000,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 2050,
                    "standard_features": ["8 seats", "17-inch alloy wheels", "Roof rails", "Wide fender flares", "Cruise control"],
                    "notes": "The definitive Australian family 4WD wagon of the 2000s."
                },
                {
                    "badge_name": "Grande",
                    "years": {"start": 2003, "end": 2009},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 65990,
                    "msrp_aud_max": 73990,
                    "fuel_consumption_l_100km": 12.0,
                    "kerb_weight_kg": 2170,
                    "standard_features": ["TEMS adjustable suspension", "Rear air suspension", "Leather seats", "Satellite navigation", "Cool box"],
                    "notes": "Flagship variant rivaling European luxury SUVs in ride comfort."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Prado GXL D-4D",
                    "body_style": "5-door Wagon",
                    "engine_code": "1KD-FTV",
                    "transmission": "5-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2006,
                    "years_end": 2009,
                    "msrp_aud": 55490,
                    "power_kw": 127.0,
                    "torque_nm": 410.0,
                    "fuel_l_100km": 9.3,
                    "towing_braked_kg": 2500,
                    "notes": "Benchmark outback tourer capable of 1,900km on a single 180-litre fill."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "150 Series",
            "generation_name": "LandCruiser Prado 150 Series",
            "years": {"start": 2009, "end": 2024},
            "body_styles": ["3-door SWB Wagon", "5-door LWB Wagon"],
            "platform": "Toyota J150",
            "ancap_rating": "5 stars",
            "summary": "15-year production run featuring KDSS (Kinetic Dynamic Suspension System), CRAWL control, Multi-Terrain Select, and later the 2.8L 1GD-FTV turbo diesel.",
            "engines": [
                {
                    "engine_code": "1GD-FTV",
                    "name": "Toyota 1GD-FTV 2.8L D-4D Turbo Diesel",
                    "displacement_cc": 2755,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 150.0,
                    "power_rpm": "3000-3400",
                    "torque_nm": 500.0,
                    "torque_rpm": "1600-2800",
                    "compression_ratio": "15.6:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Launched in 2015 with 130kW/450Nm; upgraded in late 2020 to 150kW/500Nm and 3,000kg towing."
                },
                {
                    "engine_code": "1GR-FE",
                    "name": "Toyota 1GR-FE 4.0L Dual VVT-i V6",
                    "displacement_cc": 3956,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 202.0,
                    "power_rpm": "5600",
                    "torque_nm": 381.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "10.4:1",
                    "valvetrain": "DOHC 24-valve Dual VVT-i",
                    "notes": "Offered until 2018 when Australian Prado range shifted to 100% diesel."
                }
            ],
            "badges": [
                {
                    "badge_name": "GX",
                    "years": {"start": 2009, "end": 2024},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 55990,
                    "msrp_aud_max": 62830,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 2230,
                    "standard_features": ["5 or 7 seats", "17-inch alloy wheels", "Toyota Safety Sense", "150L fuel tank", "Keyless smart entry"],
                    "notes": "Popular mining, commercial and outback touring base."
                },
                {
                    "badge_name": "GXL",
                    "years": {"start": 2009, "end": 2024},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 61990,
                    "msrp_aud_max": 69530,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 2280,
                    "standard_features": ["7 seats standard", "Tri-zone climate control", "Rear parking sensors", "Side steps", "Bi-LED headlights"],
                    "notes": "Australia's top-selling retail large SUV variant for over a decade."
                },
                {
                    "badge_name": "VX",
                    "years": {"start": 2009, "end": 2024},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 73990,
                    "msrp_aud_max": 79557,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 2340,
                    "standard_features": ["KDSS suspension", "18-inch alloys", "Leather-accented ventilated seats", "JBL 14-speaker audio", "Panoramic view monitor"],
                    "notes": "Premium spec equipped with KDSS hydraulic roll control."
                },
                {
                    "badge_name": "Kakadu",
                    "years": {"start": 2009, "end": 2024},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 84990,
                    "msrp_aud_max": 90500,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 2450,
                    "standard_features": ["Adaptive Variable Suspension", "Rear air suspension", "CRAWL Control", "Multi-Terrain Select", "Sunroof", "Rear seat entertainment"],
                    "notes": "Top-tier luxury and off-road flagship named after the iconic Australian National Park."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Prado GXL 2.8 Diesel",
                    "body_style": "5-door Wagon",
                    "engine_code": "1GD-FTV",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2020,
                    "years_end": 2024,
                    "msrp_aud": 69530,
                    "power_kw": 150.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 7.9,
                    "towing_braked_kg": 3000,
                    "notes": "Final evolution of the 150 Series with 150kW engine upgrade."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "250 Series",
            "generation_name": "LandCruiser Prado 250 Series",
            "years": {"start": 2024, "end": "Present"},
            "body_styles": ["5-door Wagon"],
            "platform": "TNGA-F (GA-F)",
            "ancap_rating": "5 stars",
            "summary": "Built on the shared global TNGA-F ladder-frame platform with LandCruiser 300, introducing 48V V-Active mild hybrid technology, 8-speed automatic, electric power steering, and 3,500kg towing capacity.",
            "engines": [
                {
                    "engine_code": "1GD-FTV-48V",
                    "name": "Toyota 1GD-FTV 2.8L V-Active 48V Turbo Diesel",
                    "displacement_cc": 2755,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Variable Nozzle Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 150.0,
                    "power_rpm": "3000-3400",
                    "torque_nm": 500.0,
                    "torque_rpm": "1600-2800",
                    "compression_ratio": "15.6:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Integrated 48V motor generator assist for enhanced low-speed response and stop-start refinement."
                }
            ],
            "badges": [
                {
                    "badge_name": "GX",
                    "years": {"start": 2024, "end": "Present"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["8-speed automatic"],
                    "msrp_aud_min": 72500,
                    "msrp_aud_max": 72500,
                    "fuel_consumption_l_100km": 7.6,
                    "kerb_weight_kg": 2350,
                    "standard_features": ["5 seats", "18-inch dark grey alloys", "12.3-inch multimedia touchscreen", "Toyota Safety Sense 3.0", "Centre and rear diff locks"],
                    "notes": "Heritage-inspired front grille design."
                },
                {
                    "badge_name": "GXL",
                    "years": {"start": 2024, "end": "Present"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["8-speed automatic"],
                    "msrp_aud_min": 79990,
                    "msrp_aud_max": 79990,
                    "fuel_consumption_l_100km": 7.6,
                    "kerb_weight_kg": 2420,
                    "standard_features": ["7 seats", "Roof rails", "Wireless phone charger", "Tri-zone climate control", "Synthetic leather upholstery"],
                    "notes": "Mainstream family touring volume model."
                },
                {
                    "badge_name": "Altitude",
                    "years": {"start": 2024, "end": "Present"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["8-speed automatic"],
                    "msrp_aud_min": 92700,
                    "msrp_aud_max": 92700,
                    "fuel_consumption_l_100km": 7.6,
                    "kerb_weight_kg": 2480,
                    "standard_features": ["5 seats dedicated off-road focus", "18-inch alloys with Toyo Open Country all-terrain tyres", "Stabiliser Disconnect Mechanism (SDM)", "Digital rear-view mirror"],
                    "notes": "Rugged enthusiast grade with round LED heritage headlamps."
                },
                {
                    "badge_name": "Kakadu",
                    "years": {"start": 2024, "end": "Present"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "Full-Time 4WD",
                    "transmissions": ["8-speed automatic"],
                    "msrp_aud_min": 99990,
                    "msrp_aud_max": 99990,
                    "fuel_consumption_l_100km": 7.6,
                    "kerb_weight_kg": 2550,
                    "standard_features": ["7 seats", "20-inch alloy wheels", "Panoramic moonroof", "Adaptive Variable Suspension", "Head-up display", "Illuminated side steps"],
                    "notes": "Ultimate luxury specification."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Prado GXL 48V",
                    "body_style": "5-door Wagon",
                    "engine_code": "1GD-FTV-48V",
                    "transmission": "8-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2024,
                    "years_end": "Present",
                    "msrp_aud": 79990,
                    "power_kw": 150.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 7.6,
                    "towing_braked_kg": 3500,
                    "notes": "Upgraded 3.5t towing capacity and 8-speed automatic gearbox."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

KLUGER_MODEL = {
    "make_slug": "toyota",
    "model_slug": "kluger",
    "name": "Kluger",
    "vehicle_type": "7-Seat Family SUV",
    "segment": "Large SUV",
    "years_sold_au": {"start": 2003, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota Kluger (sold globally as the Highlander) is Australia's quintessential car-based 7-seat family crossover SUV. Blending passenger-car ride comfort with cavernous interior room, powerful V6 and hybrid powertrains, and all-weather AWD assurance, it became a cornerstone of Australian suburban family motoring.",
    "australian_market_notes": "Introduced in October 2003 to meet exploding demand for car-like unibody SUVs, the Kluger complemented the body-on-frame Prado. While early generations were built in Kyushu, Japan, the XU50 generation was sourced from Toyota Motor Manufacturing Indiana in the United States, before returning to Japan for hybrid production on the TNGA-K platform.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "XU20",
            "generation_name": "Kluger 1st Generation",
            "years": {"start": 2003, "end": 2007},
            "body_styles": ["5-door Wagon"],
            "platform": "Toyota K platform",
            "ancap_rating": "4 stars",
            "summary": "First-generation unibody SUV offering 5 or 7 seats, car-like handling, and silky 3.3L 3MZ-FE quad-cam V6 power.",
            "engines": [
                {
                    "engine_code": "3MZ-FE",
                    "name": "Toyota 3MZ-FE 3.3L VVT-i V6",
                    "displacement_cc": 3310,
                    "displacement_litres": 3.3,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 172.0,
                    "power_rpm": "5600",
                    "torque_nm": 328.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 24-valve VVT-i",
                    "notes": "Smooth alloy V6 shared with Lexus RX330."
                }
            ],
            "badges": [
                {
                    "badge_name": "CV",
                    "years": {"start": 2003, "end": 2007},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 43990,
                    "msrp_aud_max": 47990,
                    "fuel_consumption_l_100km": 12.3,
                    "kerb_weight_kg": 1820,
                    "standard_features": ["5 seats", "Full-time AWD with viscous centre coupling", "Dual airbags", "Cruise control", "Air conditioning"],
                    "notes": "Entry-level all-wheel drive family wagon."
                },
                {
                    "badge_name": "CVX",
                    "years": {"start": 2003, "end": 2007},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 48990,
                    "msrp_aud_max": 53500,
                    "fuel_consumption_l_100km": 12.3,
                    "kerb_weight_kg": 1870,
                    "standard_features": ["7 seats standard", "Alloy wheels", "Roof rails", "Power driver seat", "Side airbags"],
                    "notes": "Popular 7-seat family choice."
                },
                {
                    "badge_name": "Grande",
                    "years": {"start": 2003, "end": 2007},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 56990,
                    "msrp_aud_max": 61990,
                    "fuel_consumption_l_100km": 12.3,
                    "kerb_weight_kg": 1910,
                    "standard_features": ["Leather trim", "DVD satellite navigation", "Sunroof", "Vehicle Stability Control (VSC)", "Woodgrain accents"],
                    "notes": "Luxury flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Kluger CVX AWD",
                    "body_style": "5-door Wagon",
                    "engine_code": "3MZ-FE",
                    "transmission": "5-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2003,
                    "years_end": 2007,
                    "msrp_aud": 48990,
                    "power_kw": 172.0,
                    "torque_nm": 328.0,
                    "fuel_l_100km": 12.3,
                    "towing_braked_kg": 1500,
                    "notes": "7-seat configuration standard."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "XU40",
            "generation_name": "Kluger 2nd Generation",
            "years": {"start": 2007, "end": 2014},
            "body_styles": ["5-door Wagon"],
            "platform": "Toyota K platform",
            "ancap_rating": "5 stars",
            "summary": "Substantially larger second generation featuring 201kW 3.5L 2GR-FE V6 power, available front-wheel drive or on-demand AWD, and clever 'Center Stow' flexible seating.",
            "engines": [
                {
                    "engine_code": "2GR-FE",
                    "name": "Toyota 2GR-FE 3.5L Dual VVT-i V6",
                    "displacement_cc": 3456,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 201.0,
                    "power_rpm": "6200",
                    "torque_nm": 337.0,
                    "torque_rpm": "4700",
                    "compression_ratio": "10.8:1",
                    "valvetrain": "DOHC 24-valve Dual VVT-i",
                    "notes": "Punchy V6 delivering 0-100 km/h in under 8 seconds."
                }
            ],
            "badges": [
                {
                    "badge_name": "KX-R",
                    "years": {"start": 2007, "end": 2014},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 47000,
                    "fuel_consumption_l_100km": 11.0,
                    "kerb_weight_kg": 1845,
                    "standard_features": ["5 or 7 seats", "17-inch alloy wheels", "Reversing camera standard", "Cruise control", "Hill-start Assist"],
                    "notes": "Reversing camera displayed in multi-info display - safety leader."
                },
                {
                    "badge_name": "KX-S",
                    "years": {"start": 2007, "end": 2014},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 50990,
                    "msrp_aud_max": 56000,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1930,
                    "standard_features": ["Leather upholstery", "19-inch alloy wheels", "3-zone climate control", "Power front seats", "Roof rails"],
                    "notes": "Sporty mid-range trim."
                },
                {
                    "badge_name": "Grande",
                    "years": {"start": 2007, "end": 2014},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["5-speed automatic"],
                    "msrp_aud_min": 60990,
                    "msrp_aud_max": 68000,
                    "fuel_consumption_l_100km": 11.6,
                    "kerb_weight_kg": 1980,
                    "standard_features": ["Rear-seat DVD screen", "Sat nav", "Sunroof", "Power tailgate", "Smart key entry"],
                    "notes": "Top-tier family luxury."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Kluger KX-S AWD",
                    "body_style": "5-door Wagon",
                    "engine_code": "2GR-FE",
                    "transmission": "5-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2007,
                    "years_end": 2014,
                    "msrp_aud": 54490,
                    "power_kw": 201.0,
                    "torque_nm": 337.0,
                    "fuel_l_100km": 11.6,
                    "towing_braked_kg": 2000,
                    "notes": "Popular suburban family hauler."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "XU50",
            "generation_name": "Kluger 3rd Generation",
            "years": {"start": 2014, "end": 2021},
            "body_styles": ["5-door Wagon"],
            "platform": "Toyota K platform",
            "ancap_rating": "5 stars",
            "summary": "Built in Indiana, USA for the Australian market. Introduced standard 7 seats, double-wishbone rear suspension, and from 2017 a direct-injected 218kW V6 with 8-speed automatic.",
            "engines": [
                {
                    "engine_code": "2GR-FKS",
                    "name": "Toyota 2GR-FKS 3.5L D-4S V6",
                    "displacement_cc": 3456,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 218.0,
                    "power_rpm": "6600",
                    "torque_nm": 350.0,
                    "torque_rpm": "4700",
                    "compression_ratio": "11.8:1",
                    "valvetrain": "DOHC 24-valve Dual VVT-iW",
                    "notes": "D-4S direct and port injection introduced in 2017 facelift paired with 8-speed auto."
                }
            ],
            "badges": [
                {
                    "badge_name": "GX",
                    "years": {"start": 2014, "end": 2021},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["6-speed automatic", "8-speed automatic"],
                    "msrp_aud_min": 40990,
                    "msrp_aud_max": 48500,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 1935,
                    "standard_features": ["7 seats standard", "18-inch alloys", "Toyota Safety Sense (from 2018)", "Rear air conditioning"],
                    "notes": "Entry 7-seater."
                },
                {
                    "badge_name": "GXL",
                    "years": {"start": 2014, "end": 2021},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["6-speed automatic", "8-speed automatic"],
                    "msrp_aud_min": 51990,
                    "msrp_aud_max": 58950,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 2000,
                    "standard_features": ["Leather-accented seats", "Heated front seats", "3-zone climate control", "Power tailgate", "Sat nav"],
                    "notes": "Heart of the Kluger range."
                },
                {
                    "badge_name": "Grande",
                    "years": {"start": 2014, "end": 2021},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "FWD or AWD",
                    "transmissions": ["6-speed automatic", "8-speed automatic"],
                    "msrp_aud_min": 63990,
                    "msrp_aud_max": 71000,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 2075,
                    "standard_features": ["19-inch alloys", "Sunroof", "Ventilated front seats", "Rear Blu-ray entertainment", "Blind spot monitor"],
                    "notes": "US-built flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Kluger GXL AWD",
                    "body_style": "5-door Wagon",
                    "engine_code": "2GR-FKS",
                    "transmission": "8-speed automatic",
                    "drivetrain": "AWD",
                    "years_start": 2017,
                    "years_end": 2021,
                    "msrp_aud": 58950,
                    "power_kw": 218.0,
                    "torque_nm": 350.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 2000,
                    "notes": "Direct-injection 8-speed automatic facelift configuration."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "XU70",
            "generation_name": "Kluger 4th Generation",
            "years": {"start": 2021, "end": "Present"},
            "body_styles": ["5-door Wagon"],
            "platform": "TNGA-K",
            "ancap_rating": "5 stars",
            "summary": "Built on Toyota's TNGA-K platform, introducing hybrid all-wheel drive returning just 5.6L/100km, upgraded rigidity, and later a 2.4L turbo replacing the V6.",
            "engines": [
                {
                    "engine_code": "A25A-FXS",
                    "name": "Toyota A25A-FXS 2.5L Hybrid e-Four",
                    "displacement_cc": 2487,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated + Electric Motors",
                    "fuel_type": "Petrol Hybrid",
                    "power_kw": 184.0,
                    "power_rpm": "6000",
                    "torque_nm": 242.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "14.0:1",
                    "valvetrain": "DOHC 16-valve Dual VVT-i",
                    "notes": "184kW combined output with independent electric rear axle (e-Four)."
                },
                {
                    "engine_code": "T24A-FTS",
                    "name": "Toyota T24A-FTS 2.4L Turbo Petrol",
                    "displacement_cc": 2393,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 198.0,
                    "power_rpm": "6000",
                    "torque_nm": 420.0,
                    "torque_rpm": "1700-3600",
                    "compression_ratio": "11.0:1",
                    "valvetrain": "DOHC 16-valve Dual VVT-i",
                    "notes": "Introduced in 2023 replacing the 3.5L V6, offering 420Nm across wide rev band."
                }
            ],
            "badges": [
                {
                    "badge_name": "GX Hybrid AWD",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "e-Four AWD",
                    "transmissions": ["e-CVT"],
                    "msrp_aud_min": 54150,
                    "msrp_aud_max": 58290,
                    "fuel_consumption_l_100km": 5.6,
                    "kerb_weight_kg": 2005,
                    "standard_features": ["7 seats", "18-inch alloys", "Toyota Safety Sense", "LED headlamps", "8-inch touchscreen"],
                    "notes": "Outstanding fuel efficiency for a full 7-seater."
                },
                {
                    "badge_name": "GXL Hybrid AWD",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "e-Four AWD",
                    "transmissions": ["e-CVT"],
                    "msrp_aud_min": 63350,
                    "msrp_aud_max": 67810,
                    "fuel_consumption_l_100km": 5.6,
                    "kerb_weight_kg": 2050,
                    "standard_features": ["Synthetic leather seats", "12.3-inch multimedia touchscreen", "Wireless Apple CarPlay", "Power tailgate", "Roof rails"],
                    "notes": "Top-selling specification."
                },
                {
                    "badge_name": "Grande Hybrid AWD",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["5-door Wagon"],
                    "drivetrain": "e-Four AWD",
                    "transmissions": ["e-CVT"],
                    "msrp_aud_min": 75400,
                    "msrp_aud_max": 80230,
                    "fuel_consumption_l_100km": 5.6,
                    "kerb_weight_kg": 2105,
                    "standard_features": ["20-inch chrome alloys", "JBL 11-speaker audio", "Panoramic roof", "Head-up display", "Hands-free tailgate", "Leather seats"],
                    "notes": "Flagship hybrid crossover."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Kluger GXL Hybrid AWD",
                    "body_style": "5-door Wagon",
                    "engine_code": "A25A-FXS",
                    "transmission": "e-CVT",
                    "drivetrain": "AWD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 67810,
                    "power_kw": 184.0,
                    "torque_nm": 242.0,
                    "fuel_l_100km": 5.6,
                    "towing_braked_kg": 2000,
                    "notes": "5.6L/100km combined fuel consumption."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}


TOYOTA_86_MODEL = {
    "make_slug": "toyota",
    "model_slug": "86-gr86",
    "name": "86 / GR86",
    "vehicle_type": "Sports Coupe",
    "segment": "Sports Car",
    "years_sold_au": {"start": 2012, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota 86 and GR86 re-energized accessible rear-wheel-drive sports motoring in Australia. Developed jointly with Subaru (who built the cars at the Gunma Main Plant), the 86 combined a low center of gravity boxer engine, lightweight chassis, razor-sharp steering, and rear-drive dynamics at an accessible price point.",
    "australian_market_notes": "Launched in June 2012 with an audacious starting price of $29,990 AUD for the GT manual, the 86 created an immediate showroom storm and lengthy waiting lists across Australia. The GR86 arrived in September 2022 under the Gazoo Racing banner with a punchier 2.4-litre engine fixing the predecessor's mid-range torque dip.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "ZN6",
            "generation_name": "86 1st Generation",
            "years": {"start": 2012, "end": 2021},
            "body_styles": ["2-door Coupe"],
            "platform": "Subaru/Toyota ZN6",
            "ancap_rating": "5 stars",
            "summary": "Original lightweight rear-drive sports coupe featuring Subaru's FA20 flat-four with Toyota D-4S direct and port injection, 6-speed manual or auto, and Torsen LSD.",
            "engines": [
                {
                    "engine_code": "FA20 / 4U-GSE",
                    "name": "Subaru/Toyota FA20 / 4U-GSE 2.0L Boxer-4",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 147.0,
                    "power_rpm": "7000",
                    "torque_nm": 205.0,
                    "torque_rpm": "6400-6600",
                    "compression_ratio": "12.5:1",
                    "valvetrain": "DOHC 16-valve Dual AVCS",
                    "notes": "Upgraded in late 2016 facelift to 152kW/212Nm for 6-speed manual variants with red aluminium intake manifold."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT",
                    "years": {"start": 2012, "end": 2021},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 29990,
                    "msrp_aud_max": 34180,
                    "fuel_consumption_l_100km": 7.8,
                    "kerb_weight_kg": 1222,
                    "standard_features": ["16-inch alloy wheels", "Torsen limited-slip differential", "Air conditioning", "Cruise control", "7 airbags"],
                    "notes": "Disruptive $29,990 launch price point."
                },
                {
                    "badge_name": "GTS",
                    "years": {"start": 2012, "end": 2021},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 35490,
                    "msrp_aud_max": 39680,
                    "fuel_consumption_l_100km": 7.8,
                    "kerb_weight_kg": 1257,
                    "standard_features": ["17-inch alloys", "Leather/Alcantara heated seats", "Keyless smart entry", "Dual-zone climate control", "HID headlamps", "Rear spoiler"],
                    "notes": "Premium grade; later offered with Sachs dampers and Brembo brakes package."
                }
            ],
            "configurations": [
                {
                    "badge_name": "86 GTS Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "FA20 / 4U-GSE",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2012,
                    "years_end": 2021,
                    "msrp_aud": 35490,
                    "power_kw": 147.0,
                    "torque_nm": 205.0,
                    "fuel_l_100km": 7.8,
                    "towing_braked_kg": 0,
                    "notes": "Benchmark driver's coupe in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ZN8",
            "generation_name": "GR86 2nd Generation",
            "years": {"start": 2022, "end": "Present"},
            "body_styles": ["2-door Coupe"],
            "platform": "Toyota/Subaru ZN8",
            "ancap_rating": "Untested",
            "summary": "Gazoo Racing developed second-generation coupe with larger 2.4L FA24 boxer engine delivering 174kW and 250Nm, curing the previous torque curve dip, with 50% stiffer torsional rigidity.",
            "engines": [
                {
                    "engine_code": "FA24D",
                    "name": "Subaru/Toyota FA24D 2.4L Boxer-4",
                    "displacement_cc": 2387,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Horizontally Opposed Boxer-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 174.0,
                    "power_rpm": "7000",
                    "torque_nm": 250.0,
                    "torque_rpm": "3700",
                    "compression_ratio": "12.5:1",
                    "valvetrain": "DOHC 16-valve Dual AVCS",
                    "notes": "Peak torque arrives at just 3,700rpm compared to 6,400rpm on predecessor."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 43240,
                    "msrp_aud_max": 45390,
                    "fuel_consumption_l_100km": 8.7,
                    "kerb_weight_kg": 1287,
                    "standard_features": ["17-inch alloy wheels", "Torsen LSD", "8-inch touchscreen", "7-inch digital cluster", "LED headlights", "Track mode ESC"],
                    "notes": "Entry enthusiast specification."
                },
                {
                    "badge_name": "GTS",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 45390,
                    "msrp_aud_max": 47540,
                    "fuel_consumption_l_100km": 8.8,
                    "kerb_weight_kg": 1306,
                    "standard_features": ["18-inch matte black alloys with Michelin Pilot Sport 4 tyres", "Ultrasuede and leather heated seats", "Aluminium sports pedals", "Blind-spot monitoring"],
                    "notes": "Top-selling model in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GR86 GTS Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "FA24D",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2022,
                    "years_end": "Present",
                    "msrp_aud": 45390,
                    "power_kw": 174.0,
                    "torque_nm": 250.0,
                    "fuel_l_100km": 8.8,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 6.3 seconds."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

SUPRA_MODEL = {
    "make_slug": "toyota",
    "model_slug": "supra",
    "name": "Supra",
    "vehicle_type": "Sports Coupe",
    "segment": "Sports Performance",
    "years_sold_au": {"start": 1983, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota Supra is a halo sports grand tourer with an indelible legacy in Australian motorsport and enthusiast culture. From early Celica Supra models through the twin-turbo 2JZ-GTE JZA80 supercar killer to the modern B58-powered GR Supra, it represents Toyota's front-engine rear-drive inline-six performance pinnacle.",
    "australian_market_notes": "First sold locally in 1983 as the Celica Supra MA61, the nameplate reached motorsport fame when Peter Williamson campaigned the MA70 Turbo in the Australian Touring Car Championship. While the iconic JZA80 Mk IV twin-turbo was primarily imported as a low-volume/grey-market legend in Australia, the GR Supra returned officially in 2019.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "MA61",
            "generation_name": "Celica Supra Mk II",
            "years": {"start": 1983, "end": 1986},
            "body_styles": ["3-door Liftback"],
            "platform": "Toyota A60",
            "ancap_rating": "Untested",
            "summary": "First Supra sold in Australia, featuring pop-up headlamps, flared wheel arches, Lotus-tuned independent rear suspension, and 2.8L 5M-E inline-six power.",
            "engines": [
                {
                    "engine_code": "5M-E",
                    "name": "Toyota 5M-E 2.8L EFI SOHC Inline-6",
                    "displacement_cc": 2759,
                    "displacement_litres": 2.8,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 105.0,
                    "power_rpm": "5200",
                    "torque_nm": 210.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Bosch L-Jetronic fuel injection."
                }
            ],
            "badges": [
                {
                    "badge_name": "Celica Supra 2.8i",
                    "years": {"start": 1983, "end": 1986},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 28500,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1360,
                    "standard_features": ["14-inch alloy wheels", "Independent rear suspension", "Digital dash (option)", "Power windows", "Sunroof"],
                    "notes": "Pioneered luxury GT performance for Toyota in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Celica Supra Manual",
                    "body_style": "3-door Liftback",
                    "engine_code": "5M-E",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1983,
                    "years_end": 1986,
                    "msrp_aud": 24990,
                    "power_kw": 105.0,
                    "torque_nm": 210.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 1200,
                    "notes": "First official Supra badge in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "MA70",
            "generation_name": "Supra Mk III",
            "years": {"start": 1986, "end": 1993},
            "body_styles": ["3-door Liftback Coupe", "Targa Sport Roof"],
            "platform": "Toyota A70",
            "ancap_rating": "Untested",
            "summary": "Separated from Celica as a dedicated model on double-wishbone suspension, offering the 3.0L 7M-GE and Australia's first factory turbocharged Supra, the 7M-GTE.",
            "engines": [
                {
                    "engine_code": "7M-GE",
                    "name": "Toyota 7M-GE 3.0L DOHC Inline-6",
                    "displacement_cc": 2954,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 149.0,
                    "power_rpm": "6000",
                    "torque_nm": 254.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "9.1:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Silky smooth naturally aspirated 3.0-litre."
                },
                {
                    "engine_code": "7M-GTE",
                    "name": "Toyota 7M-GTE 3.0L Turbo DOHC Inline-6",
                    "displacement_cc": 2954,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 173.0,
                    "power_rpm": "5600",
                    "torque_nm": 344.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "8.4:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "CT26 turbocharger; raced in Group A Australian Touring Cars."
                }
            ],
            "badges": [
                {
                    "badge_name": "Supra 3.0i",
                    "years": {"start": 1986, "end": 1993},
                    "body_styles": ["3-door Liftback", "Targa Sport Roof"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 41990,
                    "msrp_aud_max": 52000,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1520,
                    "standard_features": ["Pop-up headlights", "TEMS electronic damper control", "Power seats", "Climate control", "16-inch alloy wheels"],
                    "notes": "Naturally aspirated grand tourer."
                },
                {
                    "badge_name": "Supra Turbo",
                    "years": {"start": 1987, "end": 1993},
                    "body_styles": ["3-door Liftback", "Targa Sport Roof"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 56990,
                    "msrp_aud_max": 68000,
                    "fuel_consumption_l_100km": 12.0,
                    "kerb_weight_kg": 1590,
                    "standard_features": ["LSD differential", "Turbo boost gauge", "ABS brakes standard", "Sport roof (removable targa panel)"],
                    "notes": "Flagship Japanese supercar alternative in late 1980s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Supra Turbo Targa",
                    "body_style": "Targa Sport Roof",
                    "engine_code": "7M-GTE",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1987,
                    "years_end": 1993,
                    "msrp_aud": 64990,
                    "power_kw": 173.0,
                    "torque_nm": 344.0,
                    "fuel_l_100km": 12.0,
                    "towing_braked_kg": 1400,
                    "notes": "0-100 km/h in 6.8 seconds."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "JZA80",
            "generation_name": "Supra Mk IV",
            "years": {"start": 1993, "end": "2002"},
            "body_styles": ["2-door Coupe", "Aerotop"],
            "platform": "Toyota A80",
            "ancap_rating": "Untested",
            "summary": "Legendary Japanese supercar featuring the bulletproof 2JZ-GTE sequential twin-turbo inline-six, aluminium double-wishbone suspension, huge rear wing, and 6-speed Getrag manual.",
            "engines": [
                {
                    "engine_code": "2JZ-GE",
                    "name": "Toyota 2JZ-GE 3.0L DOHC Inline-6",
                    "displacement_cc": 2997,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 165.0,
                    "power_rpm": "5800",
                    "torque_nm": 284.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Found in SZ and SZ-R grades."
                },
                {
                    "engine_code": "2JZ-GTE",
                    "name": "Toyota 2JZ-GTE 3.0L Sequential Twin-Turbo Inline-6",
                    "displacement_cc": 2997,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Twin-Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 243.0,
                    "power_rpm": "5600",
                    "torque_nm": 451.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Cast-iron block revered worldwide for extreme tuning headroom (up to 1,000+ hp)."
                }
            ],
            "badges": [
                {
                    "badge_name": "SZ / SZ-R",
                    "years": {"start": 1993, "end": 2002},
                    "body_styles": ["Coupe", "Aerotop"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "6-speed manual", "4-speed auto"],
                    "msrp_aud_min": 65000,
                    "msrp_aud_max": 75000,
                    "fuel_consumption_l_100km": 10.9,
                    "kerb_weight_kg": 1450,
                    "standard_features": ["16-inch or 17-inch alloys", "Cloth sports bucket seats", "Bilstein dampers (SZ-R)", "Limited slip differential"],
                    "notes": "Naturally aspirated grade."
                },
                {
                    "badge_name": "RZ / GZ Twin Turbo",
                    "years": {"start": 1993, "end": 2002},
                    "body_styles": ["Coupe", "Aerotop"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed Getrag manual", "4-speed automatic"],
                    "msrp_aud_min": 89000,
                    "msrp_aud_max": 110000,
                    "fuel_consumption_l_100km": 11.8,
                    "kerb_weight_kg": 1570,
                    "standard_features": ["Sequential twin turbos", "Active front spoiler", "Iconic high rear wing", "Brembo/Toyota 4-pot brakes", "Torsen LSD"],
                    "notes": "Cult status supercar killer with 0-100 km/h in 4.9 seconds."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Supra RZ Twin Turbo",
                    "body_style": "Coupe",
                    "engine_code": "2JZ-GTE",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1993,
                    "years_end": 2002,
                    "msrp_aud": 95000,
                    "power_kw": 243.0,
                    "torque_nm": 451.0,
                    "fuel_l_100km": 11.8,
                    "towing_braked_kg": 0,
                    "notes": "One of the most celebrated Japanese sports cars ever imported to Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "J29/DB",
            "generation_name": "GR Supra Mk V",
            "years": {"start": 2019, "end": "Present"},
            "body_styles": ["2-door Coupe"],
            "platform": "BMW/Toyota CLAR-based sports platform",
            "ancap_rating": "Untested",
            "summary": "Co-developed with BMW and built by Magna Steyr in Austria. Features BMW's B58 3.0L twin-scroll turbocharged inline-six (up to 285kW/500Nm) with 50:50 weight distribution and 6-speed manual option.",
            "engines": [
                {
                    "engine_code": "B58B30O1",
                    "name": "BMW/Toyota B58 3.0L Turbo Inline-6",
                    "displacement_cc": 2998,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Twin-Scroll Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 285.0,
                    "power_rpm": "5800-6500",
                    "torque_nm": 500.0,
                    "torque_rpm": "1800-5000",
                    "compression_ratio": "10.2:1",
                    "valvetrain": "DOHC 24-valve Double-VANOS and Valvetronic",
                    "notes": "Launched at 250kW in 2019; upgraded to 285kW in late 2020."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "8-speed automatic"],
                    "msrp_aud_min": 84900,
                    "msrp_aud_max": 87000,
                    "fuel_consumption_l_100km": 7.7,
                    "kerb_weight_kg": 1495,
                    "standard_features": ["18-inch alloy wheels", "Active differential", "Adaptive variable suspension", "Dual-zone climate control"],
                    "notes": "High performance sports car entry."
                },
                {
                    "badge_name": "GTS",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual", "8-speed automatic"],
                    "msrp_aud_min": 94900,
                    "msrp_aud_max": 97000,
                    "fuel_consumption_l_100km": 7.7,
                    "kerb_weight_kg": 1500,
                    "standard_features": ["19-inch forged alloy wheels", "Brembo 4-piston front brakes", "Head-up display", "JBL 12-speaker audio"],
                    "notes": "Top-specification variant; 6-speed manual added in 2022."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GR Supra GTS Manual",
                    "body_style": "2-door Coupe",
                    "engine_code": "B58B30O1",
                    "transmission": "6-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 2022,
                    "years_end": "Present",
                    "msrp_aud": 97000,
                    "power_kw": 285.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 8.9,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 4.4 seconds with iMT rev-matching manual."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

CELICA_MODEL = {
    "make_slug": "toyota",
    "model_slug": "celica",
    "name": "Celica",
    "vehicle_type": "Sports Coupe / Liftback",
    "segment": "Sports Coupe",
    "years_sold_au": {"start": 1971, "end": 2005},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota Celica was Australia's definitive Japanese sports coupe for 34 years across seven generations. From the Mustang-inspired TA22 and RA28 liftbacks of the 1970s to the championship-winning turbo all-wheel-drive GT-Four rally homologation specials and high-revving 2ZZ-GE VVTL-i ZR, the Celica defined stylish sports performance.",
    "australian_market_notes": "Introduced to Australia in 1971 by Thiess Toyota and AMI, the Celica won immense praise for pairing affordable coupe styling with bulletproof mechanicals. In motorsport, the Celica ST185 and ST205 GT-Four dominated the Australian Rally Championship with Neal Bates and Coral Taylor, securing four ARC national titles in 1993, 1994, 1995, and 2008.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "A20/A30",
            "generation_name": "Celica 1st Generation",
            "years": {"start": 1971, "end": 1977},
            "body_styles": ["2-door Notchback Coupe", "3-door Liftback"],
            "platform": "Toyota A20",
            "ancap_rating": "Untested",
            "summary": "The 'Japanese Mustang' that started the coupe craze in Australia. TA22 notchback followed by the stunning RA28 fastback Liftback with vertical triple taillights.",
            "engines": [
                {
                    "engine_code": "2T-B",
                    "name": "Toyota 2T-B 1.6L Twin-Carb",
                    "displacement_cc": 1588,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 75.0,
                    "power_rpm": "6000",
                    "torque_nm": 137.0,
                    "torque_rpm": "4200",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "OHV 8-valve",
                    "notes": "Twin Aisan side-draught carburettors in TA22 LT/ST."
                },
                {
                    "engine_code": "18R-C",
                    "name": "Toyota 18R-C 2.0L SOHC",
                    "displacement_cc": 1968,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 66.0,
                    "power_rpm": "5000",
                    "torque_nm": 145.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Standard engine in RA23 and RA28 Australian delivered cars."
                }
            ],
            "badges": [
                {
                    "badge_name": "TA22 LT / ST",
                    "years": {"start": 1971, "end": 1975},
                    "body_styles": ["2-door Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 3195,
                    "msrp_aud_max": 3890,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 965,
                    "standard_features": ["High-back bucket seats", "Wood-grain steering wheel", "Sports instrumentation with tachometer", "Front disc brakes"],
                    "notes": "Initial Australian launch hit."
                },
                {
                    "badge_name": "RA28 Liftback",
                    "years": {"start": 1976, "end": 1977},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "3-speed automatic"],
                    "msrp_aud_min": 5690,
                    "msrp_aud_max": 6450,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1050,
                    "standard_features": ["Mustang-inspired fastback styling", "Fold-down rear seat", "Twin bonnet vents", "5-speed manual transmission"],
                    "notes": "Highly collectible 1970s coupe in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Celica RA28 Liftback",
                    "body_style": "3-door Liftback",
                    "engine_code": "18R-C",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1976,
                    "years_end": 1977,
                    "msrp_aud": 5690,
                    "power_kw": 66.0,
                    "torque_nm": 145.0,
                    "fuel_l_100km": 9.8,
                    "towing_braked_kg": 900,
                    "notes": "Iconic Australian classic."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "A40/A60",
            "generation_name": "Celica 2nd & 3rd Generation",
            "years": {"start": 1978, "end": 1985},
            "body_styles": ["2-door Coupe", "3-door Liftback"],
            "platform": "Toyota A40/A60",
            "ancap_rating": "Untested",
            "summary": "Crisp wedge styling in A40, followed by pop-up headlamps and fuel-injected 2.4L 22R-E power in the RA65 SX.",
            "engines": [
                {
                    "engine_code": "22R-E",
                    "name": "Toyota 22R-E 2.4L EFI",
                    "displacement_cc": 2366,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 87.0,
                    "power_rpm": "4800",
                    "torque_nm": 192.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "9.3:1",
                    "valvetrain": "SOHC 8-valve EFI",
                    "notes": "Torquey 2.4-litre introduced in 1984 RA65 SX."
                }
            ],
            "badges": [
                {
                    "badge_name": "RA60 / RA65 SX",
                    "years": {"start": 1982, "end": 1985},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 14990,
                    "msrp_aud_max": 18200,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 1130,
                    "standard_features": ["Pop-up headlights", "14-inch sports alloys", "8-way adjustable driver's sports seat", "Four-wheel disc brakes"],
                    "notes": "Final rear-wheel drive Celica generation."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Celica SX Liftback",
                    "body_style": "3-door Liftback",
                    "engine_code": "22R-E",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1984,
                    "years_end": 1985,
                    "msrp_aud": 16990,
                    "power_kw": 87.0,
                    "torque_nm": 192.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 1000,
                    "notes": "Last of the rear-drive Celicas."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "T160",
            "generation_name": "Celica 4th Generation (ST162 / ST165)",
            "years": {"start": 1985, "end": 1989},
            "body_styles": ["3-door Liftback", "2-door Coupe"],
            "platform": "Toyota T160",
            "ancap_rating": "Untested",
            "summary": "Switched to front-wheel drive with Yamaha-developed 3S-GE DOHC engine, and introduced the legendary ST165 GT-Four full-time AWD turbo rally weapon.",
            "engines": [
                {
                    "engine_code": "3S-GE",
                    "name": "Toyota 3S-GE 2.0L Twin-Cam 16",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 103.0,
                    "power_rpm": "6200",
                    "torque_nm": 175.0,
                    "torque_rpm": "4800",
                    "compression_ratio": "9.8:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Yamaha cylinder head with wide-angle valves."
                },
                {
                    "engine_code": "3S-GTE",
                    "name": "Toyota 3S-GTE 2.0L Turbocharged",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 136.0,
                    "power_rpm": "6000",
                    "torque_nm": 240.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Water-to-air intercooler in ST165 GT-Four."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX",
                    "years": {"start": 1985, "end": 1989},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 31500,
                    "fuel_consumption_l_100km": 8.8,
                    "kerb_weight_kg": 1160,
                    "standard_features": ["14-inch alloys", "Power steering", "Air conditioning", "Velour sports seats"],
                    "notes": "Mainstream FWD hot coupe."
                },
                {
                    "badge_name": "GT-Four",
                    "years": {"start": 1988, "end": 1989},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 42990,
                    "msrp_aud_max": 45000,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1350,
                    "standard_features": ["Full-time AWD with center diff lock", "Water-to-air intercooler", "Twin exhaust", "15-inch alloys"],
                    "notes": "Toyota's first AWD rally homologation car in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Celica GT-Four AWD",
                    "body_style": "3-door Liftback",
                    "engine_code": "3S-GTE",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 1988,
                    "years_end": 1989,
                    "msrp_aud": 42990,
                    "power_kw": 136.0,
                    "torque_nm": 240.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 1200,
                    "notes": "First Celica GT-Four delivered to Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "T180",
            "generation_name": "Celica 5th Generation (ST184 / ST185)",
            "years": {"start": 1989, "end": 1993},
            "body_styles": ["3-door Liftback", "2-door Coupe", "Convertible"],
            "platform": "Toyota T180",
            "ancap_rating": "Untested",
            "summary": "Curvaceous 'bio-kinetic' aero styling. Produced the world rally champion ST185 GT-Four Group A Rallye Carlos Sainz limited edition.",
            "engines": [
                {
                    "engine_code": "5S-FE",
                    "name": "Toyota 5S-FE 2.2L Twin-Cam",
                    "displacement_cc": 2164,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 100.0,
                    "power_rpm": "5400",
                    "torque_nm": 189.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Torquey 2.2L engine in Australian ST184 SX."
                },
                {
                    "engine_code": "3S-GTE-Gen2",
                    "name": "Toyota 3S-GTE 2.0L Turbo (Group A)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Twin-Entry Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 153.0,
                    "power_rpm": "6000",
                    "torque_nm": 275.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Air-to-air intercooler with distinctive bonnet bulge and extraction vent."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX",
                    "years": {"start": 1989, "end": 1993},
                    "body_styles": ["3-door Liftback", "2-door Coupe"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 28990,
                    "msrp_aud_max": 38000,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 1210,
                    "standard_features": ["Curved styling", "14-inch alloys", "Pop-up lights", "Power mirrors", "Sports interior"],
                    "notes": "Volume Australian sports coupe."
                },
                {
                    "badge_name": "GT-Four Group A Rallye",
                    "years": {"start": 1991, "end": 1992},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 52990,
                    "msrp_aud_max": 54500,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1460,
                    "standard_features": ["150 Australian numbered units", "Torsen rear LSD", "Round air intake for intercooler", "Lightweight front bumper", "Numbered commemorative plaque"],
                    "notes": "Homologation special for Carlos Sainz's WRC campaign; ARC winner with Neal Bates."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Celica GT-Four Group A Rallye",
                    "body_style": "3-door Liftback",
                    "engine_code": "3S-GTE-Gen2",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 1991,
                    "years_end": 1992,
                    "msrp_aud": 52990,
                    "power_kw": 153.0,
                    "torque_nm": 275.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 1200,
                    "notes": "Numbered Australian limited edition (150 units)."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "T200",
            "generation_name": "Celica 6th Generation (ST204 / ST205)",
            "years": {"start": 1994, "end": 1999},
            "body_styles": ["3-door Liftback", "2-door Coupe"],
            "platform": "Toyota T200",
            "ancap_rating": "Untested",
            "summary": "Distinctive quad round headlights. Spawned the ultimate 178kW ST205 GT-Four Group A (only 77 officially sold in Australia), as well as popular ST204 SX and ZR liftbacks.",
            "engines": [
                {
                    "engine_code": "5S-FE-Gen2",
                    "name": "Toyota 5S-FE 2.2L Twin-Cam",
                    "displacement_cc": 2164,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 100.0,
                    "power_rpm": "5200",
                    "torque_nm": 196.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Mainstream ST204 engine."
                },
                {
                    "engine_code": "3S-GTE-Gen3",
                    "name": "Toyota 3S-GTE 2.0L Turbo (ST205)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Twin-Entry Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 178.0,
                    "power_rpm": "6000",
                    "torque_nm": 302.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Aluminium bonnet, water-injection manifold, anti-lag hardware; 178kW Australian spec."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX / ZR",
                    "years": {"start": 1994, "end": 1999},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 35990,
                    "msrp_aud_max": 44500,
                    "fuel_consumption_l_100km": 8.7,
                    "kerb_weight_kg": 1190,
                    "standard_features": ["Quad projector headlights", "15-inch alloys (ZR)", "Driver airbag", "Rear spoiler", "ABS (ZR)"],
                    "notes": "Staple Aussie sports coupe of the late 1990s."
                },
                {
                    "badge_name": "GT-Four Group A (ST205)",
                    "years": {"start": 1994, "end": 1995},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 79990,
                    "msrp_aud_max": 81990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1390,
                    "standard_features": ["77 Australian delivered units", "Super Strut front suspension", "High rear aero wing with riser blocks", "4-pot front brake calipers", "Aluminium bonnet"],
                    "notes": "Hyper-rare WRC homologation holy grail in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Celica GT-Four Group A (ST205)",
                    "body_style": "3-door Liftback",
                    "engine_code": "3S-GTE-Gen3",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 1994,
                    "years_end": 1995,
                    "msrp_aud": 81990,
                    "power_kw": 178.0,
                    "torque_nm": 302.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 1200,
                    "notes": "Just 77 cars officially imported to Australia for Group A rallying."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "T230",
            "generation_name": "Celica 7th Generation (ZZT231)",
            "years": {"start": 1999, "end": 2005},
            "body_styles": ["3-door Liftback"],
            "platform": "Toyota T230",
            "ancap_rating": "Untested",
            "summary": "Dramatic sharp-edged cab-forward styling with Yamaha-developed 140kW 2ZZ-GE high-rpm screamer with VVTL-i and 6-speed manual.",
            "engines": [
                {
                    "engine_code": "2ZZ-GE",
                    "name": "Toyota/Yamaha 2ZZ-GE 1.8L VVTL-i",
                    "displacement_cc": 1796,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 140.0,
                    "power_rpm": "7600",
                    "torque_nm": 180.0,
                    "torque_rpm": "6800",
                    "compression_ratio": "11.5:1",
                    "valvetrain": "DOHC 16-valve VVTL-i",
                    "notes": "Variable valve timing and high-lift cam switch at 6,200rpm; 8,200rpm redline."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX",
                    "years": {"start": 1999, "end": 2005},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 42500,
                    "fuel_consumption_l_100km": 8.2,
                    "kerb_weight_kg": 1120,
                    "standard_features": ["15-inch alloy wheels", "Dual airbags", "ABS with EBD", "Air conditioning", "Power windows", "CD player"],
                    "notes": "Lightweight 1,120kg kerb weight."
                },
                {
                    "badge_name": "ZR",
                    "years": {"start": 1999, "end": 2005},
                    "body_styles": ["3-door Liftback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 43990,
                    "msrp_aud_max": 46990,
                    "fuel_consumption_l_100km": 8.2,
                    "kerb_weight_kg": 1140,
                    "standard_features": ["16-inch alloy wheels", "Power glass moonroof", "Front fog lamps", "Aluminium pedals", "Side airbags"],
                    "notes": "Flagship final Celica trim."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Celica ZR Manual",
                    "body_style": "3-door Liftback",
                    "engine_code": "2ZZ-GE",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1999,
                    "years_end": 2005,
                    "msrp_aud": 43990,
                    "power_kw": 140.0,
                    "torque_nm": 180.0,
                    "fuel_l_100km": 8.2,
                    "towing_braked_kg": 900,
                    "notes": "0-100 km/h in 7.4 seconds with 8,200rpm screaming redline."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}
