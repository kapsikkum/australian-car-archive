"""
Deep-dive model data for Holden Monaro, Statesman/Caprice, Gemini, and Colorado.
"""
from typing import Any, Dict

MONARO_DATA: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "monaro",
    "name": "Holden Monaro",
    "vehicle_type": "Coupe / Sedan",
    "segment": "Sports / Muscle Car",
    "years_sold_au": {"start": 1968, "end": 2006},
    "locally_built": True,
    "assembly_plants_au": [
        "Fishermans Bend, Victoria",
        "Dandenong, Victoria",
        "Elizabeth, South Australia",
        "Pagewood, New South Wales"
    ],
    "overview": "The Holden Monaro is Australia's most revered two-door muscle car and grand tourer. Introduced in July 1968 with the HK series, the pillarless hardtop coupe captured national imagination by winning the 1968 Bathurst 500 on debut with Bruce McPhee and Barry Mulholland in a GTS 327, followed by Colin Bond's win in the 1969 HT GTS 350. Resurrected thirty-three years later following a sensational reception as the 'Coupe 22' concept at the 1998 Sydney Motor Show, the modern V2 and VZ Monaro CV8 captivated enthusiasts globally and was exported to North America as the Pontiac GTO and the UK as the Vauxhall Monaro.",
    "australian_market_notes": "The original HK Monaro was styled under GM-H design chief Joe Schemansky and project designer John Schinella, featuring sweeping Coke-bottle rear hips, a dramatic semi-fastback roofline, and imported Chevrolet 327ci and 350ci small-block V8s. The HQ series brought softer, more organic proportions, offering the GTS 350 and introducing the 4-door GTS sedan in 1973. The modern rebirth engineered by Mike Simcoe in 2001 (V2/VZ) utilized the VT/VX Commodore platform, packing the 5.7L LS1 V8 and supercharged V6, before culminating in the twin-hood-scoop 2005 CV8-Z.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "HK-HG",
            "generation_name": "First Generation (HK, HT, HG)",
            "years": {"start": 1968, "end": 1971},
            "body_styles": ["2-door hardtop coupe"],
            "platform": "GM-H full-size hardtop",
            "ancap_rating": None,
            "summary": "Original pillarless hardtop coupe. 1968 Wheels Car of the Year, winner of the 1968 Bathurst 500 (GTS 327) and 1969 Bathurst 500 (GTS 350).",
            "engines": [
                {
                    "engine_code": "Chevy-327-V8",
                    "name": "Chevrolet 327ci (5.4L) Small-Block V8 (GTS 327)",
                    "displacement_cc": 5354,
                    "displacement_litres": 5.4,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 186.0,
                    "power_rpm": "4800",
                    "torque_nm": 434.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "8.75:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Rochester 4-barrel carburettor; 1968 Bathurst winner."
                },
                {
                    "engine_code": "Chevy-350-V8",
                    "name": "Chevrolet 350ci (5.7L) Small-Block V8 (GTS 350)",
                    "displacement_cc": 5733,
                    "displacement_litres": 5.7,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 224.0,
                    "power_rpm": "4800",
                    "torque_nm": 515.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "10.25:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Rochester 4-barrel Quadrajet; 1969 Bathurst winner."
                }
            ],
            "badges": [
                {
                    "badge_name": "Monaro GTS 327",
                    "years": {"start": 1968, "end": 1969},
                    "body_styles": ["2-door hardtop"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual (Saginaw)"],
                    "msrp_aud_min": 3790,
                    "msrp_aud_max": 4200,
                    "fuel_consumption_l_100km": 16.5,
                    "kerb_weight_kg": 1420,
                    "standard_features": ["327ci V8", "Tachometer on center console", "Power front disc brakes", "Limited slip differential", "GTS racing stripes"],
                    "notes": "Winner of the 1968 Bathurst 500."
                },
                {
                    "badge_name": "Monaro GTS 350",
                    "years": {"start": 1969, "end": 1971},
                    "body_styles": ["2-door hardtop"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual (Muncie)", "Powerglide / TH350 auto"],
                    "msrp_aud_min": 3995,
                    "msrp_aud_max": 4500,
                    "fuel_consumption_l_100km": 17.0,
                    "kerb_weight_kg": 1445,
                    "standard_features": ["350ci V8 (300 hp)", "Heavy-duty suspension", "Twin bonnet scoops", "Rally wheels", "Front disc brakes"],
                    "notes": "Bathurst 1969 winner; ultimate first-generation Monaro."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Monaro GTS 350",
                    "body_style": "2-door hardtop",
                    "engine_code": "Chevy-350-V8",
                    "transmission": "4-speed manual (Muncie)",
                    "drivetrain": "RWD",
                    "msrp_aud": 4150,
                    "power_kw": 224.0,
                    "torque_nm": 515.0,
                    "fuel_l_100km": 17.0,
                    "towing_braked_kg": 1400,
                    "notes": "0-100 km/h in 7.0s; 215 km/h top speed."
                }
            ]
        },
        {
            "series_code": "V2-VZ",
            "generation_name": "Third Generation (V2 & VZ)",
            "years": {"start": 2001, "end": 2006},
            "body_styles": ["2-door coupe"],
            "platform": "GM V-body (VT/VX coupe architecture)",
            "ancap_rating": None,
            "summary": "Modern rebirth designed by Mike Simcoe. Powered by the 5.7L LS1 V8 and supercharged V6, exported to the US as the Pontiac GTO and the UK as the Vauxhall Monaro.",
            "engines": [
                {
                    "engine_code": "LS1-Gen-III-5.7",
                    "name": "Chevrolet Gen III LS1 5.7L V8 (CV8)",
                    "displacement_cc": 5665,
                    "displacement_litres": 5.7,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Premium Unleaded)",
                    "power_kw": 260.0,
                    "power_rpm": "5600",
                    "torque_nm": 500.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.1:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Twin dual exhaust with throaty burble; 260kW in VZ."
                }
            ],
            "badges": [
                {
                    "badge_name": "CV8",
                    "years": {"start": 2001, "end": 2005},
                    "body_styles": ["2-door coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (Tremec T56)", "4-speed automatic (4L60-E)"],
                    "msrp_aud_min": 56990,
                    "msrp_aud_max": 62500,
                    "fuel_consumption_l_100km": 13.0,
                    "kerb_weight_kg": 1640,
                    "standard_features": ["5.7L LS1 V8", "Leather sports seats", "18-inch 5-spoke alloys", "Climate control", "10-speaker audio with 6-disc CD"],
                    "notes": "Modern grand-touring masterpiece."
                },
                {
                    "badge_name": "CV8-Z",
                    "years": {"start": 2005, "end": 2006},
                    "body_styles": ["2-door coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual (T56)", "4-speed automatic (4L65-E)"],
                    "msrp_aud_min": 60490,
                    "msrp_aud_max": 65000,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 1675,
                    "standard_features": ["260kW LS1 V8", "Twin functional bonnet scoops", "Sunroof", "Modified rear fascia with twin exhaust", "Signature Fusion orange paint option"],
                    "notes": "Final edition limited production send-off."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CV8-Z",
                    "body_style": "2-door coupe",
                    "engine_code": "LS1-Gen-III-5.7",
                    "transmission": "6-speed manual (Tremec T56)",
                    "drivetrain": "RWD",
                    "msrp_aud": 60490,
                    "power_kw": 260.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 13.5,
                    "towing_braked_kg": 1600,
                    "notes": "0-100 km/h in 5.6s; modern collector icon."
                }
            ]
        }
    ]
}

STATESMAN_CAPRICE_DATA: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "statesman-caprice",
    "name": "Holden Statesman / Caprice",
    "vehicle_type": "Sedan",
    "segment": "Upper Luxury / Limousine",
    "years_sold_au": {"start": 1971, "end": 2017},
    "locally_built": True,
    "assembly_plants_au": [
        "Fishermans Bend, Victoria",
        "Dandenong, Victoria",
        "Elizabeth, South Australia",
        "Acacia Ridge, Queensland"
    ],
    "overview": "The Holden Statesman and Caprice was Australia's presidential luxury flagship for nearly five decades. Conceived to challenge the Ford Fairlane and LTD, the Statesman rode on an extended 114-inch to 118-inch wheelbase providing unmatched rear legroom. Serving as official transport for Australian prime ministers, diplomats, business executives, and luxury hire car fleets, the Statesman and Caprice evolved from the ornate HQ-WB models to the modern IRS-equipped VQ-WL series and the billion-dollar Zeta-platform WM and WN. Exported globally as the Chevrolet Caprice, Buick Park Avenue, and US Police Pursuit Vehicle (PPV).",
    "australian_market_notes": "Originally marketed without the Holden nameplate simply as 'Statesman' in the HQ series, it featured formal roofline styling and standard V8 power. The 1990 VQ was a watershed car, introducing the first independent rear suspension (IRS) in a production Holden. The 2006 WM series was engineered on GM's global Zeta platform, offering extraordinary torsional rigidity and cavernous comfort. In 2015, the WN Series II Caprice V adopted the 304kW 6.2L LS3 V8.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "HQ-WB",
            "generation_name": "HQ-WB Series",
            "years": {"start": 1971, "end": 1985},
            "body_styles": ["4-door long-wheelbase sedan"],
            "platform": "GM-H LWB perimeter chassis",
            "ancap_rating": None,
            "summary": "Extended 114-inch wheelbase luxury cruiser. Statesman Custom, de Ville, and Caprice trims with 308ci V8 and plush velour/leather.",
            "engines": [
                {
                    "engine_code": "Holden-308-V8-Statesman",
                    "name": "Holden 308ci (5.0L) Red/Blue V8",
                    "displacement_cc": 5044,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 179.0,
                    "power_rpm": "4800",
                    "torque_nm": 427.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Standard in Caprice."
                }
            ],
            "badges": [
                {
                    "badge_name": "Caprice",
                    "years": {"start": 1974, "end": 1985},
                    "body_styles": ["4-door long-wheelbase sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["Turbo Hydra-Matic 400 3-speed automatic"],
                    "msrp_aud_min": 7950,
                    "msrp_aud_max": 18500,
                    "fuel_consumption_l_100km": 16.5,
                    "kerb_weight_kg": 1580,
                    "standard_features": ["308ci V8", "Integrated air conditioning", "Power windows", "Leather or crushed velour seating", "Radial Tuned Suspension (HZ/WB)"],
                    "notes": "Australia's premier domestic luxury limousine."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Caprice",
                    "body_style": "4-door long-wheelbase sedan",
                    "engine_code": "Holden-308-V8-Statesman",
                    "transmission": "Turbo Hydra-Matic 400 3-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 8450,
                    "power_kw": 179.0,
                    "torque_nm": 427.0,
                    "fuel_l_100km": 16.5,
                    "towing_braked_kg": 1800,
                    "notes": "VIP ministerial transportation."
                }
            ]
        },
        {
            "series_code": "WM-WN",
            "generation_name": "WM & WN Series",
            "years": {"start": 2006, "end": 2017},
            "body_styles": ["4-door long-wheelbase sedan"],
            "platform": "GM Zeta LWB platform",
            "ancap_rating": "5 Stars",
            "summary": "Billion-dollar Zeta platform limousine with 6.0L L98/L77 and 6.2L LS3 V8. Supplied to the US as the Chevrolet Caprice PPV police interceptor.",
            "engines": [
                {
                    "engine_code": "Gen-IV-LS3-Caprice",
                    "name": "Chevrolet 6.2L LS3 V8 (WN Series II)",
                    "displacement_cc": 6162,
                    "displacement_litres": 6.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 304.0,
                    "power_rpm": "6000",
                    "torque_nm": 570.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "10.7:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Fitted to final Caprice V; 0-100 km/h in 5.1 seconds."
                }
            ],
            "badges": [
                {
                    "badge_name": "Caprice V",
                    "years": {"start": 2013, "end": 2017},
                    "body_styles": ["4-door long-wheelbase sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed automatic (6L80-E)"],
                    "msrp_aud_min": 60490,
                    "msrp_aud_max": 65000,
                    "fuel_consumption_l_100km": 12.9,
                    "kerb_weight_kg": 1851,
                    "standard_features": ["304kW LS3 6.2L V8", "Rear seat dual DVD screens", "Bose premium audio", "Head-Up Display", "Forward Collision Alert", "Leather heated memory seats"],
                    "notes": "Australia's ultimate executive transport."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Caprice V",
                    "body_style": "4-door long-wheelbase sedan",
                    "engine_code": "Gen-IV-LS3-Caprice",
                    "transmission": "6-speed automatic (6L80-E)",
                    "drivetrain": "RWD",
                    "msrp_aud": 61490,
                    "power_kw": 304.0,
                    "torque_nm": 570.0,
                    "fuel_l_100km": 12.9,
                    "towing_braked_kg": 2100,
                    "notes": "Final Australian factory limousine."
                }
            ]
        }
    ]
}

GEMINI_DATA: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "gemini",
    "name": "Holden Gemini",
    "vehicle_type": "Sedan / Coupe / Wagon / Van",
    "segment": "Small",
    "years_sold_au": {"start": 1975, "end": 1987},
    "locally_built": True,
    "assembly_plants_au": [
        "Acacia Ridge, Queensland",
        "Pagewood, New South Wales"
    ],
    "overview": "The Holden Gemini was Australia's best-selling four-cylinder car of the 1970s and early 1980s. Developed from GM's global T-car platform (shared with the Opel Kadett C, Isuzu Bellett Gemini, and Chevrolet Chevette), the Gemini won the prestigious 1975 Wheels Car of the Year award on debut. Over 226,000 units were produced across TX, TC, TD, TE, TF, and TG rear-wheel-drive series before transitioning to the front-wheel-drive RB series.",
    "australian_market_notes": "Built primarily at Holden's Acacia Ridge assembly plant in Brisbane, Queensland, the Gemini was powered by Isuzu's robust chain-driven 1.6-litre G161Z SOHC cross-flow four-cylinder engine. In 1978, the TD series introduced Holden's Radial Tuned Suspension (RTS), transforming handling. The 1979 TE introduced an Isuzu 1.8-litre diesel option capable of under 5.0 L/100km, while the final TG series spawned the collector-grade ZZ/Z sporting edition.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "TX-TG",
            "generation_name": "RWD Gemini (TX, TC, TD, TE, TF, TG)",
            "years": {"start": 1975, "end": 1985},
            "body_styles": ["4-door sedan", "2-door coupe", "3-door station wagon", "3-door panel van"],
            "platform": "GM T-car (RWD)",
            "ancap_rating": None,
            "summary": "1975 Wheels Car of the Year winner; Isuzu 1.6L G161Z SOHC engine, RTS suspension on TD, diesel option on TE, and TG ZZ/Z sporting edition.",
            "engines": [
                {
                    "engine_code": "Isuzu-G161Z",
                    "name": "Isuzu G161Z 1.6L SOHC 4-Cylinder",
                    "displacement_cc": 1584,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 50.0,
                    "power_rpm": "5400",
                    "torque_nm": 111.0,
                    "torque_rpm": "3400",
                    "compression_ratio": "8.7:1",
                    "valvetrain": "SOHC 8V crossflow",
                    "notes": "Nikki 2-barrel downdraft carburettor."
                }
            ],
            "badges": [
                {
                    "badge_name": "SL",
                    "years": {"start": 1975, "end": 1985},
                    "body_styles": ["4-door sedan", "2-door coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual", "5-speed manual", "Tri-Matic 3-speed auto"],
                    "msrp_aud_min": 3290,
                    "msrp_aud_max": 7200,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 935,
                    "standard_features": ["Front disc brakes", "Cloth seating", "Flow-through ventilation", "Reclining bucket seats"],
                    "notes": "Bestselling small car in Australia."
                },
                {
                    "badge_name": "ZZ/Z",
                    "years": {"start": 1983, "end": 1984},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 8500,
                    "msrp_aud_max": 9200,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 965,
                    "standard_features": ["Sports alloy wheels", "Front air dam", "Rear deck spoiler", "Sports steering wheel", "Special silver decals"],
                    "notes": "Final sporting edition of the RWD Gemini; 1,000 units produced."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SL",
                    "body_style": "4-door sedan",
                    "engine_code": "Isuzu-G161Z",
                    "transmission": "4-speed manual",
                    "drivetrain": "RWD",
                    "msrp_aud": 3450,
                    "power_kw": 50.0,
                    "torque_nm": 111.0,
                    "fuel_l_100km": 8.4,
                    "towing_braked_kg": 800,
                    "notes": "Light, economical, and agile."
                }
            ]
        }
    ]
}

COLORADO_DATA: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "colorado",
    "name": "Holden Colorado",
    "vehicle_type": "Ute / Cab Chassis",
    "segment": "Light Commercial / Mid-size Pick-up",
    "years_sold_au": {"start": 2008, "end": 2020},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Holden Colorado was Holden's rugged 4x4 and 4x2 dual-cab, space-cab, and single-cab workhorse pick-up, replacing the legendary Rodeo in 2008. Across the RC and RG generations, the Colorado delivered class-leading 3.5-tonne braked towing capacity and up to 500Nm of torque from its Duramax 2.8L turbo-diesel engine. In 2016, Holden's engineering team at Lang Lang conducted a massive Australian-specific chassis, steering, and powertrain calibration that transformed refinement and dynamics.",
    "australian_market_notes": "The RC generation was built in Rayong, Thailand alongside the Isuzu D-Max, powered by the bulletproof 3.0L Isuzu 4JJ1-TC turbo-diesel and Holden's Australian-built 3.6L Alloytec V6. The RG series (launched in 2012 on GM's global mid-size truck platform) introduced the potent 2.8L Duramax diesel. The 2016 RG Series II introduced a Centrifugal Pendulum Absorber (CPA) torque converter—a first in the dual-cab ute segment—damping engine vibrations and enabling earlier torque converter lock-up. Range topped by the Z71 and HSV SportsCat.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "RG",
            "generation_name": "Colorado RG Series",
            "years": {"start": 2012, "end": 2020},
            "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
            "platform": "GM Global TKI truck architecture",
            "ancap_rating": "5 Stars",
            "summary": "Global GM ladder-frame platform with 2.8L Duramax turbo-diesel delivering 500Nm and 3,500kg braked towing. Comprehensive Australian suspension and steering redesign in 2016.",
            "engines": [
                {
                    "engine_code": "Duramax-2.8-LWN",
                    "name": "Duramax 2.8L Common-Rail Turbo-Diesel",
                    "displacement_cc": 2776,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 147.0,
                    "power_rpm": "3600",
                    "torque_nm": 500.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "16.5:1",
                    "valvetrain": "DOHC 16V Variable Geometry Turbo",
                    "notes": "500Nm with 6-speed auto (440Nm with 6-speed manual); CPA torque converter."
                }
            ],
            "badges": [
                {
                    "badge_name": "LTZ",
                    "years": {"start": 2012, "end": 2020},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 48990,
                    "msrp_aud_max": 54990,
                    "fuel_consumption_l_100km": 8.7,
                    "kerb_weight_kg": 2100,
                    "standard_features": ["8-inch MyLink touchscreen", "Apple CarPlay & Android Auto", "Forward Collision Alert", "Lane Departure Warning", "18-inch alloys", "3.5-tonne towing"],
                    "notes": "High-volume private buyer and trade favorite."
                },
                {
                    "badge_name": "Z71",
                    "years": {"start": 2015, "end": 2020},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 54990,
                    "msrp_aud_max": 59990,
                    "fuel_consumption_l_100km": 8.7,
                    "kerb_weight_kg": 2135,
                    "standard_features": ["Leather appointed seats with heating", "Black styling package", "Integrated sailplane sports bar", "Z71 bonnet decals", "Soft-drop tailgate"],
                    "notes": "Holden's flagship dual-cab adventure pick-up."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Z71",
                    "body_style": "Crew Cab",
                    "engine_code": "Duramax-2.8-LWN",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "msrp_aud": 57190,
                    "power_kw": 147.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 8.7,
                    "towing_braked_kg": 3500,
                    "notes": "500Nm torque and 3.5-tonne towing."
                }
            ]
        }
    ]
}
