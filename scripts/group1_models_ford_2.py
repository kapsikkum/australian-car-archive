"""
Deep-dive model data for Ford Fairlane/LTD and Ford Ranger.
"""
from typing import Any, Dict

FAIRLANE_LTD_DATA: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "fairlane-ltd",
    "name": "Ford Fairlane & LTD",
    "vehicle_type": "Sedan",
    "segment": "Upper Luxury / Limousine",
    "years_sold_au": {"start": 1967, "end": 2007},
    "locally_built": True,
    "assembly_plants_au": [
        "Broadmeadows, Victoria",
        "Eagle Farm, Queensland"
    ],
    "overview": "The Ford Fairlane and LTD was Australia's definitive long-wheelbase luxury prestige sedan. Spanning four decades and eleven model series from the 1967 ZA to the 2007 BF Mk II, the Fairlane dominated Australian corporate, hire-car, and government limousine fleets. In 1973, Ford introduced the ultra-exclusive LTD (P5) riding on a limousine-class 121-inch wheelbase with concealed headlamps and standard 351 Cleveland V8. The Fairlane and LTD offered effortless V8 cruising, cavernous rear legroom, and refined Australian engineering.",
    "australian_market_notes": "Engineered by stretching the Falcon's wheelbase behind the B-pillar, the 1967 ZA Fairlane was a brilliant marketing stroke, completely outselling Holden's imported and adapted prestige offerings and prompting Holden to hurriedly develop the Brougham and Statesman. In 1973, the Australian LTD was born as the most expensive and luxurious domestic car in Australia. The line transitioned through modern alloy-head EFI sixes in the 1980s, the return of Windsor V8 power in the 1990s, Tickford performance editions, and the 5.4L 3-valve V8 in the final BA/BF series.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "ZA-ZD",
            "generation_name": "First Generation (ZA to ZD)",
            "years": {"start": 1967, "end": 1972},
            "body_styles": ["4-door long-wheelbase sedan"],
            "platform": "Ford full-size LWB chassis",
            "ancap_rating": None,
            "summary": "Stretched 116-inch wheelbase Falcon body; 289, 302, and 351 Windsor/Cleveland V8s; Custom and 500 trims.",
            "engines": [
                {
                    "engine_code": "Windsor-302-Fairlane",
                    "name": "Ford Windsor 302ci (4.9L) V8",
                    "displacement_cc": 4942,
                    "displacement_litres": 4.9,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 157.0,
                    "power_rpm": "4600",
                    "torque_nm": 407.0,
                    "torque_rpm": "2600",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Standard engine in Fairlane 500 (ZB/ZC)."
                }
            ],
            "badges": [
                {
                    "badge_name": "Fairlane 500",
                    "years": {"start": 1967, "end": 1972},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["Cruisomatic 3-speed automatic"],
                    "msrp_aud_min": 3550,
                    "msrp_aud_max": 4350,
                    "fuel_consumption_l_100km": 15.5,
                    "kerb_weight_kg": 1470,
                    "standard_features": ["302/351 V8", "Power steering", "Twin vertical headlights (ZC/ZD)", "Plush brocade or vinyl seats"],
                    "notes": "Australia's luxury bestseller."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Fairlane 500",
                    "body_style": "4-door sedan",
                    "engine_code": "Windsor-302-Fairlane",
                    "transmission": "Cruisomatic 3-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 3890,
                    "power_kw": 157.0,
                    "torque_nm": 407.0,
                    "fuel_l_100km": 15.5,
                    "towing_braked_kg": 1500,
                    "notes": "Executive boardroom standard."
                }
            ]
        },
        {
            "series_code": "BA-BF",
            "generation_name": "Final Generation (BA & BF Fairlane / LTD)",
            "years": {"start": 2003, "end": 2007},
            "body_styles": ["4-door long-wheelbase sedan"],
            "platform": "Ford EA169 LWB platform",
            "ancap_rating": "4 Stars",
            "summary": "Control Blade independent rear suspension, Barra 182/190 inline-six, Barra 220 5.4L 3-valve V8, G220 sporting model, and ZF 6-speed automatic.",
            "engines": [
                {
                    "engine_code": "Barra-220-V8",
                    "name": "Barra 220 5.4L SOHC 24V V8",
                    "displacement_cc": 5408,
                    "displacement_litres": 5.4,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Unleaded)",
                    "power_kw": 220.0,
                    "power_rpm": "4750",
                    "torque_nm": 470.0,
                    "torque_rpm": "3250",
                    "compression_ratio": "9.1:1",
                    "valvetrain": "SOHC 24V 3-Valve per cylinder with VCT",
                    "notes": "Silky smooth modular V8 with massive low-end torque."
                }
            ],
            "badges": [
                {
                    "badge_name": "Fairlane Ghia",
                    "years": {"start": 2003, "end": 2007},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed auto / ZF 6-speed auto"],
                    "msrp_aud_min": 54950,
                    "msrp_aud_max": 61500,
                    "fuel_consumption_l_100km": 11.8,
                    "kerb_weight_kg": 1795,
                    "standard_features": ["Leather seating", "Dual-zone climate control", "Rear parking sensors", "Memory driver seat", "ICC with premium sound"],
                    "notes": "Classic long-wheelbase luxury."
                },
                {
                    "badge_name": "LTD",
                    "years": {"start": 2003, "end": 2007},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed auto / ZF 6-speed auto"],
                    "msrp_aud_min": 72000,
                    "msrp_aud_max": 76500,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1845,
                    "standard_features": ["Standard 5.4L V8", "Nappa leather", "Rear seat audio controls", "17-inch prestige alloys", "Self-levelling suspension"],
                    "notes": "Prestige flagship limousine."
                }
            ],
            "configurations": [
                {
                    "badge_name": "LTD",
                    "body_style": "4-door sedan",
                    "engine_code": "Barra-220-V8",
                    "transmission": "ZF 6-speed auto",
                    "drivetrain": "RWD",
                    "msrp_aud": 74500,
                    "power_kw": 220.0,
                    "torque_nm": 470.0,
                    "fuel_l_100km": 12.8,
                    "towing_braked_kg": 2300,
                    "notes": "Effortless luxury tourer."
                }
            ]
        }
    ]
}

RANGER_DATA: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "ranger",
    "name": "Ford Ranger",
    "vehicle_type": "Ute / Cab Chassis",
    "segment": "Mid-size Pick-up",
    "years_sold_au": {"start": 2006, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Ford Ranger is Australia's best-selling vehicle and one of the country's crowning engineering triumphs. Designed, engineered, and developed from the ground up by Ford Australia's 2,000-strong engineering and design team at Campbellfield, Victoria and the You Yangs Proving Ground, the Ranger is exported to over 180 countries. Across the PJ/PK, the revolutionary T6 (PX I, II, III), and the Next-Gen (PY), the Ranger redefined dual-cab refinement, off-road ability, and high-speed off-road performance through the bespoke Ranger Raptor.",
    "australian_market_notes": "In 2006, Ford replaced the Courier with the PJ Ranger. In 2011, Ford Australia unveiled 'Project T6' (PX Ranger)—the first vehicle developed from a clean sheet in Australia for global Ford truck production. It introduced the rugged 3.2L 5-cylinder Duratorq diesel, 3.5-tonne towing, and 800mm water wading. In 2018, Ford Australia launched the Ranger Raptor featuring Fox Racing 2.5-inch Internal Bypass dampers and coil-sprung Watts-link rear suspension. In 2022, the Next-Gen (PY) Ranger debuted with a 3.0L V6 Turbo Diesel (184kW/600Nm) and the Raptor packing a twin-turbo 3.0L EcoBoost V6 producing 292kW, becoming Australia's #1 selling motor vehicle overall.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "PX",
            "generation_name": "PX Series (T6 Platform - Series I, II, III)",
            "years": {"start": 2011, "end": 2022},
            "body_styles": ["Single Cab", "Super Cab", "Double Cab"],
            "platform": "Ford T6 global mid-size truck platform",
            "ancap_rating": "5 Stars",
            "summary": "Designed and engineered in Australia. 3.2L 5-cylinder TDCi (470Nm), 2.0L Bi-Turbo EcoBlue (500Nm, 10-speed auto), 3.5t towing, Ranger Raptor with Fox racing shocks.",
            "engines": [
                {
                    "engine_code": "Duratorq-3.2-TDCi",
                    "name": "Duratorq 3.2L 5-Cylinder Turbo Diesel",
                    "displacement_cc": 3198,
                    "displacement_litres": 3.2,
                    "cylinders": 5,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 147.0,
                    "power_rpm": "3000",
                    "torque_nm": 470.0,
                    "torque_rpm": "1500-2750",
                    "compression_ratio": "15.7:1",
                    "valvetrain": "DOHC 20V Variable Geometry Turbo",
                    "notes": "Legendary 5-cylinder workhorse engine; 3,500kg towing."
                },
                {
                    "engine_code": "EcoBlue-2.0-BiTurbo",
                    "name": "Ford EcoBlue 2.0L Bi-Turbo Diesel",
                    "displacement_cc": 1996,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Twin-Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 157.0,
                    "power_rpm": "3750",
                    "torque_nm": 500.0,
                    "torque_rpm": "1750-2000",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "DOHC 16V Sequential Bi-Turbo",
                    "notes": "Mated to 10-speed automatic; standard in Ranger Raptor (PX III)."
                }
            ],
            "badges": [
                {
                    "badge_name": "Wildtrak",
                    "years": {"start": 2011, "end": 2022},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed manual", "6-speed auto", "10-speed auto"],
                    "msrp_aud_min": 57390,
                    "msrp_aud_max": 65990,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 2246,
                    "standard_features": ["Aerodynamic sports hoop", "Roller shutter tonneau", "Heated leather seats with orange stitching", "SYNC 3 with 8-inch screen", "Adaptive Cruise Control", "Electronic rear differential lock"],
                    "notes": "The benchmark lifestyle 4WD dual-cab in Australia."
                },
                {
                    "badge_name": "Ranger Raptor",
                    "years": {"start": 2018, "end": 2022},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["10-speed automatic"],
                    "msrp_aud_min": 74990,
                    "msrp_aud_max": 79990,
                    "fuel_consumption_l_100km": 8.2,
                    "kerb_weight_kg": 2332,
                    "standard_features": ["Fox Racing 2.5-inch Internal Bypass dampers", "Coil-sprung rear axle with Watts linkage", "Widened track (150mm wider)", "33-inch BF Goodrich all-terrain tyres", "Baja race drive mode"],
                    "notes": "Pioneered the high-speed off-road desert racer truck category."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Wildtrak Bi-Turbo",
                    "body_style": "Double Cab",
                    "engine_code": "EcoBlue-2.0-BiTurbo",
                    "transmission": "10-speed automatic",
                    "drivetrain": "4WD",
                    "msrp_aud": 64490,
                    "power_kw": 157.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 3500,
                    "notes": "500Nm torque and 10-speed refinement."
                },
                {
                    "badge_name": "Ranger Raptor",
                    "body_style": "Double Cab",
                    "engine_code": "EcoBlue-2.0-BiTurbo",
                    "transmission": "10-speed automatic",
                    "drivetrain": "4WD",
                    "msrp_aud": 79290,
                    "power_kw": 157.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 8.2,
                    "towing_braked_kg": 2500,
                    "notes": "Off-road desert racer with Fox suspension."
                }
            ]
        },
        {
            "series_code": "PY",
            "generation_name": "Next-Gen Ranger (PY)",
            "years": {"start": 2022, "end": "Present"},
            "body_styles": ["Single Cab", "Super Cab", "Double Cab"],
            "platform": "Ford upgraded T6 architecture",
            "ancap_rating": "5 Stars",
            "summary": "Australia's #1 selling vehicle. Australia-led engineering with 3.0L V6 Turbo Diesel (184kW/600Nm), 12-inch portrait touchscreen, and the fearsome 292kW twin-turbo V6 Ranger Raptor.",
            "engines": [
                {
                    "engine_code": "PowerStroke-3.0-V6",
                    "name": "Ford Power Stroke 3.0L V6 Turbo Diesel",
                    "displacement_cc": 2993,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 184.0,
                    "power_rpm": "3250",
                    "torque_nm": 600.0,
                    "torque_rpm": "1750-2250",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "DOHC 24V Variable Geometry Turbo",
                    "notes": "Full-time 4WD system with electronically controlled transfer case; 600Nm."
                },
                {
                    "engine_code": "Nano-3.0-TwinTurbo-V6",
                    "name": "Ford 3.0L Twin-Turbo EcoBoost V6 (Raptor)",
                    "displacement_cc": 2956,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Twin-Turbocharged",
                    "fuel_type": "Petrol (98 RON)",
                    "power_kw": 292.0,
                    "power_rpm": "5650",
                    "torque_nm": 583.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 24V Twin Turbo with Anti-Lag",
                    "notes": "Race-bred anti-lag system; active valve twin exhaust with Baja mode."
                }
            ],
            "badges": [
                {
                    "badge_name": "Wildtrak V6",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD (Full-Time)",
                    "transmissions": ["10-speed automatic"],
                    "msrp_aud_min": 70190,
                    "msrp_aud_max": 75990,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 2348,
                    "standard_features": ["3.0L V6 600Nm", "12-inch portrait SYNC 4A screen", "Matrix LED headlamps", "Zone lighting", "360-degree camera", "Integrated box step", "3.5t towing"],
                    "notes": "The dominant dual-cab 4WD in the country."
                },
                {
                    "badge_name": "Ranger Raptor",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["Double Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["10-speed automatic"],
                    "msrp_aud_min": 85490,
                    "msrp_aud_max": 92000,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 2475,
                    "standard_features": ["292kW Twin-Turbo V6", "Fox 2.5-inch Live Valve internal bypass shocks", "Front and rear electronic locking diffs", "Active exhaust", "Ford Performance seats"],
                    "notes": "Supercar performance on dirt; 0-100 km/h in 5.8s."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Wildtrak V6",
                    "body_style": "Double Cab",
                    "engine_code": "PowerStroke-3.0-V6",
                    "transmission": "10-speed automatic",
                    "drivetrain": "4WD (Full-Time)",
                    "msrp_aud": 71190,
                    "power_kw": 184.0,
                    "torque_nm": 600.0,
                    "fuel_l_100km": 8.4,
                    "towing_braked_kg": 3500,
                    "notes": "600Nm torque and effortless towing."
                },
                {
                    "badge_name": "Ranger Raptor",
                    "body_style": "Double Cab",
                    "engine_code": "Nano-3.0-TwinTurbo-V6",
                    "transmission": "10-speed automatic",
                    "drivetrain": "4WD",
                    "msrp_aud": 87990,
                    "power_kw": 292.0,
                    "torque_nm": 583.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 2500,
                    "notes": "292kW twin-turbo off-road super truck."
                }
            ]
        }
    ]
}
