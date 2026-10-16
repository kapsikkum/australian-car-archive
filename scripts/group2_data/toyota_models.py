"""Deep-dive model data for Toyota: Hilux, LandCruiser, Corolla, Camry, and RAV4."""

HILUX_MODEL = {
    "make_slug": "toyota",
    "model_slug": "hilux",
    "name": "HiLux",
    "vehicle_type": "Ute / Cab Chassis",
    "segment": "Light Commercial",
    "years_sold_au": {"start": 1968, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota HiLux is an Australian cultural icon and the country's best-selling vehicle outright from 2016 through 2022. Renowned for near-indestructible durability, it serves on construction sites, farms, mining operations, and outback tracks nationwide.",
    "australian_market_notes": "First imported in 1968 by Thiess Toyota, the HiLux evolved from a basic 1.5-ton commercial hauler to Australia's favourite dual-cab family and adventure vehicle. The introduction of factory 4WD in 1979 and the solid-axle LN106 established its legendary reputation. The N80 generation introduced high-end Australian-developed flagship editions like Rogue, Rugged X, and the wide-track GR Sport.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "RN10",
            "generation_name": "HiLux 1st Generation",
            "years": {"start": 1968, "end": 1972},
            "body_styles": ["Single Cab Ute"],
            "platform": "Toyota N10",
            "ancap_rating": "Untested",
            "summary": "The original HiLux introduced to Australia by Thiess Toyota. Simple, durable commercial runabout with a separate chassis and rear leaf springs.",
            "engines": [
                {
                    "engine_code": "2R",
                    "name": "Toyota 2R 1.5L",
                    "displacement_cc": 1490,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 57.0,
                    "power_rpm": "5000",
                    "torque_nm": 116.0,
                    "torque_rpm": "2600",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "OHV 8-valve",
                    "notes": "Robust pushrod engine paired with 4-speed column manual."
                }
            ],
            "badges": [
                {
                    "badge_name": "Standard",
                    "years": {"start": 1968, "end": 1972},
                    "body_styles": ["Single Cab Ute"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual"],
                    "msrp_aud_min": 1850,
                    "msrp_aud_max": 2100,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 1040,
                    "standard_features": ["Vinyl bench seat", "Heater/demister", "Column gearshift", "14-inch steel wheels"],
                    "notes": "1-ton payload rating."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Standard",
                    "body_style": "Single Cab Ute",
                    "engine_code": "2R",
                    "transmission": "4-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1968,
                    "years_end": 1972,
                    "msrp_aud": 1890,
                    "power_kw": 57.0,
                    "torque_nm": 116.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 1000,
                    "notes": "Classic Australian workhorse."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "RN30/LN40",
            "generation_name": "HiLux 3rd Generation",
            "years": {"start": 1978, "end": 1983},
            "body_styles": ["Single Cab", "Dual Cab", "Cab Chassis"],
            "platform": "Toyota N30/N40",
            "ancap_rating": "Untested",
            "summary": "Pivotal generation introducing factory 4WD in 1979 and the first diesel engine (LN40), establishing the HiLux 4x4 dynasty in Australia.",
            "engines": [
                {
                    "engine_code": "18R",
                    "name": "Toyota 18R 2.0L",
                    "displacement_cc": 1968,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 66.0,
                    "power_rpm": "4800",
                    "torque_nm": 145.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Bulletproof SOHC iron-block workhorse."
                },
                {
                    "engine_code": "L",
                    "name": "Toyota L 2.2L Diesel",
                    "displacement_cc": 2188,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 46.0,
                    "power_rpm": "4200",
                    "torque_nm": 126.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "22.2:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "First diesel engine offered in the Australian HiLux range."
                }
            ],
            "badges": [
                {
                    "badge_name": "4WD",
                    "years": {"start": 1979, "end": 1983},
                    "body_styles": ["Single Cab", "Dual Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["4-speed manual", "5-speed manual"],
                    "msrp_aud_min": 6800,
                    "msrp_aud_max": 8900,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1380,
                    "standard_features": ["Dual-range transfer case", "Solid front axle", "Free-wheeling hubs", "Heavy duty leaf springs"],
                    "notes": "Revolutionary 4WD ute that opened the bush to recreational and trade buyers."
                }
            ],
            "configurations": [
                {
                    "badge_name": "4WD",
                    "body_style": "Single Cab",
                    "engine_code": "18R",
                    "transmission": "4-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1979,
                    "years_end": 1983,
                    "msrp_aud": 6990,
                    "power_kw": 66.0,
                    "torque_nm": 145.0,
                    "fuel_l_100km": 11.0,
                    "towing_braked_kg": 1500,
                    "notes": "First factory 4WD HiLux in Australia."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "LN106/RN105",
            "generation_name": "HiLux 5th Generation",
            "years": {"start": 1988, "end": 1997},
            "body_styles": ["Single Cab", "Xtra Cab", "Dual Cab"],
            "platform": "Toyota N100",
            "ancap_rating": "Untested",
            "summary": "Regarded by 4WD enthusiasts as the high-water mark for ruggedness, featuring dual live solid beam axles, leaf springs, and the unkillable 2.8L 3L diesel.",
            "engines": [
                {
                    "engine_code": "3L",
                    "name": "Toyota 3L 2.8L Diesel",
                    "displacement_cc": 2779,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 60.0,
                    "power_rpm": "4000",
                    "torque_nm": 188.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "22.2:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Renowned for legendary outback reliability and simple mechanical injection."
                },
                {
                    "engine_code": "22R",
                    "name": "Toyota 22R 2.4L Petrol",
                    "displacement_cc": 2366,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 75.0,
                    "power_rpm": "4800",
                    "torque_nm": 175.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Carburetted and later EFI 22R-E petrol workhorse."
                }
            ],
            "badges": [
                {
                    "badge_name": "SR5",
                    "years": {"start": 1988, "end": 1997},
                    "body_styles": ["Dual Cab", "Xtra Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 24500,
                    "msrp_aud_max": 34900,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1580,
                    "standard_features": ["Sports instrumentation with tacho", "Cloth bucket seats", "Chrome bumpers and mirrors", "Power steering", "Two-tone paint"],
                    "notes": "Defined the premium recreational dual-cab 4WD category in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SR5",
                    "body_style": "Dual Cab",
                    "engine_code": "3L",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1988,
                    "years_end": 1997,
                    "msrp_aud": 29800,
                    "power_kw": 60.0,
                    "torque_nm": 188.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 1800,
                    "notes": "LN106 solid axle dual cab legend."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "KUN26/GGN25",
            "generation_name": "HiLux 7th Generation",
            "years": {"start": 2005, "end": 2015},
            "body_styles": ["Single Cab", "Extra Cab", "Double Cab"],
            "platform": "Toyota IMV",
            "ancap_rating": "4 to 5 Stars",
            "summary": "Built on the IMV global ladder chassis with modern common-rail D-4D diesel and 4.0L V6 power, taking the HiLux to top sales podiums across Australia.",
            "engines": [
                {
                    "engine_code": "1KD-FTV",
                    "name": "Toyota 1KD-FTV 3.0L D-4D",
                    "displacement_cc": 2982,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 126.0,
                    "power_rpm": "3600",
                    "torque_nm": 343.0,
                    "torque_rpm": "1400-3400",
                    "compression_ratio": "17.9:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Common-rail turbo-diesel that powered thousands of Australian commercial and touring fleets."
                },
                {
                    "engine_code": "1GR-FE",
                    "name": "Toyota 1GR-FE 4.0L V6",
                    "displacement_cc": 3956,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 175.0,
                    "power_rpm": "5200",
                    "torque_nm": 376.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 24-valve VVT-i",
                    "notes": "Silky, powerful petrol V6 popular with trade and recreational buyers."
                }
            ],
            "badges": [
                {
                    "badge_name": "SR5",
                    "years": {"start": 2005, "end": 2015},
                    "body_styles": ["Double Cab", "Extra Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual", "4-speed auto", "5-speed auto"],
                    "msrp_aud_min": 42990,
                    "msrp_aud_max": 53990,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 1850,
                    "standard_features": ["17-inch alloy wheels", "Sports bar", "Climate control", "Touchscreen audio", "Cruise control", "Fog lights"],
                    "notes": "Australia's default lifestyle dual-cab benchmark."
                },
                {
                    "badge_name": "WorkMate",
                    "years": {"start": 2005, "end": 2015},
                    "body_styles": ["Single Cab", "Double Cab"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 17990,
                    "msrp_aud_max": 26990,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 1420,
                    "standard_features": ["Vinyl floor", "Black bumpers", "Steel wheels", "Heavy duty dropside tray"],
                    "notes": "Everyday tradie runabout."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SR5",
                    "body_style": "Double Cab",
                    "engine_code": "1KD-FTV",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 2005,
                    "years_end": 2015,
                    "msrp_aud": 47990,
                    "power_kw": 126.0,
                    "torque_nm": 343.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 2500,
                    "notes": "Classic D-4D SR5 dual cab."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "N80",
            "generation_name": "HiLux 8th Generation",
            "years": {"start": 2015, "end": "Present"},
            "body_styles": ["Single Cab", "Extra Cab", "Double Cab"],
            "platform": "Toyota IMV II",
            "ancap_rating": "5 Stars",
            "summary": "Australia's outright top-selling motor vehicle from 2016 through 2022, powered by the 2.8L 1GD-FTV diesel with local engineering enhancements like wide-track Rogue and GR Sport.",
            "engines": [
                {
                    "engine_code": "1GD-FTV",
                    "name": "Toyota 1GD-FTV 2.8L Turbo-Diesel",
                    "displacement_cc": 2755,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 150.0,
                    "power_rpm": "3400",
                    "torque_nm": 500.0,
                    "torque_rpm": "1600-2800",
                    "compression_ratio": "15.6:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Upgraded in 2020 to 150kW/500Nm, followed by 165kW/550Nm in GR Sport and 48V V-Active mild hybrid."
                },
                {
                    "engine_code": "2TR-FE",
                    "name": "Toyota 2TR-FE 2.7L Petrol",
                    "displacement_cc": 2694,
                    "displacement_litres": 2.7,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 122.0,
                    "power_rpm": "5200",
                    "torque_nm": 245.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.2:1",
                    "valvetrain": "DOHC 16-valve Dual VVT-i",
                    "notes": "WorkMate entry petrol 4-cylinder engine."
                }
            ],
            "badges": [
                {
                    "badge_name": "SR5",
                    "years": {"start": 2015, "end": "Present"},
                    "body_styles": ["Double Cab", "Extra Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 54440,
                    "msrp_aud_max": 64990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 2050,
                    "standard_features": ["LED headlights", "18-inch alloy wheels", "Toyota Safety Sense (AEB, Lane Trace, Adaptive Cruise)", "Satellite navigation", "Rear diff lock", "Apple CarPlay/Android Auto"],
                    "notes": "The sales backbone of the Australian dual-cab ute segment."
                },
                {
                    "badge_name": "Rogue",
                    "years": {"start": 2018, "end": "Present"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 61990,
                    "msrp_aud_max": 70200,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 2175,
                    "standard_features": ["Wide track suspension (+140mm track width)", "Rear disc brakes", "Motorised roll-cover", "Marine carpet tub liner", "Leather-accented heated seats"],
                    "notes": "Engineered in Melbourne by Toyota Australia's engineering team."
                },
                {
                    "badge_name": "GR Sport",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 73990,
                    "msrp_aud_max": 74990,
                    "fuel_consumption_l_100km": 8.1,
                    "kerb_weight_kg": 2270,
                    "standard_features": ["165kW/550Nm high-output tune", "Wide track chassis (+140mm front, +155mm rear)", "KYB monotube shock absorbers", "All-terrain tyres", "Rock sliders", "Paddle shifters", "GR leather-suede bucket seats"],
                    "notes": "Dakar-inspired Australian flagship developed with Gazoo Racing."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SR5",
                    "body_style": "Double Cab",
                    "engine_code": "1GD-FTV",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2020,
                    "years_end": "Present",
                    "msrp_aud": 62490,
                    "power_kw": 150.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 7.9,
                    "towing_braked_kg": 3500,
                    "notes": "Australia's top-selling specification."
                },
                {
                    "badge_name": "GR Sport",
                    "body_style": "Double Cab",
                    "engine_code": "1GD-FTV",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2023,
                    "years_end": "Present",
                    "msrp_aud": 74990,
                    "power_kw": 165.0,
                    "torque_nm": 550.0,
                    "fuel_l_100km": 8.1,
                    "towing_braked_kg": 3500,
                    "notes": "High-output wide-track flagship."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

LANDCRUISER_MODEL = {
    "make_slug": "toyota",
    "model_slug": "landcruiser",
    "name": "LandCruiser",
    "vehicle_type": "4WD / Wagon / Cab Chassis",
    "segment": "Upper Large 4WD",
    "years_sold_au": {"start": 1958, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The LandCruiser is the undisputed King of the Australian Outback. First brought to Australia in 1958 for the Snowy Mountains Scheme, it has conquered the country's most unforgiving deserts, pastoral stations, and mines for nearly seven decades.",
    "australian_market_notes": "Australia is the world's most demanding proving ground for the LandCruiser, absorbing over 10% of global production. The model split between the heavy-duty 70 Series workhorse and the comfort-oriented wagon bloodline (80, 100, 200, 300 Series) is unique in its enduring appeal to rural graziers, miners, and urban luxury buyers alike.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "40 Series",
            "generation_name": "LandCruiser 40 Series",
            "years": {"start": 1960, "end": 1984},
            "body_styles": ["SWB Soft-top", "SWB Hardtop (FJ40/BJ40)", "Troop Carrier (FJ45/HJ47)", "Cab Chassis (FJ45/HJ47)"],
            "platform": "Toyota J40",
            "ancap_rating": "Untested",
            "summary": "The pioneer that forged Toyota's indestructible Australian reputation, working the Snowy Mountains Scheme, outback cattle stations, and mining frontiers.",
            "engines": [
                {
                    "engine_code": "2F",
                    "name": "Toyota 2F 4.2L",
                    "displacement_cc": 4230,
                    "displacement_litres": 4.2,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 99.0,
                    "power_rpm": "3600",
                    "torque_nm": 271.0,
                    "torque_rpm": "1800",
                    "compression_ratio": "7.8:1",
                    "valvetrain": "OHV 12-valve",
                    "notes": "Low-revving iron-block tractor-like torque."
                },
                {
                    "engine_code": "2H",
                    "name": "Toyota 2H 4.0L Diesel",
                    "displacement_cc": 3980,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 77.0,
                    "power_rpm": "3500",
                    "torque_nm": 240.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "20.7:1",
                    "valvetrain": "OHV 12-valve",
                    "notes": "Legendary 6-cylinder diesel introduced in HJ47."
                }
            ],
            "badges": [
                {
                    "badge_name": "FJ40",
                    "years": {"start": 1960, "end": 1984},
                    "body_styles": ["SWB Hardtop"],
                    "drivetrain": "4WD",
                    "transmissions": ["3-speed manual", "4-speed manual"],
                    "msrp_aud_min": 3200,
                    "msrp_aud_max": 11500,
                    "fuel_consumption_l_100km": 16.5,
                    "kerb_weight_kg": 1550,
                    "standard_features": ["Dual-range 4WD", "Folding windscreen", "Removable hardtop", "Rear jump seats"],
                    "notes": "Short wheelbase off-road icon."
                },
                {
                    "badge_name": "HJ47",
                    "years": {"start": 1980, "end": 1984},
                    "body_styles": ["Troop Carrier", "Cab Chassis"],
                    "drivetrain": "4WD",
                    "transmissions": ["4-speed manual"],
                    "msrp_aud_min": 11200,
                    "msrp_aud_max": 14500,
                    "fuel_consumption_l_100km": 12.0,
                    "kerb_weight_kg": 1820,
                    "standard_features": ["2H diesel engine", "Long wheelbase", "Heavy duty dual leaf springs", "Dual fuel tanks on Troopy"],
                    "notes": "The ultimate outback bush workhorse."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HJ47",
                    "body_style": "Troop Carrier",
                    "engine_code": "2H",
                    "transmission": "4-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1980,
                    "years_end": 1984,
                    "msrp_aud": 12400,
                    "power_kw": 77.0,
                    "torque_nm": 240.0,
                    "fuel_l_100km": 12.0,
                    "towing_braked_kg": 2500,
                    "notes": "Outback 11-seat Bush Troopy."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "60 Series",
            "generation_name": "LandCruiser 60 Series",
            "years": {"start": 1980, "end": 1990},
            "body_styles": ["Station Wagon"],
            "platform": "Toyota J60",
            "ancap_rating": "Untested",
            "summary": "Bridged the gap between utilitarian toughness and family touring comfort, introducing the iconic Sahara luxury trim and 12H-T direct-injection turbo-diesel.",
            "engines": [
                {
                    "engine_code": "2H",
                    "name": "Toyota 2H 4.0L Diesel",
                    "displacement_cc": 3980,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Diesel",
                    "power_kw": 77.0,
                    "power_rpm": "3500",
                    "torque_nm": 240.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "20.7:1",
                    "valvetrain": "OHV 12-valve",
                    "notes": "Fitted to the legendary HJ60."
                },
                {
                    "engine_code": "12H-T",
                    "name": "Toyota 12H-T 4.0L Turbo-Diesel",
                    "displacement_cc": 3980,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 100.0,
                    "power_rpm": "3500",
                    "torque_nm": 315.0,
                    "torque_rpm": "1800",
                    "compression_ratio": "16.5:1",
                    "valvetrain": "OHV 12-valve",
                    "notes": "Direct injection turbo-diesel icon in the HJ61 Sahara."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sahara",
                    "years": {"start": 1985, "end": 1990},
                    "body_styles": ["Station Wagon"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 38000,
                    "msrp_aud_max": 54000,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 2080,
                    "standard_features": ["High roof design", "Velour upholstery", "Factory power sunroof", "Built-in center console fridge/ice-maker", "Air conditioning", "Power windows"],
                    "notes": "Pioneered luxury outback expedition touring in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Sahara",
                    "body_style": "Station Wagon",
                    "engine_code": "12H-T",
                    "transmission": "4-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 1986,
                    "years_end": 1990,
                    "msrp_aud": 48900,
                    "power_kw": 100.0,
                    "torque_nm": 315.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 2500,
                    "notes": "High-roof HJ61 Sahara Turbo."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "70 Series",
            "generation_name": "LandCruiser 70 Series",
            "years": {"start": 1984, "end": "Present"},
            "body_styles": ["Single Cab", "Double Cab", "Troop Carrier", "Wagon"],
            "platform": "Toyota J70",
            "ancap_rating": "5 Stars (Single Cab 2016)",
            "summary": "Heavy-duty commercial and touring legend in continuous production since 1984. Revered for live beam axles, separate chassis, and V8/2.8L turbo-diesel muscle.",
            "engines": [
                {
                    "engine_code": "1VD-FTV",
                    "name": "Toyota 1VD-FTV 4.5L V8 Turbo-Diesel",
                    "displacement_cc": 4461,
                    "displacement_litres": 4.5,
                    "cylinders": 8,
                    "configuration": "V8",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 151.0,
                    "power_rpm": "3400",
                    "torque_nm": 430.0,
                    "torque_rpm": "1200-3200",
                    "compression_ratio": "16.8:1",
                    "valvetrain": "DOHC 32-valve",
                    "notes": "Singular single-turbo V8 fitted from 2007 to 2024, celebrated for sound and torque."
                },
                {
                    "engine_code": "1GD-FTV",
                    "name": "Toyota 1GD-FTV 2.8L Turbo-Diesel",
                    "displacement_cc": 2755,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 150.0,
                    "power_rpm": "3400",
                    "torque_nm": 500.0,
                    "torque_rpm": "1600-2800",
                    "compression_ratio": "15.6:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Introduced in 2023 with 6-speed automatic transmission."
                }
            ],
            "badges": [
                {
                    "badge_name": "GXL",
                    "years": {"start": 2007, "end": "Present"},
                    "body_styles": ["Single Cab", "Double Cab", "Troop Carrier", "Wagon (76 Series)"],
                    "drivetrain": "Part-time 4WD",
                    "transmissions": ["5-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 63990,
                    "msrp_aud_max": 83500,
                    "fuel_consumption_l_100km": 10.7,
                    "kerb_weight_kg": 2240,
                    "standard_features": ["Front and rear factory differential locks", "Aluminium alloy wheels", "Snorkel", "Overfenders", "Power windows", "Cloth seats"],
                    "notes": "The grail outback touring specification."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GXL",
                    "body_style": "Double Cab",
                    "engine_code": "1VD-FTV",
                    "transmission": "5-speed manual",
                    "drivetrain": "Part-time 4WD",
                    "years_start": 2012,
                    "years_end": 2024,
                    "msrp_aud": 79200,
                    "power_kw": 151.0,
                    "torque_nm": 430.0,
                    "fuel_l_100km": 10.7,
                    "towing_braked_kg": 3500,
                    "notes": "VDJ79 Double Cab 4.5L V8 diesel."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "80 Series",
            "generation_name": "LandCruiser 80 Series",
            "years": {"start": 1990, "end": 1998},
            "body_styles": ["Station Wagon"],
            "platform": "Toyota J80",
            "ancap_rating": "Untested",
            "summary": "Coil spring all-around revolution with full-time 4WD, widely hailed as the most capable and durable all-around LandCruiser wagon ever engineered.",
            "engines": [
                {
                    "engine_code": "1HD-T",
                    "name": "Toyota 1HD-T 4.2L Turbo-Diesel",
                    "displacement_cc": 4164,
                    "displacement_litres": 4.2,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 123.0,
                    "power_rpm": "3600",
                    "torque_nm": 360.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "18.6:1",
                    "valvetrain": "SOHC 12-valve",
                    "notes": "Direct injection 4.2L turbo diesel cult favourite."
                },
                {
                    "engine_code": "1FZ-FE",
                    "name": "Toyota 1FZ-FE 4.5L Petrol",
                    "displacement_cc": 4477,
                    "displacement_litres": 4.5,
                    "cylinders": 6,
                    "configuration": "Inline-6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 158.0,
                    "power_rpm": "4600",
                    "torque_nm": 373.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Twin-cam multi-valve petrol inline-6 introduced in 1992."
                }
            ],
            "badges": [
                {
                    "badge_name": "GXL",
                    "years": {"start": 1990, "end": 1998},
                    "body_styles": ["Station Wagon"],
                    "drivetrain": "Full-time 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 43000,
                    "msrp_aud_max": 65000,
                    "fuel_consumption_l_100km": 12.2,
                    "kerb_weight_kg": 2220,
                    "standard_features": ["8-passenger seating", "Full-time 4WD with center diff lock", "Front/rear live coil axles", "Dual fuel tanks (145L total)"],
                    "notes": "Australia's outback touring standard for the 1990s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GXL",
                    "body_style": "Station Wagon",
                    "engine_code": "1HD-T",
                    "transmission": "4-speed automatic",
                    "drivetrain": "Full-time 4WD",
                    "years_start": 1990,
                    "years_end": 1995,
                    "msrp_aud": 59900,
                    "power_kw": 123.0,
                    "torque_nm": 360.0,
                    "fuel_l_100km": 12.2,
                    "towing_braked_kg": 3500,
                    "notes": "HDJ80 Turbo Diesel GXL."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "200 Series",
            "generation_name": "LandCruiser 200 Series",
            "years": {"start": 2007, "end": 2021},
            "body_styles": ["Station Wagon"],
            "platform": "Toyota J200",
            "ancap_rating": "5 Stars",
            "summary": "Pinnacle heavy-duty luxury tow vehicle, powered by the mighty 4.5L Twin-Turbo V8 diesel (1VD-FTV) with KDSS suspension and 3500kg towing.",
            "engines": [
                {
                    "engine_code": "1VD-FTV-TT",
                    "name": "Toyota 1VD-FTV 4.5L Twin-Turbo V8 Diesel",
                    "displacement_cc": 4461,
                    "displacement_litres": 4.5,
                    "cylinders": 8,
                    "configuration": "V8",
                    "aspiration": "Twin-Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 200.0,
                    "power_rpm": "3600",
                    "torque_nm": 650.0,
                    "torque_rpm": "1600-2600",
                    "compression_ratio": "16.8:1",
                    "valvetrain": "DOHC 32-valve",
                    "notes": "Twin-turbo V8 producing up to 200kW/650Nm; Australia's premier long-range towing engine."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sahara",
                    "years": {"start": 2007, "end": 2021},
                    "body_styles": ["Station Wagon"],
                    "drivetrain": "Full-time 4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 105000,
                    "msrp_aud_max": 131000,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 2740,
                    "standard_features": ["KDSS kinetic dynamic suspension", "Crawl Control and Multi-Terrain Select", "Refrigerated center cool box", "Rear seat DVD entertainment", "Premium leather upholstery", "Sunroof"],
                    "notes": "The ultimate Australian outback touring station wagon."
                },
                {
                    "badge_name": "GXL",
                    "years": {"start": 2007, "end": 2021},
                    "body_styles": ["Station Wagon"],
                    "drivetrain": "Full-time 4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 78000,
                    "msrp_aud_max": 92000,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 2680,
                    "standard_features": ["17-inch alloy wheels", "Dual fuel tanks (138L)", "Smart key entry/start", "8-passenger seating", "Reversing camera"],
                    "notes": "The high-volume choice for Australian caravaners."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Sahara",
                    "body_style": "Station Wagon",
                    "engine_code": "1VD-FTV-TT",
                    "transmission": "6-speed automatic",
                    "drivetrain": "Full-time 4WD",
                    "years_start": 2015,
                    "years_end": 2021,
                    "msrp_aud": 124500,
                    "power_kw": 200.0,
                    "torque_nm": 650.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 3500,
                    "notes": "Facelift 200 Series Sahara Twin Turbo V8."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "300 Series",
            "generation_name": "LandCruiser 300 Series",
            "years": {"start": 2021, "end": "Present"},
            "body_styles": ["Station Wagon"],
            "platform": "Toyota TNGA-F",
            "ancap_rating": "5 Stars",
            "summary": "Built on the all-new TNGA-F ladder architecture, shedding 200kg and powered by a 227kW/700Nm 3.3L Twin-Turbo V6 diesel paired with a 10-speed automatic.",
            "engines": [
                {
                    "engine_code": "F33A-FTV",
                    "name": "Toyota F33A-FTV 3.3L Twin-Turbo V6 Diesel",
                    "displacement_cc": 3346,
                    "displacement_litres": 3.3,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Twin-Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 227.0,
                    "power_rpm": "4000",
                    "torque_nm": 700.0,
                    "torque_rpm": "1600-2600",
                    "compression_ratio": "15.4:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Hot-V twin-turbo diesel producing 227kW and a massive 700Nm of torque."
                }
            ],
            "badges": [
                {
                    "badge_name": "GX",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["Station Wagon (5 seats)"],
                    "drivetrain": "Full-time 4WD",
                    "transmissions": ["10-speed automatic"],
                    "msrp_aud_min": 89990,
                    "msrp_aud_max": 96500,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 2495,
                    "standard_features": ["Vinyl floor", "Snorkel standard", "17-inch steel wheels", "Toyota Safety Sense", "Dual fuel tanks (110L total)"],
                    "notes": "Mining and fleet specification."
                },
                {
                    "badge_name": "Sahara",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["Station Wagon (7 seats)"],
                    "drivetrain": "Full-time 4WD",
                    "transmissions": ["10-speed automatic"],
                    "msrp_aud_min": 131190,
                    "msrp_aud_max": 135000,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 2630,
                    "standard_features": ["Heated and ventilated leather seats", "JBL 14-speaker audio", "Head-up display", "Power folding 3rd row", "Cool box"],
                    "notes": "Luxury long-distance touring flagship."
                },
                {
                    "badge_name": "GR Sport",
                    "years": {"start": 2021, "end": "Present"},
                    "body_styles": ["Station Wagon (5 seats)"],
                    "drivetrain": "Full-time 4WD",
                    "transmissions": ["10-speed automatic"],
                    "msrp_aud_min": 137790,
                    "msrp_aud_max": 143000,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 2630,
                    "standard_features": ["Electronic Kinetic Dynamic Suspension System (e-KDSS)", "Front and rear locking differentials", "Exclusive GR Dakar grille", "Matte grey 18-inch wheels", "Carbon-look interior trim"],
                    "notes": "Off-road capability flagship developed from Dakar Rally racing."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GR Sport",
                    "body_style": "Station Wagon",
                    "engine_code": "F33A-FTV",
                    "transmission": "10-speed automatic",
                    "drivetrain": "Full-time 4WD",
                    "years_start": 2021,
                    "years_end": "Present",
                    "msrp_aud": 141500,
                    "power_kw": 227.0,
                    "torque_nm": 700.0,
                    "fuel_l_100km": 8.9,
                    "towing_braked_kg": 3500,
                    "notes": "Top-tier off-road LC300."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

COROLLA_MODEL = {
    "make_slug": "toyota",
    "model_slug": "corolla",
    "name": "Corolla",
    "vehicle_type": "Hatchback / Sedan / Wagon",
    "segment": "Small Car",
    "years_sold_au": {"start": 1967, "end": "Present"},
    "locally_built": True,
    "assembly_plants_au": ["Port Melbourne, Victoria", "Duncans Road, Victoria", "Altona, Victoria"],
    "overview": "The Toyota Corolla is the world's most produced passenger car and an integral part of Australian life. Assembled locally in Victoria for over 30 years (1968-1999), it has provided dependable motoring for generations of Australians.",
    "australian_market_notes": "Australia was the first country outside Japan to assemble the Corolla, commencing at AMI Port Melbourne in July 1968 with the KE10. Local manufacture spanned KE20, KE30, KE55, KE70, AE82, AE92, AE102, and AE112. Under the Button Plan, it was built in Altona and shared with Holden as the Nova. In modern times, the Corolla transitioned to hybrid dominance, culminating in the 221kW GR Corolla AWD hot hatch.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "KE10",
            "generation_name": "Corolla 1st Generation",
            "years": {"start": 1967, "end": 1970},
            "body_styles": ["2-door Sedan", "4-door Sedan", "Station Wagon"],
            "platform": "Toyota E10",
            "ancap_rating": "Untested",
            "summary": "First generation Corolla; CKD assembly began at Port Melbourne in July 1968, initiating over 30 years of local Corolla manufacture.",
            "engines": [
                {
                    "engine_code": "K",
                    "name": "Toyota K 1.1L",
                    "displacement_cc": 1077,
                    "displacement_litres": 1.1,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 44.0,
                    "power_rpm": "6000",
                    "torque_nm": 83.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 8-valve",
                    "notes": "Pushrod 1.1-litre engine with 4-speed manual floor shift."
                }
            ],
            "badges": [
                {
                    "badge_name": "Deluxe",
                    "years": {"start": 1968, "end": 1970},
                    "body_styles": ["4-door Sedan", "Station Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual"],
                    "msrp_aud_min": 1780,
                    "msrp_aud_max": 1950,
                    "fuel_consumption_l_100km": 7.5,
                    "kerb_weight_kg": 730,
                    "standard_features": ["Heater/demister", "Floor shift manual", "Vinyl bucket seats", "Full wheel covers"],
                    "notes": "First locally assembled Toyota Corolla in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Deluxe",
                    "body_style": "4-door Sedan",
                    "engine_code": "K",
                    "transmission": "4-speed manual",
                    "drivetrain": "RWD",
                    "years_start": 1968,
                    "years_end": 1970,
                    "msrp_aud": 1820,
                    "power_kw": 44.0,
                    "torque_nm": 83.0,
                    "fuel_l_100km": 7.5,
                    "towing_braked_kg": 500,
                    "notes": "Historic Australian AMI Port Melbourne build."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "AE82/AE86",
            "generation_name": "Corolla 5th Generation",
            "years": {"start": 1985, "end": 1989},
            "body_styles": ["Hatchback", "Sedan", "Seca Liftback", "Sprinter Coupe (AE86)"],
            "platform": "Toyota E80",
            "ancap_rating": "Untested",
            "summary": "Pivotal generation featuring local production of the front-wheel-drive AE82 (with the legendary 4A-GE Twin Cam in Seca SX/GT) and the imported rear-wheel-drive AE86 Sprinter.",
            "engines": [
                {
                    "engine_code": "4A-GE",
                    "name": "Toyota 4A-GE 1.6L Twin Cam",
                    "displacement_cc": 1587,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 86.0,
                    "power_rpm": "6600",
                    "torque_nm": 137.0,
                    "torque_rpm": "5200",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "DOHC 16-valve T-VIS",
                    "notes": "Revered twin-cam engine revving to 7,500 rpm with T-VIS variable intake."
                },
                {
                    "engine_code": "4A-C",
                    "name": "Toyota 4A-C 1.6L SOHC",
                    "displacement_cc": 1587,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 58.0,
                    "power_rpm": "5200",
                    "torque_nm": 125.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Mainstream carburetted 1.6L workhorse in AE82 and Australian AE86 Sprinter."
                }
            ],
            "badges": [
                {
                    "badge_name": "Twin Cam (Seca SX)",
                    "years": {"start": 1986, "end": 1989},
                    "body_styles": ["Seca Liftback", "Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 16990,
                    "msrp_aud_max": 19500,
                    "fuel_consumption_l_100km": 7.8,
                    "kerb_weight_kg": 950,
                    "standard_features": ["4A-GE 16V engine", "4-wheel disc brakes", "Sports seats", "Rear spoiler", "Alloy wheels", "Tacho"],
                    "notes": "Australian hot hatch legend assembled in Victoria."
                },
                {
                    "badge_name": "Sprinter",
                    "years": {"start": 1983, "end": 1985},
                    "body_styles": ["Coupe (AE86)"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 9990,
                    "msrp_aud_max": 11500,
                    "fuel_consumption_l_100km": 8.0,
                    "kerb_weight_kg": 920,
                    "standard_features": ["Rear-wheel drive", "4A-C engine", "5-speed manual", "Sports bucket seats"],
                    "notes": "Imported RWD AE86 liftback, an enduring cult classic."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Twin Cam (Seca SX)",
                    "body_style": "Seca Liftback",
                    "engine_code": "4A-GE",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1986,
                    "years_end": 1989,
                    "msrp_aud": 17850,
                    "power_kw": 86.0,
                    "torque_nm": 137.0,
                    "fuel_l_100km": 7.8,
                    "towing_braked_kg": 900,
                    "notes": "AE82 Seca Twin Cam."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ZZE122",
            "generation_name": "Corolla 9th Generation",
            "years": {"start": 2001, "end": 2007},
            "body_styles": ["5-door Hatch", "4-door Sedan", "Station Wagon"],
            "platform": "Toyota E120",
            "ancap_rating": "4 Stars",
            "summary": "Imported from Japan and South Africa following the closure of local Corolla production, famous for the 141kW Sportivo with 2ZZ-GE VVTL-i engine.",
            "engines": [
                {
                    "engine_code": "1ZZ-FE",
                    "name": "Toyota 1ZZ-FE 1.8L VVT-i",
                    "displacement_cc": 1794,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 100.0,
                    "power_rpm": "6000",
                    "torque_nm": 171.0,
                    "torque_rpm": "4200",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve VVT-i",
                    "notes": "Standard engine across Ascent, Conquest, Levin, and Ultima."
                },
                {
                    "engine_code": "2ZZ-GE",
                    "name": "Toyota 2ZZ-GE 1.8L VVTL-i",
                    "displacement_cc": 1796,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 141.0,
                    "power_rpm": "7800",
                    "torque_nm": 180.0,
                    "torque_rpm": "6800",
                    "compression_ratio": "11.5:1",
                    "valvetrain": "DOHC 16-valve VVTL-i (Yamaha head)",
                    "notes": "High-revving Yamaha-designed head with variable valve timing and lift revving to 8,200 rpm."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sportivo",
                    "years": {"start": 2003, "end": 2006},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 29990,
                    "msrp_aud_max": 32990,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 1215,
                    "standard_features": ["2ZZ-GE 141kW engine", "6-speed manual", "Optitron instruments", "Leather sports seats", "Body kit and rear spoiler", "16-inch alloys"],
                    "notes": "Hot-hatch sleeper hitting lift at 6,200 rpm."
                },
                {
                    "badge_name": "Ascent",
                    "years": {"start": 2001, "end": 2007},
                    "body_styles": ["Hatchback", "Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 19990,
                    "msrp_aud_max": 24990,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1130,
                    "standard_features": ["Dual front airbags", "Air conditioning", "CD player", "Remote central locking"],
                    "notes": "The default private and fleet small car in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Sportivo",
                    "body_style": "5-door Hatch",
                    "engine_code": "2ZZ-GE",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2003,
                    "years_end": 2006,
                    "msrp_aud": 29990,
                    "power_kw": 141.0,
                    "torque_nm": 180.0,
                    "fuel_l_100km": 8.4,
                    "towing_braked_kg": 1000,
                    "notes": "ZZE122 Sportivo high-revving pocket rocket."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "E210",
            "generation_name": "Corolla 12th Generation",
            "years": {"start": 2018, "end": "Present"},
            "body_styles": ["Hatchback", "Sedan"],
            "platform": "Toyota TNGA-C",
            "ancap_rating": "5 Stars",
            "summary": "Built on the TNGA-C architecture with multi-link rear suspension, benchmark 4.0L/100km hybrid fuel economy, and the rally-bred GR Corolla AWD.",
            "engines": [
                {
                    "engine_code": "M20A-FKS",
                    "name": "Toyota Dynamic Force 2.0L",
                    "displacement_cc": 1987,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 125.0,
                    "power_rpm": "6600",
                    "torque_nm": 200.0,
                    "torque_rpm": "4400-4800",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve D-4S VVT-iE",
                    "notes": "High thermal efficiency 2.0L paired with direct-shift launch gear CVT."
                },
                {
                    "engine_code": "2ZR-FXE",
                    "name": "Toyota 1.8L Hybrid",
                    "displacement_cc": 1798,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Hybrid Petrol/Electric",
                    "power_kw": 103.0,
                    "power_rpm": "5200",
                    "torque_nm": 142.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve Atkinson cycle",
                    "notes": "Combined system power 103kW, delivering 4.0L/100km official consumption."
                },
                {
                    "engine_code": "G16E-GTS",
                    "name": "Toyota 1.6L Turbo 3-Cylinder (GR)",
                    "displacement_cc": 1618,
                    "displacement_litres": 1.6,
                    "cylinders": 3,
                    "configuration": "Inline-3",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Petrol",
                    "power_kw": 221.0,
                    "power_rpm": "6500",
                    "torque_nm": 370.0,
                    "torque_rpm": "3000-5550",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 12-valve Dual VVT-i",
                    "notes": "Powerhouse 3-cylinder turbo in the GR Corolla with GR-FOUR all-wheel drive."
                }
            ],
            "badges": [
                {
                    "badge_name": "Ascent Sport",
                    "years": {"start": 2018, "end": "Present"},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["10-speed CVT", "e-CVT (Hybrid)"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 33500,
                    "fuel_consumption_l_100km": 4.0,
                    "kerb_weight_kg": 1340,
                    "standard_features": ["Toyota Safety Sense (AEB with pedestrian/cyclist, adaptive cruise, lane trace)", "8-inch touchscreen", "Apple CarPlay/Android Auto", "16-inch alloy wheels"],
                    "notes": "Australia's top-selling retail compact hatchback."
                },
                {
                    "badge_name": "ZR",
                    "years": {"start": 2018, "end": "Present"},
                    "body_styles": ["Hatchback", "Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["e-CVT (Hybrid)", "10-speed CVT"],
                    "msrp_aud_min": 32990,
                    "msrp_aud_max": 39990,
                    "fuel_consumption_l_100km": 4.0,
                    "kerb_weight_kg": 1400,
                    "standard_features": ["18-inch alloys", "Heated sports bucket seats in suede/leather", "JBL 8-speaker audio", "Head-up display", "Wireless phone charging"],
                    "notes": "Flagship luxury specification."
                },
                {
                    "badge_name": "GR Corolla",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "AWD",
                    "transmissions": ["6-speed intelligent manual (iMT)"],
                    "msrp_aud_min": 62300,
                    "msrp_aud_max": 77800,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 1485,
                    "standard_features": ["221kW G16E-GTS engine", "GR-FOUR selectable AWD (60:40, 50:50, 30:70)", "Front and rear Torsen LSDs", "Triple exhaust outlets", "Wider track (+60mm front, +85mm rear)", "Alcon/GR brakes"],
                    "notes": "Rally-bred performance icon with manual transmission only."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Ascent Sport Hybrid",
                    "body_style": "Hatchback",
                    "engine_code": "2ZR-FXE",
                    "transmission": "e-CVT (Hybrid)",
                    "drivetrain": "FWD",
                    "years_start": 2018,
                    "years_end": "Present",
                    "msrp_aud": 29800,
                    "power_kw": 103.0,
                    "torque_nm": 142.0,
                    "fuel_l_100km": 4.0,
                    "towing_braked_kg": 450,
                    "notes": "Class-leading fuel economy."
                },
                {
                    "badge_name": "GR Corolla",
                    "body_style": "Hatchback",
                    "engine_code": "G16E-GTS",
                    "transmission": "6-speed intelligent manual (iMT)",
                    "drivetrain": "AWD",
                    "years_start": 2023,
                    "years_end": "Present",
                    "msrp_aud": 62300,
                    "power_kw": 221.0,
                    "torque_nm": 370.0,
                    "fuel_l_100km": 8.4,
                    "towing_braked_kg": 0,
                    "notes": "GR Corolla GTS GR-FOUR."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

CAMRY_MODEL = {
    "make_slug": "toyota",
    "model_slug": "camry",
    "name": "Camry",
    "vehicle_type": "Sedan / Wagon",
    "segment": "Mid-size Car",
    "years_sold_au": {"start": 1983, "end": "Present"},
    "locally_built": True,
    "assembly_plants_au": ["Port Melbourne, Victoria", "Altona, Victoria"],
    "overview": "The Toyota Camry was the cornerstone of Australian automotive manufacturing from 1987 to 2017. Built in Port Melbourne and Altona, it was Australia's favourite mid-size family and fleet sedan for over three decades.",
    "australian_market_notes": "Camry manufacturing commenced at Port Melbourne in 1987 (SV21) and moved to Altona in 1994. Under the Button Plan, it was badged as the Holden Apollo. In 2010, Altona launched Australia's very first locally produced hybrid car, the Camry Hybrid (AHV40). Altona was Toyota's global export hub for the Middle East, shipping hundreds of thousands of sedans. The final locally made Camry rolled off the Altona line on October 3, 2017.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "SV21",
            "generation_name": "Camry 2nd Generation (1st AU Build)",
            "years": {"start": 1987, "end": 1993},
            "body_styles": ["Sedan", "Station Wagon"],
            "platform": "Toyota V20",
            "ancap_rating": "Untested",
            "summary": "First Australian-manufactured Camry at Port Melbourne. Known for durability and fuel efficiency; also built for Holden as the Apollo.",
            "engines": [
                {
                    "engine_code": "3S-FE",
                    "name": "Toyota 3S-FE 2.0L",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 88.0,
                    "power_rpm": "5600",
                    "torque_nm": 171.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.3:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Legendary iron-block 3S-FE engine."
                }
            ],
            "badges": [
                {
                    "badge_name": "CSX",
                    "years": {"start": 1987, "end": 1993},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 17500,
                    "msrp_aud_max": 23500,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 1180,
                    "standard_features": ["Power steering", "Cloth trim", "Digital clock", "AM/FM radio cassette", "Split-folding rear seat"],
                    "notes": "Port Melbourne built family standard."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CSX",
                    "body_style": "Sedan",
                    "engine_code": "3S-FE",
                    "transmission": "4-speed auto",
                    "drivetrain": "FWD",
                    "years_start": 1987,
                    "years_end": 1993,
                    "msrp_aud": 19800,
                    "power_kw": 88.0,
                    "torque_nm": 171.0,
                    "fuel_l_100km": 8.8,
                    "towing_braked_kg": 1100,
                    "notes": "SV21 CSX Sedan."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "SXV20/MCV20",
            "generation_name": "Camry 4th Generation",
            "years": {"start": 1997, "end": 2002},
            "body_styles": ["Sedan", "Station Wagon"],
            "platform": "Toyota XV20",
            "ancap_rating": "3 Stars",
            "summary": "Manufactured at Altona with massive Middle East export contracts; offered in economical 2.2L 4-cylinder and silky 3.0L 1MZ-FE quad-cam V6.",
            "engines": [
                {
                    "engine_code": "5S-FE",
                    "name": "Toyota 5S-FE 2.2L",
                    "displacement_cc": 2164,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 94.0,
                    "power_rpm": "5200",
                    "torque_nm": 187.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Bulletproof 2.2L iron-block 4-cylinder."
                },
                {
                    "engine_code": "1MZ-FE",
                    "name": "Toyota 1MZ-FE 3.0L V6",
                    "displacement_cc": 2995,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 141.0,
                    "power_rpm": "5200",
                    "torque_nm": 279.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 24-valve",
                    "notes": "Smooth aluminum quad-cam V6."
                }
            ],
            "badges": [
                {
                    "badge_name": "Touring",
                    "years": {"start": 1997, "end": 2002},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 29990,
                    "msrp_aud_max": 35500,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 1390,
                    "standard_features": ["Sports suspension tune", "15-inch alloy wheels", "Rear wing spoiler", "Sports steering wheel", "Touring badging"],
                    "notes": "Australian-developed sports pack."
                },
                {
                    "badge_name": "CSi",
                    "years": {"start": 1997, "end": 2002},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 28990,
                    "fuel_consumption_l_100km": 9.0,
                    "kerb_weight_kg": 1350,
                    "standard_features": ["Driver airbag", "Air conditioning", "Power mirrors", "Remote central locking"],
                    "notes": "Fleet backbone across Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Touring V6",
                    "body_style": "Sedan",
                    "engine_code": "1MZ-FE",
                    "transmission": "4-speed auto",
                    "drivetrain": "FWD",
                    "years_start": 1999,
                    "years_end": 2002,
                    "msrp_aud": 34990,
                    "power_kw": 141.0,
                    "torque_nm": 279.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 1500,
                    "notes": "MCV20 Touring V6."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ACV40/AHV40",
            "generation_name": "Camry 6th Generation (Hybrid Pioneer)",
            "years": {"start": 2006, "end": 2011},
            "body_styles": ["Sedan"],
            "platform": "Toyota K platform",
            "ancap_rating": "4 to 5 Stars",
            "summary": "Built at Altona and groundbreaking for debuting Australia's very first locally manufactured hybrid passenger car in 2010 (Camry Hybrid AHV40).",
            "engines": [
                {
                    "engine_code": "2AZ-FE",
                    "name": "Toyota 2AZ-FE 2.4L VVT-i",
                    "displacement_cc": 2362,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 117.0,
                    "power_rpm": "5700",
                    "torque_nm": 218.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "9.8:1",
                    "valvetrain": "DOHC 16-valve VVT-i",
                    "notes": "Mainstream 2.4L engine in Altise, Ateva, and Sportivo."
                },
                {
                    "engine_code": "2AZ-FXE",
                    "name": "Toyota 2AZ-FXE 2.4L Hybrid",
                    "displacement_cc": 2362,
                    "displacement_litres": 2.4,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Hybrid Petrol/Electric",
                    "power_kw": 140.0,
                    "power_rpm": "6000",
                    "torque_nm": 187.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "12.5:1",
                    "valvetrain": "DOHC 16-valve Atkinson cycle",
                    "notes": "Australia's first locally built hybrid; combined system power 140kW, 6.0L/100km."
                }
            ],
            "badges": [
                {
                    "badge_name": "Hybrid",
                    "years": {"start": 2010, "end": 2011},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["e-CVT"],
                    "msrp_aud_min": 36990,
                    "msrp_aud_max": 39990,
                    "fuel_consumption_l_100km": 6.0,
                    "kerb_weight_kg": 1610,
                    "standard_features": ["Hybrid Synergy Drive", "Keyless smart entry and push button start", "Electronic stability control (VSC)", "Unique aero grille and clear tail lights", "Dual-zone climate control"],
                    "notes": "Australia's first locally built hybrid car."
                },
                {
                    "badge_name": "Altise",
                    "years": {"start": 2006, "end": 2011},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "5-speed automatic"],
                    "msrp_aud_min": 28000,
                    "msrp_aud_max": 32000,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 1450,
                    "standard_features": ["Cruise control", "Air conditioning", "Power windows", "ABS brakes"],
                    "notes": "Everyday Australian sedan."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Hybrid",
                    "body_style": "Sedan",
                    "engine_code": "2AZ-FXE",
                    "transmission": "e-CVT",
                    "drivetrain": "FWD",
                    "years_start": 2010,
                    "years_end": 2011,
                    "msrp_aud": 36990,
                    "power_kw": 140.0,
                    "torque_nm": 187.0,
                    "fuel_l_100km": 6.0,
                    "towing_braked_kg": 1200,
                    "notes": "Historic Altona-built Camry Hybrid."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "ASV50/AVV50",
            "generation_name": "Camry 7th Generation (Final AU Build)",
            "years": {"start": 2011, "end": 2017},
            "body_styles": ["Sedan"],
            "platform": "Toyota K platform",
            "ancap_rating": "5 Stars",
            "summary": "The final vehicle manufactured by Toyota in Australia at Altona, concluding 54 years of domestic vehicle assembly on October 3, 2017.",
            "engines": [
                {
                    "engine_code": "2AR-FE",
                    "name": "Toyota 2AR-FE 2.5L Dual VVT-i",
                    "displacement_cc": 2494,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 133.0,
                    "power_rpm": "6000",
                    "torque_nm": 231.0,
                    "torque_rpm": "4100",
                    "compression_ratio": "10.4:1",
                    "valvetrain": "DOHC 16-valve Dual VVT-i",
                    "notes": "Smooth, refined 2.5L with 6-speed automatic transmission (135kW in dual-exhaust Atara)."
                },
                {
                    "engine_code": "2AR-FXE",
                    "name": "Toyota 2AR-FXE 2.5L Hybrid",
                    "displacement_cc": 2494,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Hybrid Petrol/Electric",
                    "power_kw": 151.0,
                    "power_rpm": "5700",
                    "torque_nm": 213.0,
                    "torque_rpm": "4500",
                    "compression_ratio": "12.5:1",
                    "valvetrain": "DOHC 16-valve Atkinson cycle",
                    "notes": "Total system power 151kW with official fuel economy of 5.2L/100km."
                }
            ],
            "badges": [
                {
                    "badge_name": "Atara S",
                    "years": {"start": 2011, "end": 2017},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic", "e-CVT (Hybrid)"],
                    "msrp_aud_min": 33490,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 5.2,
                    "kerb_weight_kg": 1510,
                    "standard_features": ["17-inch alloy wheels", "Paddle shifters", "Smart entry and start", "Reversing camera", "Dual exhaust", "Touchscreen audio"],
                    "notes": "Popular mid-spec private and business sedan."
                },
                {
                    "badge_name": "Atara SL",
                    "years": {"start": 2011, "end": 2017},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed automatic", "e-CVT (Hybrid)"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 44440,
                    "fuel_consumption_l_100km": 5.2,
                    "kerb_weight_kg": 1540,
                    "standard_features": ["Leather upholstery", "JBL 10-speaker premium audio", "Blind spot monitor", "Rear cross traffic alert", "Satellite navigation", "Power rear sunshade"],
                    "notes": "Luxury specification."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Atara S Hybrid",
                    "body_style": "Sedan",
                    "engine_code": "2AR-FXE",
                    "transmission": "e-CVT",
                    "drivetrain": "FWD",
                    "years_start": 2011,
                    "years_end": 2017,
                    "msrp_aud": 35990,
                    "power_kw": 151.0,
                    "torque_nm": 213.0,
                    "fuel_l_100km": 5.2,
                    "towing_braked_kg": 1200,
                    "notes": "Final Australian manufactured Camry series."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "AXVH70/GSV70",
            "generation_name": "Camry 8th Generation",
            "years": {"start": 2017, "end": 2024},
            "body_styles": ["Sedan"],
            "platform": "Toyota TNGA-K",
            "ancap_rating": "5 Stars",
            "summary": "Imported from Japan on the TNGA-K platform, offering dynamic multi-link rear handling, 224kW V6 power, and class-leading 4.2L/100km hybrid economy.",
            "engines": [
                {
                    "engine_code": "A25A-FXS",
                    "name": "Toyota Dynamic Force 2.5L Hybrid",
                    "displacement_cc": 2487,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Hybrid Petrol/Electric",
                    "power_kw": 160.0,
                    "power_rpm": "5700",
                    "torque_nm": 221.0,
                    "torque_rpm": "3600-5200",
                    "compression_ratio": "14.0:1",
                    "valvetrain": "DOHC 16-valve VVT-iE",
                    "notes": "Class-leading 41% thermal efficiency, 160kW combined system output."
                },
                {
                    "engine_code": "2GR-FKS",
                    "name": "Toyota 2GR-FKS 3.5L V6",
                    "displacement_cc": 3456,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V6",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 224.0,
                    "power_rpm": "6600",
                    "torque_nm": 362.0,
                    "torque_rpm": "4700",
                    "compression_ratio": "11.8:1",
                    "valvetrain": "DOHC 24-valve D-4S Dual VVT-i",
                    "notes": "224kW high-performance V6 paired with 8-speed automatic (SX and SL grades)."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX",
                    "years": {"start": 2017, "end": 2024},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["8-speed automatic (V6)", "e-CVT (Hybrid)"],
                    "msrp_aud_min": 35990,
                    "msrp_aud_max": 43590,
                    "fuel_consumption_l_100km": 4.5,
                    "kerb_weight_kg": 1595,
                    "standard_features": ["19-inch black alloy wheels", "Sports body kit and rear spoiler", "Sports suspension tune", "Paddle shifters", "High-gloss black grille"],
                    "notes": "Aggressive sports sedan trim."
                },
                {
                    "badge_name": "Ascent",
                    "years": {"start": 2017, "end": 2024},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["e-CVT (Hybrid)", "8-speed automatic"],
                    "msrp_aud_min": 27690,
                    "msrp_aud_max": 34990,
                    "fuel_consumption_l_100km": 4.2,
                    "kerb_weight_kg": 1530,
                    "standard_features": ["Toyota Safety Sense suite", "7-inch touchscreen", "LED headlights", "Digital instrument display"],
                    "notes": "Australia's top rideshare and fleet vehicle."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Ascent Hybrid",
                    "body_style": "Sedan",
                    "engine_code": "A25A-FXS",
                    "transmission": "e-CVT",
                    "drivetrain": "FWD",
                    "years_start": 2017,
                    "years_end": 2024,
                    "msrp_aud": 33490,
                    "power_kw": 160.0,
                    "torque_nm": 221.0,
                    "fuel_l_100km": 4.2,
                    "towing_braked_kg": 400,
                    "notes": "Australia's high-efficiency rideshare favourite."
                },
                {
                    "badge_name": "SX V6",
                    "body_style": "Sedan",
                    "engine_code": "2GR-FKS",
                    "transmission": "8-speed automatic",
                    "drivetrain": "FWD",
                    "years_start": 2017,
                    "years_end": 2021,
                    "msrp_aud": 37290,
                    "power_kw": 224.0,
                    "torque_nm": 362.0,
                    "fuel_l_100km": 8.7,
                    "towing_braked_kg": 1600,
                    "notes": "224kW performance V6 sedan."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

RAV4_MODEL = {
    "make_slug": "toyota",
    "model_slug": "rav4",
    "name": "RAV4",
    "vehicle_type": "SUV",
    "segment": "Medium SUV",
    "years_sold_au": {"start": 1994, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Toyota RAV4 created the compact car-based recreational SUV category in 1994. Across five generations, it grew into Australia's favourite SUV, with the XA50 Hybrid triggering unprecedented multi-month waitlists.",
    "australian_market_notes": "Launched in Australia in 1994 as a quirky 3-door with Celica underpinnings, the RAV4 revolutionized Australian motoring by providing high ride height without the truck-like penalties of traditional body-on-frame 4WDs. The introduction of the XA50 Hybrid in 2019 transformed it into Australia's best-selling SUV outright.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "XA10",
            "generation_name": "RAV4 1st Generation",
            "years": {"start": 1994, "end": 2000},
            "body_styles": ["3-door SUV", "5-door SUV"],
            "platform": "Toyota XA10",
            "ancap_rating": "Untested",
            "summary": "Pioneered the monocoque lifestyle SUV market in Australia in 1994, blending car comfort, quirky styling, and permanent all-wheel drive.",
            "engines": [
                {
                    "engine_code": "3S-FE",
                    "name": "Toyota 3S-FE 2.0L",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 89.0,
                    "power_rpm": "5400",
                    "torque_nm": 176.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Shared with the Celica and Camry."
                }
            ],
            "badges": [
                {
                    "badge_name": "Cruiser",
                    "years": {"start": 1994, "end": 2000},
                    "body_styles": ["3-door SUV", "5-door SUV"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed manual", "4-speed auto"],
                    "msrp_aud_min": 28990,
                    "msrp_aud_max": 35500,
                    "fuel_consumption_l_100km": 9.4,
                    "kerb_weight_kg": 1220,
                    "standard_features": ["Dual sunroofs on 3-door", "16-inch alloy wheels", "Power windows and mirrors", "Center locking differential"],
                    "notes": "Pioneered beach and urban lifestyle crossover driving."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Cruiser 5-Door",
                    "body_style": "5-door SUV",
                    "engine_code": "3S-FE",
                    "transmission": "5-speed manual",
                    "drivetrain": "AWD",
                    "years_start": 1995,
                    "years_end": 2000,
                    "msrp_aud": 32900,
                    "power_kw": 89.0,
                    "torque_nm": 176.0,
                    "fuel_l_100km": 9.2,
                    "towing_braked_kg": 1500,
                    "notes": "Classic 1st-gen 5-door RAV4."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "XA50",
            "generation_name": "RAV4 5th Generation",
            "years": {"start": 2019, "end": "Present"},
            "body_styles": ["5-door SUV"],
            "platform": "Toyota TNGA-K",
            "ancap_rating": "5 Stars",
            "summary": "Built on TNGA-K, this generation became Australia's best-selling SUV and repeatedly the country's #1 selling passenger vehicle outright led by high-demand Hybrid e-Four variants.",
            "engines": [
                {
                    "engine_code": "A25A-FXS",
                    "name": "Toyota Dynamic Force 2.5L Hybrid",
                    "displacement_cc": 2487,
                    "displacement_litres": 2.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Hybrid Petrol/Electric",
                    "power_kw": 163.0,
                    "power_rpm": "5700",
                    "torque_nm": 221.0,
                    "torque_rpm": "3600-5200",
                    "compression_ratio": "14.0:1",
                    "valvetrain": "DOHC 16-valve VVT-iE",
                    "notes": "160kW in 2WD and 163kW with electric rear axle E-Four AWD; 4.7L/100km."
                },
                {
                    "engine_code": "M20A-FKS",
                    "name": "Toyota Dynamic Force 2.0L Petrol",
                    "displacement_cc": 1987,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 127.0,
                    "power_rpm": "6600",
                    "torque_nm": 203.0,
                    "torque_rpm": "4400-4900",
                    "compression_ratio": "13.0:1",
                    "valvetrain": "DOHC 16-valve D-4S",
                    "notes": "2WD entry-level petrol engine paired with 10-speed direct shift CVT."
                }
            ],
            "badges": [
                {
                    "badge_name": "GX",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "2WD or AWD",
                    "transmissions": ["10-speed CVT", "e-CVT (Hybrid)"],
                    "msrp_aud_min": 30640,
                    "msrp_aud_max": 42500,
                    "fuel_consumption_l_100km": 4.7,
                    "kerb_weight_kg": 1600,
                    "standard_features": ["Toyota Safety Sense (AEB, Lane Trace, Adaptive Cruise, Speed Sign Recognition)", "8-inch touchscreen with Apple CarPlay/Android Auto", "LED headlights", "17-inch alloy wheels"],
                    "notes": "Entry specification."
                },
                {
                    "badge_name": "Cruiser",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "2WD or AWD",
                    "transmissions": ["e-CVT (Hybrid)", "10-speed CVT"],
                    "msrp_aud_min": 39140,
                    "msrp_aud_max": 48750,
                    "fuel_consumption_l_100km": 4.8,
                    "kerb_weight_kg": 1690,
                    "standard_features": ["Leather accented heated/ventilated seats", "JBL 9-speaker audio", "Tilt-and-slide moonroof", "Power tailgate", "18-inch chrome alloys", "360-degree panoramic camera"],
                    "notes": "Australia's most sought-after hybrid family SUV."
                },
                {
                    "badge_name": "Edge",
                    "years": {"start": 2019, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "Mechanical AWD or e-Four",
                    "transmissions": ["8-speed automatic", "e-CVT (Hybrid)"],
                    "msrp_aud_min": 47140,
                    "msrp_aud_max": 56650,
                    "fuel_consumption_l_100km": 4.8,
                    "kerb_weight_kg": 1740,
                    "standard_features": ["Rugged off-road body styling and grille", "19-inch matte alloys", "SofTex water-resistant seats with orange accents", "Multi-Terrain Select with Mud & Sand/Rock & Dirt modes", "Torque-vectoring AWD"],
                    "notes": "Adventure-focused flagship grade."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Cruiser Hybrid e-Four",
                    "body_style": "5-door SUV",
                    "engine_code": "A25A-FXS",
                    "transmission": "e-CVT (Hybrid)",
                    "drivetrain": "AWD",
                    "years_start": 2019,
                    "years_end": "Present",
                    "msrp_aud": 48750,
                    "power_kw": 163.0,
                    "torque_nm": 221.0,
                    "fuel_l_100km": 4.8,
                    "towing_braked_kg": 1500,
                    "notes": "The defining Australian family crossover of the 2020s."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

TOYOTA_DEEP_DIVES = [HILUX_MODEL, LANDCRUISER_MODEL, COROLLA_MODEL, CAMRY_MODEL, RAV4_MODEL]
