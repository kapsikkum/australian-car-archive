"""
Wave 2 Deep-Dive Model Data: Holden Classics (Part 1)
Models:
1. 48-215 (FX)
2. FJ
3. FE-FC-FB-EK
4. EJ-EH-HD-HR
"""
from typing import Any, Dict

MODEL_48_215: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "48-215",
    "name": "Holden 48-215 (FX)",
    "vehicle_type": "Sedan / Coupe Utility / Business Sedan",
    "segment": "Mid-size",
    "years_sold_au": {"start": 1948, "end": 1953},
    "locally_built": True,
    "assembly_plants_au": [
        "Fishermans Bend, Victoria",
        "Woodville, South Australia",
        "Pagewood, New South Wales",
        "The Valley (Fortitude Valley), Queensland",
        "Mosman Park, Western Australia",
        "Birkenhead, South Australia"
    ],
    "overview": "The Holden 48-215 (retrospectively referred to as the 'FX') was Australia's first mass-produced domestic motor vehicle, famously unveiled on 29 November 1948 by Prime Minister Ben Chifley with the words: 'She's a beauty!'. Developed under GM Project 2000, it combined American interior room and robust unibody construction with European operating economy, tailored specifically for Australia's harsh corrugated roads. In January 1951, the 50-2106 Coupe Utility was launched, defining the iconic Australian 'ute', followed in July 1953 by the 48-215-257 Business Sedan for taxi operators. Over 120,402 examples were produced.",
    "australian_market_notes": "The 48-215 introduced unitary (monocoque) construction to Australian volume manufacturing, eliminating heavy separate chassis rails while providing extraordinary torsional rigidity. Powered by the legendary 132.5ci (2.16L) overhead valve 'Grey Motor' inline-six, it easily outperformed British four-cylinder rivals in hill-climbing, highway cruising, and reliability. Customer demand was so overwhelming that waiting lists stretched out past two years, establishing Holden's 70-year reign over Australian automotive culture.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "48-215",
            "generation_name": "Holden 48-215 / 50-2106",
            "years": {"start": 1948, "end": 1953},
            "body_styles": ["4-door sedan", "2-door coupe utility", "4-door business sedan"],
            "platform": "GM-H 48-215 integral body-frame",
            "ancap_rating": None,
            "summary": "First Australian-manufactured mass-market automobile. Features integral chassis-body construction, 2.16L Grey motor, 3-speed manual column shift, and independent front coil spring suspension.",
            "engines": [
                {
                    "engine_code": "Grey-132",
                    "name": "Holden Grey 132.5ci (2.16L) OHV Inline-6",
                    "displacement_cc": 2160,
                    "displacement_litres": 2.16,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 45.0,
                    "power_rpm": "3800",
                    "torque_nm": 136.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "6.5:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Cast iron block and cylinder head, 3-main bearing crankshaft, single Bendix-Stromberg single-barrel downdraft carburettor, 6-volt electrical system."
                }
            ],
            "badges": [
                {
                    "badge_name": "Standard Sedan",
                    "years": {"start": 1948, "end": 1953},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1466,
                    "msrp_aud_max": 1580,
                    "fuel_consumption_l_100km": 9.4,
                    "kerb_weight_kg": 1010,
                    "standard_features": [
                        "Integral body construction",
                        "6-passenger seating",
                        "15-inch steel wheels",
                        "Hydraulic drum brakes all round",
                        "Rubber floor mats",
                        "Dual front vent windows"
                    ],
                    "notes": "The original 'Australia's Own Car' model 48-215."
                },
                {
                    "badge_name": "Coupe Utility (50-2106)",
                    "years": {"start": 1951, "end": 1953},
                    "body_styles": ["Coupe Utility"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1380,
                    "msrp_aud_max": 1490,
                    "fuel_consumption_l_100km": 9.6,
                    "kerb_weight_kg": 995,
                    "standard_features": [
                        "Hardwood floor with protective steel skid strips",
                        "Removable tonneau cover cleats",
                        "Heavy-duty rear semi-elliptic leaf springs",
                        "500 kg payload capacity"
                    ],
                    "notes": "First factory-built Holden coupe utility, released January 1951."
                },
                {
                    "badge_name": "Business Sedan (48-215-257)",
                    "years": {"start": 1953, "end": 1953},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1550,
                    "msrp_aud_max": 1620,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 1025,
                    "standard_features": [
                        "Heavy-duty seat springs and commercial vinyl upholstery",
                        "Rear door assist straps",
                        "Taxi meter dashboard mounting provision",
                        "Heavy-duty front and rear springs"
                    ],
                    "notes": "Introduced in July 1953 specifically for commercial and taxi fleets."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Standard Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Grey-132",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1466,
                    "power_kw": 45.0,
                    "torque_nm": 136.0,
                    "fuel_l_100km": 9.4,
                    "towing_braked_kg": 680,
                    "notes": "Australia's own family sedan."
                },
                {
                    "badge_name": "Coupe Utility (50-2106)",
                    "body_style": "Coupe Utility",
                    "engine_code": "Grey-132",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1380,
                    "power_kw": 45.0,
                    "torque_nm": 136.0,
                    "fuel_l_100km": 9.6,
                    "towing_braked_kg": 750,
                    "notes": "Definitive early Australian workhorse ute."
                },
                {
                    "badge_name": "Business Sedan (48-215-257)",
                    "body_style": "Sedan",
                    "engine_code": "Grey-132",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1550,
                    "power_kw": 45.0,
                    "torque_nm": 136.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 680,
                    "notes": "Heavy-duty fleet and taxi specification."
                }
            ]
        }
    ]
}

MODEL_FJ: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "fj",
    "name": "Holden FJ",
    "vehicle_type": "Sedan / Coupe Utility / Panel Van",
    "segment": "Mid-size / Large",
    "years_sold_au": {"start": 1953, "end": 1956},
    "locally_built": True,
    "assembly_plants_au": [
        "Fishermans Bend, Victoria",
        "Woodville, South Australia",
        "Pagewood, New South Wales",
        "The Valley (Fortitude Valley), Queensland",
        "Mosman Park, Western Australia",
        "Birkenhead, South Australia"
    ],
    "overview": "Launched in October 1953, the Holden FJ is Australia's most recognized cultural automotive icon of the 1950s. Featuring an assertive horizontal chrome tooth grille, redesigned torpedo rear styling, and the introduction of the luxurious 'Special' sedan badge with two-tone leather options, the FJ captured 50% of Australian new car registrations. In December 1953, the iconic FJ Panel Van was introduced, creating the quintessential Aussie tradesman vehicle. The FJ was also Holden's first exported model, shipped to New Zealand in 1954. Total production reached 169,969 units.",
    "australian_market_notes": "The FJ broadened the Holden range to three sedan trim levels (Standard, Business, and Special) alongside the Coupe Utility and Panel Van. Mechanical updates included modified rear axle ratios, refined front suspension wishbones, and detail upgrades to the reliable 132.5ci Grey motor. The FJ was so ubiquitous on Australian suburban and rural roads that it became an indelible part of post-war Australian identity, celebrated in art, film, and national folklore.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "FJ",
            "generation_name": "Holden FJ Series",
            "years": {"start": 1953, "end": 1956},
            "body_styles": ["4-door sedan", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H FJ integral body-frame",
            "ancap_rating": None,
            "summary": "Definitive 1950s Australian icon. Introduced bold chrome grille, FJ Special flagship trim, two-tone paint options, and the first Holden factory Panel Van.",
            "engines": [
                {
                    "engine_code": "Grey-132-FJ",
                    "name": "Holden Grey 132.5ci (2.16L) OHV Inline-6",
                    "displacement_cc": 2160,
                    "displacement_litres": 2.16,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 45.0,
                    "power_rpm": "3800",
                    "torque_nm": 136.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "6.5:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Single Stromberg carburettor, 6-volt electrical system, 3-speed manual column shift with synchromesh on 2nd and 3rd gears."
                }
            ],
            "badges": [
                {
                    "badge_name": "FJ Standard",
                    "years": {"start": 1953, "end": 1956},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1600,
                    "msrp_aud_max": 1690,
                    "fuel_consumption_l_100km": 9.4,
                    "kerb_weight_kg": 1020,
                    "standard_features": [
                        "Single-color painted exterior",
                        "Painted hubcaps",
                        "Rubber floor mats",
                        "Dual horns",
                        "Column gear change"
                    ],
                    "notes": "Entry-level sedan, model FJ-215."
                },
                {
                    "badge_name": "FJ Business",
                    "years": {"start": 1953, "end": 1956},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1650,
                    "msrp_aud_max": 1740,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 1030,
                    "standard_features": [
                        "Heavy-duty interior vinyl",
                        "Reinforced seat springing",
                        "Passenger side sunvisor",
                        "Door pull handles"
                    ],
                    "notes": "Model FJ-217 tailored for fleet and taxi operators."
                },
                {
                    "badge_name": "FJ Special",
                    "years": {"start": 1953, "end": 1956},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1750,
                    "msrp_aud_max": 1890,
                    "fuel_consumption_l_100km": 9.4,
                    "kerb_weight_kg": 1035,
                    "standard_features": [
                        "Chrome side window surrounds",
                        "Stainless steel side body moldings",
                        "Two-tone leather upholstery options",
                        "Rear passenger armrests",
                        "Cigarette lighter and chrome horn ring"
                    ],
                    "notes": "Flagship luxury trim, model FJ-225; best-selling variant."
                },
                {
                    "badge_name": "FJ Utility",
                    "years": {"start": 1953, "end": 1956},
                    "body_styles": ["Coupe Utility"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1480,
                    "msrp_aud_max": 1590,
                    "fuel_consumption_l_100km": 9.6,
                    "kerb_weight_kg": 1005,
                    "standard_features": [
                        "500 kg payload capacity",
                        "Hardwood load bed slats",
                        "Tie-down rope hooks",
                        "Heavy-duty semi-elliptic rear springs"
                    ],
                    "notes": "Model FJ-2106 commercial utility."
                },
                {
                    "badge_name": "FJ Panel Van",
                    "years": {"start": 1953, "end": 1956},
                    "body_styles": ["Panel Van"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1520,
                    "msrp_aud_max": 1640,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1040,
                    "standard_features": [
                        "Enclosed all-steel cargo body",
                        "Dual rear barn doors",
                        "500 kg cargo rating",
                        "Heavy-duty floor timber slats"
                    ],
                    "notes": "Model FJ-2104, introduced in December 1953."
                }
            ],
            "configurations": [
                {
                    "badge_name": "FJ Special",
                    "body_style": "Sedan",
                    "engine_code": "Grey-132-FJ",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1750,
                    "power_kw": 45.0,
                    "torque_nm": 136.0,
                    "fuel_l_100km": 9.4,
                    "towing_braked_kg": 750,
                    "notes": "Most popular Holden passenger car of the 1950s."
                },
                {
                    "badge_name": "FJ Standard",
                    "body_style": "Sedan",
                    "engine_code": "Grey-132-FJ",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1600,
                    "power_kw": 45.0,
                    "torque_nm": 136.0,
                    "fuel_l_100km": 9.4,
                    "towing_braked_kg": 750,
                    "notes": "Base specification family transport."
                },
                {
                    "badge_name": "FJ Utility",
                    "body_style": "Coupe Utility",
                    "engine_code": "Grey-132-FJ",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1480,
                    "power_kw": 45.0,
                    "torque_nm": 136.0,
                    "fuel_l_100km": 9.6,
                    "towing_braked_kg": 750,
                    "notes": "Iconic Australian farmer and tradesman workhorse."
                },
                {
                    "badge_name": "FJ Panel Van",
                    "body_style": "Panel Van",
                    "engine_code": "Grey-132-FJ",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1520,
                    "power_kw": 45.0,
                    "torque_nm": 136.0,
                    "fuel_l_100km": 9.8,
                    "towing_braked_kg": 750,
                    "notes": "The birth of the Australian commercial panel van lineage."
                }
            ]
        }
    ]
}

MODEL_FE_FC_FB_EK: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "fe-fc-fb-ek",
    "name": "Holden FE / FC / FB / EK",
    "vehicle_type": "Sedan / Station Sedan / Utility / Panel Van",
    "segment": "Large",
    "years_sold_au": {"start": 1956, "end": 1962},
    "locally_built": True,
    "assembly_plants_au": [
        "Fishermans Bend, Victoria",
        "Dandenong, Victoria",
        "Woodville, South Australia",
        "Pagewood, New South Wales",
        "The Valley (Fortitude Valley), Queensland",
        "Mosman Park, Western Australia"
    ],
    "overview": "The second and third generation post-war Holdens represented major leaps forward in Australian automotive engineering and design. Launched in July 1956, the FE introduced a completely modern, longer, lower body with wrap-around windscreen, 12-volt electrical architecture, recirculating ball steering, and Holden's very first factory station wagon—marketed as the 'Station Sedan'. The May 1958 FC refined the formula with an egg-crate grille and became the first car in Australian history to sell over 100,000 units in a calendar year. In January 1960, the FB adopted American fin-tail styling and a larger 138ci Grey motor, followed in May 1961 by the EK, which brought the historic introduction of the 3-speed Hydra-Matic automatic transmission to Holden. Across all four series, over 740,000 vehicles were built.",
    "australian_market_notes": "The FE-EK era cemented Holden's absolute supremacy in Australian motoring, securing over 50% total market share. The Station Sedan revolutionized family holidays and outback travel, while the EK Hydra-Matic made two-pedal driving accessible to middle Australia. The Dandenong (Victoria) assembly plant opened during the FE era to meet soaring national demand, while exports expanded across 46 overseas markets throughout Africa, Southeast Asia, and the Pacific.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "FE",
            "generation_name": "FE Series",
            "years": {"start": 1956, "end": 1958},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H second generation unibody",
            "ancap_rating": None,
            "summary": "First clean-sheet redesign of the Holden. Introduced 12-volt electrics, wrap-around windscreen, pendant clutch and brake pedals, and the first factory Station Sedan.",
            "engines": [
                {
                    "engine_code": "Grey-132-FE",
                    "name": "Holden Grey 132.5ci (2.16L) OHV Inline-6",
                    "displacement_cc": 2160,
                    "displacement_litres": 2.16,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 52.0,
                    "power_rpm": "4000",
                    "torque_nm": 149.0,
                    "torque_rpm": "1200",
                    "compression_ratio": "6.8:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Upgraded with larger valves, higher compression, 12-volt electrical system, developing 70 bhp."
                }
            ],
            "badges": [
                {
                    "badge_name": "FE Special Sedan",
                    "years": {"start": 1956, "end": 1958},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1840,
                    "msrp_aud_max": 1960,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 1080,
                    "standard_features": [
                        "Two-tone exterior paint",
                        "Stainless body side chrome",
                        "12-volt electrical system",
                        "Wrap-around windscreen and rear window",
                        "Dual sunvisors and cigarette lighter"
                    ],
                    "notes": "Model FE-225 flagship passenger sedan."
                },
                {
                    "badge_name": "FE Special Station Sedan",
                    "years": {"start": 1957, "end": 1958},
                    "body_styles": ["Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1990,
                    "msrp_aud_max": 2120,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1130,
                    "standard_features": [
                        "Fold-down rear seat creating flat cargo floor",
                        "Wind-down tailgate rear window",
                        "Two-tone station wagon styling",
                        "Heavy-duty rear suspension"
                    ],
                    "notes": "Introduced in March 1957 as Holden's first factory station wagon."
                }
            ],
            "configurations": [
                {
                    "badge_name": "FE Special Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Grey-132-FE",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1840,
                    "power_kw": 52.0,
                    "torque_nm": 149.0,
                    "fuel_l_100km": 9.8,
                    "towing_braked_kg": 750,
                    "notes": "Modern family sedan with 12V electricals."
                },
                {
                    "badge_name": "FE Special Station Sedan",
                    "body_style": "Station Sedan",
                    "engine_code": "Grey-132-FE",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1990,
                    "power_kw": 52.0,
                    "torque_nm": 149.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 850,
                    "notes": "Holden's first factory wagon configuration."
                }
            ]
        },
        {
            "series_code": "FC",
            "generation_name": "FC Series",
            "years": {"start": 1958, "end": 1960},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H second generation unibody",
            "ancap_rating": None,
            "summary": "Refinement of the FE with bold egg-crate grille, revised chrome fins, improved steering gear, and increased 72 bhp power output. Over 191,000 produced.",
            "engines": [
                {
                    "engine_code": "Grey-132-FC",
                    "name": "Holden Grey 132.5ci (2.16L) OHV Inline-6",
                    "displacement_cc": 2160,
                    "displacement_litres": 2.16,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 54.0,
                    "power_rpm": "4000",
                    "torque_nm": 149.0,
                    "torque_rpm": "1200",
                    "compression_ratio": "7.0:1",
                    "valvetrain": "OHV 12V",
                    "notes": "72 bhp rating with redesigned camshaft profile and 7.0:1 compression ratio."
                }
            ],
            "badges": [
                {
                    "badge_name": "FC Special Sedan",
                    "years": {"start": 1958, "end": 1960},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1890,
                    "msrp_aud_max": 2010,
                    "fuel_consumption_l_100km": 9.7,
                    "kerb_weight_kg": 1090,
                    "standard_features": [
                        "Cast-metal egg-crate grille",
                        "Sweeping side body chrome molding",
                        "Two-tone exterior color schemes",
                        "Recirculating ball steering box"
                    ],
                    "notes": "Model FC-225; reached over 50% total market share in 1958-59."
                },
                {
                    "badge_name": "FC Special Station Sedan",
                    "years": {"start": 1958, "end": 1960},
                    "body_styles": ["Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 2040,
                    "msrp_aud_max": 2180,
                    "fuel_consumption_l_100km": 10.1,
                    "kerb_weight_kg": 1140,
                    "standard_features": [
                        "Long flat cargo deck",
                        "Split folding rear bench",
                        "Roll-down rear tailgate window",
                        "High-capacity luggage bay"
                    ],
                    "notes": "Model FC-229."
                }
            ],
            "configurations": [
                {
                    "badge_name": "FC Special Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Grey-132-FC",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1890,
                    "power_kw": 54.0,
                    "torque_nm": 149.0,
                    "fuel_l_100km": 9.7,
                    "towing_braked_kg": 750,
                    "notes": "Record-breaking 100,000-sales-a-year family sedan."
                }
            ]
        },
        {
            "series_code": "FB",
            "generation_name": "FB Series",
            "years": {"start": 1960, "end": 1961},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H third generation unibody",
            "ancap_rating": None,
            "summary": "Introduced prominent American-style tailfins, panoramic wrap-around windscreen with forward-slanted 'dogleg' A-pillars, lower roofline, and an enlarged 138ci Grey motor.",
            "engines": [
                {
                    "engine_code": "Grey-138-FB",
                    "name": "Holden Grey 138ci (2.26L) OHV Inline-6",
                    "displacement_cc": 2262,
                    "displacement_litres": 2.26,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 56.0,
                    "power_rpm": "4200",
                    "torque_nm": 163.0,
                    "torque_rpm": "1400",
                    "compression_ratio": "7.25:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Enlarged bore from 3.0 to 3.0625 inches, lifting output to 75 bhp and torque to 120 lb-ft."
                }
            ],
            "badges": [
                {
                    "badge_name": "FB Special Sedan",
                    "years": {"start": 1960, "end": 1961},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 1950,
                    "msrp_aud_max": 2080,
                    "fuel_consumption_l_100km": 10.0,
                    "kerb_weight_kg": 1120,
                    "standard_features": [
                        "Panoramic wrap-around front glass",
                        "Fin-tail rear wings",
                        "138ci Grey motor",
                        "New acrylic lacquer paint"
                    ],
                    "notes": "Model FB-225; 147,747 units built."
                }
            ],
            "configurations": [
                {
                    "badge_name": "FB Special Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Grey-138-FB",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 1950,
                    "power_kw": 56.0,
                    "torque_nm": 163.0,
                    "fuel_l_100km": 10.0,
                    "towing_braked_kg": 800,
                    "notes": "American-finned styling with 138ci Grey power."
                }
            ]
        },
        {
            "series_code": "EK",
            "generation_name": "EK Series",
            "years": {"start": 1961, "end": 1962},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H third generation unibody",
            "ancap_rating": None,
            "summary": "Historic introduction of Holden's first automatic transmission: the 3-speed Hydra-Matic. Added electric windscreen wipers, updated side chrome, and new interior trim. 150,214 built.",
            "engines": [
                {
                    "engine_code": "Grey-138-EK",
                    "name": "Holden Grey 138ci (2.26L) OHV Inline-6",
                    "displacement_cc": 2262,
                    "displacement_litres": 2.26,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 56.0,
                    "power_rpm": "4200",
                    "torque_nm": 163.0,
                    "torque_rpm": "1400",
                    "compression_ratio": "7.25:1",
                    "valvetrain": "OHV 12V",
                    "notes": "75 bhp output; equipped with specialized vacuum ports and oil cooler plumbing for Hydra-Matic models."
                }
            ],
            "badges": [
                {
                    "badge_name": "EK Special Sedan",
                    "years": {"start": 1961, "end": 1962},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column", "3-speed Hydra-Matic automatic"],
                    "msrp_aud_min": 1980,
                    "msrp_aud_max": 2230,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1135,
                    "standard_features": [
                        "Optional 3-speed Hydra-Matic automatic transmission",
                        "Electric windscreen wipers replacing vacuum units",
                        "Fresh air heater/demister option",
                        "Two-tone Magic-Mirror acrylic lacquer"
                    ],
                    "notes": "Model EK-225; first automatic Holden passenger sedan."
                },
                {
                    "badge_name": "EK Special Station Sedan",
                    "years": {"start": 1961, "end": 1962},
                    "body_styles": ["Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column", "3-speed Hydra-Matic automatic"],
                    "msrp_aud_min": 2150,
                    "msrp_aud_max": 2390,
                    "fuel_consumption_l_100km": 10.6,
                    "kerb_weight_kg": 1190,
                    "standard_features": [
                        "3-speed Hydra-Matic automatic option",
                        "Cargo bay length of 1,850 mm with seat folded",
                        "Tailgate roll-down rear window",
                        "Heavy-duty rear suspension"
                    ],
                    "notes": "Model EK-229."
                }
            ],
            "configurations": [
                {
                    "badge_name": "EK Special Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Grey-138-EK",
                    "transmission": "3-speed Hydra-Matic automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 2230,
                    "power_kw": 56.0,
                    "torque_nm": 163.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 850,
                    "notes": "First automatic-equipped Holden family car."
                },
                {
                    "badge_name": "EK Special Station Sedan",
                    "body_style": "Station Sedan",
                    "engine_code": "Grey-138-EK",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 2150,
                    "power_kw": 56.0,
                    "torque_nm": 163.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 850,
                    "notes": "Spacious family station wagon."
                }
            ]
        }
    ]
}

MODEL_EJ_EH_HD_HR: Dict[str, Any] = {
    "make_slug": "holden",
    "model_slug": "ej-eh-hd-hr",
    "name": "Holden EJ / EH / HD / HR",
    "vehicle_type": "Sedan / Station Sedan / Utility / Panel Van",
    "segment": "Large",
    "years_sold_au": {"start": 1962, "end": 1968},
    "locally_built": True,
    "assembly_plants_au": [
        "Fishermans Bend, Victoria",
        "Dandenong, Victoria",
        "Elizabeth, South Australia",
        "Woodville, South Australia",
        "Pagewood, New South Wales",
        "Acacia Ridge, Queensland",
        "Mosman Park, Western Australia"
    ],
    "overview": "The 1962-1968 era represents the golden age of 1960s Holden dominance. The July 1962 EJ introduced clean, modern European-inspired styling, the milestone 1,000,000th Holden produced, and the prestigious Premier luxury model with standard automatic, leather bucket seats, and metallic paint. In August 1963, the legendary EH debuted Holden's all-new, world-class 'Red Motor' inline-six—featuring a 7-bearing crankshaft, hydraulic lifters, and 149ci (2.4L) and 179ci (2.9L) capacities. The EH became Australia's fastest-selling car ever, selling over 250,000 units in 18 months and claiming podium fame at Mount Panorama with the EH S4 Bathurst homologation special. The 1965 HD brought wider passenger accommodations and the twin-carburettor X2 engine, while the April 1966 HR resolved styling with crisp modern lines, front disc brakes, wider track, and the 186S engine with twin-barrel Bendix-Stromberg WW carburettor.",
    "australian_market_notes": "The introduction of the Red Motor in the EH transformed Holden's engineering standing worldwide, vastly outclassing Ford's Falcon sixes in thermal endurance and high-speed reliability. In 1966, the HR series pioneered critical Australian safety engineering with front lap-sash seatbelt mountings, padded dash, shatter-resistant mirror, and front disc brakes as an option (standard on Premier). Over 1,020,000 units were produced across the EJ, EH, HD, and HR models.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "EJ",
            "generation_name": "EJ Series",
            "years": {"start": 1962, "end": 1963},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H fourth generation unibody",
            "ancap_rating": None,
            "summary": "Lower, squarer modern styling, marked the 1,000,000th Holden built, and introduced the luxurious Premier nameplate. Final application of the Grey motor.",
            "engines": [
                {
                    "engine_code": "Grey-138-EJ",
                    "name": "Holden Grey 138ci (2.26L) OHV Inline-6",
                    "displacement_cc": 2262,
                    "displacement_litres": 2.26,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 56.0,
                    "power_rpm": "4200",
                    "torque_nm": 163.0,
                    "torque_rpm": "1400",
                    "compression_ratio": "7.25:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Final production version of the venerable Grey motor."
                }
            ],
            "badges": [
                {
                    "badge_name": "EJ Special",
                    "years": {"start": 1962, "end": 1963},
                    "body_styles": ["Sedan", "Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column", "3-speed Hydra-Matic automatic"],
                    "msrp_aud_min": 2100,
                    "msrp_aud_max": 2340,
                    "fuel_consumption_l_100km": 10.3,
                    "kerb_weight_kg": 1140,
                    "standard_features": [
                        "Two-tone acrylic lacquer finish",
                        "Duo-servo drum brakes",
                        "Front vent windows",
                        "Magic-Mirror exterior finish"
                    ],
                    "notes": "Mainstream model EJ-225."
                },
                {
                    "badge_name": "EJ Premier",
                    "years": {"start": 1962, "end": 1963},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed Hydra-Matic automatic"],
                    "msrp_aud_min": 2700,
                    "msrp_aud_max": 2850,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1180,
                    "standard_features": [
                        "Standard Hydra-Matic transmission",
                        "Individual Howe leather front bucket seats",
                        "Center console and heater/demister",
                        "Whitewall tires and gold exterior badging"
                    ],
                    "notes": "The birth of the prestigious Holden Premier luxury badge."
                }
            ],
            "configurations": [
                {
                    "badge_name": "EJ Premier",
                    "body_style": "Sedan",
                    "engine_code": "Grey-138-EJ",
                    "transmission": "3-speed Hydra-Matic automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 2700,
                    "power_kw": 56.0,
                    "torque_nm": 163.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 850,
                    "notes": "Inaugural Holden Premier luxury flagship."
                }
            ]
        },
        {
            "series_code": "EH",
            "generation_name": "EH Series",
            "years": {"start": 1963, "end": 1965},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H fourth generation unibody",
            "ancap_rating": None,
            "summary": "Historic launch of the 7-bearing Red Motor (149ci & 179ci). Re-profiled roofline, square rear boot and tail lights. Fastest selling car in Australian history with 256,959 units sold.",
            "engines": [
                {
                    "engine_code": "Red-149",
                    "name": "Holden Red 149ci (2.4L) OHV Inline-6",
                    "displacement_cc": 2442,
                    "displacement_litres": 2.4,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 75.0,
                    "power_rpm": "4400",
                    "torque_nm": 197.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 12V",
                    "notes": "7-bearing crankshaft, hydraulic valve lifters, 100 bhp output."
                },
                {
                    "engine_code": "Red-179",
                    "name": "Holden Red 179ci (2.9L) OHV Inline-6",
                    "displacement_cc": 2934,
                    "displacement_litres": 2.9,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 86.0,
                    "power_rpm": "4000",
                    "torque_nm": 237.0,
                    "torque_rpm": "1600",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 12V",
                    "notes": "115 bhp output with 175 lb-ft of torque; standard on Premier, optional on Special."
                },
                {
                    "engine_code": "Red-179-S4",
                    "name": "Holden Red 179ci S4 Competition Inline-6",
                    "displacement_cc": 2934,
                    "displacement_litres": 2.9,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 89.0,
                    "power_rpm": "4400",
                    "torque_nm": 245.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Homologation special for Armstrong 500 at Bathurst. Reinforced clutch, metal brake linings, larger fuel tank."
                }
            ],
            "badges": [
                {
                    "badge_name": "EH Special",
                    "years": {"start": 1963, "end": 1965},
                    "body_styles": ["Sedan", "Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column", "Hydra-Matic 3-speed automatic"],
                    "msrp_aud_min": 2150,
                    "msrp_aud_max": 2420,
                    "fuel_consumption_l_100km": 10.5,
                    "kerb_weight_kg": 1150,
                    "standard_features": [
                        "Red 149 standard (Red 179 optional)",
                        "Clean squared roof and boot styling",
                        "Bench front seating",
                        "Magic-Mirror acrylic exterior lacquer"
                    ],
                    "notes": "Heart of the Australian car market in the mid-1960s."
                },
                {
                    "badge_name": "EH Premier",
                    "years": {"start": 1963, "end": 1965},
                    "body_styles": ["Sedan", "Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["Hydra-Matic 3-speed automatic"],
                    "msrp_aud_min": 2780,
                    "msrp_aud_max": 2950,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1195,
                    "standard_features": [
                        "Standard 179 Red Motor",
                        "Hydra-Matic automatic transmission",
                        "Genuine leather bucket seats and console",
                        "Premier Station Sedan introduced for the first time"
                    ],
                    "notes": "Luxury flagship; first Premier wagon."
                },
                {
                    "badge_name": "EH Special S4",
                    "years": {"start": 1963, "end": 1963},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column"],
                    "msrp_aud_min": 2490,
                    "msrp_aud_max": 2550,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1160,
                    "standard_features": [
                        "Hand-selected 179 Red Motor",
                        "Sintered iron brake linings with vacuum power booster",
                        "Heavy-duty clutch and larger radiator",
                        "12-gallon competition fuel tank"
                    ],
                    "notes": "Legendary factory Bathurst homologation special; only 126 examples produced (Melbourne and Sydney)."
                }
            ],
            "configurations": [
                {
                    "badge_name": "EH Special",
                    "body_style": "Sedan",
                    "engine_code": "Red-149",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 2150,
                    "power_kw": 75.0,
                    "torque_nm": 197.0,
                    "fuel_l_100km": 10.5,
                    "towing_braked_kg": 950,
                    "notes": "Mainstream Australian benchmark."
                },
                {
                    "badge_name": "EH Premier",
                    "body_style": "Sedan",
                    "engine_code": "Red-179",
                    "transmission": "Hydra-Matic 3-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 2780,
                    "power_kw": 86.0,
                    "torque_nm": 237.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 1000,
                    "notes": "179 Red motor luxury saloon."
                },
                {
                    "badge_name": "EH Special S4",
                    "body_style": "Sedan",
                    "engine_code": "Red-179-S4",
                    "transmission": "3-speed manual column",
                    "drivetrain": "RWD",
                    "msrp_aud": 2490,
                    "power_kw": 89.0,
                    "torque_nm": 245.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 1000,
                    "notes": "Historic Mount Panorama Bathurst homologation weapon."
                }
            ]
        },
        {
            "series_code": "HD",
            "generation_name": "HD Series",
            "years": {"start": 1965, "end": 1966},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H fifth generation unibody",
            "ancap_rating": None,
            "summary": "Introduced wider body with curved side glass, kidney front fenders, front disc brakes option, Powerglide 2-speed automatic, and the twin-carburettor X2 high-performance engine.",
            "engines": [
                {
                    "engine_code": "Red-149-HD",
                    "name": "Holden Red 149ci (2.4L) OHV Inline-6",
                    "displacement_cc": 2442,
                    "displacement_litres": 2.4,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 75.0,
                    "power_rpm": "4400",
                    "torque_nm": 197.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Base engine on Standard and Special."
                },
                {
                    "engine_code": "Red-179-HD",
                    "name": "Holden Red 179ci (2.9L) OHV Inline-6",
                    "displacement_cc": 2934,
                    "displacement_litres": 2.9,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 86.0,
                    "power_rpm": "4000",
                    "torque_nm": 237.0,
                    "torque_rpm": "1600",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Standard on Premier, optional on Special."
                },
                {
                    "engine_code": "Red-179-X2",
                    "name": "Holden Red 179ci X2 Twin-Carb Inline-6",
                    "displacement_cc": 2934,
                    "displacement_litres": 2.9,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 104.0,
                    "power_rpm": "4600",
                    "torque_nm": 241.0,
                    "torque_rpm": "2200",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Twin Bendix-Stromberg carburettors, high-flow dual exhaust manifolds, performance camshaft; 140 bhp."
                }
            ],
            "badges": [
                {
                    "badge_name": "HD Premier",
                    "years": {"start": 1965, "end": 1966},
                    "body_styles": ["Sedan", "Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["Powerglide 2-speed automatic"],
                    "msrp_aud_min": 2860,
                    "msrp_aud_max": 3100,
                    "fuel_consumption_l_100km": 11.4,
                    "kerb_weight_kg": 1210,
                    "standard_features": [
                        "179 Red motor standard",
                        "Powerglide 2-speed automatic",
                        "Front disc brakes option",
                        "Morfelde vinyl or leather bucket seats",
                        "Curved side door glass"
                    ],
                    "notes": "Spacious luxury saloon; 178,927 total HDs built."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HD Premier",
                    "body_style": "Sedan",
                    "engine_code": "Red-179-X2",
                    "transmission": "Powerglide 2-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 2980,
                    "power_kw": 104.0,
                    "torque_nm": 241.0,
                    "fuel_l_100km": 11.8,
                    "towing_braked_kg": 1050,
                    "notes": "Twin-carburettor X2 performance luxury."
                }
            ]
        },
        {
            "series_code": "HR",
            "generation_name": "HR Series",
            "years": {"start": 1966, "end": 1968},
            "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe utility", "2-door panel van"],
            "platform": "GM-H fifth generation unibody",
            "ancap_rating": None,
            "summary": "Crisp squared styling, wider track, ball-joint front suspension, standard front disc brakes on Premier, and introduced the high-output 186S engine with twin-barrel carburettor and 4-speed manual.",
            "engines": [
                {
                    "engine_code": "Red-161",
                    "name": "Holden Red 161ci (2.6L) OHV Inline-6",
                    "displacement_cc": 2638,
                    "displacement_litres": 2.6,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 85.0,
                    "power_rpm": "4400",
                    "torque_nm": 213.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Replaced the 149; 114 bhp output."
                },
                {
                    "engine_code": "Red-186",
                    "name": "Holden Red 186ci (3.0L) OHV Inline-6",
                    "displacement_cc": 3048,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 94.0,
                    "power_rpm": "4400",
                    "torque_nm": 245.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Replaced the 179; 126 bhp output."
                },
                {
                    "engine_code": "Red-186S",
                    "name": "Holden Red 186S 3.0L High-Performance Inline-6",
                    "displacement_cc": 3048,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 108.0,
                    "power_rpm": "4600",
                    "torque_nm": 249.0,
                    "torque_rpm": "2200",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Fitted with twin-barrel Bendix-Stromberg WW carburettor, performance camshaft, dual exhaust headers; 145 bhp."
                }
            ],
            "badges": [
                {
                    "badge_name": "HR Special",
                    "years": {"start": 1966, "end": 1968},
                    "body_styles": ["Sedan", "Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column", "4-speed manual floor", "Powerglide 2-speed automatic"],
                    "msrp_aud_min": 2220,
                    "msrp_aud_max": 2560,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1170,
                    "standard_features": [
                        "Red 161 standard (Red 186 optional)",
                        "Wider track and revised ball-joint front suspension",
                        "Front lap-sash seatbelt mountings",
                        "Padded dashboard and sunvisors"
                    ],
                    "notes": "Core model HR-225; 252,352 HRs produced."
                },
                {
                    "badge_name": "HR Premier",
                    "years": {"start": 1966, "end": 1968},
                    "body_styles": ["Sedan", "Station Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["Powerglide 2-speed automatic", "4-speed manual floor"],
                    "msrp_aud_min": 2890,
                    "msrp_aud_max": 3220,
                    "fuel_consumption_l_100km": 11.5,
                    "kerb_weight_kg": 1220,
                    "standard_features": [
                        "Red 186 engine standard",
                        "Power-assisted front disc brakes standard",
                        "Plush Morfelde vinyl or leather bucket seats",
                        "Woodgrain center console and glovebox trim",
                        "Twin horns and rear wheel spats"
                    ],
                    "notes": "Prestige family luxury cruiser."
                },
                {
                    "badge_name": "HR 186S",
                    "years": {"start": 1967, "end": 1968},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor", "Powerglide 2-speed automatic"],
                    "msrp_aud_min": 2680,
                    "msrp_aud_max": 2980,
                    "fuel_consumption_l_100km": 11.8,
                    "kerb_weight_kg": 1190,
                    "standard_features": [
                        "186S high-performance twin-barrel engine (145 bhp)",
                        "Opel-sourced 4-speed manual floor shift",
                        "Power front disc brakes",
                        "Dual exhaust headers"
                    ],
                    "notes": "Sports saloon precursor to the Monaro GTS."
                }
            ],
            "configurations": [
                {
                    "badge_name": "HR Premier",
                    "body_style": "Sedan",
                    "engine_code": "Red-186",
                    "transmission": "Powerglide 2-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 2890,
                    "power_kw": 94.0,
                    "torque_nm": 245.0,
                    "fuel_l_100km": 11.5,
                    "towing_braked_kg": 1100,
                    "notes": "Classic Australian executive sedan."
                },
                {
                    "badge_name": "HR 186S",
                    "body_style": "Sedan",
                    "engine_code": "Red-186S",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 2680,
                    "power_kw": 108.0,
                    "torque_nm": 249.0,
                    "fuel_l_100km": 11.8,
                    "towing_braked_kg": 1100,
                    "notes": "Potent 186S 4-speed sports specification."
                }
            ]
        }
    ]
}
