"""
Wave 2 Deep-Dive Model Data: Holden 4WDs, SUVs, and Aussie Icons (Part 3)
Models:
9. Jackaroo
10. Captiva
11. Sandman
12. Adventra-Crewman
"""
from typing import Any, Dict

MODEL_JACKAROO: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "jackaroo",
    "name": "Holden Jackaroo",
    "vehicle_type": "4WD SUV / Wagon (3-door & 5-door)",
    "segment": "Mid-size / Large 4WD SUV",
    "years_sold_au": {"start": 1981, "end": 2004},
    "locally_built": False,
    "assembly_plants_au": [
        "Imported (Fujisawa, Japan - Isuzu Motors)"
    ],
    "overview": "The Holden Jackaroo (Isuzu Trooper / Bighorn) was Holden's frontline heavy-duty four-wheel-drive wagon from 1981 to 2004. Engineered to conquer the Australian outback, the Jackaroo competed directly against the Toyota LandCruiser Prado, Mitsubishi Pajero, and Nissan Patrol. The first-generation UBS-1 (1981-1992) offered short and long wheelbase bodies with rugged four-cylinder petrol and diesel engines. The second-generation UBS-2 (1992-2004) expanded into a wide-body luxury family 4WD featuring coil-sprung rear suspension, shift-on-the-fly 4WD, potent 3.2L and 3.5L DOHC 24V V6 petrol engines (158 kW), and advanced 3.0L 4JX1 common-rail turbo-diesel. The flagship Monterey added leather trim, woodgrain, climate control, and heated seats.",
    "australian_market_notes": "The Jackaroo earned widespread admiration for its exceptional interior room, expansive glasshouse visibility, and compliant ride over outback corrugations. In 1993, legendary Australian rally driver Peter Brock competed in the Australian Safari behind the wheel of an Isuzu/Holden Jackaroo, demonstrating its extreme durability. The 3.5L V6 Monterey was regarded as one of the best-value luxury tow vehicles of its era.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "UBS-1",
            "generation_name": "UBS-1 Jackaroo",
            "years": {"start": 1981, "end": 1992},
            "body_styles": ["3-door wagon (SWB)", "5-door wagon (LWB)"],
            "platform": "Isuzu UBS platform",
            "ancap_rating": None,
            "summary": "First-generation boxy 4WD wagon. Dual-range transfer case, manual free-wheeling hubs, leaf-sprung rear axle, and durable 4-cylinder petrol and diesel powerplants.",
            "engines": [
                {
                    "engine_code": "Isuzu-4ZE1",
                    "name": "Isuzu 4ZE1 2.6L EFI Inline-4",
                    "displacement_cc": 2559,
                    "displacement_litres": 2.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 88.0,
                    "power_rpm": "5000",
                    "torque_nm": 195.0,
                    "torque_rpm": "2600",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Electronic multi-point fuel injection introduced in late 1980s."
                },
                {
                    "engine_code": "Isuzu-4JB1-T-Jackaroo",
                    "name": "Isuzu 4JB1-T 2.8L Turbo Diesel Inline-4",
                    "displacement_cc": 2771,
                    "displacement_litres": 2.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 78.0,
                    "power_rpm": "3800",
                    "torque_nm": 230.0,
                    "torque_rpm": "2300",
                    "compression_ratio": "18.2:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Direct injection turbo diesel; popular outback touring choice."
                }
            ],
            "badges": [
                {
                    "badge_name": "LS LWB 4WD",
                    "years": {"start": 1985, "end": 1992},
                    "body_styles": ["5-door wagon"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 29990,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1690,
                    "standard_features": ["Selectable 4WD with low-range", "Power steering", "Air conditioning", "Velour upholstery", "Roof rails and side steps"],
                    "notes": "Family outback explorer."
                }
            ],
            "configurations": [
                {
                    "badge_name": "LS LWB 4WD",
                    "body_style": "5-door wagon",
                    "engine_code": "Isuzu-4ZE1",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "msrp_aud": 26990,
                    "power_kw": 88.0,
                    "torque_nm": 195.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 1800,
                    "notes": "2.6L petrol 5-door family 4WD."
                }
            ]
        },
        {
            "series_code": "UBS-2",
            "generation_name": "UBS-2 Jackaroo / Monterey",
            "years": {"start": 1992, "end": 2004},
            "body_styles": ["5-door wagon"],
            "platform": "Isuzu UBS second generation platform",
            "ancap_rating": 3,
            "summary": "Wide-body full-size luxury 4WD. Coil spring suspension all round, Shift-on-the-Fly 4WD, 3.5L DOHC 24V V6, 3.0L direct-injection turbo diesel, and prestige Monterey flagship.",
            "engines": [
                {
                    "engine_code": "Isuzu-6VE1-3.5L",
                    "name": "Isuzu 6VE1 3.5L DOHC 24V V6",
                    "displacement_cc": 3494,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 158.0,
                    "power_rpm": "5400",
                    "torque_nm": 310.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.1:1",
                    "valvetrain": "DOHC 24V",
                    "notes": "Quad-cam 24-valve alloy V6 introduced in 1998."
                },
                {
                    "engine_code": "Isuzu-4JX1-3.0TD",
                    "name": "Isuzu 4JX1 3.0L DOHC 16V Turbo Diesel Inline-4",
                    "displacement_cc": 2999,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 118.0,
                    "power_rpm": "3900",
                    "torque_nm": 333.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "19.0:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Common-rail HEUI direct-injection turbo diesel with intercooler."
                }
            ],
            "badges": [
                {
                    "badge_name": "Jackaroo SE / Equipe",
                    "years": {"start": 1998, "end": 2004},
                    "body_styles": ["5-door wagon"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic with Torque-on-Demand"],
                    "msrp_aud_min": 41990,
                    "msrp_aud_max": 47990,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1980,
                    "standard_features": [
                        "Shift-on-the-fly 4WD up to 100 km/h",
                        "Dual front airbags and 4-wheel ABS disc brakes",
                        "16-inch alloy wheels",
                        "7-passenger 3-row seating",
                        "Dual air conditioning"
                    ],
                    "notes": "Popular mainstream family touring specification."
                },
                {
                    "badge_name": "Monterey",
                    "years": {"start": 1998, "end": 2004},
                    "body_styles": ["5-door wagon"],
                    "drivetrain": "4WD",
                    "transmissions": ["4-speed automatic with Torque-on-Demand"],
                    "msrp_aud_min": 52990,
                    "msrp_aud_max": 57990,
                    "fuel_consumption_l_100km": 13.2,
                    "kerb_weight_kg": 2040,
                    "standard_features": [
                        "3.5L DOHC V6 standard",
                        "Torque-On-Demand (TOD) active AWD/4WD system",
                        "Leather upholstery and walnut woodgrain trim",
                        "Heated front seats with electric adjustment",
                        "Power glass sunroof and 6-disc CD changer"
                    ],
                    "notes": "Prestige flagship competitor to LandCruiser Prado Grande."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Monterey",
                    "body_style": "5-door wagon",
                    "engine_code": "Isuzu-6VE1-3.5L",
                    "transmission": "4-speed automatic with Torque-on-Demand",
                    "drivetrain": "4WD",
                    "msrp_aud": 52990,
                    "power_kw": 158.0,
                    "torque_nm": 310.0,
                    "fuel_l_100km": 13.2,
                    "towing_braked_kg": 2500,
                    "notes": "158 kW 3.5L V6 flagship luxury 4WD."
                },
                {
                    "badge_name": "Jackaroo SE / Equipe",
                    "body_style": "5-door wagon",
                    "engine_code": "Isuzu-4JX1-3.0TD",
                    "transmission": "4-speed automatic with Torque-on-Demand",
                    "drivetrain": "4WD",
                    "msrp_aud": 45990,
                    "power_kw": 118.0,
                    "torque_nm": 333.0,
                    "fuel_l_100km": 10.4,
                    "towing_braked_kg": 2500,
                    "notes": "3.0L turbo diesel 7-seat family wagon."
                }
            ]
        }
    ]
}

MODEL_CAPTIVA: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "captiva",
    "name": "Holden Captiva",
    "vehicle_type": "Mid-size SUV (5-seater & 7-seater)",
    "segment": "Medium / Large SUV",
    "years_sold_au": {"start": 2006, "end": 2018},
    "locally_built": False,
    "assembly_plants_au": [
        "Imported (Bupyeong and Gunsan, South Korea - GM Daewoo / GM Korea)"
    ],
    "overview": "The Holden Captiva was Holden's core mid-size family SUV between 2006 and 2018, competing in Australia's exploding SUV segment against the Ford Territory and Toyota Kluger. Built on GM's global Theta platform, the range uniquely comprised two distinct body styles: the 5-seater Captiva 5 (Opel Antara twin) and the 7-seater Captiva 7 (Chevrolet Captiva). Over 150,000 Captivas found homes in Australian driveways thanks to keen pricing, standard three-row seating, AWD capability, and Australian-built Alloytec 3.2L and 3.0L SIDI V6 engines alongside 2.0L and 2.2L common-rail turbo diesels. Series II arrived in 2011 with refreshed styling, before the model was replaced by the Equinox and Acadia.",
    "australian_market_notes": "The Captiva played a vital role in Holden's transition from traditional rear-drive station wagons to modern crossover SUVs. The early V6 models featured the 3.2-litre version of Holden's Australian-manufactured Alloytec V6, cast at Port Melbourne and shipped to Korea for vehicle assembly. The Captiva was renowned for offering 7-seat packaging at a sub-$40k price point.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "CG-Series-I",
            "generation_name": "CG Captiva Series I",
            "years": {"start": 2006, "end": 2011},
            "body_styles": ["5-door SUV (5-seat)", "5-door SUV (7-seat)"],
            "platform": "GM Theta platform",
            "ancap_rating": 4,
            "summary": "Launch of Captiva 7 and sporty Captiva MaXX/5. Powered by Australian-built Alloytec 3.2L V6 and 2.0L VCDi common-rail turbo-diesel with on-demand AWD.",
            "engines": [
                {
                    "engine_code": "Alloytec-3.2-V6",
                    "name": "Holden Alloytec 3.2L DOHC 24V V6",
                    "displacement_cc": 3195,
                    "displacement_litres": 3.2,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 169.0,
                    "power_rpm": "6600",
                    "torque_nm": 297.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "10.3:1",
                    "valvetrain": "DOHC 24V",
                    "notes": "Manufactured at Holden's Port Melbourne engine plant."
                },
                {
                    "engine_code": "VCDi-2.0-Diesel-CG",
                    "name": "Holden 2.0L VCDi Common-Rail Turbo Diesel Inline-4",
                    "displacement_cc": 1991,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 110.0,
                    "power_rpm": "4000",
                    "torque_nm": 320.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "17.5:1",
                    "valvetrain": "SOHC 16V",
                    "notes": "Common-rail direct injection turbo diesel."
                }
            ],
            "badges": [
                {
                    "badge_name": "CX (7-seater)",
                    "years": {"start": 2006, "end": 2011},
                    "body_styles": ["7-seat SUV"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed automatic with Active Select"],
                    "msrp_aud_min": 38990,
                    "msrp_aud_max": 42990,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1820,
                    "standard_features": [
                        "7-passenger fold-flat seating",
                        "Active on-demand all-wheel drive",
                        "Electronic stability control with rollover mitigation",
                        "17-inch alloy wheels",
                        "Rear park assist"
                    ],
                    "notes": "High-volume 7-seat family specification."
                },
                {
                    "badge_name": "LX (7-seater)",
                    "years": {"start": 2006, "end": 2011},
                    "body_styles": ["7-seat SUV"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed automatic with Active Select"],
                    "msrp_aud_min": 42990,
                    "msrp_aud_max": 45990,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1850,
                    "standard_features": [
                        "Leather seat trim with electric driver's seat",
                        "18-inch alloy wheels",
                        "Automatic climate control",
                        "Curtain airbags and side steps",
                        "Front fog lamps and roof rails"
                    ],
                    "notes": "Luxury flagship 7-seater."
                }
            ],
            "configurations": [
                {
                    "badge_name": "CX (7-seater)",
                    "body_style": "7-seat SUV",
                    "engine_code": "Alloytec-3.2-V6",
                    "transmission": "5-speed automatic with Active Select",
                    "drivetrain": "AWD",
                    "msrp_aud": 38990,
                    "power_kw": 169.0,
                    "torque_nm": 297.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 2000,
                    "notes": "Port Melbourne Alloytec V6 7-seater."
                }
            ]
        },
        {
            "series_code": "CG-Series-II",
            "generation_name": "CG Captiva Series II",
            "years": {"start": 2011, "end": 2018},
            "body_styles": ["5-door SUV (5-seat)", "5-door SUV (7-seat)"],
            "platform": "GM Theta platform",
            "ancap_rating": 5,
            "summary": "Series II redesign. 5-star ANCAP safety, direct-injection 3.0L SIDI V6, 2.2L 400 Nm turbo diesel, and 6-speed automatic transmissions.",
            "engines": [
                {
                    "engine_code": "SIDI-3.0-V6-LF1",
                    "name": "Holden SIDI 3.0L Direct-Injection V6",
                    "displacement_cc": 2997,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 190.0,
                    "power_rpm": "6900",
                    "torque_nm": 288.0,
                    "torque_rpm": "5800",
                    "compression_ratio": "11.7:1",
                    "valvetrain": "DOHC 24V SIDI VVT",
                    "notes": "Direct injection High Feature V6."
                },
                {
                    "engine_code": "CDTi-2.2-Diesel",
                    "name": "Holden 2.2L CDTi Common-Rail Turbo Diesel Inline-4",
                    "displacement_cc": 2231,
                    "displacement_litres": 2.2,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 135.0,
                    "power_rpm": "3800",
                    "torque_nm": 400.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "16.3:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Variable geometry turbo with 400 Nm of torque."
                }
            ],
            "badges": [
                {
                    "badge_name": "LTZ (7-seater)",
                    "years": {"start": 2011, "end": 2018},
                    "body_styles": ["7-seat SUV"],
                    "drivetrain": "AWD",
                    "transmissions": ["6-speed automatic with Active Select"],
                    "msrp_aud_min": 43490,
                    "msrp_aud_max": 45490,
                    "fuel_consumption_l_100km": 10.1,
                    "kerb_weight_kg": 1920,
                    "standard_features": [
                        "19-inch alloy wheels",
                        "Leather appointed trim with heated front seats",
                        "Rear view camera and 7-inch touchscreen navigation",
                        "Hill start assist and descent control",
                        "Blind spot alert and rear cross traffic alert (later models)"
                    ],
                    "notes": "Top-spec 7-seat flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "LTZ (7-seater)",
                    "body_style": "7-seat SUV",
                    "engine_code": "CDTi-2.2-Diesel",
                    "transmission": "6-speed automatic with Active Select",
                    "drivetrain": "AWD",
                    "msrp_aud": 44490,
                    "power_kw": 135.0,
                    "torque_nm": 400.0,
                    "fuel_l_100km": 8.1,
                    "towing_braked_kg": 2000,
                    "notes": "400 Nm diesel 7-seater."
                }
            ]
        }
    ]
}

MODEL_SANDMAN: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "sandman",
    "name": "Holden Sandman",
    "vehicle_type": "Panel Van / Coupe Utility",
    "segment": "Commercial / Lifestyle Sports",
    "years_sold_au": {"start": 1974, "end": 1980},
    "locally_built": True,
    "assembly_plants_au": [
        "Elizabeth, South Australia",
        "Dandenong, Victoria",
        "Pagewood, New South Wales",
        "Acacia Ridge, Queensland"
    ],
    "overview": "The Holden Sandman is the undisputed emblem of 1970s Australian youth and beach culture. Introduced in January 1974 on the HQ series (option package XX7 / XU3), the Sandman transformed humble commercial panel vans and utilities into vibrant, psychedelic recreational machines. Featuring bold side stripes, Monaro GTS sports dashboard with tachometer, GTS steering wheel, slotted steel rally wheels, twin bucket seats, and standard or optional 253ci and 308ci Red V8 power, the Sandman became a pop-culture legend closely tied to surfing, drive-in cinemas, and Australian freedom. The Sandman package carried through the HQ, HJ, HX, and HZ series until 1980, with authentic surviving examples now among Australia's most fiercely sought-after collector cars.",
    "australian_market_notes": "Originally devised to counter the Ford Falcon Sundowner and Chrysler Valiant Drifter, the Sandman completely captured the youth zeitgeist. While legally classified as commercial vehicles (saving buyers significant sales tax at the time), Sandmans were heavily optioned with sports suspensions, dual exhaust systems, customized shag-pile carpets, and tailgate mural art. In 1977, the HZ series bestowed Radial Tuned Suspension (RTS), giving the Sandman world-class handling dynamics.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "HQ-HJ",
            "generation_name": "HQ / HJ Sandman",
            "years": {"start": 1974, "end": 1976},
            "body_styles": ["2-door panel van", "2-door coupe utility"],
            "platform": "GM-H full-size perimeter subframe",
            "ancap_rating": None,
            "summary": "Inaugural Sandman package (XX7 / XU3) on HQ and HJ. Monaro GTS dash, sports wheels, bucket seats, and optional 253ci and 308ci Red V8 engines.",
            "engines": [
                {
                    "engine_code": "Red-202-Sandman",
                    "name": "Holden Red 202ci (3.3L) OHV Inline-6",
                    "displacement_cc": 3310,
                    "displacement_litres": 3.3,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 101.0,
                    "power_rpm": "4400",
                    "torque_nm": 263.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Twin-barrel Bendix-Stromberg carburettor; standard base six."
                },
                {
                    "engine_code": "Red-253-V8-Sandman",
                    "name": "Holden Red 253ci (4.2L) OHV V8",
                    "displacement_cc": 4146,
                    "displacement_litres": 4.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 138.0,
                    "power_rpm": "4400",
                    "torque_nm": 355.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Twin-barrel Stromberg WW carburettor, 185 bhp."
                },
                {
                    "engine_code": "Red-308-V8-Sandman",
                    "name": "Holden Red 308ci (5.0L) OHV V8",
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
                    "notes": "Rochester 4-barrel Quadrajet carburettor, 240 bhp output."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sandman Van",
                    "years": {"start": 1974, "end": 1976},
                    "body_styles": ["Panel Van"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor", "Tri-Matic 3-speed automatic", "TH400 3-speed automatic"],
                    "msrp_aud_min": 3580,
                    "msrp_aud_max": 4650,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1410,
                    "standard_features": [
                        "Monaro GTS full instrumentation fascia with tachometer",
                        "GTS three-spoke steering wheel",
                        "Front bucket seats",
                        "Slotted steel GTS wheels with chrome trim rings",
                        "Distinctive Sandman multi-colour side and tailgate decals"
                    ],
                    "notes": "Iconic Australian surf lifestyle panel van."
                },
                {
                    "badge_name": "Sandman Utility",
                    "years": {"start": 1974, "end": 1976},
                    "body_styles": ["Coupe Utility"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor", "Tri-Matic 3-speed automatic"],
                    "msrp_aud_min": 3450,
                    "msrp_aud_max": 4480,
                    "fuel_consumption_l_100km": 14.0,
                    "kerb_weight_kg": 1360,
                    "standard_features": [
                        "Monaro GTS dashboard and bucket seats",
                        "Sandman body striping and decals",
                        "GTS wheels",
                        "Sports suspension package"
                    ],
                    "notes": "High-performance sports coupe utility."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Sandman Van",
                    "body_style": "Panel Van",
                    "engine_code": "Red-253-V8-Sandman",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 3890,
                    "power_kw": 138.0,
                    "torque_nm": 355.0,
                    "fuel_l_100km": 14.5,
                    "towing_braked_kg": 1500,
                    "notes": "Classic 4.2L V8 4-speed manual surf van."
                },
                {
                    "badge_name": "Sandman Van",
                    "body_style": "Panel Van",
                    "engine_code": "Red-308-V8-Sandman",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 4350,
                    "power_kw": 179.0,
                    "torque_nm": 427.0,
                    "fuel_l_100km": 16.0,
                    "towing_braked_kg": 1600,
                    "notes": "Top-spec 5.0L 308 V8 muscle van."
                }
            ]
        },
        {
            "series_code": "HX-HZ",
            "generation_name": "HX / HZ Sandman",
            "years": {"start": 1976, "end": 1980},
            "body_styles": ["2-door panel van", "2-door coupe utility"],
            "platform": "GM-H full-size perimeter subframe",
            "ancap_rating": None,
            "summary": "Large 'SANDMAN' tailgate script on HX, followed by landmark HZ introduction of Radial Tuned Suspension (RTS), front chin spoiler, and 4-wheel disc brake option.",
            "engines": [
                {
                    "engine_code": "Red-4.2-V8-ADR27A",
                    "name": "Holden Red 4.2L (253ci) V8",
                    "displacement_cc": 4146,
                    "displacement_litres": 4.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 120.0,
                    "power_rpm": "4500",
                    "torque_nm": 325.0,
                    "torque_rpm": "2600",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "ADR27A emission compliant."
                },
                {
                    "engine_code": "Red-5.0-V8-ADR27A",
                    "name": "Holden Red 5.0L (308ci) V8",
                    "displacement_cc": 5044,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 161.0,
                    "power_rpm": "4800",
                    "torque_nm": 400.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Rochester 4-barrel Quadrajet carburettor."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sandman Van (HZ)",
                    "years": {"start": 1977, "end": 1980},
                    "body_styles": ["Panel Van"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor", "Tri-Matic 3-speed automatic", "TH400 3-speed automatic"],
                    "msrp_aud_min": 5690,
                    "msrp_aud_max": 6890,
                    "fuel_consumption_l_100km": 14.8,
                    "kerb_weight_kg": 1460,
                    "standard_features": [
                        "Radial Tuned Suspension (RTS) with rear anti-roll bar",
                        "Front chin air dam spoiler",
                        "Monaro GTS dashboard and sport steering wheel",
                        "GTS slotted wheels and round headlight grille",
                        "V8 standard equipment (from 1978)"
                    ],
                    "notes": "Peak handling RTS Sandman van."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Sandman Van (HZ)",
                    "body_style": "Panel Van",
                    "engine_code": "Red-5.0-V8-ADR27A",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 6450,
                    "power_kw": 161.0,
                    "torque_nm": 400.0,
                    "fuel_l_100km": 15.5,
                    "towing_braked_kg": 1600,
                    "notes": "5.0L V8 HZ Sandman with RTS."
                }
            ]
        }
    ]
}

MODEL_ADVENTRA_CREWMAN: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "adventra-crewman",
    "name": "Holden Adventra & Crewman",
    "vehicle_type": "All-Wheel-Drive Cross Wagon / Dual-Cab Utility / Cab Chassis",
    "segment": "Large / Crossover SUV / Commercial Dual-Cab",
    "years_sold_au": {"start": 2003, "end": 2008},
    "locally_built": True,
    "assembly_plants_au": [
        "Elizabeth, South Australia"
    ],
    "overview": "Developed during Holden's multi-million dollar engineering expansion under the VY/VZ Commodore program, the Adventra and Crewman represented audacious Australian engineering innovations. The 2003 Crewman was Australia's first locally designed and manufactured monocoque dual-cab utility, seating five adults on an extended 3,200 mm wheelbase with a heavy-duty leaf-sprung live rear axle capable of carrying up to a tonne. The Adventra was Holden's crossover all-wheel-drive sport wagon, boasting an Australian-engineered 'Cross-Trac' permanent AWD system (62% rear, 38% front torque split with automatic brake-traction management) and raised ground clearance. Holden combined the two concepts to create the monstrous Crewman Cross 8 and Cross 6, alongside V8 SS performance dual-cabs.",
    "australian_market_notes": "The Cross-Trac AWD system was developed entirely in-house by Holden engineers at Fishermans Bend and tested across the Simpson Desert and Mount Hotham snowfields. It delivered incredible off-road tractive ability without low-range gearing. The Crewman SS and Cross 8 became instant cult machines for tradies who wanted Monaro V8 thunder combined with family dual-cab practicality.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "VY-II",
            "generation_name": "VY Series II Adventra & Crewman",
            "years": {"start": 2003, "end": 2004},
            "body_styles": ["5-door AWD wagon", "4-door dual-cab ute"],
            "platform": "GM V-body extended / Cross-Trac AWD",
            "ancap_rating": 4,
            "summary": "Launch of Adventra AWD (CX8, LX8) powered by Gen III 5.7L LS1 V8 (235 kW), and Crewman (Base 3.8L V6, SS 5.7L V8 235 kW, and Crewman Cross 8 AWD).",
            "engines": [
                {
                    "engine_code": "ECOTEC-3.8-V6",
                    "name": "Holden ECOTEC 3.8L OHV V6",
                    "displacement_cc": 3791,
                    "displacement_litres": 3.8,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 152.0,
                    "power_rpm": "5200",
                    "torque_nm": 305.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Standard engine in base Crewman."
                },
                {
                    "engine_code": "Gen-III-5.7-LS1",
                    "name": "GM Gen III 5.7L (LS1) Pushrod V8",
                    "displacement_cc": 5665,
                    "displacement_litres": 5.7,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 235.0,
                    "power_rpm": "5200",
                    "torque_nm": 460.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.1:1",
                    "valvetrain": "OHV 16V",
                    "notes": "All-aluminium V8, standard in Adventra CX8/LX8 and Crewman SS / Cross 8."
                }
            ],
            "badges": [
                {
                    "badge_name": "Adventra LX8",
                    "years": {"start": 2003, "end": 2004},
                    "body_styles": ["AWD Wagon"],
                    "drivetrain": "AWD",
                    "transmissions": ["4-speed automatic heavy duty 4L65-E"],
                    "msrp_aud_min": 52990,
                    "msrp_aud_max": 56990,
                    "fuel_consumption_l_100km": 15.2,
                    "kerb_weight_kg": 1965,
                    "standard_features": [
                        "Cross-Trac permanent AWD (62/38 split)",
                        "235 kW 5.7L LS1 V8",
                        "Raised heavy-duty suspension and skid plates",
                        "Leather seat trim and dual-zone climate control",
                        "17-inch alloy wheels with all-terrain tyres"
                    ],
                    "notes": "Flagship luxury AWD all-road wagon."
                },
                {
                    "badge_name": "Crewman SS",
                    "years": {"start": 2003, "end": 2004},
                    "body_styles": ["Dual Cab Ute"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual Tremec T56", "4-speed automatic 4L65-E"],
                    "msrp_aud_min": 46990,
                    "msrp_aud_max": 49990,
                    "fuel_consumption_l_100km": 14.8,
                    "kerb_weight_kg": 1850,
                    "standard_features": [
                        "235 kW 5.7L LS1 V8",
                        "FE2 sports suspension",
                        "17-inch SS alloy wheels and fog lamps",
                        "Sports bucket seats and leather-wrapped steering wheel",
                        "Rear limited-slip differential (LSD)"
                    ],
                    "notes": "Muscle dual-cab utility."
                },
                {
                    "badge_name": "Crewman Cross 8",
                    "years": {"start": 2004, "end": 2004},
                    "body_styles": ["Dual Cab Ute"],
                    "drivetrain": "AWD",
                    "transmissions": ["4-speed automatic heavy duty 4L65-E"],
                    "msrp_aud_min": 51990,
                    "msrp_aud_max": 54990,
                    "fuel_consumption_l_100km": 15.6,
                    "kerb_weight_kg": 2010,
                    "standard_features": [
                        "Cross-Trac permanent AWD",
                        "235 kW 5.7L LS1 V8",
                        "Raised suspension and wheel arch flares",
                        "Heavy-duty leaf rear axle with limited-slip differential",
                        "Full dual-cab sports interior"
                    ],
                    "notes": "World's only 5.7L V8 AWD factory dual-cab ute."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Adventra LX8",
                    "body_style": "AWD Wagon",
                    "engine_code": "Gen-III-5.7-LS1",
                    "transmission": "4-speed automatic heavy duty 4L65-E",
                    "drivetrain": "AWD",
                    "msrp_aud": 52990,
                    "power_kw": 235.0,
                    "torque_nm": 460.0,
                    "fuel_l_100km": 15.2,
                    "towing_braked_kg": 2100,
                    "notes": "Cross-Trac permanent AWD LS1 V8 wagon."
                },
                {
                    "badge_name": "Crewman SS",
                    "body_style": "Dual Cab Ute",
                    "engine_code": "Gen-III-5.7-LS1",
                    "transmission": "6-speed manual Tremec T56",
                    "drivetrain": "RWD",
                    "msrp_aud": 46990,
                    "power_kw": 235.0,
                    "torque_nm": 460.0,
                    "fuel_l_100km": 14.8,
                    "towing_braked_kg": 2100,
                    "notes": "6-speed manual 5.7L V8 dual cab ute."
                },
                {
                    "badge_name": "Crewman Cross 8",
                    "body_style": "Dual Cab Ute",
                    "engine_code": "Gen-III-5.7-LS1",
                    "transmission": "4-speed automatic heavy duty 4L65-E",
                    "drivetrain": "AWD",
                    "msrp_aud": 51990,
                    "power_kw": 235.0,
                    "torque_nm": 460.0,
                    "fuel_l_100km": 15.6,
                    "towing_braked_kg": 2500,
                    "notes": "Cross-Trac AWD 5.7L V8 heavy-duty dual cab."
                }
            ]
        },
        {
            "series_code": "VZ",
            "generation_name": "VZ Series Adventra & Crewman",
            "years": {"start": 2004, "end": 2008},
            "body_styles": ["5-door AWD wagon", "4-door dual-cab ute", "2-door cab chassis (One Tonner)"],
            "platform": "GM V-body extended / Cross-Trac AWD",
            "ancap_rating": 4,
            "summary": "VZ powertrain update. Introduction of 190 kW Alloytec V6 in Adventra SX6/CX6 and Crewman Cross 6, alongside upgraded 250 kW Gen III 5.7L and 260 kW 6.0L L76 V8 in Crewman SS / SSZ.",
            "engines": [
                {
                    "engine_code": "Alloytec-190-V6",
                    "name": "Holden Alloytec 190 3.6L DOHC 24V V6",
                    "displacement_cc": 3564,
                    "displacement_litres": 3.6,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 190.0,
                    "power_rpm": "6500",
                    "torque_nm": 340.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "10.2:1",
                    "valvetrain": "DOHC 24V VVT",
                    "notes": "Variable Cam Phasing (VCP) and dual exhaust; paired with 5-speed 5L40-E automatic."
                },
                {
                    "engine_code": "Gen-IV-6.0-L76",
                    "name": "GM Gen IV 6.0L (L76) Pushrod V8",
                    "displacement_cc": 5967,
                    "displacement_litres": 6.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 260.0,
                    "power_rpm": "5600",
                    "torque_nm": 510.0,
                    "torque_rpm": "4400",
                    "compression_ratio": "10.4:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Introduced in 2006 on Crewman SS; 260 kW and 510 Nm."
                }
            ],
            "badges": [
                {
                    "badge_name": "Adventra CX6",
                    "years": {"start": 2005, "end": 2006},
                    "body_styles": ["AWD Wagon"],
                    "drivetrain": "AWD",
                    "transmissions": ["5-speed automatic 5L40-E with paddle shifters"],
                    "msrp_aud_min": 44990,
                    "msrp_aud_max": 47990,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1895,
                    "standard_features": [
                        "Cross-Trac permanent AWD",
                        "190 kW Alloytec V6",
                        "Electronic Stability Program (ESP)",
                        "17-inch alloy wheels",
                        "Climate control"
                    ],
                    "notes": "V6 powered AWD wagon."
                },
                {
                    "badge_name": "Crewman SSZ",
                    "years": {"start": 2005, "end": 2006},
                    "body_styles": ["Dual Cab Ute"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual Tremec T56", "4-speed automatic 4L65-E"],
                    "msrp_aud_min": 49990,
                    "msrp_aud_max": 52990,
                    "fuel_consumption_l_100km": 14.6,
                    "kerb_weight_kg": 1860,
                    "standard_features": [
                        "5.7L LS1 V8 (250 kW)",
                        "Leather sports seats with 'SSZ' embroidery",
                        "Premium color-coded brake calipers",
                        "Auxiliary dashboard gauge pod",
                        "17-inch SS alloy wheels"
                    ],
                    "notes": "Special edition high-spec performance V8 dual-cab."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Adventra CX6",
                    "body_style": "AWD Wagon",
                    "engine_code": "Alloytec-190-V6",
                    "transmission": "5-speed automatic 5L40-E with paddle shifters",
                    "drivetrain": "AWD",
                    "msrp_aud": 44990,
                    "power_kw": 190.0,
                    "torque_nm": 340.0,
                    "fuel_l_100km": 12.8,
                    "towing_braked_kg": 2100,
                    "notes": "190 kW V6 Cross-Trac AWD wagon."
                },
                {
                    "badge_name": "Crewman SSZ",
                    "body_style": "Dual Cab Ute",
                    "engine_code": "Gen-IV-6.0-L76",
                    "transmission": "6-speed manual Tremec T56",
                    "drivetrain": "RWD",
                    "msrp_aud": 49990,
                    "power_kw": 260.0,
                    "torque_nm": 510.0,
                    "fuel_l_100km": 14.6,
                    "towing_braked_kg": 2100,
                    "notes": "6.0L Gen-IV 260 kW muscle dual-cab ute."
                }
            ]
        }
    ]
}
